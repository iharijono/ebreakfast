import reacton.ipyvuetify as rv
import solara

from ..data import menus


@solara.component
def MenuCard(name):
    menu = menus[name]
    with rv.Card(max_width="400px") as main:
        # with solara.Link(f"/menu/{name}"):
        rv.Img(height="250", src=menu.image_url)
        rv.CardTitle(children=[menu.price])
        with rv.CardText():
            solara.Markdown(menu.markdown)
    return main


@solara.component
def Overview():
    with solara.ColumnsResponsive(12) as main:
        with solara.Card("Menu"):
            with solara.ColumnsResponsive(12, small=6, large=4):
                for name in menus:
                    MenuCard(name)
    return main
