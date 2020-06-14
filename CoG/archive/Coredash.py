import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1("Centre of Gravity",id="Title"),
    html.Nav(children=[
        html.H2("Layout Style",id="Layout-Style"),
        html.Br(id="Br"),
        html.Button("Add File",id = "add-file",n_clicks = 0),
        dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'},
                # Allow multiple files to be uploaded
                multiple=False
            ), 
        #Add File Box
        dcc.Upload(
                id='upload-data-output',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'},
                # Allow multiple files to be uploaded
                multiple=False
            )
    ]),
    html.Div(children=[
        dcc.Graph(id="Graph")
    ])
])
@app.callback(
    Output('upload-data', 'children'),
    [Input('add-file', 'n_clicks')],
    [State('upload-data', 'children')])
def UploadPath(n_clicks, children):
    new_element = html.Div([
        dcc.Upload(
            id={
                'type': 'dynamic-upload',
                'index': n_clicks
            },
            options=[{'label': i, 'value': i} for i in ['NYC', 'MTL', 'LA', 'TOKYO']]
        ),
        html.Div(
            id={
                'type': 'dynamic-output',
                'index': n_clicks
            }
        )
    ])
    children.append(new_element)
    return children


@app.callback(
    Output({'type': 'dynamic-output', 'index': }, 'children'),
    [Input({'type': 'dynamic-dropdown', 'index': }, 'value')],
    [State({'type': 'dynamic-dropdown', 'index': }, 'id')],
)
def display_output(value, id):
    return html.Div('Path {} = {}'.format(id['index'], value))
