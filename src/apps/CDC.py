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
                    html.H3('State Level Vaccine Distribution and Administration Across the US', style={'text-transform':'None','color':'white'}), style={'margin-left':'4%'}
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
    
    dcc.Loading(
        children = [
            dbc.Row(
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_1'
                    )
                ),
            ),
            dbc.Row([
                dbc.Col(
                    width = 3
                ),
                dbc.Col(
                    dbc.Toast(
                        [
                            html.P("Scroll up/down in the map area to zoom in/out. Double-click anywhere on the map to reset the graph size.")
                        ],
                        header = 'Tips',
                        icon = 'primary',
                        dismissable=True,
                        is_open=True
                    )
                ),
                dbc.Col(
                    width = 3
                )
            ])
        ]
    ),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.P("You may select a vaccine type filter here"), style={'padding-left':'4%'}
        )
    ]),

    html.Br(),

    dcc.Loading(
        children = [
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        # options = {'All':'', 'pfizer':'pfizer','moderna':'moderna'},
                        options = ['All', 'pfizer','moderna','janssen'],
                        value = 'All',
                        id = 'vaccine_type_dropdown'
                    ), width = 3, style={'padding-left':'4%'}
                )
            ]),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_2',
                        style={"border":"3px black solid", "margin-left":"2.5%", "margin-right":"1.25%"},
                    ), width = 6
                ),
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_3',
                        style={"border":"3px black solid", "margin-left":"1.25%", "margin-right":"2.5%"},
                    ), width = 6
                )
            ]),

            html.Br(),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_4',
                        style={"border":"3px black solid", "margin-left":"2.5%", "margin-right":"1.25%"},
                    ),  width = 6
                ),
                dbc.Col(
                    dcc.Graph(
                        id = 'cdc_graph_5',
                        style={"border":"3px black solid", "margin-left":"1.25%", "margin-right":"2.5%"},
                    ),  width = 6
                )
            ]),
        ]
    ),

    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col(
            html.P("Please select a state in the dropdown"), style={'padding-left':'4%'}
        ),
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
                value = 'NC',
                id = 'state_dropdown'
            ), width = 3, style={'padding-left':'4%'}
        ),
        dbc.Col(
            dbc.Toast(
                [
                    html.P("Below graphs are going to render after a specific state is selected (Default North Carolina)."),
                    html.Br(),
                    html.P("You may also drag-select an area to zoom in. Double-click anywhere on the graph to reset the graph size.")
                ],
                header = 'Tips',
                icon = 'primary',
                dismissable=True,
                is_open=True
            )
        ),
        dbc.Col(
            width = 2
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
                    ]), width = 12, 
                ), style={"border":"4px black solid", "margin-left":"2.5%", "margin-right":"2.5%"}
            ),
            html.Br(),
            html.Br(),

            dbc.Row(
                dbc.Col(
                    html.Div([
                        dcc.Graph(
                            id = 'state_graph2'
                        )
                    ]), width = 12,
                ), style={"border":"4px black solid", "margin-left":"2.5%", "margin-right":"2.5%"}
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
    Input('submit', 'n_clicks'),
)

def render_overall(n_clicks:int):
    filtered_df = cdc_df.copy()
    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    recent_date = pd.to_datetime(cdc_df['date']).max()

    filtered_df = filtered_df[filtered_df['date'] == recent_date]
    filtered_df = filtered_df[filtered_df['location'] != 'US']



    cdc_fig1 = px.choropleth(
        filtered_df,
        locations = 'location',
        hover_name = 'location',
        color = 'series_complete_pop_pct',
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.BuPu,
        labels = {
            'series_complete_pop_pct' : 'Series Complete Percentage'
        }
    )

    cdc_fig1.update_layout(
        title_text='<b>Percentage of Population Fully Vaccinated as of ' + recent_date.strftime("%m/%d/%Y") + '</b>',
        geo_scope='usa',
    )

    return cdc_fig1

@app.callback(
    Output('cdc_graph_2','figure'),
    Output('cdc_graph_3','figure'),
    Output('cdc_graph_4','figure'),
    Output('cdc_graph_5','figure'),
    Output('state_graph1', 'figure'),
    Output('state_graph2', 'figure'),
    Input('state_dropdown', 'value'),
    Input('vaccine_type_dropdown','value')
)

def make_figures(state:str, type:str):
    type_key = '_' + type
    if type == 'All':
        type = ' '
        type_key = ''
    else:
        type = ' ' + type + ' '

    

    filtered_df = cdc_df.copy()
    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    recent_date = pd.to_datetime(cdc_df['date']).max()

    filtered_df = filtered_df[filtered_df['date'] == recent_date]
    filtered_df = filtered_df[filtered_df['location'] != 'US']


    filtered_df['Available'+type_key] = filtered_df['distributed'+type_key] - filtered_df['administered'+type_key]
    filtered_df['Available Percentage'+type_key] = filtered_df['Available'+type_key] / filtered_df['distributed'+type_key] * 100



    # cdc_fig1 = px.choropleth(
    #     filtered_df,
    #     locations = 'location',
    #     hover_name = 'location',
    #     color = 'series_complete_pop_pct',
    #     locationmode = 'USA-states',
    #     color_continuous_scale=px.colors.sequential.BuPu,
    # )

    # cdc_fig1.update_layout(
    #     title_text='<b>Percentage of Population Fully Vaccinated as of ' + recent_date.strftime("%m/%d/%Y") +'</b>',
    #     geo_scope='usa'
    # )

    # cdc_fig1.update_xaxes(
    #     mirror=True,
    #     ticks='outside',
    #     showline=True,
    # )

    # cdc_fig1.update_yaxes(
    #     mirror=True,
    #     ticks='outside',
    #     showline=True,
    # )

    cdc_fig2 = px.choropleth(
        filtered_df,
        locations = 'location',
        hover_name = 'location',
        color = 'distributed' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig2.update_layout(
        title_text='<b>Cumulative Number of' + type + 'Doses distributed as of ' + recent_date.strftime("%m/%d/%Y") +'</b>',
        geo_scope='usa'
    )

    cdc_fig3 = px.choropleth(
        filtered_df,
        locations = 'location',
        hover_name = 'location',
        color = 'administered' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig3.update_layout(
        title_text='<b>Cumulative Number of' + type + 'Doses administered as of ' + recent_date.strftime("%m/%d/%Y") +'</b>',
        geo_scope='usa'
    )

    cdc_fig4 = px.choropleth(
        filtered_df,
        locations = 'location',
        hover_name = 'location',
        color = 'Available' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig4.update_layout(
        title_text='<b>Number of' + type + 'Doses Received But Not administered as of ' + recent_date.strftime("%m/%d/%Y") +'</b>',
        geo_scope='usa'
    )

    cdc_fig5 = px.choropleth(
        filtered_df,
        locations = 'location',
        hover_name = 'location',
        color = 'Available Percentage' + type_key,
        locationmode = 'USA-states',
        color_continuous_scale=px.colors.sequential.YlGnBu,
    )

    cdc_fig5.update_layout(
        title_text= '<b>Percentage of' + type + 'Doses Received But Not administered as of ' + recent_date.strftime("%m/%d/%Y") +'</b>',
        geo_scope='usa'
    )

    

    state_df = cdc_df[cdc_df['location'] == state].copy()

    state_df['date'] = pd.to_datetime(state_df['date'])
    state_df = state_df.sort_values(by = 'date')

    if not state:
        state = " "
    else:
        state = states_dic[state]

    state_fig1 = px.line(
        state_df,
        x = 'date',
        y = 'distributed',
        title = '<b>Cumulative Number of distributed Doses in ' + state +'</b>'
    )

    state_fig1.update_layout(
        template = 'plotly_white',
        yaxis_title = "Number of Doses",
    )

    # state_fig1.update_xaxes(
    #     showline=True, 
    #     linewidth=2, 
    #     linecolor='black', 
    #     mirror=True
    # )

    # state_fig1.update_yaxes(
    #     showline=True, 
    #     linewidth=2, 
    #     linecolor='black', 
    #     mirror=True
    # )

    state_df.loc[:, 'Shifted distributed'] = state_df['distributed'].shift(1)
    state_df.loc[:, 'Non Cumulative distributed'] = state_df['distributed'] - state_df['Shifted distributed']
    state_df.loc[state_df['Non Cumulative distributed'] < 0, 'Non Cumulative distributed'] = 0

    state_fig2 = px.line(
        state_df,
        x = 'date',
        y = 'Non Cumulative distributed',
        title = '<b>Number of Daily/Weekly Doses distributed in ' + state +'</b>'
    )


    state_fig2.update_layout(
        template = 'plotly_white',
        yaxis_title = "Number of Doses",
    )

    separation_date = pd.to_datetime('2022-06-16')

    state_fig2.add_vline(
        x = separation_date,
        line_dash="dash", 
        line_color="red",
    )

    state_fig2.add_vrect(
        x0=state_df['date'].min(), 
        x1=separation_date, 
        annotation_text="Data Aggregated Daily     ", 
        annotation_position="top right",
        fillcolor="green", 
        opacity=0.05, 
        line_width=0
    )

    state_fig2.add_vrect(
        x0=separation_date, 
        x1=state_df['date'].max(), 
        annotation_text="     Data Aggregated Weekly", 
        annotation_position="top left",
        fillcolor="orange", 
        opacity=0.05, 
        line_width=0
    )





    
    
    return cdc_fig2, cdc_fig3, cdc_fig4, cdc_fig5, state_fig1, state_fig2