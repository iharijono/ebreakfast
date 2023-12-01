import reacton.ipyvuetify as rv
import solara

from .order import QUANTITY, ORDER

@solara.component
def Overview():
    def purchase():
        print('increment')
        
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
                            subtotal = int(quantity) * float(price[1:])
                            solara.Markdown(f"{cnt}")
                            solara.Markdown(f"{name}")
                            solara.Markdown(f"{price}")
                            solara.Markdown(f"{quantity}")
                            solara.Markdown(f"${subtotal}")
                            total += subtotal
                            cnt += 1
                        else:
                            continue
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"# TOTAL")
                    solara.Markdown(f"# ${total}")
                    
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Markdown(f"")
                    solara.Button(label="PURCHASE", color="primary", on_click=purchase)

    return main
