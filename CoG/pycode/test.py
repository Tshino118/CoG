

def Pngprint(fig,path):
    fig.write_image(path)

def T_Sig2amp(time,sig_x,sig_y,Sigcolor_X,Sigcolor_Y,SigRan_X,SigRan_Y,outputpath):
    
    sig_x -= np.mean(sig_x)
    sig_y -= np.mean(sig_y)
    
    dt=0.001
    freq,amp_x,F_x = process.Sig2amp(time,sig_x,dt)
    freq,amp_y,F_y = process.Sig2amp(time,sig_y,dt)
    a,b=time[0],time[-1]

    Pngprint((Figu(time,sig_x,Sigcolor_X,yran=SigRan_X,title="Sample Signal_X {} to {}".format(a,b))),outputpath+r"\Signal_X {} to {}.png".format(a,b))
    
    Pngprint((F_Fig(F_Hist(x=amp_x,color=Ampcolor_X)),(F_layout(yran=AmpRan_X,title="Sample Amplitude_X {} to {}".format(a,b)))),outputpath+r"\Amplitude_X .png".format(a,b))
    
    Pngprint((Figu(time,sig_y,Sigcolor_Y,yran=SigRan_Y,title="Sample Signal_Y {} to {}".format(a,b))),outputpath+r"\Signal_Y {} to {}.png".format(a,b))

    Pngprint((F_Fig(F_Hist(x=amp_y,color=Ampcolor_Y)),(F_layout(yran=AmpRan_Y,title="Sample Amplitude_Y {} to {}".format(a,b)))),outputpath+r"\Amplitude_Y {} to {}.png".format(a,b))
    
    Pngprint((Figu2(sig_x,sig_y,xran=SigRan_X,yran=SigRan_Y,title="Sample HeatMap {} to {}".format(a,b))),outputpath+r"\HeatMap {} to {}.png".format(a,b))

    #Inv
    i_sig_x=process.Amp2sig(F_x)
    i_sig_y=process.Amp2sig(F_y)

    Pngprint((F_Fig(F_Line(t=time,x=i_sig_x,color=Sigcolor_Y)),(F_Layout(yran=SigRan_X,title="invSignal of X {} to {}".format(a,b)))),outputpath+r"\invSignal_X {} to {}.png".format(a,b))
    Pngprint((F_Fig(F_Line(t=time,x=i_sig_y,color=Sigcolor_Y)),(F_Layout(yran=SigRan_Y,title="invSignal of Y {} to {}".format(a,b)))),outputpath+r"\invSignal_Y {} to {}.png".format(a,b))

    return 0
