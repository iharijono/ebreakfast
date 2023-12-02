import reacton.ipyvuetify as rv
import solara
import dataclasses
from typing import Optional, cast

from ..models import models

@dataclasses.dataclass
class OrderItem:
    name: str
    quantity: int
    price: float

@dataclasses.dataclass
class Order:
    username: str
    menuitems: list[OrderItem]

order = None
QUANTITY = {}
order_submitted = solara.reactive(False)
ORDER = []

def get_menuitem(name, menuitems):
    for m in menuitems:
        if m.name == name:
            return m
    return None

@solara.component
def MenuCard(name, menu):
    def increment():
        q = QUANTITY.get(name, None)
        m = get_menuitem(name, order.menuitems)
        if q:
            QUANTITY[name].value += 1
        if m:
            m.quantity = QUANTITY[name].value
    def decrement():
        q = QUANTITY.get(name, None)
        m = get_menuitem(name, order.menuitems)
        if q:
            if QUANTITY[name].value > 0:
                QUANTITY[name].value -= 1
        if m:
            m.quantity = QUANTITY[name].value
            
    with rv.Card(max_width="400px") as main:
        rv.Img(height="250", src=menu.image_url)
        rv.CardTitle(children=[f'${menu.price}'])
        with rv.CardText():
            solara.Markdown(menu.markdown)
        with solara.Row(justify="space-around", margin=10):
            solara.Button("add", color="green", icon_name="add", on_click=increment)
            solara.Button(f"{QUANTITY[name]}", color="yellow")
            solara.Button("min", color="red", icon_name="remove", on_click=decrement)
    return main


@solara.component
def Overview(user):
    global order
    print(f'order component: user => {user}')
    if order is None:
        order = Order(username=user.username if user else '', menuitems=[])
        ORDER.insert(0, order)
    menus = models.get_menus('ebreakfast')    
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Menu"):
            with solara.ColumnsResponsive(12, small=6, large=4):
                for name in menus:
                    menu = menus[name]
                    m = get_menuitem(name, order.menuitems)
                    if m is None:
                        q = QUANTITY.get(name, None)
                        if q is None:
                            QUANTITY[name] = solara.reactive(0)
                        oitem = OrderItem(name=name, quantity=QUANTITY[name].value, price=float(menu.price))
                        order.menuitems.append(oitem)
                    MenuCard(name, menu)
                    
# Add a button at the end of the page to confirm changes
        with solara.Row(justify="flex-end", margin=10):
            confirm_button = solara.Button("Confirm Changes", color="blue", on_click=confirm_changes)

    return main

def confirm_changes():
    print("Changes confirmed!")
    for m in order.menuitems:
        m.quantity = QUANTITY[m.name].value
    
    order_submitted.value = True
    Overview()
    