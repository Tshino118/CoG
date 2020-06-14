import os
import base64
import io
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#myScript
from asset import reader,plt,process

style={'width': '100%','height': '60px','lineHeight': '60px','borderWidth': '1px','borderStyle': 'dashed','borderRadius': '5px','textAlign': 'center','margin': '10px'}

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Hr(),
    #color,showscale,colorscale,showlegend,row,col
    html.Div(style={"display":"inline-block"},children=[
        html.Div("Row"),dcc.Input(id="row",type="number",placeholder="Row",min=1,max=100),
        html.Div("Column"),dcc.Input(id="col",type="number",placeholder="Row",min=1,max=4),
        html.Hr(),
        html.Div("Style"),dcc.RadioItems(id="style",options=[{'label': 'Nomal', 'value': "nomal"},{'label': '3D', 'value': "3d"}],value="nomal",labelStyle={'display': 'inline-block'}),
        html.Hr(),
        html.Div("Red"),dcc.Input(id="red",type="number",placeholder="Red",min=0,max=255),
        html.Div("Green"),dcc.Input(id="green",type="number",placeholder="Green",min=0,max=255),
        html.Div("Blue"),dcc.Input(id="blue",type="number",placeholder="Blue",min=0,max=255),
        html.Div(id="color",hidden=True),
        html.Hr(),
        html.Div("Show ColorScale"),dcc.RadioItems(id="showscale",options=[{'label': 'Show', 'value': "True"},{'label': 'Hide', 'value': "False"}],value="True",labelStyle={'display': 'inline-block'}),
        html.Div("ColorScale"),dcc.RadioItems(id="colorscale",options=[{'label': 'inferno', 'value': 'inferno'},{'label': 'Blues', 'value': 'Blues'},{'label': 'Jet', 'value': 'Jet'}],value='inferno',labelStyle={'display': 'inline-block'}),
        html.Hr(),
        html.Div("ShowLegend"),dcc.RadioItems(id="showlegend",options=[{'label': 'Show', 'value': "True"},{'label': 'Hide', 'value': "False"}],value="True",labelStyle={'display': 'inline-block'}),
        html.Hr(),
        html.Div("figtype"),dcc.RadioItems(id="figtype",options=[{'label': 'Histogram', 'value': 'hist'},{'label': 'Hist2d', 'value': 'hist2d'},{'label': 'Line', 'value': 'line'}],value='hist',labelStyle={'display': 'inline-block'})
    ]),
    html.Hr(),
    dcc.Graph(id="graph"),
    html.Hr(),
    #path,name
    html.Div(style={"display":"inline"},children=[
        dcc.Input(id="name",type="search",placeholder="DataName"),
        dcc.Upload(id="path",children=[html.Button(children='Upload File')])
    ]),
    html.Hr()
])
@app.callback(Output("color","children"),[Input("red","value"),Input("blue","value"),Input("green","value")])
def RGB(r,g,b):
    return "rgb({},{},{})".format(r,g,b)

@app.callback(
    Output("graph","figure"),
    [
        Input("path","contents"),
        Input("name","value"),
        Input("colorscale","value"),
        Input("showscale","value"),
        Input("showlegend","value"),
        Input("row","value"),
        Input("col","value"),
        Input("style","value"),
        Input("figtype","value")
    ]
)
def Figure(contents,name,colorscale,showscale,showlegend,row,col,style,figtype):
    if showscale == "True":showscale = True
    else:showlegend = False
    if showlegend == "True":showscale = True
    else:showlegend = False
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')),usecols=['time',' COPx',' COPy']).dropna().astype('f8')
    df = df.rename(columns={'time': 'S',' COPx': 'X',' COPy': 'Y'})
    x,y = df["X"],df["Y"]
    basefig = plt.Subplt(row,col,style)
    color="red"
    figure = plt.MakeFigure(basefig=basefig,x=x,y=y,name=name,color=color,colorscale=colorscale,showscale=showscale,showlegend=showlegend,row=row,col=col,figtype=figtype)
    figure = plt.Layout(figure)
    return figure

if __name__ == '__main__':
    app.run_server(debug=False)