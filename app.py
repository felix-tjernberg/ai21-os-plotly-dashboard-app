import dash
import logging


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)
server = app.server

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
