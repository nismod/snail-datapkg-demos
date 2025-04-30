from pathlib import Path

from snail_datapkg.download import download_file


if __name__ == "__main__":
    downloads = [
        (
            "https://zenodo.org/records/14536877/files/GHA.zip?download=1",
            "starter-data-kit/GHA.zip",
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
    ]
    data_path = Path(__file__).parent.parent / "incoming_data"

    for url, output_file in downloads:
        download_file(url, data_path / output_file)
