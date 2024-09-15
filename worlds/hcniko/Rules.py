from . import Options
from .Options import *

def universal_item_rule(item):
    pass

def has_all_coins(state, player):
    return state.has("Coin", player, 76)

def can_talk_to_peper(state, player):
    return state.has("Coin", player, 46)

def has_enough_cassettes(state, player, int):
    return state.has("Cassette", player, int*5)

def has_superjump(state, player):
    return state.has("Super Jump", player)

def superjump_logic():
    return True if Options.TalkToPepperWithSuperJumpOnly.value else False

def get_region_rules(player):
    return {
        "Home -> Hairball City":
            lambda state: state.has("Hairball City Ticket", player),
        "Hairball City -> Turbine Town":
            lambda state: state.has("Turbine Town Ticket", player),
        "Turbine Town -> Salmon Creek Forest":
            lambda state: state.has("Salmon Creek Forest Ticket", player),
        "Salmon Creek Forest -> Public Pool":
            lambda state: state.has("Public Pool Ticket", player),
        "Public Pool -> Bathhouse":
            lambda state: state.has("Bathhouse Ticket", player),
        "Bathhouse -> Tadpole HQ":
            lambda state: state.has("Tadpole HQ Ticket", player),
        "Tadpole HQ -> Home Party":
            lambda state: can_talk_to_peper(state, player)
                          #or has_superjump(state,player) and superjump_logic(),
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
        "Employee Of The Month!":
            lambda state: has_all_coins(state, player),
        "Dustan on lighthouse":
            lambda state: state.has("Key", player, 1),
        "Help Blippy 2 (PP)":
            lambda state: state.has("Key", player, 2),
        "Help Paul":
            lambda state: state.has("Key", player, 3),
        "Help Blippy Coin (HQ)":
            lambda state: state.has("Key", player, 4),
        "Behind frog statue (HC)":
            lambda state: state.has("Key", player, 5),
        "Letter in locked cave":
            lambda state: state.has("Key", player, 6),
        "Mahjong hideout":
            lambda state: state.has("Key", player, 7),
        "Give Mai 5 Cassettes (SCF)":
            lambda state: state.has("Contact List 1", player) and has_enough_cassettes(state,player,1) and state.has("Key", player, 8),
        "Give Mitch 5 Cassettes (SCF)":
            lambda state: has_enough_cassettes(state, player, 2),
        "Give Mai 5 Cassettes (PP)":
            lambda state: has_enough_cassettes(state, player, 3),
        "Give Mitch 5 Cassettes (Bath)":
            lambda state: has_enough_cassettes(state, player, 4),
        "Give Mai 5 Cassettes (Bath)":
            lambda state: has_enough_cassettes(state, player, 5),
        "Give Mai 5 Cassettes (HQ)":
            lambda state: has_enough_cassettes(state, player, 6),
        "Give Mitch 5 Cassettes (HQ)":
            lambda state: has_enough_cassettes(state, player, 7),
        "Fish with Fischer (SCF)":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_1":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_2":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_3":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_4":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL2_1":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_2":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_3":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_4":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL1_1 (TT)":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_2 (TT)":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL1_3 (TT)":
            lambda state: state.has("Contact List 1", player),
        "Unknown CL2_1 (TT)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_2 (TT)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_1 (SCF)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_2 (SCF)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_3 (SCF)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_1 (PP)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_2 (PP)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_3 (PP)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_4 (PP)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_1 (Bath)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_2 (Bath)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_3 (Bath)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_4 (Bath)":
            lambda state: state.has("Contact List 2", player),
        "Unknown CL2_5 (Bath)":
            lambda state: state.has("Contact List 2", player),
    }
