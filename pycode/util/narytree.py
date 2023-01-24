from __future__ import annotations
from typing import Optional

class NTreeNode:
    def __init__(
        self,
        val: int = 0,
        children: Optional[list[NTreeNode]] = None,
    ) -> None:
        self.val = val
        self.children = children if children else []

    def __repr__(self) -> str:
        return f'NTN:{self.val}'

