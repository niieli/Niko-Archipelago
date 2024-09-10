from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld

def universal_item_rule(item):
    pass

def has_all_coins(state, player):
    return state.has("Coin", player, 76)

def get_region_rules(player):
    return {
        "Tadpole HQ -> Home Party":
            lambda state: state.has("Coin", player, 46),
        "Home -> Hairball City":
            lambda state: state.has("Hairball City", player),
        "Hairball City -> Turbine Town":
            lambda state: state.has("Coin", player),
        "Turbine Town -> Salmon Creek":
            lambda state: state.has("Coin", player),
        "Salmon Creek Forest -> Public Pool":
            lambda state: state.has("Coin", player),
        "Public Pool -> Bathhouse":
            lambda state: state.has("Coin", player),
        "Bathhouse -> Tadpole HQ":
            lambda state: state.has("Coin", player),
    }

def get_location_rules(player):
    return {
        "Home Kiosk":
            lambda state: state.has("Coin", player, 1),
        "Hairball City Kiosk":
            lambda state: state.has("Coin", player, 6),
        "Turbine Town Kiosk":
            lambda state: state.has("Coin", player, 11),
        "Salmon Creek Forest Kiosk":
            lambda state: state.has("Coin", player, 21),
        "Public Pool Kiosk":
            lambda state: state.has("Coin", player, 26),
        "Bathhouse Kiosk":
            lambda state: state.has("Coin", player, 31),
    }
