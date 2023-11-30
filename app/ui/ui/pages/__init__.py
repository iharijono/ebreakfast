"""# ebreakfast
The `Layout` component checks if the current route requires authorization and if the user is logged in. If not, it
redirects to the login form.
"""

import solara
import dataclasses
from typing import Optional, cast
import json
from ..models import models

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base

from ..components.order import order, order_submitted

@dataclasses.dataclass
class User:
    username: str
    admin: bool = False

user = solara.reactive(cast(Optional[User], None))
login_failed = solara.reactive(False)
login_msg = solara.reactive('')

def is_password_correct(customer, pwd):
    if customer.password == pwd:
        login_failed.value = False
        user.value = User(customer.id, admin=False)
        login_msg.value = 'You are successfully signed in'
    else:
        order.value = None

def login(username: str, password: str):
    # this function can be replace by a custom username/password check
    stmt = select(models.Customer).where(models.Customer.id == username)
    with Session(models.myengine()) as session:
        try:
            customer = session.scalars(stmt).one()
            is_password_correct(customer, password)
            print(f'USER => {user.value}')
        except NoResultFound:
            stmt = select(models.Customer).where(models.Customer.email == username)
            try:
                customer = session.scalars(stmt).one()
                is_password_correct(customer, password)
            except NoResultFound:
                login_msg.value = 'No User found'

@solara.component
def LoginForm():
    username = solara.use_reactive("")
    password = solara.use_reactive("")
    with solara.Card("Login"):
        solara.Markdown(
            """
                Sign In with your user name or email that you've registered
                for testing, enter 'test' and password 'secret'
                or enter 'test@email.com' and password 'secret'
            """
        )
        solara.InputText(label="Username or Email", value=username)
        solara.InputText(label="Password", password=True, value=password)
        solara.Button(label="Login", on_click=lambda: login(username.value, password.value))
        solara.Markdown("")
        solara.Markdown(f"{login_msg.value}")

@solara.component
def Layout(children=[]):
    route, routes = solara.use_route(peek=True)
    if route is None:
        return solara.Error("Route not found")

    # print(f'ROUTE => {route}\n\n')
    # print(f'ROUTES => {routes}\n\n')
    # print(f'CHILDREN => {children}')
    # children = check_auth(route, children)

    with solara.AppLayout(children=children, navigation=True):
        with solara.AppBar():
            with solara.lab.Tabs(align="center"):
                for route in routes:
                    name = route.path if route.path != "/" else "Sign In"
                    disabled = False
                    if not user.value:
                        disabled = (route.path == "order" or route.path == "checkout")
                    else:
                        if route.path == "admin":
                            disabled = route.path == "admin"
                        else:
                            if not order_submitted.value:
                                disabled = route.path == "checkout"
                            
                    solara.lab.Tab(name, path_or_route=route, disabled=disabled)
            if user.value:
                solara.Text(f"Logged in as {user.value.username} as {'admin' if user.value.admin else 'user'}")
                with solara.Tooltip("Logout"):
                    solara.Button(icon_name="mdi-logout", icon=True, on_click=lambda: user.set(None))
            else:
                with solara.AppBar():
                    solara.Text("Not logged in")


@solara.component
def Page():
    with solara.ColumnsResponsive(6, large=4) as main:
        solara.Title("ebreakfast » Sign In")
        LoginForm()
