# %%

from enum import StrEnum

from log_setup import log

base_headers = {"User-Agent": "OptADeck/0.1", "Accept": "application/json"}

# r.get(headers=base_headers)


class Routes(StrEnum):
    ROOT = "https://api.scryfall.com"
    BULK_DATA = "bulk-data"


log.debug(Routes.BULK_DATA)
