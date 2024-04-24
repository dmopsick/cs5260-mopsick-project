from __future__ import annotations
from uuid import UUID, uuid4
from worldstate import WorldState
from template import Template

##################
# Copied from sample code
#
##################
class Node(object):

    ID: UUID
    STATE: WorldState
    PARENT: Node
    PARENT_ACTION: Template
    PATH_COST: float

    def __init__(self, state: WorldState, parent: Node, parent_action: Template, path_cost: float) -> None:
        super().__init__()
        self.ID = uuid4()
        self.STATE = state
        self.PARENT = parent
        self.PARENT_ACTION = parent_action
        self.PATH_COST = path_cost

    def __eq__(self, other: Node) -> bool:
        return self.ID == other.ID

    def __hash__(self) -> int:
        return hash(self.ID)
