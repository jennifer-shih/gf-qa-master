from dataclasses import dataclass


@dataclass
class PagingInfo:
    """
    Paging info text on list page right bottom
    e.g., Showing 1 to 10 of 100 records
    """

    start: int = None
    end: int = None
    all: int = None

    def get_cnt(self) -> int:
        return self.end - self.start + 1
