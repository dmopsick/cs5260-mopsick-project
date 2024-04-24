
from typing import List
from worldstate import WorldState
from template import Template
from solution import Solution
from node import Node
from country import Country
from statequality import calc_state_quality
from executeTemplateFunction import country_can_execute_template, execute_template


################################
# Going with breadth first search based on provided sample code
#
# How do we define our goal states? Is that our state function?
###############################
def search(initial_state: WorldState, actions: List[Template], country_searching_for: Country) -> Solution:
    visited = []
    node = Node(initial_state, None, None, 0.0)

    # if node.STATE in goals:
    #     return Solution(node, visited + [node.STATE])
    
    frontier = [ node ]
    reached = [ node.STATE ]

    current_best_state_quality = -1

    found_node: Node = None

    while len(frontier):
        node = frontier.pop(0)
        visited.append(node.STATE)

        calculated_state_quality = -1
        best_state_quality_country = None
        
        # Iterate through each potential action
        for action in actions:
            # Check if the country we are searching for can execute this action at this time
            if country_can_execute_template(country_searching_for, action) == False:
                print("Country: " + country_searching_for.NAME + " cannot run this action at this time: " + action.NAME)
                continue

            print ("Country: " + country_searching_for.NAME + " CAN run this action: " + action.NAME)

            # Calculate the state of the country after this action
            potential_country_state = execute_template(initial_state, country_searching_for, action)

            print("Executed the action. There are " + str(len(potential_country_state.COUNTRIES)) + " countries in the world")

            country_to_measure = potential_country_state.COUNTRIES[1]

            print("Checking country: " + country_to_measure.NAME)

            # Calculate the state quality of the specified country after the potential action
            calculated_state_quality = calc_state_quality(country_to_measure)

            print("Calculated state quality: " + str(calculated_state_quality))

            # Check if the latest 
            if calculated_state_quality > current_best_state_quality:
                current_best_state_quality = calculated_state_quality
                best_state_quality_country = potential_country_state
                node.STATE = best_state_quality_country
                node.PARENT_ACTION = action
                found_node = node

    return Solution(found_node, [node])
