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

    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.H3('CDC Data Dashboard')
                    )
                ],
                style = {
                    'margin-left': '280px',
                    'margin-top': '20px',
                    'margin-bottom': '20px',
                    'width': '70%',
                    'border': '2px solid black',
                    'text-align': 'center',
                    'font-family': 'Century Gothic'
                }
            )
        )
    ),
    # All elements from the top of the page
    dbc.Row([

        ## Button element
        dbc.Col(
            html.Div(
                dbc.Button(
                    'Submit',
                    id = 'submit',
                    style = {
                        'background-color' : '#F56262'    
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




    templates.backHome()


])

@app.callback(
    Output('cdc_graph_1','figure'),
    Input('submit', 'n_clicks'),
)

def make_figures(n_clicks:int):
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
    
    
    return fig1