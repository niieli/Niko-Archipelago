from dataclasses import dataclass

from Options import Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions


class ShuffleKioskReward(Toggle):
    """Choose whether to shuffle the Kiosk to NOT give a new level but instead something else."""
    display_name = "Shuffle Kiosk Reward"


class EnableAchievements(Toggle):
    """Enables if Achievements should be a location. If NOT it will be junk"""
    display_name = "Enable Achievements"


class ShuffleHandsomeFrog(Toggle):
    """Enables if talking to Handsome Frog should be a location. If NOT it will be junk"""
    display_name = "Enable Achievements"


class ShufflGarysGarden(Toggle):
    """Choose whether Gary's Garden should have locations. If NOT it will ONLY contain junk"""
    display_name = "Shuffle Gary's Garden"


class TalkToPepperWithSuperJumpOnly(Toggle):
    """If Enabled, taking to Pepper in Tadpole HQ is logically accessible with only Super Jump"""
    display_name = "Pepper with Super Jump only"


class HCNDeathLink(DeathLink):
    """When somebody dies the level will be reloaded"""

@dataclass
class HereComesNikoOptions(PerGameCommonOptions):
    shuffle_kiosk_reward: ShuffleKioskReward
    enable_achievements: EnableAchievements
    shuffle_handsome_frog: ShuffleHandsomeFrog
    shuffle_garys_garden: ShufflGarysGarden
    superjump_only: TalkToPepperWithSuperJumpOnly
    start_inventory_from_pool: StartInventoryPool
    death_link: HCNDeathLink