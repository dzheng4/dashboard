from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps import templates


layout = html.Div([
    dbc.Row([
        templates.navbar(),
             
    ], className = 'navigationbar'),

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
                            "State Level Vaccine Dist./Admin. Data",
                            href='/apps/CDC'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
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
                        src = "/assets/tableau_demo2.png",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Vaccine Shipment/Provider",
                            href='apps/FOIA'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
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
                        src = "/assets/parquet_demo.png",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Vaccine Administration",
                            href='apps/Parquet'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
                        'margin-right' : 'auto',
                        'border' : 'none'
                    }
                ),
            ]
        ),

        

        
                
        # dbc.Col(
        #     [
        #         dbc.Card([
        #             dbc.CardImg(
        #                 src = "/assets/tableau_demo.png",
        #                 top=True,
        #                 style = {
        #                     "width" : "330px",
        #                     "height": "220px"
        #                 },
        #                 className = 'align-self-center'
        #             ),
        #             dbc.CardBody([
        #                 dbc.Button(
        #                     "Customized Visualizations",
        #                     href='/apps/IndividualStates'
        #                 )
        #             ], className = 'align-self-center')
        #         ],
        #             style = {
        #                 "width" : "30rem",
        #                 'margin-left' : 'auto',
        #                 'margin-right' : 'auto',
        #                 'border' : 'none'
        #             }
        #         ),
        #     ]
        # ),
    ]),

    html.Br(),
    html.Br(),

    dbc.Row([
    
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
                            "State Official Websites",
                            href='/apps/official_navigation'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
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
                        src = "/assets/optimization.jpg",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Model Explanation",
                            href='apps/model'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
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
                        src = "/assets/book.jpg",
                        top=True,
                        style = {
                            "width" : "330px",
                            "height": "220px"
                        },
                        className = 'align-self-center'
                    ),
                    dbc.CardBody([
                        dbc.Button(
                            "Literature Resources",
                            href='/apps/LiteratureResources'
                        )
                    ], className = 'align-self-center')
                ],
                    style = {
                        "width" : "30rem",
                        'margin-left' : 'auto',
                        'margin-right' : 'auto',
                        'border' : 'none'
                    }
                ),
            ]
        ),


        # dbc.Col(
        #     [
        #         dbc.Card([
        #             dbc.CardImg(
        #                 src = "/assets/oimization.jpg",
        #                 top=True,
        #                 style = {
        #                     "width" : "330px",
        #                     "height": "220px"
        #                 },
        #                 className = 'align-self-center'
        #             ),
        #             dbc.CardBody([
        #                 dbc.Button(
        #                     "State Policy",
        #                     href='https://public.tableau.com/views/COVID-19VaccineShipmentSummary/COVID-19VaccineShipmentSummary?:language=en-US&:display_count=n&:origin=viz_share_link'
        #                 )
        #             ], className = 'align-self-center')
        #         ],
        #             style = {
        #                 "width" : "30rem",
        #                 'margin-left' : 'auto',
        #                 'margin-right' : 'auto',
        #                 'border' : 'none'
        #             }
        #         ),
        #     ]
        # ),
    ]),

    html.Br(),
    html.Br(),

    templates.contact_footer()
])