import copy

# Calling it MyResource because Python told me Resource was reserved
from myresource import MyResource
from country import Country
from engine import STARTING_WASTE_VALUE

def parse_resource(file_path):
    country_obj_list = []

    # Load the file
    with open(file_path, 'r') as file:
        content = file.read()
        # Split the read file by line
        countries = content.split('\n')

        # Skip the first row of the CSV which holds the titles
        # If we wanted to make this smarter we would define the resource names
        # Based on what is passed in here
        for x in range(1, len(countries)): 
            # Select a row which represents a country
            country_row = countries[x]

            # Separate the line by the comma to get the individual values
            country_val_list = country_row.split(',')

            # Build the object from the passed in values
            # Load them in the order the are set in the csv
            # Again this could be made smarter by using the first row to determine what is being used
            # Country name
            country_name = country_val_list[0]

            # Population
            population = country_val_list[1]

            # Available Land
            available_land = country_val_list[2]

            # Water
            water = country_val_list[3]

            # MetallicElements
            metallic_elements = country_val_list[4]

            # Timber
            timber = country_val_list[5]

            # MetallicAlloys
            metallic_elements = country_val_list[6]

            # Electronics
            electronics = country_val_list[7]

            # Housing
            housing = country_val_list[8]

            # Build county object



    return country_obj_list
