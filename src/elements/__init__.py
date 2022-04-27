"""
This module is an interface that we can interact with or read values from the web page. We
store the locator when initializing the instance, and use it to get a WebElement when calling
methods.

Notice that these classes are different from WebElement provided by selenium. WebElement is an element that
connects to a real element on the current web page.
"""

from .add_file_button import *
from .autocomplete import *
from .autocomplete_multi_select import *
from .button import *
from .check_datepicker import *
from .check_select import *
from .checkbox import *
from .col_config import *
from .datepicker import *
from .dropdown_multi_select import *
from .edit_input import *
from .element import *
from .email_tags import *
from .input import *
from .label import *
from .link import *
from .multi_autocomplete import *
from .period_datepicker import *
from .popup_select import *
from .radio_group import *
from .select import *
from .spin_bar import *
from .status_icon import *
from .table_header import *
from .tag_input import *
from .textarea import *
