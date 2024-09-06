from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class HereComesNikoLocation(Location):
    game = "Here Comes Niko!"


class HereComesNikoLocationData(NamedTuple):
    region: str
    id: int

base_id = 598_145_444_000

coin_location_table: Dict[str, HereComesNikoLocationData] = {
    "Give High Frog Lunchbox": HereComesNikoLocationData("Home", base_id + 0),
    "Letter near crane": HereComesNikoLocationData("Home", base_id + 1),
    "Get hired": HereComesNikoLocationData("Home", base_id + 2),
    "Win BIG VOLLEY (HC)": HereComesNikoLocationData("Hairball City", base_id + 3),
    "Dustan on lighthouse": HereComesNikoLocationData("Hairball City", base_id + 4),
    "Gabi's Flowers (HC)": HereComesNikoLocationData("Hairball City", base_id + 5),
    "Gunter on Skyscraper": HereComesNikoLocationData("Hairball City", base_id + 6),
    "Fish with Fischer (HC)": HereComesNikoLocationData("Hairball City", base_id + 7),
    "Give Blessley 30 bugs (HC)": HereComesNikoLocationData("Hairball City", base_id + 8),
    "Unknown CL1_1": HereComesNikoLocationData("Hairball City", base_id + 9),
    "Unknown CL1_2": HereComesNikoLocationData("Hairball City", base_id + 10),
    "Unknown CL1_3": HereComesNikoLocationData("Hairball City", base_id + 11),
    "Unknown CL1_4": HereComesNikoLocationData("Hairball City", base_id + 12),
    "Unknown CL2_1": HereComesNikoLocationData("Hairball City", base_id + 13),
    "Unknown CL2_2": HereComesNikoLocationData("Hairball City", base_id + 14),
    "Unknown CL2_3": HereComesNikoLocationData("Hairball City", base_id + 15),
    "Unknown CL2_4": HereComesNikoLocationData("Hairball City", base_id + 16),
    "Fish with Fischer (TT)": HereComesNikoLocationData("Turbine Town", base_id + 17),
    "Win AIR VOLLEY (TT)": HereComesNikoLocationData("Turbine Town", base_id + 18),
    "Gabi's Flowers (TT)": HereComesNikoLocationData("Turbine Town", base_id + 19),
    "Bring back the wind": HereComesNikoLocationData("Turbine Town", base_id + 20),
    "Give Blessley 30 bugs (TT)": HereComesNikoLocationData("Turbine Town", base_id + 21),
    "Dustan on wind turbine": HereComesNikoLocationData("Turbine Town", base_id + 22),
    "Unknown CL1_1 (TT)": HereComesNikoLocationData("Turbine Town", base_id + 23),
    "Unknown CL1_2 (TT)": HereComesNikoLocationData("Turbine Town", base_id + 24),
    "Unknown CL1_3 (TT)": HereComesNikoLocationData("Turbine Town", base_id + 25),
    "Unknown CL2_1 (TT)": HereComesNikoLocationData("Turbine Town", base_id + 26),
    "Unknown CL2_2 (TT)": HereComesNikoLocationData("Turbine Town", base_id + 27),
    "Get Stijn and Melissa together": HereComesNikoLocationData("Salmon Creek Forest", base_id + 28),
    "Give Mitch 5 Cassettes (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 29),
    "Dustan on mountain": HereComesNikoLocationData("Salmon Creek Forest", base_id + 30),
    "Collect all 10 seeds (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 31),
    "Collect 5 Bones (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 32),
    "Help the tree": HereComesNikoLocationData("Salmon Creek Forest", base_id + 33),
    "Give Blessley 30 bugs (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 34),
    "Secret waterfall cave": HereComesNikoLocationData("Salmon Creek Forest", base_id + 35),
    "Win SPORTVIVAL (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 36),
    "Gabi's Flowers (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 37),
    "Paint 5 graffiti near Nina (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 38),
    "Give Mai 5 Cassettes (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 39),
    "Fish with Fischer (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 40),
    "Unknown CL2_1 (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 41),
    "Unknown CL2_2 (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 42),
    "Unknown CL2_3 (SCF)": HereComesNikoLocationData("Salmon Creek Forest", base_id + 43),
    "End of 2D section": HereComesNikoLocationData("Public Pool", base_id + 44),
    "Give Mai 5 Cassettes (PP)": HereComesNikoLocationData("Public Pool", base_id + 45),
    "Help Blippy (PP)": HereComesNikoLocationData("Public Pool", base_id + 46),
    "Help Blippy 2 (PP)": HereComesNikoLocationData("Public Pool", base_id + 47),
    "Fish with Fischer (PP)": HereComesNikoLocationData("Public Pool", base_id + 48),
    "Solve the crime": HereComesNikoLocationData("Public Pool", base_id + 49),
    "Unknown CL2_1 (PP)": HereComesNikoLocationData("Public Pool", base_id + 50),
    "Unknown CL2_2 (PP)": HereComesNikoLocationData("Public Pool", base_id + 51),
    "Unknown CL2_3 (PP)": HereComesNikoLocationData("Public Pool", base_id + 52),
    "Unknown CL2_4 (PP)": HereComesNikoLocationData("Public Pool", base_id + 53),
    "Bring Louist to Serschel (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 54),
    "Collect all 10 seeds (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 55),
    "Help Paul": HereComesNikoLocationData("Bathhouse", base_id + 56),
    "Paint 5 graffiti near Nina (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 57),
    "Give Mitch 5 Cassettes (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 58),
    "Give Mai 5 Cassettes (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 59),
    "Dustan on Bathhouse": HereComesNikoLocationData("Bathhouse", base_id + 60),
    "Win LONG VOLLEY (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 61),
    "Beat Game Kid": HereComesNikoLocationData("Bathhouse", base_id + 62),
    "Unknown CL2_1 (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 63),
    "Unknown CL2_2 (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 64),
    "Unknown CL2_3 (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 65),
    "Unknown CL2_4 (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 66),
    "Unknown CL2_5 (Bath)": HereComesNikoLocationData("Bathhouse", base_id + 67),
    "Give Mai 5 Cassettes (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 68),
    "Give Mitch 5 Cassettes (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 69),
    "Listen to King Frog": HereComesNikoLocationData("Tadpole HQ", base_id + 70),
    "Win HUGE VOLLEY (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 71),
    "Fish with Fischer (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 72),
    "Gabi's Flowers (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 73),
    "Help Blippy Coin (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 74),
    "Give Blessley 30 bugs (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 75),
    "Bring Louist to Serschel (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 76),
    "Help Blippy Bone (HQ)": HereComesNikoLocationData("Tadpole HQ", base_id + 77),
    #"": HereComesNikoLocationData("Home", base_id + 78),
    #"": HereComesNikoLocationData("Home", base_id + 79),
    #"": HereComesNikoLocationData("Home", base_id + 80),
}



