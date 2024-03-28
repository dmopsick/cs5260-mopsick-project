from __future__ import annotations
from uuid import UUID, uuid4

###########################
# The world state holds a snapshot of all the countries and their resources at a point in time
#
###########################
class WorldState(object):

    ID: UUID
    NAME: str
    COUNTRIES: list

    def __init__(self, countries: list) -> None:
      super().__init__()
      self.ID = uuid4()
      self.COUNTRIES = list
      # What else does the state need to hold?

    def __eq__(self, other: WorldState) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
