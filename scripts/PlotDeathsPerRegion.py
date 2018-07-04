import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from scipy.misc import imread
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.colors as colors
import pylab as pl
import time
warnings.filterwarnings('ignore')

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/lol-data-analysis/Plots/Death Heatmaps/'

def plotDeathsHeatmap(team, part, region):
    input_csv = PATH + 'sheets/' + team + part + region + 'Kills.csv'
    output_img = PATH + team + part + region + 'KillsHeatMap_ABCDE.png'

    mapImage = imread(PATH + 'rift.jpg')
    plotDeathsTable = pd.read_csv(input_csv)
    height, width, nbands = mapImage.shape
    print("Input data: " + input_csv)
    print("Input BG: " + PATH + 'rift.jpg')
    dpi = 80
    figsize = width / float(dpi), height / float(dpi)

    
    print(" Handling axes...")
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    plt.xlim(0,width)
    plt.ylim(0,height)
    
    print(" Creating new image...")
    ax.imshow(mapImage, zorder=0, extent=[0.0, width, 0.0, height])

    print(" Preparing colors...")
    cmap = pl.cm.Purples if str(team) == 'Red' else pl.cm.Blues
    my_cmap = cmap(np.arange(cmap.N))
    my_cmap[:,-1] = np.linspace(0, 1, cmap.N)
    my_cmap = colors.ListedColormap(my_cmap)

    print(" Finishing new image...")
    sns.kdeplot(plotDeathsTable['x'], plotDeathsTable['y'], cmap=my_cmap, shade=True, shade_lowest=False, ax=ax)
    ax.axis('off')
    fig.savefig(output_img, dpi=dpi, transparent=False)
    print("New image is at " + output_img + '\n')

parts = ['Late']
regions = ['CBLoL', 'LCK']
for part in parts:
    for region in regions:
        plotDeathsHeatmap('Blue', part, region)
        plotDeathsHeatmap('Red', part, region)