from worldstate import WorldState
from resourceparser import parse_resource
from templateparser import parse_template

# Define the file names for different starting states
INITIAL_STATE1_FILE1 = "initial_state1.csv"

# Define the file name for different sets of templates
TEMPLATE_FILE1 = "templates1.txt"

# Set the initial world state with the resource parser
initial_country_list1 = parse_resource(INITIAL_STATE1_FILE1)
initial_state_1 = WorldState(initial_country_list1)

# Load the list of templates
template_list = parse_template(TEMPLATE_FILE1)