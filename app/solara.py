from solara import Solara
from app import app, db

solara = Solara(app)

if __name__ == "__main__":
    solara.run(db)
