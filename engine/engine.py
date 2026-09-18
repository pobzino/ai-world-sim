import json
from models.agent import Agent
from models.actions.action import Action
from models.actions.attack_action import AttackAction
from models.actions.action_instance import ActionInstance
from models.actions.influence_action import InfluenceAction
from models.actions.move_action import MoveAction
from models.actions.wait_action import WaitAction
from loaders.world_loader import world

#lists and global variables
wait_action = WaitAction(name = "Wait",id = "wait",effect ="Wait to recover stamina, this uses your turn",stamina_use = 0)
action_list = [wait_action]
active_agents = []
move_action_list = []
attack_action_list = []
influence_action_list = []
turn_list= []
turns = turn_list.count
round = 0
turn_order = []
#Movement import
with open("data/move_actions.json", "r") as file:
    move_actions_data = json.load(file)
    for data in move_actions_data:
        move_action = MoveAction(**data)
        move_action_list.append(move_action)
    action_list.extend(move_action_list)

#Attack import
with open("data/attack_actions.json", "r") as file:
    attack_actions_data = json.load(file)
    for data in attack_actions_data:
        attack_action = AttackAction(**data)
        attack_action_list.append(attack_action)
    action_list.extend(attack_action_list)

#Influence import
with open("data/influence_actions.json", "r") as file:
    influence_actions_data = json.load(file)
    for data in influence_actions_data:
        influence_action = InfluenceAction(**data)
        influence_action_list.append(influence_action)
    action_list.extend(influence_action_list)
print(action_list)

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

#Spending action points


## Action validation - is it an action, can the agent use it, is the agent alive or is the agent incapacitated 


#Action Execution logic





