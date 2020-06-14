import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#myScript
from pycode import reader,plt,process

style = {'width': '100%','height': '60px','lineHeight': '60px','borderWidth': '1px','borderStyle': 'dashed','borderRadius': '5px','textAlign': 'center','margin': '10px'}
x = plt.xtest()
y = plt.ytest()
t = plt.ztest()
HIST = plt.HISTOGRAM(x,y)
SCATTER = plt.SCATTER(x,y,t)

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.layout = html.Div([
    html.Div(id="HEADER",children=[
        html.H1("HEADER"),
        html.Button(children=[html.Img(src=app.get_asset_url(r"Scatter.png"))]),
        html.Button(children=[html.Img(src=app.get_asset_url(r"Scatter3d.png"))]),
        html.Button(children=[html.Img(src=app.get_asset_url(r"Histogram.png"))]),
        html.Hr()
    ]),
    #color,showscale,colorscale,showlegend,row,col
    html.Div(id="BODY",style={},children=[
        html.Div(id="left-pannel",style={"width":"25%","float":"left"},children=[
            dcc.Tabs(
                id="tabs-with-classes",
                value='tab-1',
                parent_className='custom-tabs',
                className='custom-tabs-container',
                children=[
                    dcc.Tab(
                        children=[
                            #path,name
                            html.Div(style={"display":"inline"},children=[
                                dcc.Input(id="name",type="search",placeholder="DataName"),
                                dcc.Upload(id="path",children=[html.Button(children='Upload File')])
                            ]),
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
                            html.Div("figtype"),dcc.RadioItems(id="figtype",options=[{'label': 'Histogram', 'value': 'hist'},{'label': 'Hist2d', 'value': 'hist2d'},{'label': 'Line', 'value': 'line'}],value='hist',labelStyle={'display': 'inline-block'}),
                            html.Hr()
                        ],
                        label='Tab one',
                        value='tab-1',
                        className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),
                    dcc.Tab(
                        children=[
                            html.Hr(),
                            dcc.Graph(id="graph"),
                            html.Hr()
                        ],
                        label='Tab two',
                        value='tab-2',
                        className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),
                    dcc.Tab(
                        label='Tab three, multiline',
                        value='tab-3', className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),
                    dcc.Tab(
                        label='Tab four',
                        value='tab-4',
                        className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),
                ],
            ),
        ]),
        html.Div(id="right-pannel",children=[
            dcc.Tabs(
                id="graph-tabs-with-classes",
                value='graph-tab-1',
                parent_className='graph-tabs',
                className='graph-tabs-container',
                children=[
                    dcc.Tab(
                        label="Histogram",
                        value='graph-tab-1',
                        className='graph-tab',
                        selected_className='graph-tab--selected',
                        children=[dcc.Graph(figure = HIST)]
                    ),
                    dcc.Tab(
                        label="Scatter",
                        value='graph-tab-2',
                        className='graph-tab',
                        selected_className='graph-tab--selected',
                        children=[dcc.Graph(figure = SCATTER)]
                    ),
            ]),
            html.Hr()
        ]),
    ]),
    html.Div(id="FOOTER",style={"clear":"left"},children=[
        html.Hr(),
        html.H1("FOOTER"),
        html.Hr()
    ])
])

@app.callback(Output("color","children"),[Input("red","value"),Input("blue","value"),Input("green","value")])
def RGB(r,g,b):
    return "rgb({},{},{})".format(r,g,b)

@app.callback(
    Output("graph","figure"),
    [
        Input("path","contents"),
        Input("name","value"),
        Input("color","children"),
        Input("colorscale","value"),
        Input("showscale","value"),
        Input("showlegend","value"),
        Input("row","value"),
        Input("col","value"),
        Input("style","value"),
        Input("figtype","value")
    ]
)
def Figure(contents,name,color,colorscale,showscale,showlegend,row,col,style,figtype):
    if showscale == "True":showscale = True
    else:showlegend = False
    if showlegend == "True":showscale = True
    else:showlegend = False
    df = reader.ContentsReader(contents)
    x,y = df["X"],df["Y"]
    basefig = plt.Subplt(row,col,style)
    figure = plt.MakeFigure(basefig=basefig,x=x,y=y,name=name,color=color,colorscale=colorscale,showscale=showscale,showlegend=showlegend,row=row,col=col,figtype=figtype)
    figure = plt.Layout(figure)
    return figure

if __name__ == '__main__':
    app.run_server(debug=False)