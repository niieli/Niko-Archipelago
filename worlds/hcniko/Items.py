from typing import NamedTuple, Dict, Callable, Optional

from BaseClasses import Item, ItemClassification


class HereComesNikoItem(Item):
    game = "Here Comes Niko!"


class HereComesNikoItemData(NamedTuple):
    id: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True

base_id = 598_145_444_000

item_data_table: Dict[str, HereComesNikoItemData] = {
    "Coin": HereComesNikoItemData(base_id, type=ItemClassification.progression_skip_balancing, num_exist=79),
    "Cassette": HereComesNikoItemData(base_id+1, type=ItemClassification.progression_skip_balancing, num_exist=71),
    "Key": HereComesNikoItemData(base_id+2, type=ItemClassification.progression, num_exist=8),
    "Letter": HereComesNikoItemData(base_id+7, type=ItemClassification.filler),
    "25 Apples": HereComesNikoItemData(base_id + 3, type=ItemClassification.filler),
    "Contact List 1": HereComesNikoItemData(base_id+4, type=ItemClassification.progression, num_exist=1, can_create=lambda options: not options.progressive_contact_list.value),
    "Contact List 2": HereComesNikoItemData(base_id+5, type=ItemClassification.progression, num_exist=1, can_create=lambda options: not options.progressive_contact_list.value),
    "Progressive Contact List": HereComesNikoItemData(base_id+15, type=ItemClassification.progression, num_exist=2, can_create=lambda options:  options.progressive_contact_list.value),
    "Super Jump": HereComesNikoItemData(base_id+6, type=ItemClassification.useful, num_exist=1),
    "10 Bugs": HereComesNikoItemData(base_id + 14, type=ItemClassification.filler),

    # Levels
    #"Home": HereComesNikoItemData(base_id + 7, type=ItemClassification.progression),
    "Hairball City Ticket": HereComesNikoItemData(base_id + 8, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    "Turbine Town Ticket": HereComesNikoItemData(base_id + 9, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    "Salmon Creek Forest Ticket": HereComesNikoItemData(base_id + 10, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    "Public Pool Ticket": HereComesNikoItemData(base_id + 11, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    "Bathhouse Ticket": HereComesNikoItemData(base_id + 12, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    "Tadpole HQ Ticket": HereComesNikoItemData(base_id + 13, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value),
    #"Gary's Garden Ticket": HereComesNikoItemData(base_id + 16, type=ItemClassification.progression, can_create=lambda options: options.shuffle_kiosk_reward.value and options.access_garys_garden.value == 1),

    "Victory": HereComesNikoItemData(type=ItemClassification.progression, can_create=lambda options: False)
}

item_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}
id_to_item_table = {data.id: name for name, data in item_data_table.items() if data.id is not None}
