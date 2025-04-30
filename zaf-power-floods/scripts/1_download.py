from pathlib import Path

from snail_datapkg.download import download_file


if __name__ == "__main__":
    downloads = [
        (
            "https://zenodo.org/records/15271243/files/ZAF.zip?download=1",
            "starter-data-kit/ZAF.zip",
        ),
        (
            "https://globalenergymonitor.org/wp-content/uploads/2025/03/Global-Integrated-Power-March-2025.xlsx",
            "global-energy-monitor/Global-Integrated-Power-March-2025.xlsx",
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
