"""# ebreakfast
The `Layout` component checks if the current route requires authorization and if the user is logged in. If not, it
redirects to the login form.
"""

import solara
import dataclasses
from typing import Optional, cast
import json
from ..models import models
from .components.basket import basket, add_to_basket
from ..data import menus
from ..basket import add_to_basket


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

def is_password_correct(customer, pwd):
    if customer.password == pwd:
        login_failed.value = False
        user.value = User(customer.id, admin=False)
        login_msg.value = 'You are successfully signed in'

def login(username: str, password: str):
    # this function can be replace by a custom username/password check
    stmt = select(models.Customer).where(models.Customer.id == username)
    with Session(models.myengine()) as session:
        try:
            customer = session.scalars(stmt).one()
            is_password_correct(customer, password)
        except NoResultFound:
            stmt = select(models.Customer).where(models.Customer.email == username)
            try:
                customer = session.scalars(stmt).one()
                is_password_correct(customer, password)
            except NoResultFound:
                login_msg.value = 'No User found'
            
def register():
    print('register')

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
        solara.Button(label="Register", disabled=True, on_click=lambda: register())
        solara.Markdown(f"{login_msg.value}")

@solara.component
def Layout(children=[]):
    route, routes = solara.use_route(peek=True)
    if route is None:
        return solara.Error("Route not found")

    with solara.AppLayout(children=children, navigation=True):
        with solara.AppBar():
            with solara.lab.Tabs(align="center"):
                for route in routes:
                    name = route.path if route.path != "/" else "Sign In"
                    disabled = False
                    if not user.value:
                        disabled = route.path == "order"
                    else:
                        disabled = route.path == "admin"
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
        MenuPage()  # Added the MenuPage component
        Basket()    # Added the Basket component
    # solara.Markdown("This page is visible for everyone")

    # solara.Markdown(__doc__)

    # return main

@solara.component
def MenuItemCard(menu_name):
    with solara.Card(max_width="400px") as main:
        with solara.CardImage(top=True):
            solara.Img(height="250", src=menus[menu_name].image_url)
        solara.CardTitle(children=[menus[menu_name].title])
        with solara.CardText():
            solara.Markdown(f"Price: {menus[menu_name].price}")
            solara.Button("Add to Basket", on_click=lambda: add_to_basket(menu_name))
    return main

@solara.component
def MenuPage():
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Menus"):
            with solara.ColumnsResponsive(12, small=6, large=4):
                for menu_name in menus:
                    MenuItemCard(menu_name)
        Basket()  
    return main

