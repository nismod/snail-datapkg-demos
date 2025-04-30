from pathlib import Path

from snail_datapkg.download import download_file


if __name__ == "__main__":
    downloads = [
        (
            "https://zenodo.org/records/15271219/files/NGA.zip?download=1",
            "starter-data-kit/NGA.zip",
        ),
        (
            "https://globalenergymonitor.org/wp-content/uploads/2025/04/Africa-Energy-Data-Download-March-2025-Release-2025-04-10.xlsx",
            "global-energy-monitor/Africa-Energy-Data-Download-March-2025-Release-2025-04-10.xlsx",
        ),
    ]
    data_path = Path(__file__).parent.parent / "incoming_data"

    for url, output_file in downloads:
        download_file(url, data_path / output_file)
