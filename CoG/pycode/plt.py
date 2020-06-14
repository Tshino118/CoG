import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import numpy as np


def xtest():
    t = np.linspace(-1, 1.2, 2000)
    x = (t**3) + (0.3 * np.random.randn(2000))
    return x
def ytest():
    t = np.linspace(-1, 1.2, 2000)
    y = (t**6) + (0.3 * np.random.randn(2000))
    return y
def ztest():
    z = [_ for _ in range(2000)]
    return z

def SCATTER(x,y,t):
    basefig = Subplt(2,2,"scat",specs=[[{"type": "xy"}, {"type": "scene"}],[{"type": "xy"}, {"type": "xy"}]])
    fig = Scatter(basefig,x,y,row=2,col=1)
    fig = Line(basefig,x=x,y=t,color="red",row=1,col=1)
    fig = Line(basefig,x=t,y=y,color="blue",row=2,col=2)
    fig = Line3d(basefig,x=x,y=y,t=t,row=1,col=2)
    fig = Layout(basefig)
    fig.update_xaxes(range=[-50, 40], zerolinecolor="red", row=1, col=1)
    fig.update_yaxes(range=[0, 60], zerolinecolor="blue", row=1, col=1)
    fig.update_xaxes(range=[-50, 40], zerolinecolor="red", row=2, col=1)
    fig.update_yaxes(range=[-70, 20], zerolinecolor="blue", row=2, col=1)
    fig.update_xaxes(range=[0, 60], zerolinecolor="red", row=2, col=2)
    fig.update_yaxes(range=[-70, 20], zerolinecolor="blue", row=2, col=2)
    return fig

def HISTOGRAM(x,y):
    basefig = Subplt(2,2,"hist",specs=[[{"type": "xy"}, {"type": "scene"}],[{"type": "xy"}, {"type": "xy"}]])
    fig = Hist2d(basefig,x,y,row=2,col=1)
    fig = Hist(basefig,x=x,color="red",row=1,col=1)
    fig = Hist(basefig,y=y,color="blue",row=2,col=2)
    fig = Layout(basefig)
    fig.update_xaxes(range=[-50, 40], zerolinecolor="black", row=1, col=1)
    #fig.update_yaxes(range=[0, 60], row=1, col=1)
    fig.update_xaxes(range=[-50, 40], zerolinecolor="black", row=2, col=1)
    fig.update_yaxes(range=[-70, 20], zerolinecolor="black", row=2, col=1)
    #fig.update_xaxes(range=[0, 60], row=2, col=2)
    fig.update_yaxes(range=[-70, 20], zerolinecolor="black", row=2, col=2)
    return fig

def MakeFigure(basefig,x=None,y=None,name='Line',color='red',colorscale=False,showscale=False,showlegend=False,row=1,col=1,figtype="Line"):
    if figtype == "line":
        return Line(basefig,x,y,name,color,showlegend,row,col)
        
    elif figtype == "hist":
        return Hist(basefig,x,y,name,color,showlegend,row,col)

    elif figtype == "hist2d":
        return Hist2d(basefig,x,y,name,colorscale,showscale,row,col)

    elif figtype == "viol":
        return Viol(basefig,x,y,name,color,showlegend,row,col)


def Subplt(rows,cols,style,specs):
    styles={
        'nomal':[[_ for _ in range(rows)],[_ for _ in range(cols)]],
        'hist' :[[(i%2+1) for i in range(rows)],[((i+1)%2+1) for i in range(cols)]],
        'scat' :[[((i+1)%2+1) for i in range(rows)],[(i%2+1) for i in range(cols)]],
        '3d'   :[[_ for _ in range(rows)],[((i+1)%2+1) for i in range(cols)]],
    }
    if style in styles:
        heights=styles[style][0]
        widths =styles[style][1]

    basefig = make_subplots(
        rows=rows,cols=cols,
        row_heights=heights,
        column_widths=widths,
        specs=specs
    )
    return basefig

#Layout
def Layout(basefig):
    layout = basefig.update_layout(
        plot_bgcolor = 'lightyellow',
        barmode='overlay',
        width=800,
        height=800,
        legend=go.layout.Legend(
            x=1,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color="black"
            ),
            bgcolor="ghostwhite",
            bordercolor="Black",
            borderwidth=2
        ),
        margin=go.layout.Margin(
            l=0, #left margin
            r=0, #right margin
            b=0, #bottom margin
            t=0, #top margin
        )
    )
    return layout

#Scatter
#Scatter
def Scatter(basefig,x=None,y=None,name='Scatter',color='black',showlegend=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            name=name,
            mode='markers',
            marker=dict(
                size=2,
                color=color,
                line_width=1
            ),
            opacity=0.75,
            showlegend=showlegend,
            ),
        row=row,col=col
    )
    return fig

def Line(basefig,x=None,y=None,name='Line',color='red',showlegend=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            name=name,
            line_color=color,
            opacity=0.75,
            showlegend=showlegend,
            ),
        row=row,col=col
    )
    return fig

def Line3d(basefig,x=None,y=None,t=None,name='Line',color='red',showlegend=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Scatter3d(
            x=x,
            y=y,
            z=t,
            name=name,
            mode='lines',
            marker=dict(
                size=4,
                color="red",
                opacity=0.75
            ),
            line=dict(
                color='darkblue',
                width=2
            ),
            showlegend=showlegend,
            ),
        row=row,col=col
    )
    return fig
#Histograms
def Hist(basefig,x=None,y=None,name='hist',color='red',showlegend=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Histogram(
            x=x,
            y=y,
            name=name,
            marker_color=color,
            opacity=0.75,
            showlegend=showlegend,
            ),
        row=row,col=col
    )
    return fig

def Hist2d(basefig,x=None,y=None,name='HeatMap',colorscale='inferno',showscale=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Histogram2dContour(
            x=x,
            y=y,
            name=name,
            colorscale=colorscale,
            showscale=showscale,
            reversescale=True
            ),
        row=row,col=col,
    )
    return fig

#Violin
def Viol(basefig,x=None,y=None,name='viol',color='red',showlegend=False,row=1,col=1):
    fig = basefig.add_trace(
        go.Violin(
            x=x,
            y=y,
            name=name,
            marker_color=color,
            opacity=0.75,
            showlegend=showlegend,
            ),
        row=row,col=col,
    )
    return fig
