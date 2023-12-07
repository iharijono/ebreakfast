import reacton.ipyvuetify as rv
import solara

from .order import QUANTITY, ORDER, order, order_submitted
from ..models import models

USER = None
order_purchased = solara.reactive(False)
order_nr = solara.reactive(0)

def clear_order():
    print("Clear Order")
    for k, v in QUANTITY.items():
        QUANTITY[k].value = 0
    if order:    
        for m in order.menuitems:
            m.quantity = 0 

@solara.component
def Overview(user):
    global USER
    USER = user
    def purchase():
        if ORDER:
            order = ORDER[0]        
            u = USER.value
            order_meals = []
            for o in order.menuitems:
                meal = {'meal_id': o.name,
                        'quantity': o.quantity}
                order_meals.append(meal)
            oid = models.create_ordermeals(u.username, order_meals)   
            if oid is None:
                print(f'warning: failed in adding order')
            else:
                order_nr.value = oid
                order_purchased.value = True

    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Checkout"):
            # print(f'ORDER => {ORDER}')
            # print(f'QUANTITY => {QUANTITY}')
            if ORDER:
                order = ORDER[0]
                with solara.GridFixed(columns=5):
                    solara.Markdown(f"")
                    solara.Markdown(f"ITEM")
                    solara.Markdown(f"PRICE")
                    solara.Markdown(f"QUANTITY")
                    solara.Markdown(f"SUBTOTAL")
                    cnt = 1
                    total = 0
                    for o in order.menuitems:
                        price = o.price
                        name = o.name
                        quantity = o.quantity
                        if quantity > 0:
                            subtotal = int(quantity) * price
                            subtotal_str = '{0:.2f}'.format(subtotal)
                            solara.Markdown(f"{cnt}")
                            solara.Markdown(f"{name}")
                            solara.Markdown(f"${price}")
                            solara.Markdown(f"{quantity}")
                            solara.Markdown(f"${subtotal_str}")
                            total += subtotal
                            cnt += 1
                        else:
                            continue
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"# TOTAL")
                    total_str = '{0:.2f}'.format(total)
                    solara.Markdown(f"# ${total_str}")
                    
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Button(label="PURCHASE", color="primary", on_click=purchase)
                    
                if order_purchased.value:
                    u = USER.value
                    solara.Text(f"Order for user '{u.username}' with Nr {order_nr.value} is submitted successfully")
                    order_submitted.value = False
                    QUANTITY = {}
                    clear_order()

    return main
