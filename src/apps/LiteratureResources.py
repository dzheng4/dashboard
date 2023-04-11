from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from apps import templates


layout = html.Div([
    dbc.Row([
        templates.navbar(),
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


    dbc.Row([
    
        dbc.Col(
            width = 4,
        ),
    
        dbc.Col([
            html.H3(
                "Transportation Science paper",
                style = {
                    'color' : 'grey'
                }
            ),
            html.Br(),
            html.Br(),
            html.Center(
                "Hajibabai, Leila, et al. “Using COVID-19 Data on Vaccine Shipments and Wastage to Inform Modeling and Decision-Making.” Transportation Science, vol. 56, no. 5, 2022, pp. 1135–1147., https://doi.org/10.1287/trsc.2022.1134. ",
                # style = {
                #     'font-size' : '10px'
                # }
            ),

        ], align = 'center', ),

        dbc.Col(
            width = 4,
        ),
    ]),


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