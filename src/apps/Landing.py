from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

layout = dbc.Container(
    dcc.Location(
        id = 'url_landing',
        refresh = True
    ),

    dbc.Row(
        
    )


)