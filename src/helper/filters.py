from src.models import VerifiedModel


class ExceptedFilter:
    """
    A filter object for the dynamic field
    """

    def oi_mbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        dynamic_fields = ["OB/L Received", "Telex release received"]
        refer_field_name = "OB/L Type"

        if field in dynamic_fields:
            if verify_model.get_data(refer_field_name) == "ORIGINAL BILL OF LADING":
                keep_fields = ["OB/L Received"]
            else:
                keep_fields = ["Telex release received"]

            excepted_fields = [i for i in dynamic_fields if i not in keep_fields]
            return True if field in excepted_fields else False
        else:
            return False

    def oi_hbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        dynamic_fields = ["Telex release received", "OB/L Received", "Frt. Released"]
        refer_field_name = "Express B/L"

        if field in dynamic_fields:
            d = verify_model.get_data(refer_field_name)
            if d == "Yes":
                keep_fields = ["Telex release received", "Frt. Released"]
            elif d == "No":
                keep_fields = ["OB/L Received"]
            else:
                raise Exception("Can not find filter rule of [{0}={1}]".format(refer_field_name, d))

            excepted_fields = [i for i in dynamic_fields if i not in keep_fields]
            return True if field in excepted_fields else False
        else:
            return False

    def oe_mbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        return False

    def oe_hbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        dynamic_fields = ["Frt. Released"]
        refer_field_name = "Express B/L"

        if field in dynamic_fields:
            d = verify_model.get_data(refer_field_name)
            if d == "Yes":
                keep_fields = ["Frt. Released"]
            elif d == "No":
                keep_fields = []
            else:
                raise Exception("Can not find filter rule of [{0}={1}]".format(refer_field_name, d))

            excepted_fields = [i for i in dynamic_fields if i not in keep_fields]
            return True if field in excepted_fields else False
        else:
            return False

    def tk_mbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        dynamic_fields = [
            "Port of Loading",
            "Port of Discharge",
            "Departure",
            "Destination",
        ]
        refer_field_name = "Ship Type"

        if field in dynamic_fields:
            if verify_model.get_data(refer_field_name) == "Air":
                keep_fields = ["Departure", "Destination"]
            else:
                keep_fields = ["Port of Loading", "Port of Discharge"]

            excepted_fields = [i for i in dynamic_fields if i not in keep_fields]
            return True if field in excepted_fields else False
        else:
            return False

    def ms_mbl_filter(verify_model: VerifiedModel, field: str) -> bool:
        dynamic_fields = [
            "Port of Loading",
            "Port of Discharge",
            "Departure",
            "Destination",
        ]
        refer_field_name = "Ship Type"

        if field in dynamic_fields:
            if verify_model.get_data(refer_field_name) == "Air":
                keep_fields = ["Departure", "Destination"]
            else:
                keep_fields = ["Port of Loading", "Port of Discharge"]

            excepted_fields = [i for i in dynamic_fields if i not in keep_fields]
            return True if field in excepted_fields else False
        else:
            return False
