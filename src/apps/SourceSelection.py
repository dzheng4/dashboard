from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


layout = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(
            [
                dbc.Card([
                    dbc.CardImg(
                        src = "/assets/cdc-socialmedia-600x300px.jpg",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Consistent Datasets",
                            href='/apps/official_navigation'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : '40%',
                        'margin-right' : 'auto',
                        'border' : 'none'
                    }
                ),
            ]
        ),

        dbc.Col(
            [
                dbc.Card([
                    dbc.CardImg(
                        src = "/assets/individual_states.jpg",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Individual States Datasets",
                            href='/apps/official_navigation'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
                        'margin-right' : '40%',
                        'border' : 'none'
                    }
                ),
            ]
        ),
    ]),

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