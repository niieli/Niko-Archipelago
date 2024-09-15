from typing import NamedTuple, List, Dict


class HereComesNikoRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, HereComesNikoRegionData] = {
    "Menu": HereComesNikoRegionData(["Home"]),
    "Home": HereComesNikoRegionData(["Hairball City","Turbine Town","Salmon Creek Forest","Public Pool","Bathhouse","Tadpole HQ"]),
    "Hairball City": HereComesNikoRegionData([]),
    "Turbine Town": HereComesNikoRegionData([]),
    "Salmon Creek Forest": HereComesNikoRegionData([]),
    "Public Pool": HereComesNikoRegionData([]),
    "Bathhouse": HereComesNikoRegionData([]),
    "Tadpole HQ": HereComesNikoRegionData(["Home Party", "Gary's Garden"]),
    "Home Party": HereComesNikoRegionData([]),
    "Gary's Garden": HereComesNikoRegionData([])
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit