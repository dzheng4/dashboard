from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import page01, page02, summary, Illinois


app.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),
    html.Div([
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(
                "Penn", href="/apps/page-01"
            ),
            dbc.DropdownMenuItem(
                "Penn2", href="/apps/page-02"
            ),
            dbc.DropdownMenuItem(
                "summary", href="/apps/summary"
            ),
            dbc.DropdownMenuItem(
                "North Carolina", href="/apps/North_Carolina"
            ),
            dbc.DropdownMenuItem(
                "New York", href="/apps/summary/New_York"
            ),
            dbc.DropdownMenuItem(
                "California", href="/apps/summary/California"
            ),
            dbc.DropdownMenuItem(
                "Illinois", href="/apps/Illinois"
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
    if pathname == '/apps/page-01':
        return page01.layout
    if pathname == '/apps/page-02':
        return page02.layout
    if pathname == '/apps/summary':
        return summary.layout
    if pathname == '/apps/Illinois':
       return Illinois.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug = True)