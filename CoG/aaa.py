# -*- coding: utf-8 -*-
import numpy as np
from pycode import reader,plt,process
import matplotlib.pyplot as pypl
import plotly.graph_objects as go
from scipy import interpolate

path = r'C:\Users\tshin\CoG\data\honda\BC00.csv'
df = reader.CsvReader(path)
x,y,t = df["X"],df["Y"],df["S"]
#trace1=go.Scatter(x=t,y=y,marker_color="red")

linerX=interpolate.interp1d(t,x)
trace1=go.Scatter(y=linerX,marker_color="blue")

x = abs(process.Fourier(x))
y = abs(process.Fourier(y))
t = abs(process.Fourier(t))
N = len(df)

freq = np.fft.fftfreq(N, d=0.01)
#df = process.Interpolation(df)
trace1=go.Scatter(y=x.real,marker_color="blue")
trace2=go.Scatter(y=x.imag,marker_color="green")
fig=go.Figure([trace1,trace2])
fig.show()

ip1 = ["最近傍点補間", lambda x, y: interpolate.interp1d(x, y, kind="nearest")]
ip2 = ["線形補間", interpolate.interp1d]
ip3 = ["ラグランジュ補間", interpolate.lagrange]
ip4 = ["重心補間", interpolate.BarycentricInterpolator]
ip5 = ["Krogh補間", interpolate.KroghInterpolator]
ip6 = ["2次スプライン補間", lambda x, y: interpolate.interp1d(x, y, kind="quadratic")]
ip7 = ["3次スプライン補間", lambda x, y: interpolate.interp1d(x, y, kind="cubic")]
ip8 = ["秋間補間", interpolate.Akima1DInterpolator]
ip9 = ["区分的 3 次エルミート補間", interpolate.PchipInterpolator]


def fourierTest(n,dt):
    # データのパラメータ
    N = n            # サンプル数
    dt = dt          # サンプリング間隔
    fq1, fq2 = 5, 40    # 周波数
    fc = 20  # カットオフ周波数
    A1, A2 = 20, 5

    t = np.arange(0, N*dt, dt)  # 時間軸
    freq = np.linspace(0, 1.0/dt, N)  # 周波数軸

    # 時間信号（周波数5の正弦波 + 周波数40の正弦波）の生成
    f1 = A1 * np.sin(2 * np.pi * fq1 * t)
    f2 = A2 * np.sin(2*np.pi*fq2*t)
    f = f1 + f2

    # 高速フーリエ変換（周波数信号に変換）
    F = np.fft.fft(f)

    # 正規化 + 交流成分2倍
    F = F/(N/2)
    F[0] = F[0]/2

    # 配列Fをコピー
    F2 = F.copy()

    # ローパスフィル処理（カットオフ周波数を超える帯域の周波数信号を0にする）
    F2[(freq > fc)] = 0

    # 高速逆フーリエ変換（時間信号に戻す）
    f2 = np.fft.ifft(F2)

    # 振幅を元のスケールに戻す
    f2 = np.real(f2*N)

    return 0
# グラフ表示
fig = pypl.figure(figsize=(10.0, 8.0))
pypl.rcParams['font.family'] = 'Times New Roman'
pypl.rcParams['font.size'] = 12

# 時間信号（元）
pypl.subplot(221)
pypl.plot(t, f, label='f(n)')
pypl.xlabel("Time", fontsize=12)
pypl.ylabel("Signal", fontsize=12)
pypl.grid()
leg = pypl.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 周波数信号(元)
pypl.subplot(222)
pypl.plot(freq, np.abs(F), label='|F(k)|')
pypl.xlabel('Frequency', fontsize=12)
pypl.ylabel('Amplitude', fontsize=12)
pypl.grid()
leg = pypl.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 時間信号(処理後)
pypl.subplot(223)
pypl.plot(t, f2, label='f2(n)')
pypl.xlabel("Time", fontsize=12)
pypl.ylabel("Signal", fontsize=12)
pypl.grid()
leg = pypl.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 周波数信号(処理後)
pypl.subplot(224)
pypl.plot(freq, np.abs(F2), label='|F2(k)|')
pypl.xlabel('Frequency', fontsize=12)
pypl.ylabel('Amplitude', fontsize=12)
pypl.grid()
leg = pypl.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)
pypl.show()