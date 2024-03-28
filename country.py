from __future__ import annotations
from uuid import UUID, uuid4
from myresource import MyResource, STARTING_WASTE_VALUE, DEFAULT_RESOURCE_WEIGHT

class Country(object):

    ID: UUID
    NAME: str
    AVAILABLE_LAND: MyResource
    WATER: MyResource
    POPULATION: MyResource
    METALLIC_ELEMENTS: MyResource
    TIMBER: MyResource
    METALLIC_ALLOYS: MyResource
    METALLIC_ALLOYS_WASTE: MyResource 
    ELECTRONICS: MyResource 
    ELECTRONICS_WASTE: MyResource
    HOUSING: MyResource
    HOUSING_WASTE: MyResource

    def __init__(self, name: str, population: MyResource,  available_land: MyResource,
                 water: MyResource, metallic_elements: MyResource, timber: MyResource,
                 metallic_alloys: MyResource, electronics: MyResource, housing: MyResource) -> None:
      super().__init__()
      self.ID = uuid4()
      self.NAME = name
      self.POPULATION = population
      self.AVAILABLE_LAND = available_land
      self.WATER = water
      self.METALLIC_ELEMENTS = metallic_elements
      self.TIMBER = timber
      self.METALLIC_ALLOYS = metallic_alloys
      self.ELECTRONICS = electronics
      self.HOUSING = housing

      # Default the waste values
      self.METALLIC_ALLOYS_WASTE = MyResource('Metallic Alloy Waste', STARTING_WASTE_VALUE, DEFAULT_RESOURCE_WEIGHT)
      self.ELECTRONICS_WASTE = MyResource('Electronics Waste', STARTING_WASTE_VALUE, DEFAULT_RESOURCE_WEIGHT)
      self.HOUSING_WASTE = MyResource('Housing Waste', STARTING_WASTE_VALUE, DEFAULT_RESOURCE_WEIGHT)

    def __eq__(self, other: MyResource) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
