from typing import List, Dict

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Items import item_data_table, HereComesNikoItem, item_table
from .Locations import location_data_table, HereComesNikoLocation, locked_locations, location_table
from .Options import *
from .Regions import region_data_table
from .Rules import *


class HereComesNikoWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Here Comes Niko! in Archipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["nieli"]
    )

    tutorials = [setup_en]


class HereComesNikoWorld(World):
    """A cozy little game, about frogs and being a good friend"""

    game = "Here Comes Niko!"
    data_version = 1
    web = HereComesNikoWebWorld()
    options: HereComesNikoOptions
    options_dataclass = HereComesNikoOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def generate_early(self):
        # Random starting Ticket
        if self.options.start_with_ticket.value:
            tickets = [
                "Hairball City Ticket",
                "Turbine Town Ticket",
                "Salmon Creek Forest Ticket",
                "Public Pool Ticket",
                "Bathhouse Ticket",
                "Tadpole HQ Ticket"
            ]
            self.selected_ticket = self.random.choice(tickets)
            self.multiworld.push_precollected(self.create_item(self.selected_ticket))

    def create_item(self, name: str) -> HereComesNikoItem:
        return HereComesNikoItem(name, item_data_table[name].type, item_data_table[name].id, self.player)

    def create_items(self) -> None:
        mw = self.multiworld

        item_pool: List[HereComesNikoItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.id and item.can_create(self.options):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1
        if not self.options.shuffle_garys_garden.value:
            for _ in range(3):
                item_pool.remove(self.create_item("Coin"))
            for _ in range(10):
                item_pool.remove(self.create_item("Cassette"))
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        item_pool += [self.create_filler() for _ in range(total_locations - len(item_pool))]
        mw.itempool += item_pool



    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld

        # Create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        # Create locations
        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.id for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            },  HereComesNikoLocation)
            region.add_exits(region_data.connecting_regions)

        # Place locked locations
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.options):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            mw.get_location(location_name, player).place_locked_item(locked_item)

        if not self.options.shuffle_kiosk_reward.value:
            kiosk_locations = {
                "Home - Kiosk": "Hairball City Ticket",
                "Hairball City - Kiosk": "Turbine Town Ticket",
                "Turbine Town - Kiosk": "Salmon Creek Forest Ticket",
                "Salmon Creek Forest - Kiosk": "Public Pool Ticket",
                "Public Pool - Kiosk": "Bathhouse Ticket",
                "Bathhouse - Kiosk": "Tadpole HQ Ticket"
            }
            selected_ticket = getattr(self, 'selected_ticket', None)
            for location, ticket in kiosk_locations.items():
                # Skip placing this ticket if it matches the selected_ticket
                if selected_ticket and ticket == selected_ticket:
                    continue  # Skip this iteration to prevent placing the selected ticket
                mw.get_location(location, player).place_locked_item(self.create_item(ticket))

    def get_filler_item_name(self) -> str:
        return "25 Apples"

    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld

        # Complete condition
        mw.completion_condition[player] = lambda state: state.has("Victory", player)

        region_rules = get_region_rules(player)
        for entrance_name, rule in region_rules.items():
            entrance = mw.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        location_rules = get_location_rules(player)
        for location in mw.get_locations(player):
            name = location.name
            if name in location_rules and location_data_table[name].can_create(self.options):
                location.access_rule = location_rules[name]

    def fill_slot_data(self):
        return  {
            "shuffle_kiosk_reward": self.options.shuffle_kiosk_reward.value,
            "start_with_ticket": self.options.start_with_ticket.value,
            "enable_achievements": self.options.enable_achievements.value,
            "shuffle_handsome_frog": self.options.shuffle_handsome_frog.value,
            "shuffle_garys_garden": self.options.shuffle_garys_garden.value,
            #"superjump_only": self.options.superjump_only.value,
            "death_link": self.options.death_link.value
        }