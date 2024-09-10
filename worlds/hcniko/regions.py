from typing import NamedTuple, List, Dict


class HereComesNikoRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, HereComesNikoRegionData] = {
    "Menu": HereComesNikoRegionData(["Home"]),
    "Home": HereComesNikoRegionData(["Hairball City"]),
    "Hairball City": HereComesNikoRegionData(["Turbine Town"]),
    "Turbine Town": HereComesNikoRegionData(["Salmon Creek Forest"]),
    "Salmon Creek Forest": HereComesNikoRegionData(["Public Pool"]),
    "Public Pool": HereComesNikoRegionData(["Bathhouse"]),
    "Bathhouse": HereComesNikoRegionData(["Tadpole HQ"]),
    "Tadpole HQ": HereComesNikoRegionData(["Home Party","Gary's Garden"]),
    "Home Party": HereComesNikoRegionData([]),
    "Gary's Garden": HereComesNikoRegionData([])

    # "Home": HereComesNikoRegionData(["Hairball City",
    #                                  "Turbine Town",
    #                                  "Salmon Creek Forest",
    #                                  "Public Pool",
    #                                  "Bathhouse",
    #                                  "Tadpole HQ"
    #                                  ]),
    # "Hairball City": HereComesNikoRegionData(["Turbine Town",
    #                                           "Home",
    #                                           "Salmon Creek Forest",
    #                                           "Public Pool",
    #                                           "Bathhouse",
    #                                           "Tadpole HQ"
    #                                           ]),
    # "Turbine Town": HereComesNikoRegionData(["Salmon Creek Forest",
    #                                          "Home",
    #                                          "Hairball City",
    #                                          "Public Pool",
    #                                          "Bathhouse",
    #                                          "Tadpole HQ"
    #                                          ]),
    # "Salmon Creek Forest": HereComesNikoRegionData(["Public Pool",
    #                                                 "Home",
    #                                                 "Hairball City",
    #                                                 "Turbine Town",
    #                                                 "Public Pool",
    #                                                 "Bathhouse",
    #                                                 "Tadpole HQ"
    #                                                 ]),
    # "Public Pool": HereComesNikoRegionData([
    #     "Bathhouse",
    #     "Home",
    #     "Hairball City",
    #     "Turbine Town",
    #     "Salmon Creek Forest",
    #     "Tadpole HQ"
    # ]),
    # "Bathhouse": HereComesNikoRegionData([
    #     "Tadpole HQ",
    #     "Home",
    #     "Hairball City",
    #     "Turbine Town",
    #     "Salmon Creek Forest",
    #     "Public Pool",
    # ]),
    # "Tadpole HQ": HereComesNikoRegionData(["Home Party",
    #                                        # "Gary's Garden"
    #                                        ]),
    # "Home Party": HereComesNikoRegionData([])
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit