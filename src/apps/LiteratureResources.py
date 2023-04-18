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

    dbc.Row([
    
        dbc.Col(
            width = 4,
        ),
    
        dbc.Col([
            html.H3(
                "Transportation Science Paper",
                style = {
                    'color' : 'grey'
                }
            ),

            html.Center(
                "Hajibabai, Leila, et al. “Using COVID-19 Data on Vaccine Shipments and Wastage to Inform Modeling and Decision-Making.” Transportation Science, vol. 56, no. 5, 2022, pp. 1135–1147.",
                # style = {
                #     'font-size' : '10px'
                # }
            ),
            html.A("https://doi.org/10.1287/trsc.2022.1134", id = 'link', href="https://doi.org/10.1287/trsc.2022.1134", style={'margin-left':'17%'}),

            html.Br(),
            html.Br(),
            html.Br(),

            html.H4(
                "Presentations at INFORMS, DSI, TRB",
                style = {
                    'color' : 'grey'
                }
            ),


            html.Center(
                "Li K., Atik A., Zheng D., Hajibabai L., Hajbabaie A. “A Location-Allocation Model for Optimizing COVID-19 Vaccine Distribution Using Real-World Shipment Data”, 2022 INFORMS (Institute for Operations Research and Management Sciences) Annual Meeting",
                # style = {
                #     'font-size' : '10px'
                # }
            ),

            html.Br(),

            html.Center(
                "Li K., Atik A., Zheng D., Hajibabai L., Hajbabaie A. “A Location-Allocation Model for Optimizing COVID-19 Vaccine Distribution Using Real-World Shipment Data”, 53rd Annual Conference of the Decision Sciences Institute",
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

    templates.backHome(),


    templates.contact_footer()
    
])