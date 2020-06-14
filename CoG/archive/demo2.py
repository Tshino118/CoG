import os
import base64
import io
from asset import reader,plt,process
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.Div(style={"display":"inline"},children=[
        dcc.Input(id="name",type="search",placeholder="DataName"),
        dcc.Upload(id="path",children=[html.Button(children='Upload File')])
    ]),
    html.Div(id="test",children=[]),
    dcc.Graph(id="up-figure")
])

@app.callback(Output("test","children"),[Input("path","contents")])
def call(path):
    content_type, content_string = path.split(',')
    decoded = base64.b64decode(content_string)
    filepath=io.StringIO(decoded.decode('utf-8'))
    return "{}\n{}\n{}".format(path,content_string,filepath)
@app.callback(Output("up-figure","figure"),[Input("path","contents")])
def FigureUpdate(pathcontents):
    content_type, content_string = pathcontents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')),usecols=['time',' COPx',' COPy']).dropna().astype('f8')
    df = df.rename(columns={'time': 'S',' COPx': 'X',' COPy': 'Y'})
    x,y = df["X"],df["Y"]
    basefig = plt.Subplt()
    figure = plt.Line(basefig=basefig,x=x,y=y)
    figure = plt.Layout(figure)
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)