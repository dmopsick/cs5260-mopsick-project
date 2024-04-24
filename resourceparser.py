
from myresource import MyResource, DEFAULT_RESOURCE_WEIGHT
from country import Country

#######################################
# Parse a CSV file into a list of countries
# Each country contains a name and a list of resources 
# CSV titles
# country,population,availableLand,water,metallicElements,timber,metallicAlloys,electronics,housing
#######################################
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
            population = MyResource('Population', int(country_val_list[1]), DEFAULT_RESOURCE_WEIGHT)

            # Available Land
            available_land = MyResource('Available Land', int(country_val_list[2]), DEFAULT_RESOURCE_WEIGHT)

            # Water
            water = MyResource('Water', int(country_val_list[3]), DEFAULT_RESOURCE_WEIGHT)

            # MetallicElements
            metallic_elements = MyResource('Metallic Elements', int(country_val_list[4]), DEFAULT_RESOURCE_WEIGHT)

            # Timber
            timber = MyResource('Timber', int(country_val_list[5]), DEFAULT_RESOURCE_WEIGHT)

            # MetallicAlloys
            metallic_alloys = MyResource('Metallic Alloys', int(country_val_list[6]), DEFAULT_RESOURCE_WEIGHT)

            # Electronics
            electronics = MyResource('Electronics', int(country_val_list[7]), DEFAULT_RESOURCE_WEIGHT)

            # Housing
            housing = MyResource('Housing', int(country_val_list[8]), DEFAULT_RESOURCE_WEIGHT)

            # Build county object
            country = Country(country_name, population, available_land, water, metallic_elements, timber,
                               metallic_alloys, electronics, housing)
            
            # Add the country to the country list
            country_obj_list.append(country)

            print("Added " + country_name + " to the country list.")
            # print(vars(country))

    return country_obj_list
