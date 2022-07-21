from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import page01, page02, official_navigation, Illinois


app.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),

    dbc.Navbar([
            html.Div(
                children=[
                    dbc.Row([
                        dbc.Col(
                            dbc.NavbarBrand(
                                "NCSU COVID DATA PORTAL", 
                                class_name= 'ms-2', 
                                style={
                                    'margin-left': 'auto',
                                    'margin-top': '100%',
                                    # 'text-align':'center'
                                }
                            ), width = 'auto', align='center'
                        ),
                    ], className = 'g-0'),
                ],style=dict(justifyContent='auto')
            )
        ],
        className='start',
        color = '#CC0000', 
        dark = True, 
        # style=dict(display='none'),
        id='nav'
        ),

    html.Div([
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(
                "Official Navigation", href="/apps/navigation"
            ),
            dbc.DropdownMenuItem(
                "Penn", href="/apps/page-01"
            ),
            dbc.DropdownMenuItem(
                "Penn2", href="/apps/page-02"
            ),
            dbc.DropdownMenuItem(
                "Illinois", href="/apps/Illinois"
            ),
            dbc.DropdownMenuItem(
                "Michigan", href="https://public.tableau.com/views/Michigan_COVID19_Dashboard/MichiganDashboard?:language=en-US&:display_count=n&:origin=viz_share_link", target="_blank"
            ),
            dbc.DropdownMenuItem(
                "Maine", href="https://public.tableau.com/views/Maine_COVID19_Dashboard/MaineMonthlyAdministrationDashboard?:language=en-US&:display_count=n&:origin=viz_share_link", target="_blank"
            ),
            dbc.DropdownMenuItem(
                "North Carolina", href="https://public.tableau.com/views/NC_Demographics/NorthCarolinaVaccinationStatusSummary?:language=en-US&:display_count=n&:origin=viz_share_link", target="_blank"
            ),
            dbc.DropdownMenuItem(
                "Texas", href="https://public.tableau.com/shared/D4N655QT3?:display_count=n&:origin=viz_share_link", target="_blank"
            ),
            dbc.DropdownMenuItem(
                "Connecticut", href="https://public.tableau.com/views/Connecticut_COVID19_Dashboard/ConnecticutStateLevelWeeklyVaccineAllocation?:language=en-US&:display_count=n&:origin=viz_share_link", target="_blank"
            ),
            dbc.DropdownMenuItem(
                "Delaware", href="https://public.tableau.com/shared/39DFRRWZS?:display_count=n&:origin=viz_share_link", target="_blank"
            ),

        ],label="Menu",),
        html.P(id="item-clicks", className="mt-3"),
    ]),

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
        return official_navigation.layout
    if pathname == '/apps/page-01':
        return page01.layout
    if pathname == '/apps/page-02':
        return page02.layout
    if pathname == '/apps/navigation':
        return official_navigation.layout
    if pathname == '/apps/Illinois':
       return Illinois.layout
    
    
    return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug = True)