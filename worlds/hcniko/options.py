from typing import Dict

from Options import Choice, Option, Toggle, StartInventoryPool, DeathLink


herecomesniko_options: Dict[str, type(Option)] = {
    "start_inventory_from_pool": StartInventoryPool,
    "death_link": DeathLink
}