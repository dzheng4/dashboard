from dash import dcc, html

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