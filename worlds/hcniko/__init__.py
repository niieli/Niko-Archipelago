from BaseClasses import Item, ItemClassification, Region
from worlds.AutoWorld import World
from .items import item_data_table
from .locations import coin_location_table


class HereComesNikoWorld(World):
    game = "Here Comes Niko!"
    location_name_to_id = coin_location_table
    item_name_to_id = item_data_table


    def create_regions(self):
        region = Region("Home", self.player, self.multiworld)
        region.add_locations(self.location_name_to_id)
        self.multiworld.regions.append(region)

    def create_items(self):
        coin_item = Item("Coin", ItemClassification.progression, 598_145_444_000, self.player)
        self.multiworld.itempool.append(coin_item)
