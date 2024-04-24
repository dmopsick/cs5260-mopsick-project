from worldstate import WorldState
from resourceparser import parse_resource
from templateparser import parse_template
from agent import search
from solution import Solution
from typing import List

# Define the file names for different starting states
INITIAL_STATE1_FILE = "initial_state1.csv"
INITIAL_STATE2_FILE = "initial_state2.csv"

# Define the file name for different sets of templates
TEMPLATE_FILE1 = "templates1.txt"

# Set the initial world state with the resource parser
initial_country_list1 = parse_resource(INITIAL_STATE1_FILE)
initial_state_1 = WorldState(initial_country_list1)

# Load the list of templates
template_list = parse_template(TEMPLATE_FILE1)

# Now that the world state is set up time to start our AI agent
schedule: List[Solution] = []

# Let's search for our first country, United States of Dan
country_to_search_for = initial_country_list1[0]

# It is a depth based search 
max_depth = 5
for i in range(max_depth):
    schedule.append(search(initial_state_1, template_list, country_to_search_for))

# So I believe then we just start up the search agent and have it go and print results...
for result in schedule:
    result.print_solution()
    result.print_visited_order()
