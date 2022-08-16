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
    plt.ylabel('$y$',fontsize=15)
    plt.xlabel('$x$',fontsize=15,loc='right')
    plt.axis([0,1.05,-1.11,1.11])
    # plt.axis([])
    # tick_params(direction='in')
    # tick_params( left='on', right='on')
    return plt
runplt()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
x = np.arange(0.001,1,0.001)
y = np.sin((np.pi)/x)
plt.plot(x,y,color = 'tab:blue',linewidth=1.0,zorder=2)
plt.vlines(0,-1,1,color = 'tab:blue',linewidth=1.0,zorder=2)
plt.text(np.array([0.43]),np.sin((np.pi)/np.array([0.41])),'$Z$')

plt.savefig('sin_1.pdf',bbox_inches='tight')
plt.show()