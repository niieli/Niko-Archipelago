from typing import NamedTuple, Dict

from BaseClasses import Item, ItemClassification


class HereComesNikoItem(Item):
    game = "Here Comes Niko"


class HereComesNikoItemData(NamedTuple):
    id: int
    type: ItemClassification
    num_exist: int

base_id = 598_145_444_000

item_data_table: Dict[str, HereComesNikoItemData] = {
    "Coin": HereComesNikoItemData(base_id, type=ItemClassification.progression, num_exist=76),
    "Cassette": HereComesNikoItemData(base_id+1, type=ItemClassification.progression, num_exist=61),
    "Key": HereComesNikoItemData(base_id+2, type=ItemClassification.progression, num_exist=8),
    "Letter": HereComesNikoItemData(base_id, type=ItemClassification.filler, num_exist=11),
    "Contact List 1": HereComesNikoItemData(base_id, type=ItemClassification.progression, num_exist=1),
    "Contact List 2": HereComesNikoItemData(base_id, type=ItemClassification.progression, num_exist=1),
    "Super Jump": HereComesNikoItemData(base_id, type=ItemClassification.useful, num_exist=1)
}
