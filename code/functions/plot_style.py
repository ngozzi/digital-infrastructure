import matplotlib.pyplot as plt 
import matplotlib.font_manager as font_manager

def plot_style(font_path='./fonts/Encode_Sans_Condensed/'):

    colors = ['#6CC2BD', '#5A809E', '#7C79A2','#F57D7C', '#FFC1A6', '#FFC1A6']

    plt.rcParams['axes.linewidth'] = 0.7
    plt.rcParams['axes.edgecolor'] = 'grey'
    plt.rcParams['xtick.major.width'] = 0.3
    plt.rcParams['ytick.major.width'] = 0.3
    plt.rcParams['xtick.major.size'] = 3
    plt.rcParams['ytick.major.size'] = 3
    plt.rcParams['xtick.minor.width'] = 0.2
    plt.rcParams['ytick.minor.width'] = 0.2
    plt.rcParams['xtick.minor.size'] = 1.5
    plt.rcParams['ytick.minor.size'] = 1.5

    font_dirs = [font_path]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    font_list = font_manager.createFontList(font_files)
    font_manager.fontManager.ttflist.extend(font_list)
    plt.rcParams['font.family'] = 'Encode Sans Condensed'
    
    return colors