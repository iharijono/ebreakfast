from typing import Optional

import solara

from ... import data
from ...components.checkout import Overview
from ... import models
from .. import user

from sqlalchemy.orm import Session

@solara.component
def Page(name: Optional[str] = None, page: int = 0, page_size=100):
    with solara.Column() as main:
        solara.Title("ebreakfast » Checkout")
        Overview(user)
    return main
