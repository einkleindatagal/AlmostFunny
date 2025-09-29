# %%

import os
from dataclasses import dataclass
from enum import StrEnum
from pprint import pprint  # noqa

import requests as r
from log_setup import log

# %%


@dataclass
class ScryPy:
    class Routes(StrEnum):
        ROOT = "https://api.scryfall.com"
        BULK_DATA = "bulk-data"

    base_headers = {
        "User-Agent": "OptADeck/0.1",
        "Accept": "application/   json",
    }

    def create_url(*url_parts):
        url = "/".join([ScryPy.Routes.ROOT, *url_parts])
        return url

    def download_data(url):
        local_filename = url.split("/")[-1]
        download_location = f"{os.getcwd()}/data_download/{local_filename}"
        with r.get(url=url, stream=True, headers=ScryPy.base_headers) as req:
            req.raise_for_status()
            with open(download_location, "wb") as file:
                for chunk in req.iter_content(chunk_size=8192):
                    file.write(chunk)
        log.info(f"{local_filename} has been downloaded to {download_location}")
        return download_location


# %%

bulk_info = r.get(
    url=ScryPy.create_url(ScryPy.Routes.BULK_DATA), headers=ScryPy.base_headers
)
bulk_data = bulk_info.json()["data"]
default_cards_entry = next(
    (entry for entry in bulk_data if entry["name"] == "Default Cards"), None
)
default_cards_uri = default_cards_entry["download_uri"]
all_cards_entry = next(
    (entry for entry in bulk_data if entry["name"] == "All Cards"), None
)
all_cards_uri = all_cards_entry["download_uri"]

# %%
