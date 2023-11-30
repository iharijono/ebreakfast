import reacton.ipyvuetify as rv
import solara

from ..data import menus
from .order import order

@solara.component
def Overview():
    def increment():
        print('increment')
        
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Checkout"):
            if order.value:
                with solara.GridFixed(columns=5):
                    solara.Markdown(f"")
                    solara.Markdown(f"ITEM")
                    solara.Markdown(f"PRICE")
                    solara.Markdown(f"QUANTITY")
                    solara.Markdown(f"SUBTOTAL")
                    cnt = 1
                    total = 0
                    for o in order.value.menuitems:
                        quantity = o.quantity
                        price = o.price
                        name = o.name
                        subtotal = int(quantity) * float(price[1:])
                        solara.Markdown(f"{cnt}")
                        solara.Markdown(f"{name}")
                        solara.Markdown(f"{price}")
                        solara.Markdown(f"{quantity}")
                        solara.Markdown(f"${subtotal}")
                        total += subtotal
                        cnt += 1
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"# TOTAL")
                    solara.Markdown(f"# ${total}")
                    
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Button(label="PURCHASE", color="primary", on_click=increment)

    return main
