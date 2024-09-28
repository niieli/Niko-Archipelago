from dataclasses import dataclass

from Options import Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions, Choice


class ShuffleKioskReward(Toggle):
    """Choose whether to shuffle the Kiosk to NOT give the next Ticket but instead something else.
    Compatible with 'Start with Ticket'.
    Scuffed but works. Check the in-game Tracker for Kiosk Cost and if you bought it."""
    display_name = "Shuffle Kiosk Reward"
    default = 1


class StartWithTicket(Toggle):
    """You'll start with a random Ticket. Highly recommended as there are only 3 checks at Home!"""
    display_name = "Start with Ticket"
    default = 1


class EnableAchievements(Choice):
    """Enables if Achievements should be a location.
    Frog Fan only needs 10 bumps & Volley Dreams only needs a highscore of 5 in every level."""
    display_name = "Enable Achievements"
    option_all_achievements = 0
    option_except_snail_fashion_show = 1


class ShuffleHandsomeFrog(Toggle):
    """Enables if talking to Handsome Frog should be a location."""
    display_name = "Shuffle Handsome Frog"


class ShuffleGarysGarden(Toggle):
    """Choose whether Gary's Garden should have locations."""
    display_name = "Shuffle Gary's Garden"
    default = 1


class CassetteLogic(Choice):
    """This changes how Mitch & Mai work

    levelbased: Hairball City Mitch/Mai want 5/10 Cassettes, Turbine Town Mitch/Mai want 15/20, SCF Mitch/Mai want 25/30,
    Public Pool Mitch/Mai want 35/40, Bathhouse Mitch/Mai want 45/50, Tadpole HQ Mitch/Mai want 55/60 and (if enabled) Gary's Garden Mitch/Mai want 65/70.
    progressive: NOT IMPLEMENTED Mitch/Mai will need progressively more Cassettes. 5 -> 10 -> 15 -> 20 -> 25 | Level doesn't matter."""
    display_name = "Cassette Logic"
    option_Level_Based = 0
    option_progressive = 1
    default = 0


class Fishsanity(Toggle):
    """Every single fish you can fish with Fischer is a unique location."""
    display_name = "Fishsanity"


class HCNDeathLink(DeathLink):
    """When somebody dies the level will be reloaded"""

@dataclass
class HereComesNikoOptions(PerGameCommonOptions):
    shuffle_kiosk_reward: ShuffleKioskReward
    start_with_ticket: StartWithTicket
    enable_achievements: EnableAchievements
    shuffle_handsome_frog: ShuffleHandsomeFrog
    shuffle_garys_garden: ShuffleGarysGarden
    cassette_logic: CassetteLogic
    fishsanity: Fishsanity
    start_inventory_from_pool: StartInventoryPool
    death_link: HCNDeathLink