from typing import Dict

from Options import Choice, Option, Toggle, StartInventoryPool, DeathLink


class ShuffleKioskReward(Toggle):
    """Choose whether to shuffle the Kiosk to NOT give a new level but instead something else."""
    display_name = "Shuffle Kiosk Reward"

hcn_options: Dict[str, type(Option)] = {
    "start_inventory_from_pool": StartInventoryPool,
    "shuffle_kiosk_reward": ShuffleKioskReward,
    "death_link": DeathLink
}