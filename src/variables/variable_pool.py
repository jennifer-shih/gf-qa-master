class VariablePool:
    def __init__(self):
        self._dict = {}

    def add_dict(self, dict_name: str, value: dict):
        """
        Add a dictionary to variable pool with key [dict_name].
        If the dictionary is existed merge the existed dictionary with the input one.
        """
        if dict_name in self._dict:
            # self._dict[dict_name][key] = value
            self._dict[dict_name] = {**self._dict[dict_name], **value}
        else:
            self._dict[dict_name] = value

    def add_v(self, v_name: str, value):
        self._dict[v_name] = value

    def add_list(self, list_name: str, value, index=None):
        if list_name not in self._dict:
            self._dict[list_name] = []
        if index:
            self._dict[list_name].insert(index, value)
        else:
            self._dict[list_name].append(value)

    def pop(self, dict_name: str):
        return self._dict.pop(dict_name)

    def get(self, dict_name: str):
        return self._dict[dict_name]

    def has_v(self, dict_name: str) -> bool:
        return dict_name in self._dict
