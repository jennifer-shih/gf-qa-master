from src.elements.element import Element


class Textarea(Element):
    __name = "Textarea"

    def __init__(self, locator: tuple):
        super(Textarea, self).__init__(locator)

    def get_value(self, timeout=5) -> str:
        return self._get_val(timeout=timeout)
