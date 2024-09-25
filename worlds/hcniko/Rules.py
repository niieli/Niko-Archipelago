from . import Options
from .Options import *

def has_all_coins(state, player):
    return state.has("Coin", player, 76)

def can_talk_to_peper(state, player):
    return state.has("Coin", player, 46)

def has_enough_cassettes(state, player, int):
    return state.has("Cassette", player, int*5)

def has_all_tickets(state, player):
    return (state.has("Hairball City Ticket", player)
            and state.has("Turbine Town Ticket", player)
            and state.has("Salmon Creek Forest Ticket", player)
            and state.has("Public Pool Ticket", player)
            and state.has("Bathhouse Ticket", player)
            and state.has("Tadpole HQ Ticket", player))

def get_region_rules(player):
    return {
        "Home -> Hairball City":
            lambda state: state.has("Hairball City Ticket", player),
        "Home -> Turbine Town":
            lambda state: state.has("Turbine Town Ticket", player),
        "Home -> Salmon Creek Forest":
            lambda state: state.has("Salmon Creek Forest Ticket", player),
        "Home -> Public Pool":
            lambda state: state.has("Public Pool Ticket", player),
        "Home -> Bathhouse":
            lambda state: state.has("Bathhouse Ticket", player),
        "Home -> Tadpole HQ":
            lambda state: state.has("Tadpole HQ Ticket", player),
        "Tadpole HQ -> Home Party":
            lambda state: can_talk_to_peper(state, player)
    }

def get_location_rules(player):
    return {
        "Home - Kiosk":
            lambda state: state.has("Coin", player, 1),
        "Hairball City - Kiosk":
            lambda state: state.has("Coin", player, 6),
        "Turbine Town - Kiosk":
            lambda state: state.has("Coin", player, 11),
        "Salmon Creek Forest - Kiosk":
            lambda state: state.has("Coin", player, 21),
        "Public Pool - Kiosk":
            lambda state: state.has("Coin", player, 26),
        "Bathhouse - Kiosk":
            lambda state: state.has("Coin", player, 31),
        "Employee Of The Month!":
            lambda state: has_all_coins(state, player),
        "Bottled Up":
            lambda state: state.has("Hairball City Ticket", player)
                          and state.has("Turbine Town Ticket", player)
                          and state.has("Salmon Creek Forest Ticket", player)
                          and state.has("Public Pool Ticket", player)
                          and state.has("Bathhouse Ticket", player),
        "Hopeless Romantic":
            lambda state: state.has("Hairball City Ticket", player)
                          and state.has("Turbine Town Ticket", player)
                          and state.has("Salmon Creek Forest Ticket", player)
                          and state.has("Public Pool Ticket", player)
                          and state.has("Bathhouse Ticket", player),
        "Volley Dreams":
            lambda state: has_all_tickets(state, player),
        "Hairball City - Dustan on Lighthouse":
            lambda state: state.has("Key", player, 1),
        "Public Pool - Blippy Coin":
            lambda state: state.has("Key", player, 2),
        "Bathhouse - Poppy":
            lambda state: state.has("Key", player, 3),
        "Tadpole HQ - Blippy Coin":
            lambda state: state.has("Key", player, 4),
        "Hairball City - Cassette behind Frog Statue":
            lambda state: state.has("Key", player, 5),
        "Salmon Creek Forest - Letter inside locked Cave":
            lambda state: state.has("Key", player, 6),
        "Mahjong hideout":
            lambda state: state.has("Key", player, 7),
        "Salmon Creek Forest - Fish with Fischer":
            lambda state: state.has("Contact List 1", player),
        "Hairball City - Nina":
            lambda state: state.has("Contact List 1", player),
        "Hairball City - Moomy":
            lambda state: state.has("Contact List 1", player),
        "Hairball City - Game Kid":
            lambda state: state.has("Contact List 2", player),
        "Hairball City - Blippy Dog":
            lambda state: state.has("Contact List 2", player),
        "Hairball City - Blippy Coin":
            lambda state: state.has("Contact List 2", player),
        "Hairball City - Serschel & Louist":
            lambda state: state.has("Contact List 2", player),
        "Turbine Town - Blippy Dog":
            lambda state: state.has("Contact List 1", player),
        "Turbine Town - Blippy Coin":
            lambda state: state.has("Contact List 2", player),
        "Turbine Town - Serschel & Louist":
            lambda state: state.has("Contact List 2", player),
        "Salmon Creek Forest - Game Kid":
            lambda state: state.has("Contact List 2", player),
        "Salmon Creek Forest - Blippy Coin":
            lambda state: state.has("Contact List 2", player),
        "Salmon Creek Forest - Serschel & Louist":
            lambda state: state.has("Contact List 2", player),
        "Public Pool - SPORTVIVAL VOLLEY":
            lambda state: state.has("Contact List 2", player),
        "Public Pool - Blessley":
            lambda state: state.has("Contact List 2", player),
        "Public Pool - Little Gabi's Flowers":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Fish with Fischer":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Blessley":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Little Gabi's Flowers":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Blippy Dog":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Blippy Coin":
            lambda state: state.has("Contact List 2", player),
        "Dustan - Meeting First Time":
            lambda state: state.has("Hairball City Ticket", player)
                          or state.has("Turbine Town Ticket", player)
                          or state.has("Salmon Creek Forest Ticket", player)
                          or state.has("Bathhouse Ticket", player),
        #Cassette
        "Hairball City - Give Mitch 5 Cassettes":
            lambda state: state.has("Contact List 1", player)
                          and has_enough_cassettes(state, player, 1),
        "Hairball City - Give Mai 5 Cassettes":
            lambda state: state.has("Contact List 1", player)
                          and has_enough_cassettes(state, player, 2),
        "Turbine Town - Give Mitch 5 Cassettes":
            lambda state: state.has("Contact List 1", player)
                          and has_enough_cassettes(state, player, 3),
        "Turbine Town - Give Mai 5 Cassettes":
            lambda state: state.has("Contact List 1", player)
                          and has_enough_cassettes(state, player, 4),
        "Salmon Creek Forest - Give Mai 5 Cassettes":
            lambda state: state.has("Contact List 1", player)
                          and has_enough_cassettes(state, player, 5)
                          and state.has("Key", player, 8),
        "Salmon Creek Forest - Give Mitch 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 6),
        "Public Pool - Give Mitch 5 Cassettes":
            lambda state: state.has("Contact List 2", player)
                          and has_enough_cassettes(state, player, 7),
        "Public Pool - Give Mai 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 8),
        "Bathhouse - Give Mitch 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 9),
        "Bathhouse - Give Mai 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 10),
        "Tadpole HQ - Give Mai 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 11),
        "Tadpole HQ - Give Mitch 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 12),
        "Gary's Garden - Give Mai 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 13),
        "Gary's Garden - Give Mitch 5 Cassettes":
            lambda state: has_enough_cassettes(state, player, 14),
        "Salmon Creek Forest - Bass":
            lambda state: state.has("Contact List 1", player),
        "Salmon Creek Forest - Catfish":
            lambda state: state.has("Contact List 1", player),
        "Salmon Creek Forest - Pike":
            lambda state: state.has("Contact List 1", player),
        "Salmon Creek Forest - Salmon":
            lambda state: state.has("Contact List 1", player),
        "Salmon Creek Forest - Trout":
            lambda state: state.has("Contact List 1", player),
        "Bathhouse - Anglerfish":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Clione":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Little Wiggly Guy":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Jellyfish":
            lambda state: state.has("Contact List 2", player),
        "Bathhouse - Pufferfish":
            lambda state: state.has("Contact List 2", player),
    }