from __future__ import annotations
from uuid import UUID, uuid4

class Resource(object):

    ID: UUID
    name: str
    availableLand: Resource
    water: Resource
    population: Resource
    metallicElements: Resource
    timber: Resource
    metallicAlloysWate: Resource # Unsure if I need this
    nintendo3DS: Resource # I am treating this as electronics in the example
    # It just has a more fun name
    nintendo3DSWaste: Resource # I am not sure I need this
    housing: Resource
    houseingWaste: Resource

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
