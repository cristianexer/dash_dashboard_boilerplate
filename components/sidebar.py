import dash_bootstrap_components as dbc
import dash_html_components as html
from settings import APP_NAME
from routes import routes
from utils.styles import SIDEBAR_STYLE
from routes import routes

sidebar = html.Div(
    [
        html.H2(APP_NAME, className="display-5"),
        html.Hr(),
        dbc.Nav([dbc.NavLink(x.name, href=x.path, id=x.name)
                 for x in routes], vertical=True, pills=True,),
    ],
    style=SIDEBAR_STYLE,
)
