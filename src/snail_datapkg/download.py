import logging
import zipfile

import requests

logging.basicConfig(level="INFO")


def download_file(url, output_path):
    logging.info("Checking output %s", output_path)

    output_path.parent.mkdir(exist_ok=True, parents=True)

    if not output_path.exists():
        logging.info("Downloading from %s", url)
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)

    if output_path.suffix == ".zip":
        logging.info("Extracting from %s", output_path)
        with zipfile.ZipFile(output_path, "r") as zip_ref:
            zip_ref.extractall(output_path.parent)
