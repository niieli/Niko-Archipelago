from dataclasses import dataclass
from typing import Dict

from Options import Choice, Option, Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions


class ShuffleKioskReward(Toggle):
    """Choose whether to shuffle the Kiosk to NOT give a new level but instead something else."""
    display_name = "Shuffle Kiosk Reward"


@dataclass
class HereComesNikoOptions(PerGameCommonOptions):
    shuffle_kiosk_reward: ShuffleKioskReward
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink