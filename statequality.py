from country import Country

# What does the state quality function look like in code
# My state quality function is 1 housing for every 2 population and 1 electronic per population.
# How do we model this in code?
def calc_state_quality(country: Country):
    print("Population: " + str(country.HOUSING.QUANTITY ))
    # We want 1 house per 2 population and 1 electronic per 1 population
    return 1 - ((country.HOUSING.QUANTITY / (country.POPULATION.QUANTITY / 2)) + (country.ELECTRONICS.QUANTITY / country.POPULATION.QUANTITY ))
