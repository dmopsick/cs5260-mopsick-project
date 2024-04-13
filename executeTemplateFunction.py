
from country import Country
from template import Template
from worldstate import WorldState

##########################################
# Execute a transform/transfer template on a world state to create a new world state
# Take in the current world state, the country we want to execute a action on, and the template to execute
#
##########################################
def execute_template(state: WorldState, country: Country, template: Template):
    # Do we want to check here? Shoudl we check on a higher level?
    # Verify we can execute the template with the specified country
    if country_can_execute_template(country, template) == False:
           return None
    
    # Update the country
    # How would we want to handle templates that affect multiple countries?
    updated_country = apply_template_to_country(country, template)

    # Perhaps it would be better to just update the values directly in the state itself
    # This would require just the updating of some values instead of add/remove the same things
    # Remove the previous record of the country
    for i in range(len(state.COUNTRIES)):
        # Select the country from the list to check
        previous_country = state.COUNTRIES[i]

        if previous_country.NAME == country.NAME:
              # This is the country we are updating
              state.COUNTRIES.remove(i)
              break
        
    # Add the new version of the country to the list
    state.COUNTRIES.append(updated_country)

    # Return the new world state
    return state

######################################
# Check if the current state has the resources to execute the specific template
# This means that a country has all the required inputs
# An enhancement to this code base would be to replace all of the string literals with constants
######################################
def country_can_execute_template(country: Country, template: Template):
    # Verify that the incoming state has each of the required inputs
    for resource in template.INPUTS:
        if resource.NAME == "population" and resource.QUANTITY > country.POPULATION:
                return False
        elif resource.NAME == "availableLand" and resource.QUANTITY > country.AVAILABLE_LAND:
                return False
        elif resource.NAME == "water" and resource.QUANTITY > country.WATER:
                return False
        elif resource.NAME == "metallicElements" and resource.QUANTITY > country.METALLIC_ELEMENTS:
                return False
        elif resource.NAME == "metallicAlloys" and resource.QUANTITY > country.METALLIC_ALLOYS:
                return False
        elif resource.NAME == "timber" and resource.QUANTITY > country.TIMBER:
                return False
        elif resource.NAME == "electronics" and resource.QUANTITY > country.ELECTRONICS:
                return False
        elif resource.NAME == "housing" and resource.QUANTITY > country.HOUSING:
                return False
        else:
            print("Unexpected resouce name provided: " + resource.NAME)
            return False
        

    # All inputs and outputs have been checked
    return True

def apply_template_to_country(country: Country, template: Template):
       # Decrement the resources for the country for each input
        for resource in template.INPUTS:
            if resource.NAME == "population":
                country.POPULATION.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "availableLand":
                country.AVAILABLE_LAND.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "water":
                country.WATER.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "metallicElements":
                country.METALLIC_ELEMENTS.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "timber":
                country.TIMBER.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "metallicAlloys":
                country.METALLIC_ALLOYS.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "electronics":
                country.ELECTRONICS.QUANTITY -= resource.QUANTITY
            elif resource.NAME == "housing":
                country.HOUSING.QUANTITY -= resource.QUANTITY
            else:
                print("Unexpected resouce name provided: " + resource.NAME)

       # Increment the resources for the country for each output
