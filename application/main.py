
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from utils.styles import CONTENT_STYLE
from components.sidebar import sidebar
from settings import settings
from server import app, server
from routes import routes
from dash.dependencies import Input, Output

sets = settings()

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback([Output(i.name, "active") for i in routes], [Input("url", "pathname")])
def toggle_active_links(pathname):
    actives = list()
    for x in routes:
        if type(x.path) == str:
            if pathname == x.path:
                actives.append(True)
            else:
                actives.append(False)
        if type(x.path) == list:
            if pathname in x.path:
                actives.append(True)
            else:
                actives.append(False)
    return actives


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    for x in routes:
        if type(x.path) == str:
            if pathname == x.path:
                return x.content
        if type(x.path) == list:
            if pathname in x.path:
                return x.content
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=sets.APP_PORT, debug=sets.APP_DEBUG,
                   threaded=sets.APP_THREADED)
