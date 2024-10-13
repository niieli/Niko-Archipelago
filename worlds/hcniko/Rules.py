TICKETS = ["Hairball City Ticket", "Turbine Town Ticket", "Salmon Creek Forest Ticket", "Public Pool Ticket", "Bathhouse Ticket", "Tadpole HQ Ticket"]
def has_all_coins(state, player):
    return state.has("Coin", player, 76)

def can_talk_to_peper(state, player, int):
    return state.has("Coin", player, int)

def has_enough_cassettes(state, player, int):
    return state.has("Cassette", player, int*5)

def has_all_tickets(state, player):
    return (state.has("Hairball City Ticket", player)
            and state.has("Turbine Town Ticket", player)
            and state.has("Salmon Creek Forest Ticket", player)
            and state.has("Public Pool Ticket", player)
            and state.has("Bathhouse Ticket", player)
            and state.has("Tadpole HQ Ticket", player))

def has_tickets(state, player, required_tickets):
    ticket_count = sum(1 for ticket in TICKETS if state.has(ticket, player))
    return ticket_count >= required_tickets

def get_region_rules(player, world):
    if world.options.min_elevator_cost.value == world.options.max_elevator_cost.value:
        world.kiosk_cost["Elevator"] = world.options.max_elevator_cost.value
    else:
        world.kiosk_cost["Elevator"] = world.random.randint(world.options.min_elevator_cost.value,
                                                world.options.max_elevator_cost.value)
    return {
        "Home -> Hairball City":
            lambda state: state.has("Hairball City Ticket", player),
        "Home -> Turbine Town":
            lambda state: state.has("Turbine Town Ticket", player),
        "Home -> Salmon Creek Forest":
            lambda state: state.has("Salmon Creek Forest Ticket", player),
        "Home -> Public Pool":
            lambda state: state.has("Public Pool Ticket", player),
        "Home -> Bathhouse":
            lambda state: state.has("Bathhouse Ticket", player),
        "Home -> Tadpole HQ":
            lambda state: state.has("Tadpole HQ Ticket", player),
        "Tadpole HQ -> Home Party":
            lambda state: can_talk_to_peper(state, player, world.kiosk_cost["Elevator"])
    }

def get_location_rules(player, world):
    lowest_cost: int = world.options.min_kiosk_cost.value
    highest_cost: int = world.options.max_kiosk_cost.value
    cost_increment: int = (highest_cost - lowest_cost) // len(world.kiosk_cost)
    min_difference = 4
    last_cost = 0

    kiosk_names = list(world.kiosk_cost.keys())
    kiosk_names.remove("Elevator")
    if world.options.shuffle_kiosk_reward.value == 1:
        world.random.shuffle(kiosk_names)

    if world.options.shuffle_kiosk_reward.value == 0:
        for i, kiosk_name in enumerate(kiosk_names):
            if i >= 3:
                cost = 1 + 5 + (5*i)
            else:
                cost = 1 + (5*i)
            world.kiosk_cost[kiosk_name] = cost
    else:
        for i, kiosk_name in enumerate(kiosk_names):
            min_range: int = lowest_cost + (cost_increment * i)
            if min_range >= highest_cost:
                min_range = highest_cost - 1

            value: int = world.random.randint(min_range, min(highest_cost, max(lowest_cost, last_cost + cost_increment)))
            cost = world.random.randint(value, min(value + cost_increment, highest_cost))
            if i >= 1:
                if last_cost + min_difference > cost:
                    cost = last_cost + min_difference

            cost = min(cost, highest_cost)
            world.kiosk_cost[kiosk_name] = cost
            last_cost = cost

    if world.options.cassette_logic.value == 2:
        cassette_values = list(range(1, 14 + 1))
        world.random.shuffle(cassette_values)
        cassette_locations = list(world.cassette_cost.keys())
        for i, location_name in enumerate(cassette_locations):
            world.cassette_cost[location_name] = cassette_values[i]
    else:
        cassette_values = list(range(1, 14 + 1))
        cassette_locations = list(world.cassette_cost.keys())
        for i, location_name in enumerate(cassette_locations):
            world.cassette_cost[location_name] = cassette_values[i]

    return {
        "Home - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Home"])),
        "Hairball City - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Hairball City"])),
        "Turbine Town - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Turbine Town"])),
        "Salmon Creek Forest - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Salmon Creek Forest"])),
        "Public Pool - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Public Pool"])),
        "Bathhouse - Kiosk":
            lambda state: (state.has("Coin", player, world.kiosk_cost["Kiosk Bathhouse"])),
        "Employee Of The Month!":
            lambda state: has_all_coins(state, player),
        "Bottled Up":
            lambda state: state.has("Hairball City Ticket", player)
                          and state.has("Turbine Town Ticket", player)
                          and state.has("Salmon Creek Forest Ticket", player)
                          and state.has("Public Pool Ticket", player)
                          and state.has("Bathhouse Ticket", player),
        "Hopeless Romantic":
            lambda state: state.has("Hairball City Ticket", player)
                          and state.has("Turbine Town Ticket", player)
                          and state.has("Salmon Creek Forest Ticket", player)
                          and state.has("Public Pool Ticket", player)
                          and state.has("Bathhouse Ticket", player),
        "Volley Dreams":
            lambda state: has_all_tickets(state, player),
        "Best Employee!":
            lambda state: has_all_coins(state, player),
        "Turbine Town - Dustan on Wind Turbine":
            lambda state: state.has("Key", player, 7),
        "Public Pool - Blippy Coin":
            lambda state: state.has("Key", player, 7),
        "Bathhouse - Poppy":
            lambda state: state.has("Key", player, 7),
        "Tadpole HQ - Blippy Coin":
            lambda state: state.has("Key", player, 7),
        "Hairball City - Cassette above Frog Statue":
            lambda state: state.has("Key", player, 7),
        "Salmon Creek Forest - Letter inside locked Cave":
            lambda state: state.has("Key", player, 7),
        "Bathhouse - Cassette Mahjong Hideout":
            lambda state: state.has("Key", player, 7),
        "Salmon Creek Forest - Fish with Fischer":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Hairball City - Nina":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Hairball City - Moomy":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Hairball City - Game Kid":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Hairball City - Blippy Dog":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Hairball City - Blippy Coin":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Hairball City - Serschel & Louist":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Turbine Town - Blippy Dog":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Turbine Town - Blippy Coin":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Turbine Town - Serschel & Louist":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Salmon Creek Forest - Game Kid":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Salmon Creek Forest - Blippy Coin":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Salmon Creek Forest - Serschel & Louist":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Public Pool - SPORTVIVAL VOLLEY":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Public Pool - Blessley":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Public Pool - Little Gabi's Flowers":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Fish with Fischer":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Blessley":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Little Gabi's Flowers":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Blippy Dog":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Blippy Coin":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Dustan - Meeting First Time":
            lambda state: state.has("Hairball City Ticket", player)
                          or state.has("Turbine Town Ticket", player)
                          or state.has("Salmon Creek Forest Ticket", player)
                          or state.has("Bathhouse Ticket", player),
        #Cassette
        "Hairball City - Mitch": lambda state: (state.has("Contact List 1", player)
                              or state.has("Progressive Contact List", player, 1))
                              and has_enough_cassettes(state, player, world.cassette_cost["Hairball City - Mitch"]),
        "Hairball City - Mai": lambda state: (state.has("Contact List 1", player)
                              or state.has("Progressive Contact List", player, 1))
                              and has_enough_cassettes(state, player, world.cassette_cost["Hairball City - Mai"]),
        "Turbine Town - Mitch": lambda state: (state.has("Contact List 1", player)
                              or state.has("Progressive Contact List", player, 1))
                              and has_enough_cassettes(state, player, world.cassette_cost["Turbine Town - Mitch"]),
        "Turbine Town - Mai": lambda state: (state.has("Contact List 1", player)
                              or state.has("Progressive Contact List", player, 1))
                              and has_enough_cassettes(state, player, world.cassette_cost["Turbine Town - Mai"]),
        "Salmon Creek Forest - Mai": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Salmon Creek Forest - Mai"])
                              and state.has("Key", player, 8),
        "Salmon Creek Forest - Mitch": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Salmon Creek Forest - Mitch"]),
        "Public Pool - Mitch": lambda state: (state.has("Contact List 2", player)
                              or state.has("Progressive Contact List", player, 2))
                              and has_enough_cassettes(state, player, world.cassette_cost["Public Pool - Mitch"]),
        "Public Pool - Mai": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Public Pool - Mai"]),
        "Bathhouse - Mitch": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Bathhouse - Mitch"]),
        "Bathhouse - Mai": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Bathhouse - Mai"]),
        "Tadpole HQ - Mai": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Tadpole HQ - Mai"]),
        "Tadpole HQ - Mitch": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Tadpole HQ - Mitch"]),
        "Gary's Garden - Mai": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Gary's Garden - Mai"]),
        "Gary's Garden - Mitch": lambda state: has_enough_cassettes(state, player, world.cassette_cost["Gary's Garden - Mitch"]),
        #Fish
        "Salmon Creek Forest - Bass":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Salmon Creek Forest - Catfish":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Salmon Creek Forest - Pike":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Salmon Creek Forest - Salmon":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Salmon Creek Forest - Trout":
            lambda state: state.has("Contact List 1", player)
                          or state.has("Progressive Contact List", player, 1),
        "Bathhouse - Anglerfish":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Clione":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Little Wiggly Guy":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Jellyfish":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        "Bathhouse - Pufferfish":
            lambda state: state.has("Contact List 2", player)
                          or state.has("Progressive Contact List", player, 2),
        #Snail Shop
        "Snail Shop - Bowtie": lambda state: has_tickets(state, player, 4), #10000$
        "Snail Shop - Motorcycle": lambda state: has_tickets(state, player, 2), #500$
        "Snail Shop - Sunglasses": lambda state: has_tickets(state, player, 3), #2000$
        "Snail Shop - Mahjong": lambda state: has_tickets(state, player, 1), #100$
        "Snail Shop - Cap": lambda state: has_tickets(state, player, 2), #500$
        "Snail Shop - King Staff": lambda state: has_tickets(state, player, 4), #10000$
        "Snail Shop - Mouse": lambda state: has_tickets(state, player, 3), #1000$
        "Snail Shop - Clown Face": lambda state: has_tickets(state, player, 2), #500$
        "Snail Shop - Phone": lambda state: has_tickets(state, player, 3), #1000$
        "Snail Shop - Bandanna": lambda state: has_tickets(state, player, 2), #500$
        "Snail Shop - Stars": lambda state: has_tickets(state, player, 2), #500$
        "Snail Shop - Sword": lambda state: has_tickets(state, player, 3), #3000$
        "Snail Shop - Top hat": lambda state: has_tickets(state, player, 1), #50$
        "Snail Shop - Glasses": lambda state: has_tickets(state, player, 1), #50$
        "Snail Shop - Flower": lambda state: has_tickets(state, player, 1), #50$
        "Snail Shop - Small Hat": lambda state: has_tickets(state, player, 1), #50$
    }