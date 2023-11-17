import solara
from .components.basket import basket, add_to_basket

@solara.component
def Layout(children=[]):
    basket_quantity = solara.reactive(0)

    solara.watch(basket, lambda: basket_quantity.set(sum(item['quantity'] for item in basket.value)))

    return solara.VBox(children=[
        solara.Text(f"Basket Quantity: {basket_quantity.value}"),
        *children,
    ])

