"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.heading("Simple app")
    )
    
def about():
    return pc.text("About Page")


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.compile()
