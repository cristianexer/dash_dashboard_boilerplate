import dash_bootstrap_components as dbc
import dash_html_components as html
from utils.styles import SIDEBAR_STYLE
from routes import routes
from settings import settings

sets = settings()

sidebar = html.Div(
    [
        html.H5(sets.APP_NAME, className="display-5 text-center"),
        html.Hr(),
        dbc.Nav([dbc.NavLink(x.name, href=x.path, id=x.name)
                 for x in routes], vertical=True, pills=True,),
    ],
    style=SIDEBAR_STYLE,
)
