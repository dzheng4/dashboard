from data_repo import summary_df, fips_df
from datetime import datetime
import pandas as pd
import numpy as np
import json
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib
from app import app
import json
from urllib.request import urlopen
from apps import templates

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data").resolve()

layout = html.Div([
    dbc.Row([
        templates.navbar()
    ]),
    
    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'output-state'
                )
            ])
        ),
    ]),

    dbc.Row([
        dbc.Col(width = 1),
        dbc.Col(
            dbc.Toast(
                [
                    html.P("Hover over each state to view the data completeness score."),
                    html.P("Then click on the state of interest, you will get an overview of what's available for this state."),
                    html.P("Finally, the link at the bottom will take you to the official website of this state.")
                ],
                header = 'Tips',
                icon = 'primary',
                dismissable=True,
                is_open=True
            )
        ),
    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.Br(),
                html.P("State:",
                    style = {
                        # "margin-left":'50px',
                        'font-weight': '900'
                    }
                ),
            ]),width = {'offset':1},
        ),
    ]),
    
    html.Br(),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.Th(
                    html.Th(
                        id ='state_info',
                        style = {
                            'color' : '#e8bc1c',
                            'backgroundColor':'#414141'
                        }
                    )
                ),  
            ]),width = {'offset':1},
        )
    ),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.Br(),
                html.P("What's available:",
                    style = {
                        # "margin-left":'50px',
                        'font-weight': '900'
                    }
                ),
            ]),width = {'offset':1},
        ),
    ]),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.P(id = 'description')
            ]),width = {'offset':1},
        )
    ),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.Br(),
                html.P("Update Frequency:",
                    style = {
                        # "margin-left":'50px',
                        'font-weight': '900'
                    }
                ),
            ]),width = {'offset':1},
        ),
    ]),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.P(id = 'frequency')
            ]),width = {'offset':1},
        )
    ),

    
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Br(),
                html.P("Policy:",
                    style = {
                        # "margin-left":'50px',
                        'font-weight': '900'
                    }
                ),
            ]),width = {'offset':1},
        ),
    ]),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.P(id = 'policy')
            ]),width = {'offset':1},
        )
    ),

    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(
        dbc.Col(
            html.A("Go to official state website", id = 'link', target="_blank"),
            width = {'offset':1},
        ),
    ),

    


    templates.backHome(),

    html.Br(),
    html.Br(),


    templates.contact_footer()

])


@app.callback(
    Output('output-state','figure'),
    Output('link', 'href'),
    Output('state_info','children'),
    Output('description', 'children'),
    Output('frequency', 'children'),
    Output('policy', 'children'),
    Input('output-state', 'clickData')
)

def update_graph(clickData):
    link = '/'
    state = '/'
    description = '/'
    frequency = '/'
    policy = '/'
    if clickData:
        state = clickData['points'][0]['hovertext']
    
        link = (summary_df[summary_df['State']==state]).values[0][19]

        description = (summary_df[summary_df['State']==state]).values[0][20]

        frequency = (summary_df[summary_df['State']==state]).values[0][21]

        policy = (summary_df[summary_df['State']==state]).values[0][25]


    FipsDF = fips_df

    data_path = "states_data/Official_State_COVID_LINKS.csv"

    df = summary_df

    StateDf = FipsDF[['StateName', 'StateFIPS', 'StateAbbr']]

    df = StateDf.merge(df, how='inner', left_on='StateName',right_on='State').drop_duplicates()

    df = df.drop(columns=['StateName'])

    fig2 = px.choropleth(
        df,
        locations = 'StateAbbr',
        hover_name='State',
        color='Data Score',
        locationmode='USA-states',
        color_continuous_scale=px.colors.sequential.Tealgrn,
        labels = {
            'Data Score' : 'Data Completeness'
        }
    )

    fig2.update_layout(
        title_text='<b>Navigation to States\' Official Website</b>',
        geo_scope='usa'
    )


    return fig2, link, state, description, frequency, policy
