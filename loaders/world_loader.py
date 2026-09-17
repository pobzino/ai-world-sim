import json
import random
from models.agent import Agent #importing the dataclasses from their respective files
from models.faction import Faction
from models.location import Location
from models.world import World
from models.zone import Zone

#STEP 1: this loads the world, take all the data from the different files, and folders, creates the agents then drops them into the world
world_width = 250 #world data
world_height = 200
#create empty lists
agent_list = [] #create list that we're going to append data to
faction_list = []
location_list = []
zone_list = []
# lists for validating that an agent's values are real
faction_id_list = []
location_name_list = []

#STEP 2: Load data from json files and use the data to create relavant objects and add them to the empty lists
#ORDER IS BASED ON referal. so factions refers to nobody, locations refer to faction control and agents refer to both

with open("data/factions.json","r") as file:
    factions_data = json.load(file)
    for data in factions_data:
        faction_id = data["id"]
        faction = Faction(**data)

        faction_list.append(faction)
        faction_id_list.append(faction_id) # for later Validating the values
with open("data/locations.json","r") as file: 
    location_data = json.load(file)
    for data in location_data:
        if 0 <= data["x_min"] and data["x_max"] <= world_width and  0 <= data["y_min"] and data["y_max"] <= world_height:
            if data["x_min"] < data["x_max"] and data["y_min"] < data["y_max"]:  
                location_name = data["name"]
                location = Location(**data)
                location_list.append(location)
                location_name_list.append(location_name) # for later Validating the values
            else:
                print("invalid location bound")

with open("data/zones.json") as file:
    zone_data = json.load(file)
    for data in zone_data:
        if data["location_name"]  in location_name_list and data["faction_id"] in faction_id_list:
            for location in location_list:
                if location.name == data["location_name"]:
                    if data["x_min"] >= location.x_min and data["x_max"] <= location.x_max and data["y_min"] >= location.y_min and data["y_max"] <= location.y_max:
                        zone = Zone(**data)
                        zone_list.append(zone)
                    else:
                            print("invalid zone")

        elif data["location_name"] not in location_name_list :
            print("invalid location")
        elif data["faction_id"] not in faction_id_list:
            print("invalid faction")

with open("data/agents.json","r") as file: # r is read mode, we're saying open the agents.json file, assign it the name file then read it then we can do something with it
    agents_data = json.load(file) # give agents data the list of data to create a list of new Agent instances
    for data in agents_data:
        valid_zones = []
        selected_zone = None
        if data["faction_id"] in faction_id_list: 
            for zone in zone_list:
                if zone.faction_id == data["faction_id"]:
                    valid_zones.append(zone)
            if valid_zones:
                selected_zone = random.choice(valid_zones)
                agent_x_position = random.randint(selected_zone.x_min, selected_zone.x_max)
                agent_y_position = random.randint(selected_zone.y_min, selected_zone.y_max)
                agent = Agent(**data,
                            position = (agent_x_position, agent_y_position)) #take every key-value pair in this dictionary and pass them in as named arguments.
                agent_list.append(agent)
                print(f"{selected_zone.name} works for {data["name"]}")
            else:
                print(f"{zone.name} is not valid for {data["name"]}")

        elif data["faction_id"] not in faction_id_list:
            print(f"Invalid faction, {data["faction_id"]} for {data["name"]}")
        elif data["location"] not in location_name_list:
            print(f"Invalid location for {data["name"]}. There is no {data["location"]} in our list")

# STEP 4: initalise world with the filled lists

world = World(
        width = 250,
        height = 200,
        zones = zone_list,
        agents = agent_list, #passing the arguments World dataclass expects
        factions = faction_list,
        locations = location_list,
        current_turn = 0,
        event_history = []
)
