from dataclasses import dataclass


@dataclass
class MAWBStockModel:
    mawb_no: str = None
    prefix: str = None
    carrier: str = None
    status: str = None
    reserved_by: str = None
    file_no: str = None
    office: str = None
    created_date: str = None
    remark: str = None
