import reacton.ipyvuetify as rv
import solara

from ..data import menus

@solara.component
def MenuCard(name):
    menu = menus[name]

    # Reactive variable to store the quantity
    quantity = solara.reactive(0)

    def increment():
        quantity.value +=1

    def decrement():
        if quantity.value > 0:
            quantity.value -= 1

    with rv.Card(max_width="400px") as main:
        # with solara.Link(f"/menu/{name}"):
        rv.Img(height="250", src=menu.image_url)
        rv.CardTitle(children=[menu.price])
        with rv.CardText():
            solara.Markdown(menu.markdown)
        with solara.Row(justify="space-around", margin=10):
            solara.Button("add", color="green", icon_name="add", on_click=increment)
            solara.Info(f"value: {quantity.value}")
            solara.Button("min", color="green", icon_name="remove", on_click=decrement)
          
    return main


@solara.component
def Overview():
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Menu"):
            with solara.ColumnsResponsive(12, small=6, large=4):
                for name in menus:
                    MenuCard(name)

# Add a button at the end of the page to confirm changes
        with solara.Row(justify="flex-end", margin=10):
            confirm_button = solara.Button("Confirm Changes", on_click=confirm_changes)
            
    return main

def confirm_changes():
    print("Changes confirmed!")