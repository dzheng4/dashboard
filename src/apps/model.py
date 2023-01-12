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
        dbc.Col(width = 1),
        

        dbc.Col([
            html.Br(),

            dbc.Row(
                dcc.Markdown('''
                    ### Model Sets

                    $I\\text{ : Set of Distribution Centers (DC)}$

                    $J\\text{ : Set of Providers}$

                    $K\\text{ : Set of Blocks}$

                    $G\\text{ : Set of Groups}$

                    ''', mathjax=True
                )
            ),

            html.Br(),

            dbc.Row(
                dcc.Markdown('''
                    ### Model Decision Variables

                    $y_j\\text{ : 1 if provider j is utilized, 0 otherwise}$

                    $w_k\\text{ : 1 if block k is covered, 0 otherwise}$

                    $x_{gjk}\\text{ : Unit of vaccine at provider j prepared for group g living in block k}$

                    $z_{i_j}\\text{ : Unit of vaccine distributed from DC i to provider j}$

                    ''', mathjax=True
                )
            ),
        ]),

        dbc.Col([
            html.Br(),

            dbc.Row(
                dcc.Markdown('''
                    ### Model Parameters

                    $f_j\\text{ : Fixed cost of opening provide j}$

                    $a_{j_k}\\text{ : 1 if block k is within the coverage distance from provide j, 0 otherwise}$

                    $c_{i_j}\\text{ : Cost of transporting 1 unit of vaccine from DC i to provide j}$

                    $k_j\\text{ : Capacity of provider j}$

                    $B_i\\text{ : Unit of vaccine available at DC i}$

                    $n_{g_k}\\text{ : Demand of group g at block k}$

                    $\\alpha\\text{ : Weight constant in the objective funtion}$

                    $\\beta\\text{ : Equity constant}$

                    $\\theta\\text{ : Demand percentage constant}$

                    ''', mathjax=True
                )
            ),
        ]),
        
    ]),

    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col(width = 1),
        dbc.Col(
            dbc.Row(
                dcc.Markdown('''
                    ### Model Formulations
                    ''', mathjax=True
                )
            ),
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