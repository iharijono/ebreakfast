import solara
from .components.basket import basket, add_to_basket

basket = solara.reactive({})

@solara.component
def Basket():
    with solara.Card("Basket"):
        with solara.ListGroup():
            for menu_name, quantity in basket.value.items():
                solara.ListGroupItem(f"{menu_name} (Quantity: {quantity})")

def add_to_basket(menu_name, quantity=1):
    current_quantity = basket.value.get(menu_name, 0)
    basket.value[menu_name] = current_quantity + quantity
    print(f"Added {quantity}x {menu_name} to the basket")


def checkout():
    print("Proceeding to checkout...")

    if not basket.value:
        print("Basket is empty. Cannot proceed to checkout.")
        return
    
    total_price = sum(item['quantity'] * menus[item['name']].price for item in basket.value)

    print("Items in the basket:")
    for item in basket.value:
        print(f"{item['name']} - Quantity: {item['quantity']}")

    print(f"Total Price: ${total_price:.2f}")

    basket.set([])
