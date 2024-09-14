def universal_item_rule(item):
    pass

def has_all_coins(state, player):
    return state.has("Coin", player, 76)

def can_talk_to_peper(state, player):
    return state.has("Coin", player, 46)

def get_region_rules(player):
    return {
        "Home -> Hairball City":
            lambda state: state.has("Hairball City", player),
        "Hairball City -> Turbine Town":
            lambda state: state.has("Turbine Town", player),
        "Turbine Town -> Salmon Creek Forest":
            lambda state: state.has("Salmon Creek Forest", player),
        "Salmon Creek Forest -> Public Pool":
            lambda state: state.has("Public Pool", player),
        "Public Pool -> Bathhouse":
            lambda state: state.has("Bathhouse", player),
        "Bathhouse -> Tadpole HQ":
            lambda state: state.has("Tadpole HQ", player),
        "Tadpole HQ -> Home Party":
            lambda state: can_talk_to_peper(state, player),
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
        "Dustan on lighthouse":
            lambda state: state.has("Key", player),
        "Help Blippy 2 (PP)":
            lambda state: state.has("Key", player),
        "Help Paul":
            lambda state: state.has("Key", player),
        "Help Blippy Coin (HQ)":
            lambda state: state.has("Key", player),
        "Behind frog statue (HC)":
            lambda state: state.has("Key", player),
        "Letter in locked cave":
            lambda state: state.has("Key", player),
        "Mahjong hideout":
            lambda state: state.has("Key", player),
        "Give Mai 5 Cassettes (SCF)":
            lambda state: state.has("Contact List 1", player),
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
