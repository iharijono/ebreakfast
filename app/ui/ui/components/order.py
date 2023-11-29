import reacton.ipyvuetify as rv
import solara

from ..data import menus

@solara.component
def MenuCard(name):
    menu = menus[name]

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
            solara.Info(f"value: {quantity}")
            solara.Button("min", color="red", icon_name="remove", on_click=decrement)
          
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
            confirm_button = solara.Button("Confirm Changes", color="blue", on_click=confirm_changes)
            
    return main

def confirm_changes():
    print("Changes confirmed!")