import os
import base64
import io
import pandas as pd
import numpy as np
import wave

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 07:40:48 2020

@author: tshin
"""

def ContentsReader(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')),usecols=['time',' COPx',' COPy']).dropna().astype('f8')
    df = df.rename(columns={'time': 'S',' COPx': 'X',' COPy': 'Y'})
    return df

def CsvReader(path):
    base,ext = os.path.splitext(path)
    data = FileReader(base, ext)
    return data

def MakePickle(data,base):
    #to pickle
    pkl = data.to_pickle(r'{}.pkl'.format(base))
    return pkl
    
#Data Reader
def FileReader(base, ext):
    if ext == '.csv':
        #pickleFile Exist #read pickle
        if os.path.isfile(r'{}.pkl'.format(base)) == True:
            data = pd.read_pickle(r'{}.pkl'.format(base))
            return data
        #read csvFile
        else:
            data = pd.read_csv(r'{}.csv'.format(base),
                               usecols=['time',' COPx',' COPy']).dropna().astype('f8')#read .csv
            data = data.rename(columns={'time': 'S',' COPx': 'X',' COPy': 'Y'})
            return data
    else:
        data = print('Unknown extension.')

def Wave(contents):

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    wr = wave.open(io.StringIO(decoded.decode('utf-8')), mode="rb")

    # waveファイルが持つ性質を取得
    channel = wr.getnchannels()
    samplt_width = wr.getsampwidth()
    frame_rate = wr.getframerate()
    frame_num = wr.getnframes()
    params = wr.getparams()
    total_time = (1.0 * frame_num / frame_rate)

    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = np.frombuffer(data, dtype=np.int16)
    S = np.linspace(0,len(X),len(X))
    df = pd.DataFrame({"S":S,"X":X})
    return df

    return data
