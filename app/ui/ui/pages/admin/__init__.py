import solara
from ... import models

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base


# engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", echo=True, future=True)
engine = create_engine("mysql+pymysql://root:root@localhost/ebreakfast_db", future=True)

login_failed = solara.reactive(False)

def login(username: str, password: str):
    # this function can be replace by a custom username/password check
    if username == "admin" and password == "admin":
        login_failed.value = False
    else:
        login_failed.value = True
        if login_failed.value:
            solara.Error("Wrong adminname or password")

@solara.component
def AdminLoginForm():
    adminname = solara.use_reactive("")
    adminpassword = solara.use_reactive("")
    with solara.Card("Login"):
        solara.Markdown(
            """
                Sign In with your admin name or email that you've registered as admin
            """
        )
        solara.InputText(label="Username or Email", value=adminname)
        solara.InputText(label="Password", password=True, value=adminpassword)
        solara.Button(label="Login", on_click=lambda: login(adminname.value, adminpassword.value))

@solara.component
def Page():
    with solara.ColumnsResponsive(6, large=4) as main:
        solara.Title("ebreakfast » Admin")
        AdminLoginForm()
    return main
