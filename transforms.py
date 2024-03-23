from country import Country

def build_house(country: Country):
    # Validate that the passed in country has a the required resources
    if (country.population.QUANTITY < 5 or
        country.metallicElements.QUANTITY < 1 or
        country.timber.QUANTITY < 5 or
        country.metallicAlloys.QUANTITY < 3
    ):
        return 1

    # Perform the decrement of resources
    country.metallicElements -= 1
    country.timber -= 5
    country.metallicAlloys -= 3

    # Add in the created resources
    country.housing += 1
    country.housingWaste +=1

    # Population remains steadfast at 5

    # Returning 0 will mean all good
    return 0

def refine_metal(country: Country):
    # Validate that the passed in country has valid resources to make this transform


    # Perform the decrement of resources

    # Add in the created resources

    # Returning 0 means all good
    return 0
