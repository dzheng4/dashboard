from datetime import datetime
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
from urllib.request import urlopen
from apps import templates
from data_repo import cdc_df


layout = html.Div([

    dbc.Row([
        templates.navbar()
    ]),

    html.Br(),

    dbc.Row([
        # dbc.Col(
        #     width = 1
        # ),
        dbc.Col(
            # html.Table(
            #     [
            #         html.Tr(
            #             html.H3('CDC Data Dashboard')
            #         )
            #     ],
            #     style = {
            #         # 'margin-left': '280px',
            #         'margin-top': '20px',
            #         'margin-bottom': '20px',
            #         # 'width': '70%',
            #         'border': '2px solid black',
            #         'text-align': 'center',
            #         'font-family': 'Century Gothic'
            #     }
            # )
            html.H3('CDC Data Dashboard'), style={'margin-left':'5%'}
        )
    ]),
    # All elements from the top of the page
    dbc.Row([

        ## Button element
        dbc.Col(
            html.Div(
                dbc.Button(
                    'Submit',
                    id = 'submit',
                    style = {
                        'background-color' : '#F56262',
                        'display' : 'none' 
                    }
                )
            ), width = 3
        ),
    ], className = "g-0"), #className = "g-0" sets the column gutter size to 0. This removes column padding.
    
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'cdc_graph_1'
                )
            ]), width = 12
        )
    ),

    html.Br(),

    dbc.Row(
        dcc.Dropdown(
            options = ['MP', 'VA', 'BP2', 'WA', 'WY', 'NC', 'DC', 'MI', 'AZ', 'NJ', 'LA', 'IL', 'IA', 'MD',
                        'OH', 'FL', 'VA2', 'MN', 'MS', 'WV', 'SC', 'PR', 'HI', 'MA', 'RI', 'GA', 'NM', 'IN',
                        'WI', 'CT', 'VT', 'SD', 'VI', 'UT', 'OR', 'DE', 'KS', 'OK', 'CO', 'MO', 'MH', 'FM',
                        'CA', 'MT', 'ND', 'ID', 'NH', 'PA', 'ME', 'TN', 'NE', 'IH2', 'KY', 'AK', 'NV', 'AS',
                        'TX', 'AR', 'DD2', 'AL', 'GU', 'NY', 'PW'],
            value = 'NC',
            id = 'state_dropdown'
        )
    ),

    html.Br(),
    html.Br(),

    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'state_graph1'
                )
            ]), width = 12
        )
    ),
    html.Br(),
    html.Br(),

    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'state_graph2'
                )
            ]), width = 12
        )
    ),
    html.Br(),
    html.Br(),
    html.Br(),





    templates.backHome()


])

@app.callback(
    Output('cdc_graph_1','figure'),
    Output('state_graph1', 'figure'),
    Output('state_graph2', 'figure'),
    Input('submit', 'n_clicks'),
    Input('state_dropdown', 'value')
)

def make_figures(n_clicks:int, state:str):
    filtered_df = cdc_df
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    recent_date = cdc_df['Date'].max()

    filtered_df = filtered_df[filtered_df['Date'] == recent_date]
    filtered_df = filtered_df[filtered_df['Location'] != 'US']

    fig1 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Distributed',
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.BuPu,
    )

    fig1.update_layout(
        title_text='Cumulative Distributed Doses As Of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    state_df = cdc_df[cdc_df['Location'] == state].copy()

    fig2 = px.line(
        state_df,
        x = 'Date',
        y = 'Distributed',
        title = 'Cumulative Vaccine Distributed Count for ' + state
    )

    state_df.loc[:, 'Shifted Distributed'] = state_df['Distributed'].shift(1)
    state_df.loc[:, 'Non Cumulative Distributed'] = state_df['Shifted Distributed'] - state_df['Distributed']

    fig3 = px.line(
        state_df,
        x = 'Date',
        y = 'Non Cumulative Distributed',
        title = 'Non Cumulative Vaccine Distributed COunt for ' + state
    )




    
    
    return fig1, fig2, fig3