from matplotlib import pyplot as plt
from matplotlib import rcParams
import matplotlib
import pandas as pd
import numpy as np
import math
#设置好看的字体
from matplotlib.pyplot import tick_params

matplotlib.rcParams['text.usetex'] = True
np.set_printoptions(suppress=True)

config = {
    "font.family":'serif',
    "font.size": 12,
    "mathtext.fontset":'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)

print(matplotlib.matplotlib_fname())
def runplt(size=None):
    plt.figure(figsize=(6,4))
    # plt.title("The Topologist's sine curve")
    # plt.ylabel('$y$',fontsize=15)
    # plt.xlabel('$x$',fontsize=15,loc='right')
    plt.yticks([])
    plt.xticks([])
    plt.axis([-0.05,0.5,0.5,0.7])
    # plt.axis([])
    # tick_params(direction='in')
    tick_params(bottom='off',top ='off',left='off', right='off')
    return plt
runplt()
x = np.arange(0.001,1,0.001)
y = np.sin((np.pi)/x)
plt.plot(x,y,color = 'tab:blue',linewidth=1.0,zorder=2)
plt.text(np.array([0.365]),np.sin((np.pi)/np.array([0.3573])),'$P$')
plt.text(np.array([-0.046]),np.sin((np.pi)/np.array([0.36])),'$\gamma(t_{0})$')
plt.text(0.277,0.702,'$x=a$')
plt.text(-0.02,0.49,'$U\cap Y$')
plt.scatter(np.array([0.357]),np.sin((np.pi)/np.array([0.357])),color='black',zorder=3)
plt.scatter(np.array([0]),np.sin((np.pi)/np.array([0.36])),color='black',zorder=4)
plt.vlines(0,-1,1,color = 'tab:blue',linewidth=1.0,zorder=2)
plt.vlines(0.3,-1,1,color = 'tab:red',linewidth=1.0,zorder=2)

plt.savefig('sin_2.pdf',bbox_inches='tight')
plt.show()