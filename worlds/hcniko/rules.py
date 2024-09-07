from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld

def universal_item_rule(item):
    pass

def get_region_rules(player):
    return {
        "Tadpole HQ -> Home Party":
            lambda state: state.has("Coin", player, 46)
    }

def get_location_rules(player):
    return {
        "You're hired!":
            lambda state: state.has("Coin", player, 46)
    }
