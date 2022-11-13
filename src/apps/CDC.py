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


states_dic = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'DC': 'District of Columbia',
    'MP': 'Northern Mariana Islands',
    'PW': 'Palau',
    'PR': 'Puerto Rico',
    'VI': 'Virgin Islands',
}


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
            dbc.Card(
                dbc.CardBody(
                    html.H3('CDC Data Dashboard', style={'text-transform':'None','color':'white'}), style={'margin-left':'4%'}
                ),
                color="dark"
            )
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
            dcc.Graph(
                id = 'cdc_graph_1'
            )
        )
    ),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.P("You may select a vaccine type filter here"), style={'padding-left':'4%'}
        )
    ]),

    dcc.Loading(
        children = [
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        # options = {'All':'', 'Pfizer':'Pfizer','Moderna':'Moderna'},
                        options = ['All', 'Pfizer','Moderna','Janssen'],
                        value = 'All',
                        id = 'vaccine_type_dropdown'
                    ), width = 3, style={'padding-left':'4%'}
                )
            ]),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_2'
                    ), width = 6
                ),
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_3'
                    ), width = 6
                )
            ]),
        ]
    ),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id = 'cdc_graph_4'
            ), width = 6
        ),
        dbc.Col(
            dcc.Graph(
                id = 'cdc_graph_5'
            ), width = 6
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.P("Please select a state in the dropdown"), style={'padding-left':'4%'}
        )
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                # options = ['MP', 'VA', 'BP2', 'WA', 'WY', 'NC', 'DC', 'MI', 'AZ', 'NJ', 'LA', 'IL', 'IA', 'MD',
                #             'OH', 'FL', 'VA2', 'MN', 'MS', 'WV', 'SC', 'PR', 'HI', 'MA', 'RI', 'GA', 'NM', 'IN',
                #             'WI', 'CT', 'VT', 'SD', 'VI', 'UT', 'OR', 'DE', 'KS', 'OK', 'CO', 'MO', 'MH', 'FM',
                #             'CA', 'MT', 'ND', 'ID', 'NH', 'PA', 'ME', 'TN', 'NE', 'IH2', 'KY', 'AK', 'NV', 'AS',
                #             'TX', 'AR', 'DD2', 'AL', 'GU', 'NY', 'PW'],
                options = states_dic,
                id = 'state_dropdown'
            ), width = 3, style={'padding-left':'4%'}
        )
    ]),

    html.Br(),
    html.Br(),

    dcc.Loading(
        children = [
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
        ]
    ),

    
    html.Br(),
    html.Br(),
    html.Br(),


    templates.backHome()


])

@app.callback(
    Output('cdc_graph_1','figure'),
    Output('cdc_graph_2','figure'),
    Output('cdc_graph_3','figure'),
    Output('cdc_graph_4','figure'),
    Output('cdc_graph_5','figure'),
    Output('state_graph1', 'figure'),
    Output('state_graph2', 'figure'),
    Input('submit', 'n_clicks'),
    Input('state_dropdown', 'value'),
    Input('vaccine_type_dropdown','value')
)

def make_figures(n_clicks:int, state:str, type:str):
    type_key = '_' + type
    if type == 'All':
        type = ' '
        type_key = ''
    else:
        type = ' ' + type + ' '

    

    filtered_df = cdc_df
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    recent_date = cdc_df['Date'].max()

    filtered_df = filtered_df[filtered_df['Date'] == recent_date]
    filtered_df = filtered_df[filtered_df['Location'] != 'US']

    filtered_df['Available'+type_key] = filtered_df['Distributed'+type_key] - filtered_df['Administered'+type_key]
    filtered_df['Available Percentage'+type_key] = filtered_df['Available'+type_key] / filtered_df['Distributed'+type_key] * 100

    cdc_fig1 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Series_Complete_Pop_Pct',
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.BuPu,
    )

    cdc_fig1.update_layout(
        title_text='Series Complete Percentage as of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    cdc_fig2 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Distributed' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig2.update_layout(
        title_text='Cumulative Distributed' + type + 'Doses Count as of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    cdc_fig3 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Administered' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig3.update_layout(
        title_text='Cumulative Administered' + type + 'Doses Count as of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    cdc_fig4 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Available' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig4.update_layout(
        title_text='Theoretically Available' + type + 'Doses Count as of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    cdc_fig5 = px.choropleth(
        filtered_df,
        locations = 'Location',
        hover_name = 'Location',
        color = 'Available Percentage' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig5.update_layout(
        title_text= type + 'Theoretically Available Percentage as of ' + recent_date.strftime("%m/%d/%Y"),
        geo_scope='usa'
    )

    

    state_df = cdc_df[cdc_df['Location'] == state].copy()

    if not state:
        state = " "
    else:
        state = states_dic[state]

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
        title = 'Non-Cumulative Vaccine Distributed Count for ' + state
    )




    
    
    return cdc_fig1, cdc_fig2, cdc_fig3, cdc_fig4, cdc_fig5, fig2, fig3