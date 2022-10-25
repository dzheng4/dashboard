from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from apps import templates


layout = html.Div([
    dbc.Row([
        templates.navbar(),
        templates.createMenu(),
    ]),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    templates.backHome(),


    templates.contact_footer()
    
])