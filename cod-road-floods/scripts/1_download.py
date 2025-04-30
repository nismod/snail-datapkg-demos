from pathlib import Path

from snail_datapkg.download import download_file


if __name__ == "__main__":
    downloads = [
        (
            "https://zenodo.org/records/15276150/files/COD.zip?download=1",
            "starter-data-kit/COD.zip",
        ),
        (
            "https://zenodo.org/records/13889558/files/Table_D1_Summary_CI_Vulnerability_Data_V1.1.0.xlsx?download=1",
            "nirandjan-2024-vulnerabilty/Table_D1_Summary_CI_Vulnerability_Data_V1.1.0.xlsx",
        ),
        (
            "https://zenodo.org/records/13889558/files/Table_D2_Hazard_Fragility_and_Vulnerability_Curves_V1.1.0.xlsx?download=1",
            "nirandjan-2024-vulnerabilty/Table_D2_Hazard_Fragility_and_Vulnerability_Curves_V1.1.0.xlsx",
        ),
        (
            "https://zenodo.org/records/13889558/files/Table_D3_Costs_V1.1.0.xlsx?download=1",
            "nirandjan-2024-vulnerabilty/Table_D3_Costs_V1.1.0.xlsx",
        ),
        (
            "https://data.humdata.org/dataset/104bfeb2-f102-4770-90a7-fc8372b488f0/resource/e54fa557-96f8-4144-af40-4a309ff9779f/download/democratic-republic-of-the-congo-shapefiles.zip",
            "healthsites/democratic-republic-of-the-congo-shapefiles.zip",
        ),
    ]
    data_path = Path(__file__).parent.parent / "incoming_data"

    for url, output_file in downloads:
        download_file(url, data_path / output_file)
