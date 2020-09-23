import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from server import app
from datetime import datetime as dt
import dash
import re

content = html.Div([
    html.Div([
        html.Div([
            dcc.DatePickerRange(
                id='date-range-map',
                min_date_allowed=dt(2020, 1, 1),
                max_date_allowed=dt.now().date(),
                initial_visible_month=dt.now().date(),
                end_date=dt.now().date(),
            ),
        ], className='col-xs-12 col-md-6'),

        html.Div([

            html.Div(id='output-container-date-picker-range')

        ], className='col-xs-12 col-md-6')

    ], className='row')
])


@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('date-range-map', 'start_date'),
     dash.dependencies.Input('date-range-map', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix
