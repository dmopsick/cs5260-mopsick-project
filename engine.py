from worldstate import WorldState
from resourceparser import parse_resource

# Define the file names for different starting states
INITIAL_STATE1_FILE1 = "initial_state1.csv"

# Define constants to modify world settings
STARTING_WASTE_VALUE = 0
DEFAULT_RESOURCE_WEIGHT = 1

# Set the initial world state with the resource parser
initial_country_list1 = parse_resource(INITIAL_STATE1_FILE1)
initial_state_1 = WorldState(initial_country_list1)