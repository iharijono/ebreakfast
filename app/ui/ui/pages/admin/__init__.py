import solara
from ...models import models
import dataclasses
from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

@dataclasses.dataclass
class User:
    username: str
    admin: bool = False

user = solara.reactive(cast(Optional[User], None))
login_failed = solara.reactive(False)
login_msg = solara.reactive('')

def is_password_correct(admin, pwd):
    if admin.password == pwd:
        login_failed.value = False
        user.value = User(admin.id, admin=True)
        login_msg.value = 'You are successfully signed in with admin privilege'

def login(username: str, password: str):
    stmt = select(models.Admin).where(models.Admin.id == username)
    with Session(models.myengine()) as session:
        try:
            admin = session.scalars(stmt).one()
            is_password_correct(admin, password)
        except NoResultFound:
            stmt = select(models.Admin).where(models.Admin.email == username)
            try:
                admin = session.scalars(stmt).one()
                is_password_correct(admin, password)
            except NoResultFound:
                login_msg.value = 'No Admin/User found'

@solara.component
def AdminLoginForm():
    adminname = solara.use_reactive("")
    adminpassword = solara.use_reactive("")
    with solara.Card("Login"):
        solara.Markdown(
            """
                Sign In with your admin name (admin) or email (admin@email.com) that you've registered as admin
                password for above admins are 'secret'
            """
        )
        solara.InputText(label="Username or Email", value=adminname)
        solara.InputText(label="Password", password=True, value=adminpassword)
        solara.Button(label="Login", on_click=lambda: login(adminname.value, adminpassword.value))
        solara.Markdown(f"{login_msg.value}")

@solara.component
def Page():
    with solara.ColumnsResponsive(6, large=4) as main:
        solara.Title("ebreakfast » Admin")
        AdminLoginForm()
    return main
