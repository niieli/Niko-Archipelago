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
    "Hairball City - Mitch": HereComesNikoLocationData(region="Hairball City",id=base_id + 11),
    "Hairball City - Mai": HereComesNikoLocationData(region="Hairball City",id=base_id + 12),
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
    "Turbine Town - Mitch": HereComesNikoLocationData(region="Turbine Town",id=base_id + 23),
    "Turbine Town - Mai": HereComesNikoLocationData(region="Turbine Town",id=base_id + 24),
    "Turbine Town - Blippy Dog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 25),
    "Turbine Town - Blippy Coin": HereComesNikoLocationData(region="Turbine Town",id=base_id + 26),
    "Turbine Town - Serschel & Louist": HereComesNikoLocationData(region="Turbine Town",id=base_id + 27),
    # ~ Salmon Creek Forest
    "Salmon Creek Forest - Stijn & Melissa": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 28),
    "Salmon Creek Forest - Mitch": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 29),
    "Salmon Creek Forest - Dustan on Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 30),
    "Salmon Creek Forest - Moomy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 31),
    "Salmon Creek Forest - Blippy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 32),
    "Salmon Creek Forest - Treeman": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 33),
    "Salmon Creek Forest - Blessley": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 34),
    "Salmon Creek Forest - Secret of the Forest": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 35),
    "Salmon Creek Forest - SPORTVIVAL": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 36),
    "Salmon Creek Forest - Little Gabi's Flowers": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 37),
    "Salmon Creek Forest - Nina": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 38),
    "Salmon Creek Forest - Mai": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 39),
    "Salmon Creek Forest - Fish with Fischer": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 40),
    "Salmon Creek Forest - Game Kid": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 41),
    "Salmon Creek Forest - Blippy Coin": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 42),
    "Salmon Creek Forest - Serschel & Louist": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 43),
    # ~ Public Pool
    "Public Pool - Far Away Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 44),
    "Public Pool - Mai": HereComesNikoLocationData(region="Public Pool",id=base_id + 45),
    "Public Pool - Blippy Dog": HereComesNikoLocationData(region="Public Pool",id=base_id + 46),
    "Public Pool - Blippy Coin": HereComesNikoLocationData(region="Public Pool",id=base_id + 47),
    "Public Pool - Fish with Fischer": HereComesNikoLocationData(region="Public Pool",id=base_id + 48),
    "Public Pool - Frogtective": HereComesNikoLocationData(region="Public Pool",id=base_id + 49),
    "Public Pool - SPORTVIVAL VOLLEY": HereComesNikoLocationData(region="Public Pool",id=base_id + 50),
    "Public Pool - Blessley": HereComesNikoLocationData(region="Public Pool",id=base_id + 51),
    "Public Pool - Mitch": HereComesNikoLocationData(region="Public Pool",id=base_id + 52),
    "Public Pool - Little Gabi's Flowers": HereComesNikoLocationData(region="Public Pool",id=base_id + 53),
    # ~ Bathhouse
    "Bathhouse - Serschel & Louist": HereComesNikoLocationData(region="Bathhouse",id=base_id + 54),
    "Bathhouse - Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 55),
    "Bathhouse - Poppy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 56),
    "Bathhouse - Nina": HereComesNikoLocationData(region="Bathhouse",id=base_id + 57),
    "Bathhouse - Mitch": HereComesNikoLocationData(region="Bathhouse",id=base_id + 58),
    "Bathhouse - Mai": HereComesNikoLocationData(region="Bathhouse",id=base_id + 59),
    "Bathhouse - Dustan on Bathhouse": HereComesNikoLocationData(region="Bathhouse",id=base_id + 60),
    "Bathhouse - LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 61),
    "Bathhouse - Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 62),
    "Bathhouse - Fish with Fischer": HereComesNikoLocationData(region="Bathhouse",id=base_id + 63),
    "Bathhouse - Blessley": HereComesNikoLocationData(region="Bathhouse",id=base_id + 64),
    "Bathhouse - Little Gabi's Flowers": HereComesNikoLocationData(region="Bathhouse",id=base_id + 65),
    "Bathhouse - Blippy Dog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 66),
    "Bathhouse - Blippy Coin": HereComesNikoLocationData(region="Bathhouse",id=base_id + 67),
    # ~ Tadpole HQ
    "Tadpole HQ - Mai": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 68),
    "Tadpole HQ - Mitch": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 69),
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
    "Hairball City - Cassette above Frog Statue": HereComesNikoLocationData(region="Hairball City",id=base_id + 109),
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
    "Salmon Creek Forest - Cassette Behind Train": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 122),
    "Salmon Creek Forest - Cassette Wooden Bridge": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 123),
    "Salmon Creek Forest - Cassette On Treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 124),
    "Salmon Creek Forest - Cassette Rocks near Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 125),
    "Salmon Creek Forest - Cassette Near Edge Inside Waterfall Cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 126),
    "Salmon Creek Forest - Cassette Boxes Inside Waterfall Cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 127),
    "Salmon Creek Forest - Cassette Next to Treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 128),
    "Salmon Creek Forest - Cassette Rocks in Ocean": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 129),
    "Salmon Creek Forest - Cassette Behind Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 130),
    "Salmon Creek Forest - Cassette Next to Treeman": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 131),
    "Salmon Creek Forest - Cassette Near Hamster Ball": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 132),
    #  ~ Public Pool
    "Public Pool - Cassette Frog Statue": HereComesNikoLocationData(region="Public Pool",id=base_id + 134),
    "Public Pool - Cassette On Springboard": HereComesNikoLocationData(region="Public Pool",id=base_id + 135),
    "Public Pool - Cassette Small Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 136),
    "Public Pool - Cassette Rocks in Ocean": HereComesNikoLocationData(region="Public Pool",id=base_id + 137),
    "Public Pool - Cassette Inside the Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 138),
    "Public Pool - Cassette Inside the BIG Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 139),
    "Public Pool - Cassette Behind Frog Statue": HereComesNikoLocationData(region="Public Pool",id=base_id + 140),
    "Public Pool - Cassette Palm Tree": HereComesNikoLocationData(region="Public Pool",id=base_id + 141),
    "Public Pool - Cassette Breakable near Frogtective": HereComesNikoLocationData(region="Public Pool",id=base_id + 142),
    "Public Pool - Cassette Above BIG Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 143),
    #  ~ Bathhouse
    "Bathhouse - Cassette Behind Frog Statue": HereComesNikoLocationData(region="Bathhouse",id=base_id + 145),
    "Bathhouse - Cassette Near Axolotl Family in Water": HereComesNikoLocationData(region="Bathhouse",id=base_id + 146),
    "Bathhouse - Cassette Hut in Water": HereComesNikoLocationData(region="Bathhouse",id=base_id + 147),
    "Bathhouse - Cassette Giant Frog Statue": HereComesNikoLocationData(region="Bathhouse",id=base_id + 148),
    "Bathhouse - Cassette Lamp near Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 149),
    "Bathhouse - Cassette Behind LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 150),
    "Bathhouse - Cassette Behind Waterfall": HereComesNikoLocationData(region="Bathhouse",id=base_id + 151),
    "Bathhouse - Cassette Fan to Fan": HereComesNikoLocationData(region="Bathhouse",id=base_id + 152),
    "Bathhouse - Cassette On Pipes near Kiosk": HereComesNikoLocationData(region="Bathhouse",id=base_id + 153),
    "Bathhouse - Cassette Mahjong Hideout": HereComesNikoLocationData(region="Bathhouse",id=base_id + 154),
    # ~ Tadpole HQ
    "Tadpole HQ - Cassette Wall Jump Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 156),
    "Tadpole HQ - Cassette next to Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 157),
    "Tadpole HQ - Cassette near Little Gabi": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 158),
    "Tadpole HQ - Cassette behind Tall Skyscraper": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 159),
    "Tadpole HQ - Cassette near Serschel & Louist": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 160),
    "Tadpole HQ - Cassette on Golden Frog Statue": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 161),
    "Tadpole HQ - Cassette Breakable Box near Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 162),
    "Tadpole HQ - Cassette near Fischer": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 163),
    "Tadpole HQ - Cassette under Giant Umbrella": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 164),
    "Tadpole HQ - Cassette between Buildings near Little Gabi": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 165),

    # Misc
    "Tadpole HQ - Dojo Guy": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 166),
    "Salmon Creek Forest - Contact List": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 167),
    "Tadpole HQ - Contact List": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 168),

    # Achievements
    "Frog Fan": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 176, can_create=lambda options: options.enable_achievements.value != 2),
    "Employee Of The Month!": HereComesNikoLocationData(region="Home", id=base_id + 177, can_create=lambda options: options.enable_achievements.value != 2 and options.goal_completion.value != 1),
    "Bottled Up": HereComesNikoLocationData(region="Bathhouse", id=base_id + 178, can_create=lambda options: options.enable_achievements.value != 2),
    "Snail Fashion Show": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 179, can_create=lambda options: options.enable_achievements.value == 0),
    "Volley Dreams": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 180, can_create=lambda options: options.enable_achievements.value != 2),
    "Hopeless Romantic": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 181, can_create=lambda options: options.enable_achievements.value != 2),
    "Lost at Sea": HereComesNikoLocationData(region="Home", id=base_id + 182, can_create=lambda options: options.enable_achievements.value != 2),

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
    "Gary's Garden - Mai": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 199, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Mitch": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 200, can_create=lambda options: options.shuffle_garys_garden.value),
    #"Gary's Garden - Handsome Frog": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 201, can_create=lambda options: options.shuffle_garys_garden.value and options.shuffle_handsome_frog.value),

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

    #Dustan
    "Dustan - Meeting First Time": HereComesNikoLocationData(region="Home", id=base_id + 202),

    #Fishsanity
    "Hairball City - Moorish Idol": HereComesNikoLocationData(region="Hairball City", id=base_id + 203, can_create=lambda options: options.fishsanity.value),
    "Hairball City - Not Nemo": HereComesNikoLocationData(region="Hairball City", id=base_id + 204, can_create=lambda options: options.fishsanity.value),
    "Hairball City - Eel": HereComesNikoLocationData(region="Hairball City", id=base_id + 205, can_create=lambda options: options.fishsanity.value),
    "Hairball City - Flying Fish": HereComesNikoLocationData(region="Hairball City", id=base_id + 206, can_create=lambda options: options.fishsanity.value),
    "Hairball City - Orange Fish": HereComesNikoLocationData(region="Hairball City", id=base_id + 207, can_create=lambda options: options.fishsanity.value),
    "Turbine Town - Albino Corydoras": HereComesNikoLocationData(region="Turbine Town", id=base_id + 208, can_create=lambda options: options.fishsanity.value),
    "Turbine Town - Axolotl": HereComesNikoLocationData(region="Turbine Town", id=base_id + 209, can_create=lambda options: options.fishsanity.value),
    "Turbine Town - Prianha": HereComesNikoLocationData(region="Turbine Town", id=base_id + 210, can_create=lambda options: options.fishsanity.value),
    "Turbine Town - Mantaray": HereComesNikoLocationData(region="Turbine Town", id=base_id + 211, can_create=lambda options: options.fishsanity.value),
    "Turbine Town - Sand Shrimp": HereComesNikoLocationData(region="Turbine Town", id=base_id + 212, can_create=lambda options: options.fishsanity.value),
    "Salmon Creek Forest - Bass": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 213, can_create=lambda options: options.fishsanity.value),
    "Salmon Creek Forest - Catfish": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 214, can_create=lambda options: options.fishsanity.value),
    "Salmon Creek Forest - Pike": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 215, can_create=lambda options: options.fishsanity.value),
    "Salmon Creek Forest - Salmon": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 216, can_create=lambda options: options.fishsanity.value),
    "Salmon Creek Forest - Trout": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 217, can_create=lambda options: options.fishsanity.value),
    "Public Pool - Baby Crocodile": HereComesNikoLocationData(region="Public Pool", id=base_id + 218, can_create=lambda options: options.fishsanity.value),
    "Public Pool - Gramma Loreto": HereComesNikoLocationData(region="Public Pool", id=base_id + 219, can_create=lambda options: options.fishsanity.value),
    "Public Pool - Shark": HereComesNikoLocationData(region="Public Pool", id=base_id + 220, can_create=lambda options: options.fishsanity.value),
    "Public Pool - Squid": HereComesNikoLocationData(region="Public Pool", id=base_id + 221, can_create=lambda options: options.fishsanity.value),
    "Public Pool - Turtle": HereComesNikoLocationData(region="Public Pool", id=base_id + 222, can_create=lambda options: options.fishsanity.value),
    "Bathhouse - Anglerfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 223, can_create=lambda options: options.fishsanity.value),
    "Bathhouse - Clione": HereComesNikoLocationData(region="Bathhouse", id=base_id + 224, can_create=lambda options: options.fishsanity.value),
    "Bathhouse - Little Wiggly Guy": HereComesNikoLocationData(region="Bathhouse", id=base_id + 225, can_create=lambda options: options.fishsanity.value),
    "Bathhouse - Jellyfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 226, can_create=lambda options: options.fishsanity.value),
    "Bathhouse - Pufferfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 227, can_create=lambda options: options.fishsanity.value),
    "Tadpole HQ - Blue Fairy Shrimp": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 228, can_create=lambda options: options.fishsanity.value),
    "Tadpole HQ - Bluestreak Cleaner Wrasse": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 229, can_create=lambda options: options.fishsanity.value),
    "Tadpole HQ - Honey Gourami": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 230, can_create=lambda options: options.fishsanity.value),
    "Tadpole HQ - Loach": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 231, can_create=lambda options: options.fishsanity.value),
    "Tadpole HQ - Neon Tetra": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 232, can_create=lambda options: options.fishsanity.value),

    # Snail Shop
    "Snail Shop - Bowtie": HereComesNikoLocationData(region="Home",id=base_id + 233, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Motorcycle": HereComesNikoLocationData(region="Home",id=base_id + 234, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Sunglasses": HereComesNikoLocationData(region="Home",id=base_id + 235, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Mahjong": HereComesNikoLocationData(region="Home",id=base_id + 236, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Cap": HereComesNikoLocationData(region="Home",id=base_id + 237, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - King Staff": HereComesNikoLocationData(region="Home",id=base_id + 238, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Mouse": HereComesNikoLocationData(region="Home",id=base_id + 239, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Clown Face": HereComesNikoLocationData(region="Home",id=base_id + 240, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Phone": HereComesNikoLocationData(region="Home",id=base_id + 241, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Bandanna": HereComesNikoLocationData(region="Home",id=base_id + 242, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Stars": HereComesNikoLocationData(region="Home",id=base_id + 243, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Sword": HereComesNikoLocationData(region="Home",id=base_id + 244, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Top hat": HereComesNikoLocationData(region="Home",id=base_id + 245, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Glasses": HereComesNikoLocationData(region="Home",id=base_id + 246, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Flower": HereComesNikoLocationData(region="Home",id=base_id + 247, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Small Hat": HereComesNikoLocationData(region="Home",id=base_id + 248, can_create=lambda options: options.snail_shop.value),

    # Victory
    "You're Hired!": HereComesNikoLocationData(region="Home Party", locked_item="Victory", can_create=lambda options: options.goal_completion.value == 0),
    "Best Employee!": HereComesNikoLocationData(region="Home", locked_item="Victory", can_create=lambda options: options.goal_completion.value == 1)
}

location_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}
id_to_location_table = {data.id: name for name, data in location_data_table.items() if data.id is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}



