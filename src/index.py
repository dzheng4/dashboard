from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import page01, official_navigation, Illinois, NewYork, PennMap, Connecticut, Maryland, Minnesota, SourceSelection, IndividualStates, CDC, California, Ohio, model, FOIA, Parquet, LiteratureResources



app.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),
    # dbc.Navbar([
    #     html.Div(
    #         children=[
    #             dbc.Row([
    #                 dbc.Col(
    #                     # dbc.NavbarBrand(
    #                     #     html.P("NCSU COVID-19 Vaccine Data Portal", ),
                            
    #                     #     class_name= 'ms-2', 
    #                     #     style={
    #                     #         'margin-left': 'auto',
    #                     #         'margin-top': '100%',
    #                     #         # 'text-align':'center'
    #                     #     }
    #                     # ), width = 'auto', align='center'
    #                     html.P("NCSU COVID-19 Vaccine Data Portal")
    #                 ),
    #             ], className = 'g-0'),
    #         ],style=dict(justifyContent='auto')
    #     )
    #     ],
    #     className='start',
    #     color = '#CC0000', 
    #     dark = True, 
    #     # style=dict(display='none'),
    #     id='nav'
    # ),
    # dbc.Row([
    #     html.P(),
    #     dbc.Col(
    #         html.P("NCSU COVID-19 Vaccine Data Portal",style={'color':'white','margin-left':'3%'}),
    #         # style={'algin-self':'center'}
    #     ),
    # ],style = {'display':'flex','background-color':'#CC0000','align-self':'center'}),

    

    # content will be rendered in this element
    html.Div(id='page-content', children=[])
])

server = app.server


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return SourceSelection.layout
    if pathname == '/apps/official_navigation':
        return official_navigation.layout
    if pathname == '/apps/IndividualStates':
        return IndividualStates.layout
    if pathname == '/apps/LiteratureResources':
        return LiteratureResources.layout
    if pathname == '/apps/page-01':
        return page01.layout
    if pathname == '/apps/navigation':
        return official_navigation.layout
    if pathname == '/apps/Illinois':
        return Illinois.layout
    if pathname == '/apps/NewYork':
        return NewYork.layout
    if pathname == '/apps/PennMap':
        return PennMap.layout
    if pathname == '/apps/Connecticut':
        return Connecticut.layout
    if pathname ==  '/apps/Maryland':
        return Maryland.layout
    if pathname == '/apps/Minnesota':
        return Minnesota.layout
    if pathname == '/apps/CDC':
        return CDC.layout
    if pathname == '/apps/California':
        return California.layout
    if pathname == '/apps/Ohio':
        return Ohio.layout
    if pathname == '/apps/model':
        return model.layout
    if pathname == '/apps/FOIA':
        return FOIA.layout
    if pathname == '/apps/Parquet':
        return Parquet.layout

    
    
    return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug = True)