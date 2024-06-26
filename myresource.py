from __future__ import annotations
from uuid import UUID, uuid4

# Define constants to modify world settings
STARTING_WASTE_VALUE = 0
# DEFAULT_RESOURCE_WEIGHT is a constant I have set to 1 for now making every resource the same weight
DEFAULT_RESOURCE_WEIGHT = 1

class MyResource(object):

    ID: UUID
    NAME: str
    QUANTITY: int
    WEIGHT: int

    def __init__(self, name: str, quantity: int, weight: int) -> None:
      super().__init__()
      self.ID = uuid4()
      self.NAME = name
      self.QUANTITY = quantity
      self.WEIGHT = weight

    def __eq__(self, other: MyResource) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
