import logging

import geopandas as gpd
import rasterio
import rasterio.features
import shapely

from pyproj import Geod


def polygonise_targets(targets_path: str, crs=None) -> gpd.GeoDataFrame:
    """
    Take a raster of electricity consuming 'targets' and a geometry extent and
    return a set of target polygons with computed areas.

    Args:
        targets_path: Path to raster file containing targets
        crs: CRS of input data. Will lookup CRS from dataset if not provided.
            May be any type accepted by:
            https://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS.from_user_input

    Returns:
        Table of target geometries and areas
    """

    geod = Geod(ellps="WGS84")
    geoms = []
    areas_km2 = []

    # Targets: Binary raster showing locations predicted to be connected to distribution grid.
    with rasterio.open(targets_path) as dataset:
        if crs is None:
            crs = dataset.crs

        # Read the dataset's valid data mask as a ndarray.
        try:
            # Extract feature shapes and values from the array.
            data = dataset.read(1)
            for geom, val in rasterio.features.shapes(
                data, transform=dataset.transform
            ):
                if val > 0:
                    feature = shapely.geometry.shape(geom)
                    geoms.append(feature)
                    area_m2, _ = geod.geometry_area_perimeter(feature)
                    areas_km2.append(abs(area_m2 / 1e6))
        except ValueError as ex:
            # could be that extent does not overlap dataset
            logging.info("Extent may not overlap targets", ex)
            pass

    targets = gpd.GeoDataFrame(data={"area_km2": areas_km2, "geometry": geoms}, crs=crs)

    # this is the globally unique integer id of each target
    targets["id"] = targets.index

    return targets
