from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from apps import templates


layout = html.Div([
    dbc.Row(
        templates.createMenu()
    ),

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


    dbc.Row(
        dbc.Col([
            html.Footer(
                "ATLAS @ North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Dr. Leila Hajibabai, Dr. Ali Hajbabaie, Asya Atik, Kuangying Li, Dayang Zheng",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Department of Industrial & Systems Engineering, North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Department of Civil, Construction and Environmental Engineering, North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            )
        ], align = 'center', className = 'footerbottom')
    )
    
])