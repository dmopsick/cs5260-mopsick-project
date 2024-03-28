from __future__ import annotations
from uuid import UUID, uuid4

class State(object):

    ID: UUID
    COUNTRIES: list

    def __eq__(self, other: State) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
