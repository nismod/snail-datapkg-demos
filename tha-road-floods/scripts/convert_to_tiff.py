from pathlib import Path
import xarray as xr

fields = ["u10", "tp", "mslp"]
field_names = ["windspeed", "precipitation", "pressure"]
units = ["ms-1", "m", "Pa"]
units_scaled = ["ms-1", "mm", "hPa"]
scale_factors = [1, 1e3, 1e-2]

methods = ["gaussian", "gumbel", "rescaled", "uniform"]

def ds_to_raster(ds, field, field_name, scale_factor, unit_scaled, sample, dirname):
     ss = ds.data \
     .sel(sample=sample, field=field) \
     * scale_factor

     ss \
     .rio.set_spatial_dims(x_dim='lon', y_dim='lat') \
     .rio.write_crs("EPSG:4326") \
     .rio.to_raster(dirname / f"s{sample:03d}_{field_name}_{unit_scaled}.tif")


for method in methods:
    dirname = Path(method)
    (dirname / "tiffs").mkdir(exist_ok=True)
    ds = xr.load_dataset(dirname / "nc" / "data.nc")
    zipped = zip(fields, field_names, units_scaled, scale_factors)
    for field, field_name, unit_scaled, scale_factor in zipped:
        for sample in ds.sample.data:
            ds_to_raster(
                ds, 
                field, 
                field_name, 
                scale_factor, 
                unit_scaled, 
                int(sample), 
                dirname / "tiffs"
            )

