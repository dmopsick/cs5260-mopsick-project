from __future__ import annotations
from uuid import UUID, uuid4

# Define constants to modify world settings
STARTING_WASTE_VALUE = 0
DEFAULT_RESOURCE_WEIGHT = 1

class Template(object):

    ID: UUID
    NAME: str
    TYPE: str
    INPUTS: list
    OUTPUTS: list

    def __init__(self, name: str, type: str, inputs: list, outputs: list) -> None:
      super().__init__()
      self.ID = uuid4()
      self.NAME = name
      self.TYPE = type
      self.INPUTS = inputs
      self.OUTPUTS = outputs

    def __eq__(self, other: Template) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
