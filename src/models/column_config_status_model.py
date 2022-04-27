from dataclasses import dataclass


@dataclass
class ColConfigStatus:
    """
    column config status
    status: True-> checked; False-> unchecked
    is_pinned: True-> above freeze column divider; False-> below freeze column divider
    """

    name: str = ""
    status: bool = None
    is_pinned: bool = None
