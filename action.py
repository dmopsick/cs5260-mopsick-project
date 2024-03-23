from __future__ import annotations
from uuid import UUID, uuid4

class Action(object):

    ID: UUID
    NAME: str

    def __init__(self, name: str, type: str, inputs: list, outputs: list) -> None:
      super().__init__()
      self.ID = uuid4()
      self.NAME = name
      self.TYPE = type
      self.inputs = inputs
      self.outputs = outputs

    def __eq__(self, other: Action) -> bool:
      return self.ID == other.ID

    def __hash__(self) -> int:
      return hash(self.ID)

    def __repr__(self) -> str:
      return self.NAME
