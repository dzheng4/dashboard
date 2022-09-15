from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from apps import templates
import base64


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/jpg;base64,' + base64.b64encode(image).decode('utf-8')

layout = html.Div([
    html.Br(),

    dbc.Row([
        dbc.Col([
            html.Tr(
                html.Th("Model Formulations"),
            ),
        ],
        style = {
            'margin-left' : '10%'
        }
        )
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Img(
                src = b64_image('src/assets/model.jpg'),
            ),
            
        ], 
        style = {
            'margin-left' :'auto',
            'margin-right' : 'auto',
        },
        width = 'auto'), 
    ]),
    html.Br(),
    html.Br(),



    templates.backHome(),


    templates.contact_footer()
    
])