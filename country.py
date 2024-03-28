from __future__ import annotations
from uuid import UUID, uuid4
from myresource import MyResource

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

    def __init__(self, name: str, count: int) -> None:
      super().__init__()
      self.ID = uuid4()
      self.NAME = name
      self.COUNT = count

    def __eq__(self, other: Resource) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
