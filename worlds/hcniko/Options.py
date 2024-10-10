from dataclasses import dataclass
from Options import Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions, Choice, Range

def adjust_options(world: "HereComesNikoWorld"):
    if world.options.max_kiosk_cost < world.options.min_kiosk_cost:
        world.options.max_kiosk_cost.value, world.options.min_kiosk_cost.value = \
         world.options.min_kiosk_cost.value, world.options.max_kiosk_cost.value

    if world.options.max_elevator_cost < world.options.min_elevator_cost:
        world.options.max_elevator_cost.value, world.options.min_elevator_cost.value = \
         world.options.min_elevator_cost.value, world.options.max_elevator_cost.value

    tot_coins: int = total_coins(world)
    if world.options.max_kiosk_cost > tot_coins - 6:
        world.options.max_kiosk_cost.value = min(70, tot_coins - 6)

    if world.options.min_kiosk_cost > tot_coins - 6:
        world.options.min_kiosk_cost.value = min(70, tot_coins - 6)

    if world.options.max_elevator_cost > tot_coins:
        world.options.max_elevator_cost.value = min(79, tot_coins)

    if world.options.min_elevator_cost > tot_coins:
        world.options.min_elevator_cost.value = min(79, tot_coins)

def total_coins(world: "HereComesNikoWorld") -> int:
    count: int = 76
    if world.options.shuffle_garys_garden.value:
        count += 3

    return count

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
    option_disabled = 2
    default = 2


class ShuffleHandsomeFrog(Toggle):
    """Enables if talking to Handsome Frog should be a location."""
    display_name = "Shuffle Handsome Frog"


class ShuffleGarysGarden(Toggle):
    """Choose whether Gary's Garden should have locations."""
    display_name = "Shuffle Gary's Garden"
    default = 1


class GoalCompletion(Choice):
    """Set your Completion Goal.
    Hired: Reach Pepper's Interview and get hired!
    Employee: Get 76 Coins and be the Employee Of The Month!"""
    display_name = "Completion Goal"
    option_hired = 0
    option_employee = 1
    default = 0


class MinKioskCost(Range):
    """Determines the lowest possible cost for a Kiosk.
    Disabled if 'Shuffle Kiosk Reward' is false"""
    display_name = "Minimum Kiosk Cost"
    range_start = 0
    range_end = 55
    default = 1


class MaxKioskCost(Range):
    """Determines the highest possible cost for a Kiosk.
    Disabled if 'Shuffle Kiosk Reward' is false"""
    display_name = "Maximum Kiosk Cost"
    range_start = 20
    range_end = 70
    default = 38


class MinElevatorCost(Range):
    """Determines the lowest possible cost for the elevator"""
    display_name = "Minimum Elevator Repair Cost"
    range_start = 0
    range_end = 79
    default = 46


class MaxElevatorCost(Range):
    """Determines the highest possible cost for the elevator"""
    display_name = "Maximum Elevator Repair Cost"
    range_start = 0
    range_end = 79
    default = 46


class CassetteLogic(Choice):
    """This changes how Mitch & Mai work

    levelbased: Hairball City Mitch/Mai want 5/10 Cassettes, Turbine Town Mitch/Mai want 15/20, SCF Mitch/Mai want 25/30,
    Public Pool Mitch/Mai want 35/40, Bathhouse Mitch/Mai want 45/50, Tadpole HQ Mitch/Mai want 55/60 and (if enabled) Gary's Garden Mitch/Mai want 65/70.
    Scattered: Prices are randomly shuffled between all Mitch & Mai Locations"""
    #"Progressive: !!NOT IMPLEMENTED!! Mitch/Mai will need progressively more Cassettes. 5 -> 10 -> 15 -> 20 -> 25 | Level doesn't matter."
    display_name = "Cassette Logic"
    option_Level_Based = 0
    #option_progressive = 1
    option_scattered = 2
    default = 2


class ProgressiveContactList(Toggle):
    """If this option is enabled, the Contact Lists will not be separate, so you cannot get Contact List 2 before Contact List 1."""
    display_name = "Progressive Contact List"
    default = 1


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
    goal_completion: GoalCompletion
    min_kiosk_cost: MinKioskCost
    max_kiosk_cost: MaxKioskCost
    min_elevator_cost: MinElevatorCost
    max_elevator_cost: MaxElevatorCost
    cassette_logic: CassetteLogic
    progressive_contact_list: ProgressiveContactList
    fishsanity: Fishsanity
    start_inventory_from_pool: StartInventoryPool
    death_link: HCNDeathLink