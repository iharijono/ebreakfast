from typing import Optional

import solara

from ... import data
from ...components.order import Overview
from ... import models
from .. import user
# from . import restaurant

@solara.component
def Page(name: Optional[str] = None, page: int = 0, page_size=100):
    with solara.Column() as main:
        solara.Title("ebreakfast » Order")
        Overview(user.value)
    # restaurant.make_multiple_restaurant()
    return main
