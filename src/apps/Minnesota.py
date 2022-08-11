from datetime import datetime
from tokenize import group
from flask import g
import pandas as pd
import numpy as np
import json
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
from data_repo import minnesota_vaccination_df
import json
from urllib.request import urlopen

layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.Table(
                [
                    html.Tr(
                        html.H3('Minnesota Vaccine Distribution Dashboard')
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
        dbc.Col(
            html.Div(
                dcc.DatePickerRange(
                    id = 'my-date-picker-range',
                    min_date_allowed = datetime(2020, 12, 13),
                    max_date_allowed = datetime(2022, 8, 7),
                    initial_visible_month = datetime(2021, 1, 18),
                    start_date = datetime(2020, 12, 13),
                    end_date = datetime(2022, 8, 7)
                ),
            ), width = 2,
        ),

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
                    id = 'minnesota_graph_1'
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
                    id = 'minnesota_graph_2'
                )
            ]), width = 12
        )
    ),

    # dbc.Row(
    #     dbc.Col(
    #         html.Div([
    #             dcc.Graph(
    #                 id = 'minnesota_graph_3'
    #             )
    #         ]), width = 12
    #     )
    # )


])

@app.callback(
    Output('minnesota_graph_1','figure'),
    Output('minnesota_graph_2','figure'),
    # Output('maryland_graph_3','figure'),
    Input('submit', 'n_clicks'),
    State('my-date-picker-range', 'start_date'), 
    State('my-date-picker-range', 'end_date'),
)

def make_figures(n_clicks:int, Start_date: datetime, End_date: datetime):
    filtered_df = minnesota_vaccination_df
    filtered_df['Week Start Date'] = pd.to_datetime(filtered_df['Week Start Date'])
    filtered_df = filtered_df[(filtered_df['Week Start Date'] >= Start_date) & (filtered_df['Week Start Date'] <= End_date)]
    fig1 = px.line(
        filtered_df, 
        x = 'Week Start Date', 
        y = 'Doses Administered Per Week',
        title = "Weekly Vaccination Amount"
    )

    fig2 = px.line(
        filtered_df, 
        x = 'Week Start Date', 
        y = 'Cumulative Total Doses Administered, by week',
        title = "Cumulative Vaccination Timeline"
    )


    # vaccination_df = maryland_vaccination_df
    # # vaccination_df['VACCINATION_DATE'] = pd.to_datetime(vaccination_df['VACCINATION_DATE'])

    # fig2 = px.line(
    #     vaccination_df, 
    #     x = 'VACCINATION_DATE', 
    #     y = 'CompletedVax',
    #     title = 'Daily Vaccination Completed'
    # )

    # fig3 = px.line(
    #     vaccination_df, 
    #     x = 'VACCINATION_DATE', 
    #     y = 'CompletedVaxCumulative',
    #     title = 'Cumulative Vaccination Completed'
    # )

    return fig1, fig2