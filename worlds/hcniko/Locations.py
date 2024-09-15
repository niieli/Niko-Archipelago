from typing import Dict, NamedTuple, Callable, Optional

from BaseClasses import Location


class HereComesNikoLocation(Location):
    game = "Here Comes Niko!"


class HereComesNikoLocationData(NamedTuple):
    region: str
    id: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None

base_id = 598_145_444_000

location_data_table: Dict[str, HereComesNikoLocationData] = {
    # Coins
    "Give High Frog Lunchbox": HereComesNikoLocationData(region="Home",id=base_id + 0),
    # ~ Hairball City
    "Win BIG VOLLEY (HC)": HereComesNikoLocationData(region="Hairball City", id=base_id + 3),
    "Dustan on lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 4),
    "Gabi's Flowers (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 5),
    "Gunter on Skyscraper": HereComesNikoLocationData(region="Hairball City",id=base_id + 6),
    "Fish with Fischer (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 7),
    "Give Blessley 30 bugs (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 8),
    "Unknown CL1_1": HereComesNikoLocationData(region="Hairball City",id=base_id + 9),
    "Unknown CL1_2": HereComesNikoLocationData(region="Hairball City",id=base_id + 10),
    "Unknown CL1_3": HereComesNikoLocationData(region="Hairball City",id=base_id + 11),
    "Unknown CL1_4": HereComesNikoLocationData(region="Hairball City",id=base_id + 12),
    "Unknown CL2_1": HereComesNikoLocationData(region="Hairball City",id=base_id + 13),
    "Unknown CL2_2": HereComesNikoLocationData(region="Hairball City",id=base_id + 14),
    "Unknown CL2_3": HereComesNikoLocationData(region="Hairball City",id=base_id + 15),
    "Unknown CL2_4": HereComesNikoLocationData(region="Hairball City",id=base_id + 16),
    # ~ Turbine Town
    "Fish with Fischer (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 17),
    "Win AIR VOLLEY (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 18),
    "Gabi's Flowers (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 19),
    "Bring back the wind": HereComesNikoLocationData(region="Turbine Town",id=base_id + 20),
    "Give Blessley 30 bugs (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 21),
    "Dustan on wind turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 22),
    "Unknown CL1_1 (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 23),
    "Unknown CL1_2 (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 24),
    "Unknown CL1_3 (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 25),
    "Unknown CL2_1 (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 26),
    "Unknown CL2_2 (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 27),
    # ~ Salmon Creek Forest
    "Get Stijn and Melissa together": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 28),
    "Give Mitch 5 Cassettes (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 29),
    "Dustan on mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 30),
    "Collect all 10 seeds (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 31),
    "Collect 5 Bones (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 32),
    "Help the tree": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 33),
    "Give Blessley 30 bugs (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 34),
    "Secret waterfall cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 35),
    "Win SPORTVIVAL (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 36),
    "Gabi's Flowers (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 37),
    "Paint 5 graffiti near Nina (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 38),
    "Give Mai 5 Cassettes (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 39),
    "Fish with Fischer (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 40),
    "Unknown CL2_1 (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 41),
    "Unknown CL2_2 (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 42),
    "Unknown CL2_3 (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 43),
    # ~ Public Pool
    "End of 2D section": HereComesNikoLocationData(region="Public Pool",id=base_id + 44),
    "Give Mai 5 Cassettes (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 45),
    "Help Blippy (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 46),
    "Help Blippy 2 (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 47),
    "Fish with Fischer (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 48),
    "Solve the crime": HereComesNikoLocationData(region="Public Pool",id=base_id + 49),
    "Unknown CL2_1 (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 50),
    "Unknown CL2_2 (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 51),
    "Unknown CL2_3 (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 52),
    "Unknown CL2_4 (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 53),
    # ~ Bathhouse
    "Bring Louist to Serschel (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 54),
    "Collect all 10 seeds (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 55),
    "Help Paul": HereComesNikoLocationData(region="Bathhouse",id=base_id + 56),
    "Paint 5 graffiti near Nina (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 57),
    "Give Mitch 5 Cassettes (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 58),
    "Give Mai 5 Cassettes (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 59),
    "Dustan on Bathhouse": HereComesNikoLocationData(region="Bathhouse",id=base_id + 60),
    "Win LONG VOLLEY (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 61),
    "Beat Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 62),
    "Unknown CL2_1 (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 63),
    "Unknown CL2_2 (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 64),
    "Unknown CL2_3 (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 65),
    "Unknown CL2_4 (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 66),
    "Unknown CL2_5 (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 67),
    # ~ Tadpole HQ
    "Give Mai 5 Cassettes (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 68),
    "Give Mitch 5 Cassettes (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 69),
    "Listen to King Frog": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 70),
    "Win HUGE VOLLEY (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 71),
    "Fish with Fischer (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 72),
    "Gabi's Flowers (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 73),
    "Help Blippy Coin (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 74),
    "Give Blessley 30 bugs (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 75),
    "Bring Louist to Serschel (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 76),
    "Help Blippy Bone (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 77),

    # Letters
    "Letter near crane": HereComesNikoLocationData(region="Home",id=base_id + 80),
    "Letter on a tree": HereComesNikoLocationData(region="Hairball City",id=base_id + 81),
    "Letter behind train": HereComesNikoLocationData(region="Hairball City",id=base_id + 82),
    "Letter behind wind dragon": HereComesNikoLocationData(region="Turbine Town",id=base_id + 83),
    "Letter in sunken container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 84),
    "Letter in locked cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 85),
    "Letter behind waterfall": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 86),
    "Letter start of 2D section": HereComesNikoLocationData(region="Public Pool",id=base_id + 87),
    "Letter end of 2D section": HereComesNikoLocationData(region="Public Pool",id=base_id + 88),
    "Letter behind axolotl family": HereComesNikoLocationData(region="Bathhouse",id=base_id + 89),
    "Letter near Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 90),

    # Keys
    "Key inside container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 91),
    "Key on tall island": HereComesNikoLocationData(region="Turbine Town",id=base_id + 92),
    "Key on rock in ocean": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 93),
    "Key in pond": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 94),
    "Key near SPORTVIVAL": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 95),
    "Key over breakable box": HereComesNikoLocationData(region="Public Pool",id=base_id + 96),
    "Key on torii": HereComesNikoLocationData(region="Bathhouse",id=base_id + 97),
    "Key near bathhouse box": HereComesNikoLocationData(region="Bathhouse",id=base_id + 98),
    "Key under Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 99),

    # Cassettes
    "Cassette Behind Pepper": HereComesNikoLocationData(region="Hairball City",id=base_id+100),
    "On frog statue (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 101),
    "Big umbrella": HereComesNikoLocationData(region="Hairball City",id=base_id + 102),
    "Lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 103),
    "On palm tree (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 104),
    "Inside the tunnel": HereComesNikoLocationData(region="Hairball City",id=base_id + 105),
    "Breakable box on small island": HereComesNikoLocationData(region="Hairball City",id=base_id + 106),
    "Behind lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 107),
    "Near bench on small island": HereComesNikoLocationData(region="Hairball City",id=base_id + 108),
    "Behind frog statue (HC)": HereComesNikoLocationData(region="Hairball City",id=base_id + 109),
    #  ~ Turbine Town
    "Inside container on water": HereComesNikoLocationData(region="Turbine Town",id=base_id + 111),
    "Rocks on water": HereComesNikoLocationData(region="Turbine Town",id=base_id + 112),
    "On top of containers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 113),
    "Behind Blessley (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 114),
    "Container with A LOT of buttons": HereComesNikoLocationData(region="Turbine Town",id=base_id + 115),
    "Inside container behind Pepper": HereComesNikoLocationData(region="Turbine Town",id=base_id + 116),
    "Next to turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 117),
    "Next to torii gates": HereComesNikoLocationData(region="Turbine Town",id=base_id + 118),
    "Near fishing containers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 119),
    "Floating above water (TT)": HereComesNikoLocationData(region="Turbine Town",id=base_id + 120),
    #  ~ Salmon Creek Forest
    "Behind train": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 122),
    "Wooden bridge": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 123),
    "On treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 124),
    "Rocks near mountain (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 125),
    "Near void in waterfall cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 126),
    "Inside boxes behind waterfall cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 127),
    "Next to treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 128),
    "Rocks in ocean (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 129),
    "Behind mountain (SCF)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 130),
    "Next to Treeman": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 131),
    "Near hamster ball": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 132),
    #  ~ Public Pool
    "Frog statue (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 134),
    "On springboard": HereComesNikoLocationData(region="Public Pool",id=base_id + 135),
    "Small island on the left": HereComesNikoLocationData(region="Public Pool",id=base_id + 136),
    "Rocks in ocean (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 137),
    "Inside the pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 138),
    "Inside the BIG pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 139),
    "Behind frog statue (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 140),
    "Palm tree (PP)": HereComesNikoLocationData(region="Public Pool",id=base_id + 141),
    "Breakable box in pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 142),
    "Above BIG pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 143),
    #  ~ Bathhouse
    "Frog statue butt (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 145),
    "Near axolotl family in water": HereComesNikoLocationData(region="Bathhouse",id=base_id + 146),
    "Hut in water": HereComesNikoLocationData(region="Bathhouse",id=base_id + 147),
    "Giant frog statue (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 148),
    "Lamp near Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 149),
    "Behind LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 150),
    "Behind waterfall (Bath)": HereComesNikoLocationData(region="Bathhouse",id=base_id + 151),
    "Fan to fan": HereComesNikoLocationData(region="Bathhouse",id=base_id + 152),
    "On pipes": HereComesNikoLocationData(region="Bathhouse",id=base_id + 153),
    "Mahjong hideout": HereComesNikoLocationData(region="Bathhouse",id=base_id + 154),
    # ~ Tadpole HQ
    "Between skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 156),
    "Next to skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 157),
    "?": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 158),
    "Main skyscraper backside": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 159),
    "??": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 160),
    "King frog statue": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 161),
    "Breakable box near Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 162),
    "Rocks in ocean (HQ)": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 163),
    "Under giant umbrella": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 164),
    "Inbetween buildings": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 165),

    # Misc
    "Give 250 Apples to Dojo guy": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 166),
    "Contact List 1": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 167),
    "Contact List 2": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 168),

    # Achievements
    "Frog Fan": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 176, can_create=lambda options: options.enable_achievements.value),
    "Employee Of The Month!": HereComesNikoLocationData(region="Home", id=base_id + 177, can_create=lambda options: options.enable_achievements.value),
    "Bottled Up": HereComesNikoLocationData(region="Bathhouse", id=base_id + 178, can_create=lambda options: options.enable_achievements.value),
    "Snail Fashion Show": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 179, can_create=lambda options: options.enable_achievements.value),
    "Volley Dreams": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 180, can_create=lambda options: options.enable_achievements.value),
    "Hopeless Romantic": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 181, can_create=lambda options: options.enable_achievements.value),
    "Lost at Sea": HereComesNikoLocationData(region="Home", id=base_id + 182, can_create=lambda options: options.enable_achievements.value),

    # DLC Garden
    "Cassette 1": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 183, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 2": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 184, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 3": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 185, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 4": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 186, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 5": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 187, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 6": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 188, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 7": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 189, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 8": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 190, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 9": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 191, can_create=lambda options: options.shuffle_garys_garden.value),
    "Cassette 10": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 192, can_create=lambda options: options.shuffle_garys_garden.value),

    # Handsome Frog
    "Hairball City - Handsome Frog": HereComesNikoLocationData(region="Hairball City",id=base_id + 193, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Turbine Town - Handsome Frog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 194, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Salmon Creek Forest - Handsome Frog": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 195, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Public Pool - Handsome Frog": HereComesNikoLocationData(region="Public Pool",id=base_id + 196, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Bathhouse - Handsome Frog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 197, can_create=lambda options: options.shuffle_handsome_frog.value),

    # Kiosk
    "Home Kiosk": HereComesNikoLocationData(region="Home",id=base_id + 170),
    "Hairball City Kiosk": HereComesNikoLocationData(region="Hairball City",id=base_id + 171),
    "Turbine Town Kiosk": HereComesNikoLocationData(region="Turbine Town",id=base_id + 172),
    "Salmon Creek Forest Kiosk": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 173),
    "Public Pool Kiosk": HereComesNikoLocationData(region="Public Pool",id=base_id + 174),
    "Bathhouse Kiosk": HereComesNikoLocationData(region="Bathhouse",id=base_id + 175),

    # Victory
    "Job Interview": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 169),
    "You're Hired!": HereComesNikoLocationData(region="Home Party", locked_item="Victory"),
}

location_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}
id_to_location_table = {data.id: name for name, data in location_data_table.items() if data.id is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}



