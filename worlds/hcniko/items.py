from typing import NamedTuple, Dict, Callable, Optional

from BaseClasses import Item, ItemClassification


class HereComesNikoItem(Item):
    game = "Here Comes Niko"


class HereComesNikoItemData(NamedTuple):
    id: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True

base_id = 598_145_444_000

item_data_table: Dict[str, HereComesNikoItemData] = {
    "Coin": HereComesNikoItemData(base_id, type=ItemClassification.progression, num_exist=76),
    "Cassette": HereComesNikoItemData(base_id+1, type=ItemClassification.progression, num_exist=61),
    "Key": HereComesNikoItemData(base_id+2, type=ItemClassification.progression, num_exist=8),
    "Letter": HereComesNikoItemData(base_id+3, type=ItemClassification.filler, num_exist=11),
    "Contact List 1": HereComesNikoItemData(base_id+4, type=ItemClassification.progression, num_exist=1),
    "Contact List 2": HereComesNikoItemData(base_id+5, type=ItemClassification.progression, num_exist=1),
    "Super Jump": HereComesNikoItemData(base_id+6, type=ItemClassification.useful, num_exist=1)
}

item_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}
id_to_item_table = {data.id: name for name, data in item_data_table.items() if data.id is not None}
