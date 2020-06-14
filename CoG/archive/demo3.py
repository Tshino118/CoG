from asset import reader,plt,process

x=[i for i in range(0,100)]
y=[i*i for i in range(0,100)]
basefig = plt.Subplt()
fig = plt.MakeFigure(basefig=basefig,x=x,y=y)
fig.show()