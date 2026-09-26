import json
from models.agent import Agent
from models.actions.action import Action
from models.actions.attack_action import AttackAction
from models.actions.action_instance import ActionInstance
from models.actions.influence_action import InfluenceAction
from models.actions.move_action import MoveAction
from models.actions.wait_action import WaitAction
from loaders.world_loader import world
import random
import math
from dataclasses import dataclass

#lists and global variables
wait_action = WaitAction(name = "Wait",id = "wait", type= "wait", effect = "Wait to recover stamina, this uses your turn",stamina_use = 0)
action_list = [wait_action]
action_type_list = []
active_agents = []
turn_list= []
turns = turn_list.count
round = 0
turn_order = []
action_router = {
    "move": move_action_handler,
    "attack": attack_action_handler,
    "influence": influence_action_handler,
    "wait": wait_action_handler
}
#function definition and router
def start_action(chosen_action, target_position):
    if chosen_action in action_list and chosen_action.type in action_router:
        action_instance = ActionInstance(
            action =  chosen_action,
            target = target_position
        )
        return action_instance
    elif chosen_action not in action_list:
        print(f"{chosen_action} is an invalid action")
    elif chosen_action.type not in action_router:
        print(f"{chosen_action} has no corresponding function")
       
def distance_check (agent, action_instance):
   
    agent_position_x =  agent.position[0]
    agent_position_y = agent.position[1]
    action = action_instance.action 
    
    if action_instance.target is not None:
        target_position_x, target_position_y = action_instance.target ## Right side = where the value comes from. Left side = where you want to store it.
        
        distance = ((target_position_x - agent_position_x)**2 + (target_position_y - agent_position_y)**2)**(1/2)
        
        if distance <=  action.range and 0 <= target_position_x <= world.width and 0 <= target_position_y <= world.height: #Euclidean distance, the shortest straight-line distance between two points
            return True

        elif  (0 > target_position_x or target_position_x > world.width) or (0 > target_position_y or target_position_y > world.height):
            print(f"Invalid target")
            return False

        elif distance > action.range:
            print(f"For {agent.name}, {distance} exceeds  {action.name}'s range of {action.range}")
            return False


def handle_action(agent, chosen_action):
    current_action_instance = start_action(chosen_action)
    if current_action_instance:
        if stamina_check(agent.stamina, chosen_action.stamina_use) == True:
            action_function = action_router.get(chosen_action.type)
            return action_function(agent, current_action_instance, world)

    elif chosen_action not in action_list:
        print(f"{chosen_action} is not a valid action")
        return None
    
    elif chosen_action.type not in action_router:
         print(f"{chosen_action.type} has no action function yet.")
         return None

def move_action_handler(agent, action):
    agent_position_x =  agent.position[0]
    agent_position_y = agent.position[1]

    target_position_x, target_position_y = target_position
    distance = ((target_position_x - agent_position_x)**2 + (target_position_y - agent_position_y)**2)**(1/2)
    
    if distance <=  random_action.range and 0 <= target_position_x <= world.width and 0 <= target_position_y <= world.height:
        agent.position = (target_position_x, target_position_y)
        current_turn["actions_available"] -= 1
        agent.stamina -= random_action.stamina_use
        print(f"{agent.name} moved by {distance} ")
        return agent.position

    elif distance > random_action.range:
        print(f"For {agent.name}, {distance} exceeds the {random_action.name}'s range of {random_action.range}")

    elif  (0 > target_position_x or target_position_x > world.width) or (0 > target_position_y or target_position_y > world.height):
        print(f"You can not move outside the world")

def attack_action_handler(agent, action, world):
     return
def influence_action_handler(agent, action, world):
     return
def wait_action_handler(agent, action, world):
     return



#Movement import
with open("data/move_actions.json", "r") as file:
    move_actions_data = json.load(file)
    for data in move_actions_data:
        move_action = MoveAction(**data)
        action_list.append(move_action)
        action_type_list.append(move_action.type)

#Attack import
with open("data/attack_actions.json", "r") as file:
    attack_actions_data = json.load(file)
    for data in attack_actions_data:
        attack_action = AttackAction(**data)
        action_list.append(attack_action)
        action_type_list.append(attack_action.type)

#Influence import
with open("data/influence_actions.json", "r") as file:
    influence_actions_data = json.load(file)
    for data in influence_actions_data:
        influence_action = InfluenceAction(**data)
        action_list.append(influence_action)
        action_type_list.append(influence_action.type)

#Turn queue
if turn_list == []:
    for agent in world.agents:
            if agent.incapacitated is False and agent.health > 0:
                    turn_list.append({
                    "current_agent": agent,
                    "actions_available": 2
                    })

if turn_list != []: 
        current_turn = turn_list[0]
        agent = current_turn["current_agent"]

        if agent.incapacitated == True or current_turn["actions_available"] == 0 or agent.health <= 0:
            turn_list.pop(0)
        else:
            while current_turn and current_turn["actions_available"] > 0:
                ## ai select item from action_list
                random_action = random.choice(action_list) ##placeholder for agent decision
                if agent.stamina > 0:
                    if agent.stamina >= random_action.stamina_use:
                        #Movement Action
                        if random_action.type == "move":
                            target_position_x = random.randint(1,350)
                            target_position_y = random.randint(1,350)

                            agent_position_x =  agent.position[0]
                            agent_position_y = agent.position[1]

                            distance = ((target_position_x - agent_position_x)**2 + (target_position_y - agent_position_y)**2)**(1/2)
                            if distance <=  random_action.range and 0 <= target_position_x <= world.width and 0 <= target_position_y <= world.height:
                                agent.position = (target_position_x, target_position_y)
                                current_turn["actions_available"] -= 1
                                agent.stamina -= random_action.stamina_use
                                print(f"{agent.name} moved by {distance} ")
                            elif distance > random_action.range:
                                print(f"For {agent.name}, {distance} exceeds the {random_action.name}'s range of {random_action.range}")
                            elif  (0 > target_position_x or target_position_x > world.width) or (0 > target_position_y or target_position_y > world.height):
                                print(f"You can not move outside the world")
                        #Attack Action
                        #Wait Action
                        
                else:
                    wait_action
            

                    '''
                    target = None
                        action = ActionInstance(
                            "action = random_action,
                            "result": idk,
                            "target": idk
                        )

                    '''

#Spending action points

## Action validation - is it an action, can the agent use it, is the agent alive or is the agent incapacitated 



#Action Execution logic


## FUNCTIONS


def stamina_check(agent_stamina, chosen_action):
           required_stamina = chosen_action.stamina_requred 
           if agent_stamina >= required_stamina:
                return True
           else:
                
                return False
def distance_check (agent, action_instance):
   
    agent_position_x =  agent.position[0]
    agent_position_y = agent.position[1]

    target_position_x, target_position_y = target_position
    distance = ((target_position_x - agent_position_x)**2 + (target_position_y - agent_position_y)**2)**(1/2)
    
    if distance <=  action.range and 0 <= target_position_x <= world.width and 0 <= target_position_y <= world.height:
        return target_position

    elif distance > random_action.range:
        print(f"For {agent.name}, {distance} exceeds  {action.name}'s range of {action.range}")
        return False

    elif  (0 > target_position_x or target_position_x > world.width) or (0 > target_position_y or target_position_y > world.height):
        print(f"Invalid target")
        return False


    

# Target rang check