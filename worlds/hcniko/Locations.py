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
    "Home - Give High Frog Lunchbox": HereComesNikoLocationData(region="Home",id=base_id + 0),
    # ~ Hairball City
    "Hairball City - BIG VOLLEY": HereComesNikoLocationData(region="Hairball City", id=base_id + 3),
    "Hairball City - Dustan on Lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 4),
    "Hairball City - Little Gabi's Flowers": HereComesNikoLocationData(region="Hairball City",id=base_id + 5),
    "Hairball City - Gunter on Skyscraper": HereComesNikoLocationData(region="Hairball City",id=base_id + 6),
    "Hairball City - Fish with Fischer": HereComesNikoLocationData(region="Hairball City",id=base_id + 7),
    "Hairball City - Blessley": HereComesNikoLocationData(region="Hairball City",id=base_id + 8),
    "Hairball City - Nina": HereComesNikoLocationData(region="Hairball City",id=base_id + 9),
    "Hairball City - Moomy": HereComesNikoLocationData(region="Hairball City",id=base_id + 10),
    "Hairball City - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Hairball City",id=base_id + 11),
    "Hairball City - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Hairball City",id=base_id + 12),
    "Hairball City - Game Kid": HereComesNikoLocationData(region="Hairball City",id=base_id + 13),
    "Hairball City - Blippy Dog": HereComesNikoLocationData(region="Hairball City",id=base_id + 14),
    "Hairball City - Blippy Coin": HereComesNikoLocationData(region="Hairball City",id=base_id + 15),
    "Hairball City - Serschel & Louist": HereComesNikoLocationData(region="Hairball City",id=base_id + 16),
    # ~ Turbine Town
    "Turbine Town - Fish with Fischer": HereComesNikoLocationData(region="Turbine Town",id=base_id + 17),
    "Turbine Town - AIR VOLLEY": HereComesNikoLocationData(region="Turbine Town",id=base_id + 18),
    "Turbine Town - Little Gabi's Flowers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 19),
    "Turbine Town - Pelly the Engineer": HereComesNikoLocationData(region="Turbine Town",id=base_id + 20),
    "Turbine Town - Blessley": HereComesNikoLocationData(region="Turbine Town",id=base_id + 21),
    "Turbine Town - Dustan on Wind Turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 22),
    "Turbine Town - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Turbine Town",id=base_id + 23),
    "Turbine Town - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Turbine Town",id=base_id + 24),
    "Turbine Town - Blippy Dog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 25),
    "Turbine Town - Blippy Coin": HereComesNikoLocationData(region="Turbine Town",id=base_id + 26),
    "Turbine Town - Serschel & Louist": HereComesNikoLocationData(region="Turbine Town",id=base_id + 27),
    # ~ Salmon Creek Forest
    "Salmon Creek Forest - Stijn & Melissa": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 28),
    "Salmon Creek Forest - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 29),
    "Salmon Creek Forest - Dustan on Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 30),
    "Salmon Creek Forest - Moomy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 31),
    "Salmon Creek Forest - Blippy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 32),
    "Salmon Creek Forest - Treeman": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 33),
    "Salmon Creek Forest - Blessley": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 34),
    "Salmon Creek Forest - Secret of the Forest": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 35),
    "Salmon Creek Forest - SPORTVIVAL": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 36),
    "Salmon Creek Forest - Little Gabi's Flowers": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 37),
    "Salmon Creek Forest - Nina": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 38),
    "Salmon Creek Forest - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 39),
    "Salmon Creek Forest - Fish with Fischer": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 40),
    "Salmon Creek Forest - Game Kid": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 41),
    "Salmon Creek Forest - Blippy Coin": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 42),
    "Salmon Creek Forest - Serschel & Louist": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 43),
    # ~ Public Pool
    "Public Pool - Far Away Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 44),
    "Public Pool - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Public Pool",id=base_id + 45),
    "Public Pool - Blippy Dog": HereComesNikoLocationData(region="Public Pool",id=base_id + 46),
    "Public Pool - Blippy Coin": HereComesNikoLocationData(region="Public Pool",id=base_id + 47),
    "Public Pool - Fish with Fischer": HereComesNikoLocationData(region="Public Pool",id=base_id + 48),
    "Public Pool - Frogtective": HereComesNikoLocationData(region="Public Pool",id=base_id + 49),
    "Public Pool - SPORTVIVAL VOLLEY": HereComesNikoLocationData(region="Public Pool",id=base_id + 50),
    "Public Pool - Blessley": HereComesNikoLocationData(region="Public Pool",id=base_id + 51),
    "Public Pool - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Public Pool",id=base_id + 52),
    "Public Pool - Little Gabi's Flowers": HereComesNikoLocationData(region="Public Pool",id=base_id + 53),
    # ~ Bathhouse
    "Bathhouse - Serschel & Louist": HereComesNikoLocationData(region="Bathhouse",id=base_id + 54),
    "Bathhouse - Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 55),
    "Bathhouse - Poppy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 56),
    "Bathhouse - Nina": HereComesNikoLocationData(region="Bathhouse",id=base_id + 57),
    "Bathhouse - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Bathhouse",id=base_id + 58),
    "Bathhouse - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Bathhouse",id=base_id + 59),
    "Bathhouse - Dustan on Bathhouse": HereComesNikoLocationData(region="Bathhouse",id=base_id + 60),
    "Bathhouse - LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 61),
    "Bathhouse - Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 62),
    "Bathhouse - Fish with Fischer": HereComesNikoLocationData(region="Bathhouse",id=base_id + 63),
    "Bathhouse - Blessley": HereComesNikoLocationData(region="Bathhouse",id=base_id + 64),
    "Bathhouse - Little Gabi's Flowers": HereComesNikoLocationData(region="Bathhouse",id=base_id + 65),
    "Bathhouse - Blippy Dog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 66),
    "Bathhouse - Blippy Coin": HereComesNikoLocationData(region="Bathhouse",id=base_id + 67),
    # ~ Tadpole HQ
    "Tadpole HQ - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 68),
    "Tadpole HQ - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 69),
    "Tadpole HQ - Frog King": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 70),
    "Tadpole HQ - HUGE VOLLEY": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 71),
    "Tadpole HQ - Fish with Fischer": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 72),
    "Tadpole HQ - Little Gabi's Flowers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 73),
    "Tadpole HQ - Blippy Coin": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 74),
    "Tadpole HQ - Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 75),
    "Tadpole HQ - Serschel & Louist": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 76),
    "Tadpole HQ - Blippy Dog": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 77),

    # Letters
    "Home - Letter near Crane": HereComesNikoLocationData(region="Home",id=base_id + 80),
    "Hairball City - Letter in a Tree": HereComesNikoLocationData(region="Hairball City",id=base_id + 81),
    "Hairball City - Letter behind the Train": HereComesNikoLocationData(region="Hairball City",id=base_id + 82),
    "Turbine Town - Letter behind Wind Dragon": HereComesNikoLocationData(region="Turbine Town",id=base_id + 83),
    "Turbine Town - Letter on Shipping Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 84),
    "Salmon Creek Forest - Letter inside locked Cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 85),
    "Salmon Creek Forest - Letter in Secret of the Forest": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 86),
    "Public Pool - Letter on Far Away Island Left": HereComesNikoLocationData(region="Public Pool",id=base_id + 87),
    "Public Pool - Letter on Far Away Island Right": HereComesNikoLocationData(region="Public Pool",id=base_id + 88),
    "Bathhouse - Letter behind Axolotl Family": HereComesNikoLocationData(region="Bathhouse",id=base_id + 89),
    "Bathhouse - Letter behind Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 90),

    # Keys
    "Turbine Town - Key inside Shipping Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 91),
    "Turbine Town - Key on Stone Pillar": HereComesNikoLocationData(region="Turbine Town",id=base_id + 92),
    "Salmon Creek Forest - Key on a Large Rock": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 93),
    "Salmon Creek Forest - Key in Pond": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 94),
    "Salmon Creek Forest - Key behind Frog Statue": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 95),
    "Public Pool - Key above Green Frog Statue": HereComesNikoLocationData(region="Public Pool",id=base_id + 96),
    "Bathhouse - Key on Torii": HereComesNikoLocationData(region="Bathhouse",id=base_id + 97),
    "Bathhouse - Key near Bathhouse Box": HereComesNikoLocationData(region="Bathhouse",id=base_id + 98),
    "Bathhouse - Key under Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 99),

    # Cassettes
    "Hairball City - Cassette behind Pepper": HereComesNikoLocationData(region="Hairball City",id=base_id+100),
    "Hairball City - Cassette on Frog Statue": HereComesNikoLocationData(region="Hairball City",id=base_id + 101),
    "Hairball City - Cassette above Big umbrella": HereComesNikoLocationData(region="Hairball City",id=base_id + 102),
    "Hairball City - Cassette Lighthouse Front Door": HereComesNikoLocationData(region="Hairball City",id=base_id + 103),
    "Hairball City - Cassette on Palm Tree": HereComesNikoLocationData(region="Hairball City",id=base_id + 104),
    "Hairball City - Cassette inside Tunnel": HereComesNikoLocationData(region="Hairball City",id=base_id + 105),
    "Hairball City - Cassette Breakable Box near Lighthouse under ramp": HereComesNikoLocationData(region="Hairball City",id=base_id + 106),
    "Hairball City - Cassette behind Lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 107),
    "Hairball City - Cassette Breakable Box on Small Island near Bench": HereComesNikoLocationData(region="Hairball City",id=base_id + 108),
    "Hairball City - Cassette behind Frog Statue": HereComesNikoLocationData(region="Hairball City",id=base_id + 109),
    #  ~ Turbine Town
    "Turbine Town - Cassette inside partially sunken Shipping Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 111),
    "Turbine Town - Cassette on Cube Rock": HereComesNikoLocationData(region="Turbine Town",id=base_id + 112),
    "Turbine Town - Cassette on top of Containers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 113),
    "Turbine Town - Cassette behind Blessley": HereComesNikoLocationData(region="Turbine Town",id=base_id + 114),
    "Turbine Town - Cassette inside Container with Buttons": HereComesNikoLocationData(region="Turbine Town",id=base_id + 115),
    "Turbine Town - Cassette inside Container behind Pepper": HereComesNikoLocationData(region="Turbine Town",id=base_id + 116),
    "Turbine Town - Cassette near Wind Turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 117),
    "Turbine Town - Cassette near Torii Gates": HereComesNikoLocationData(region="Turbine Town",id=base_id + 118),
    "Turbine Town - Cassette near Fishing Containers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 119),
    "Turbine Town - Cassette near AIR VOLLEY": HereComesNikoLocationData(region="Turbine Town",id=base_id + 120),
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
    "Tadpole HQ - Cassette Walljump Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 156),
    "Tadpole HQ - Cassette next to Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 157),
    "Tadpole HQ - Cassette near Little Gabi": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 158),
    "Tadpole HQ - Cassette behind tall Skyscraper": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 159),
    "Tadpole HQ - Cassette near Serschel & Louist": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 160),
    "Tadpole HQ - Cassette on Golden Frog Statue": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 161),
    "Tadpole HQ - Cassette Breakable box near Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 162),
    "Tadpole HQ - Cassette near Fischer": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 163),
    "Tadpole HQ - Cassette under Giant Umbrella": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 164),
    "Tadpole HQ - Cassette between Buildings near Little Gabi": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 165),

    # Misc
    "Tadpole HQ - Dojo Guy": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 166),
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
    "Gary's Garden - Cassette 1": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 183, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 2": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 184, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 3": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 185, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 4": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 186, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 5": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 187, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 6": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 188, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 7": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 189, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 8": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 190, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 9": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 191, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Cassette 10": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 192, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Gunter & Little Gabi": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 198, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Give Mai 5 Cassettes": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 199, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Give Mitch 5 Cassettes": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 200, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Handsome Frog": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 201, can_create=lambda options: options.shuffle_garys_garden.value),

    # Handsome Frog
    "Hairball City - Handsome Frog": HereComesNikoLocationData(region="Hairball City",id=base_id + 193, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Turbine Town - Handsome Frog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 194, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Salmon Creek Forest - Handsome Frog": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 195, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Public Pool - Handsome Frog": HereComesNikoLocationData(region="Public Pool",id=base_id + 196, can_create=lambda options: options.shuffle_handsome_frog.value),
    "Bathhouse - Handsome Frog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 197, can_create=lambda options: options.shuffle_handsome_frog.value),

    # Kiosk
    "Home - Kiosk": HereComesNikoLocationData(region="Home",id=base_id + 170),
    "Hairball City - Kiosk": HereComesNikoLocationData(region="Hairball City",id=base_id + 171),
    "Turbine Town - Kiosk": HereComesNikoLocationData(region="Turbine Town",id=base_id + 172),
    "Salmon Creek Forest - Kiosk": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 173),
    "Public Pool - Kiosk": HereComesNikoLocationData(region="Public Pool",id=base_id + 174),
    "Bathhouse - Kiosk": HereComesNikoLocationData(region="Bathhouse",id=base_id + 175),

    # Victory
    #"Tadpole HQ - Job Interview": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 169),
    "You're Hired!": HereComesNikoLocationData(region="Home Party", locked_item="Victory"),
}

location_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}
id_to_location_table = {data.id: name for name, data in location_data_table.items() if data.id is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}



