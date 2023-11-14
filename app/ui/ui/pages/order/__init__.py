from typing import Optional

import solara

from ... import data
from ...components.order import Overview
from ... import models
from .. import user

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base


# engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", echo=True, future=True)
engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", future=True)

@solara.component
def Page(name: Optional[str] = None, page: int = 0, page_size=100):
    with solara.Column() as main:
        solara.Title("ebreakfast » Order")
        Overview()
    return main
