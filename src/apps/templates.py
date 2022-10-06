from dash import dcc, html
import dash_bootstrap_components as dbc

def createTable(pagename, component):
    content = html.Table(
        [
            html.Tr(
                html.Th(id = pagename + component + "label")
            ),
            html.Tr(
                html.Td(id = pagename + component)
            )
        ]
    )
    return content


def createMenu():
    content = html.Div([
            dbc.DropdownMenu([
                dbc.DropdownMenuItem(
                    "Penn", href="/apps/page-01"
                ),
                dbc.DropdownMenuItem(
                    "Penn Map", href="/apps/PennMap"
                ),
                dbc.DropdownMenuItem(
                    "Illinois", href="/apps/Illinois"
                ),
                dbc.DropdownMenuItem(
                    "New York", href="/apps/NewYork"
                ),
                dbc.DropdownMenuItem(
                    "Connecticut", href="/apps/Connecticut"
                ),
                dbc.DropdownMenuItem(
                    "Maryland", href="/apps/Maryland"
                ),
                dbc.DropdownMenuItem(
                    "Minnesota", href="/apps/Minnesota"
                ),
                dbc.DropdownMenuItem(
                    "California", href="/apps/California"
                ),
                dbc.DropdownMenuItem(
                    "Ohio", href="/apps/Ohio"
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
                    "Texas", href="https://public.tableau.com/shared/6W2NYPWFN?:display_count=n&:origin=viz_share_link", target="_blank"
                ),
                dbc.DropdownMenuItem(
                    "Delaware", href="https://public.tableau.com/shared/39DFRRWZS?:display_count=n&:origin=viz_share_link", target="_blank"
                ),

            ],label="Menu",),
            html.P(id="item-clicks", className="mt-3"),
    ])
    return content


def backHome():
    content = dbc.Col([
        dbc.Button(
            'Back to Home Page',
            href='/'
        )
    ], align = 'center', className='backbutton')

    return content


def contact_footer():
    content = dbc.Row(
        dbc.Col([
            html.Footer(
                "ATLAS @ North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Dr. Leila Hajibabai, Dr. Ali Hajbabaie, Asya Atik, Kuangying Li, Dayang Zheng",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Department of Industrial & Systems Engineering, North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            ),
            html.Footer(
                "Department of Civil, Construction and Environmental Engineering, North Carolina State University",
                style = {
                    'font-size' : '10px'
                }
            )
        ], align = 'center', className = 'footerbottom')
    )

    return content