
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
from asset import plt

import plotly.graph_objs as go

style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center',
        'margin': '10px'
}

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = html.Div(children=[
        html.H2("Centre of Gravity",id="Page-Name"),
        html.Nav(style={"display":"inline"},children=[
                html.Div(children=[
                ]),
                html.Button('Add Path', id='add-path', n_clicks=0),
                html.Nav(id="upload-data",children=[
                        dcc.Upload(
                                id='upload-data-input',
                                children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                ]),
                                style=style,
                                # Allow multiple files to be uploaded
                                multiple=False
                        ),
                        html.Div(id='upload-data-input-text')
                ]),
                html.Nav(children=[
                        dcc.RadioItems(
                                id="Layout-Style-Radioitems",
                                options=[
                                        {'label': 'Histgram', 'value': 'hist'},
                                        {'label': 'Hist & Line', 'value': 'hist-line'},
                                        {'label': 'Line', 'value': 'line'}
                                ],
                                value='hist',
                                labelStyle={'display': 'inline-block'},
                                style=style
                        ),
                        html.Div(id="Layout-Style-Text"),
                        html.Br(),
                        dcc.Upload(
                                id='upload-data-output',
                                children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                ]),
                                style=style,
                                # Allow multiple files to be uploaded
                                multiple=False
                        ),
                        html.Div(id="upload-data-output-text"),
                        html.Br()
                ]),
                html.Div(id="Graph-Area",children=[
                        dcc.Graph(id="Graph",figure=go.Figure())
                ])
        ])
])
#Layout-Style-Text
@app.callback(Output("Layout-Style-Text","children"),[Input("Layout-Style-Radioitems","value")])
def LayoutStyleText(radiovalue):
        text = radiovalue
        return "clicked {}".format(text)

#upload-data-output-text
@app.callback(Output("upload-data-output-text","children"),[Input('upload-data-output',"contents")])
def UploadDataOutputText(filename):
        return "{}".format(filename)

"""@app.callback(Output("Graph","figure"),[Input()])
def FigureOutPut(x,y,name,color,colorscale,showscale,showlegend,row,col,style,figtype):
        basefig = plt.Subplt(row,col,style)
        figure = plt.MakeFigure(basefig,x,y,name,color,colorscale,showscale,showlegend,row,col,style,figtype)
        return figure
"""

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)