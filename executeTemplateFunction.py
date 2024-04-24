
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
              state.COUNTRIES.remove(previous_country)
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

    print("Checking if " + country.NAME + " can perform " + template.NAME)

    # Verify that the incoming state has each of the required inputs
    for resource in template.INPUTS:
        resource_quantity = int(resource.QUANTITY)
        if resource.NAME == "Population":
                if resource_quantity > country.POPULATION.QUANTITY:
                    print("Not enough " + resource.NAME)
                    return False
        elif resource.NAME == "AvailableLand":
            if resource_quantity > country.AVAILABLE_LAND.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "Water":
            if resource_quantity > country.WATER.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "MetallicElements":
            if resource_quantity > country.METALLIC_ELEMENTS.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "MetallicAlloys":
            if resource_quantity > country.METALLIC_ALLOYS.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "Timber":
            if resource_quantity > country.TIMBER.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "Electronics":
            if resource_quantity > country.ELECTRONICS.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        elif resource.NAME == "Housing":
            if resource_quantity > country.HOUSING.QUANTITY:
                print("Not enough " + resource.NAME)
                return False
        else:
            print("Unexpected resouce name provided: " + resource.NAME)
            return False
        

    # All inputs and outputs have been checked
    return True

def apply_template_to_country(country: Country, template: Template):
       # Decrement the resources for the country for each input
        for resource in template.INPUTS:
            resource_quantity = int(resource.QUANTITY)

            if resource.NAME == "Population":
                country.POPULATION.QUANTITY -= resource_quantity
            elif resource.NAME == "AvailableLand":
                country.AVAILABLE_LAND.QUANTITY -= resource_quantity
            elif resource.NAME == "Water":
                country.WATER.QUANTITY -= resource_quantity
            elif resource.NAME == "MetallicElements":
                country.METALLIC_ELEMENTS.QUANTITY -= resource_quantity
            elif resource.NAME == "Timber":
                country.TIMBER.QUANTITY -= resource_quantity
            elif resource.NAME == "MetallicAlloys":
                country.METALLIC_ALLOYS.QUANTITY -= resource_quantity
            elif resource.NAME == "Electronics":
                country.ELECTRONICS.QUANTITY -= resource_quantity
            elif resource.NAME == "Housing":
                country.HOUSING.QUANTITY -= resource_quantity
            else:
                print("Unexpected resouce name provided: " + resource.NAME)

        # Increment the resources for the country for each output
        return country
