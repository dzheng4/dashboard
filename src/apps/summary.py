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

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../states_data").resolve()

layout = html.Div([
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
            html.Table(
                [
                    html.Tr(
                        html.Th('Navigation Dashboard')
                    )
                ],
                style = {
                    'margin-left': '50px',
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
    
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Graph(
                    id = 'output-state'
                )
            ]), width = 12
        )
    ),

    dbc.Row(
        dcc.Input(
            id="input_box",
            type="text",
            placeholder="State Website Link Populates Here",
        ),
    ),

    dbc.Row(
        html.A("Go to website", id = 'link', target="_blank")
    )
    

    

])


@app.callback(
    Output('output-state','figure'),
    Output('link', 'href'),
    Input('submit', 'n_clicks'),
    Input('output-state', 'clickData')
)

def update_graph(n_clicks:int, clickData):
    # try:
    #     print(clickData['points'][0]['hovertext'])
    # except TypeError:
    #     print(TypeError)
    link = '/'
    if clickData:
        state = clickData['points'][0]['hovertext']
    
        link = (summary_df[summary_df['State']==state]).values[0][1]

    # path = "~/Downloads/fips2county.tsv"
    # path = "fips2county.tsv"
    # FipsDF = pd.read_csv(path, sep='\t', header='infer', dtype=str, encoding='latin-1')
    FipsDF = fips_df

    # data_path = "~/github projects/ncsu-covid-19-vaccine-logistics-dashboard/states_data/Official_State_COVID_LINKS.csv"
    data_path = "states_data/Official_State_COVID_LINKS.csv"


    # df = pd.read_csv(data_path)
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
        color_continuous_scale=px.colors.sequential.BuPu,
    )

    fig2.update_layout(
        title_text='United States COVID-19 Vaccine Distribution Summary',
        geo_scope='usa'
    )


    return fig2, link
