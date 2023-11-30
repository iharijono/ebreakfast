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

order = solara.reactive(cast(Optional[Order], None))
order_submitted = solara.reactive(False)

@solara.component
def MenuCard(name, menu):
    quantity, set_quantity = solara.use_state(0)
    def increment():
        set_quantity(quantity + 1)
    def decrement():
        if quantity > 0:
            set_quantity(quantity - 1)
            
    with rv.Card(max_width="400px") as main:
        # with solara.Link(f"/menu/{name}"):
        rv.Img(height="250", src=menu.image_url)
        rv.CardTitle(children=[menu.price])
        with rv.CardText():
            solara.Markdown(menu.markdown)
        with solara.Row(justify="space-around", margin=10):
            solara.Button("add", color="green", icon_name="add", on_click=increment)
            solara.Button(f"{quantity}", color="yellow")
            solara.Button("min", color="red", icon_name="remove", on_click=decrement)
            
            
    oitem = OrderItem(name=name, quantity=2, price=menu.price)
    order.value.menuitems.append(oitem)
    return main


@solara.component
def Overview(user):
    print(f'order component: user => {user}')
    order.value = Order(username=user.username if user else '', menuitems=[])
    menus = models.get_menus('ebreakfast')
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Menu"):
            with solara.ColumnsResponsive(12, small=6, large=4):
                for name in menus:
                    MenuCard(name, menus[name])
    order_submitted.value = True
    return main

def confirm_changes():
    print("Changes confirmed!")