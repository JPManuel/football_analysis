#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:28:27 2020

@author: Jonathan Manuel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.projections import get_projection_class
from matplotlib.patches import Rectangle
import matplotlib as mpl
from PIL import Image
import sys, os
sys.path.append(os.path.abspath("modules"))

import importing_sb as imsb
import draw_pitch as dp


def change_range(value, old_range, new_range):
    return ((value - old_range[0])/(old_range[1]-old_range[0])) * (new_range[1]-new_range[0]) + new_range[0]


# Define a function which creates an inset axes, i.e. the radar for a player
def plot_inset(width, axis_main, data, x, y, ymax=0.3, alpha=0.6, c_map='viridis', zero_loc='E'):
    if len(data) == 0:
        return
        
    ax_sub = inset_axes(axis_main, width=width, height=width, loc='center',
                       bbox_to_anchor=(x, y),bbox_transform=axis_main.transData,
                       borderpad=0.0, axes_class=get_projection_class("polar"))

    theta = data["angle_mid"]
    radii = data["pass_frac"]
    p_length = data['pass.length']
    bars = ax_sub.bar(theta, radii, width=0.5, bottom=0.0)

    ax_sub.set_ylim(0,ymax)
    ax_sub.set_xticklabels([])
    ax_sub.set_yticklabels([])
    ax_sub.set_yticks([0.1,0.2,0.3])
    ax_sub.tick_params(which='major',grid_color='0.9',grid_alpha=alpha)
    #ax_sub.yaxis.set_minor_locator(AutoMinorLocator(2))
    #ax_sub.tick_params(which='minor',grid_color='0.8',grid_linestyle='--')
    ax_sub.yaxis.grid(True, which='major')
    ax_sub.xaxis.grid(False)
    ax_sub.spines['polar'].set_visible(True)
    ax_sub.set_theta_direction('clockwise')
    ax_sub.set_theta_zero_location(zero_loc)
    ax_sub.set_facecolor('0.6')
    ax_sub.patch.set_alpha(alpha)  # Sets the axis backgrounds alpha
    
    # Colour the bars according to average pass length
    cmap = plt.cm.get_cmap(c_map)
    norm = plt.Normalize(vmin=0,vmax=30)
    for p, bar in zip(p_length, bars):
        bar.set_facecolor(cmap(norm(p)))
        bar.set_alpha(alpha)
    
    return ax_sub


def pass_sonar(df, bin_num=12, vmax=None, facecol='w', bar_len_var='fraction', bar_cmap_var='length', bar_cmap='Blues', bar_width='default', theta_zero_loc='N', radial_ticks='default', grid_col='0.3', ygrid=True, xgrid=False, figsize=(5,5), alpha=0.8):
    """
    A generic function for plotting a single pass sonar for a provided DataFrame.
    
    Parameters
    ----------
    df : A DataFrame which contains the columns 'angle', 'length' and 'outcome'. The 'outcome' column should have values '1' corresponding to complete passes and '0' otherwise.
    bin_num : The number of angular bins to split the passes into. The default is 12.
    vmax : The maxmimum value for the bar colourmap. The default is None, in which case the maximum of the bar_cmap_var column is used.
    facecol : Set the facecolour of the axis. The default is 'w'.
    bar_len_var : The variable off which the length of the bars is based. Can take the values 'fraction', 'length' or 'success'. The default is 'fraction'.
    bar_cmap_var : The variable off which the colour of the bars is based. Can take the values 'fraction', 'length' or 'success'. The default is 'length'.
    bar_cmap : The colourmap used for the bars. The default is 'Blues'.
    bar_width : The bar width. The default is "default, which is 2*pi/bin_num.
    theta_zero_loc : The zero-location for the theta. The default is 'N'.
    radial_ticks : What ticks to show on the radar. The default is "default", which shows three equally spaced ticks up to, and including, the maximum.
    grid_col : Colour of the grid. The default is '0.3'.
    ygrid : Whether to display the y-axis grid. The default is True.
    xgrid : Whether to display the x-axis grid. The default is False.
    figsize : Size of the figure. The default is (5,5).
    alpha : Alpha for the whole figure. The default is 0.8.

    Returns
    -------
    fig : Returns the figure.
    ax : Returns the axis for further use.

    """
    
    
    angle_bins = np.linspace(-np.pi, np.pi+0.001, bin_num)
    df['angle_mid'] = pd.cut(df['angle'], angle_bins, include_lowest=True).apply(lambda x: x.mid)
    
    df_grouped = df.groupby('angle_mid',as_index=False)['length'].mean().dropna()
    #df_grouped['fraction'] = (df.groupby('angle_mid').size()/len(df)).values
    df_grouped = df_grouped.join((df.groupby('angle_mid').size()/len(df)).rename('fraction'), on='angle_mid', how='left')
    df_grouped['success'] = (df.groupby('angle_mid')['outcome'].sum()/df.groupby('angle_mid').size()).dropna().values
    
    # Plotting
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='polar')
    
    theta = df_grouped['angle_mid']
    if bar_len_var is "fraction":
        radii = df_grouped['fraction']
        if radial_ticks is "default":
            radial_ticks = np.linspace(0,df_grouped['fraction'].max(),4)[1:]
    elif bar_len_var is "length":
        radii = df_grouped['length']
        if radial_ticks is "default":
            radial_ticks = np.linspace(0,df_grouped['length'].max(),4)[1:]
    elif bar_len_var is "success":
        radii = df_grouped['success']
        if radial_ticks is "default":
            radial_ticks = np.linspace(0,df_grouped['success'].max(),4)[1:]
    else:
        raise ValueError("Only 'fraction', 'length' and 'success' are valid values for bar_len_var.")
        
    if bar_cmap_var is "fraction":
        col = df_grouped['fraction']
        if vmax is None:
            vmax = df_grouped['fraction'].max()
    elif bar_cmap_var is "length":
        col = df_grouped['length']
        if vmax is None:
            vmax = df_grouped['length'].max()
    elif bar_cmap_var is "success":
        col = df_grouped['success']
        if vmax is None:
            vmax = df_grouped['success'].max()
    else:
        raise ValueError("Only 'fraction', 'length' and 'success' are valid values for bar_cmap_var.")
    
    if bar_width is "default":
        bar_width = (2*np.pi)/bin_num
    
    bars = ax.bar(theta, radii, width=bar_width)

    cmap = plt.cm.get_cmap(bar_cmap)
    norm = plt.Normalize(vmin=0,vmax=vmax)
    for c, bar in zip(col, bars):
        bar.set_facecolor(cmap(norm(c)))
        bar.set_alpha(alpha)

    ax.set_theta_direction('clockwise')
    ax.set_theta_zero_location(theta_zero_loc)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_yticks(radial_ticks)
    ax.tick_params(which='major',grid_color=grid_col,grid_alpha=alpha)
    ax.yaxis.grid(ygrid)
    ax.xaxis.grid(xgrid)
    ax.spines['polar'].set_visible(False)
    ax.set_facecolor(facecol)
    ax.patch.set_alpha(alpha)

    return fig, ax


def pass_sonar_zones(data_dir, match_id, name, sonar='player', zone_cmap='Reds', bar_cmap='YlGnBu', zone_vmax='count', legend=True, badge=False):
    """
    Create a figure showing the pass sonars/radars from 18 distinct pitch zones using the StatsBomb open data.

    Parameters
    ----------
    data_dir : Directory in which the relevant StatsBomb event file is stored.
    match_id : The name of the event file.
    name : String
        Name of the player or team whose passes will be plotted.
    sonar : String, optional
        'player' or 'team'. Select whether plotting an individual player or a team's passes. The default is 'player'.
    zone_cmap : String, optional
        The colourmap for the zones. The default is 'Reds'.
    bar_cmap : String, optional
        The colourmap for the sonar bars. The default is 'YlGnBu'.
    zone_vmax : String or Float, optional
        Choose 'count' to use the maximum number of passes over all zones. Otherwise choose a custom float value. The default is 'count'.
    legend : Bool, optional
        Whether to add the legend/annotations to the left of the pitch plot. The default is True.
    badge : Bool, optional
        Whether to add the club badge. Currently this can only plot the Barcelona badge. The default is False.

    Returns
    -------
    fig : The created figure.
    ax : The pitch axis.
    ax2 : The sonar/radar annotation.
    ax3 : The sonar/radar annotation colourbar.
    ax4 : The zone annotation colourbar.

    """
    data = imsb.open_data(data_dir + '{}.json'.format(match_id))
    xgrid = np.linspace(0,120,7)
    ygrid = np.linspace(0,80,4)
    df = pd.json_normalize(data)
    df_pass = df.copy()
    
    if sonar is "player":
        if name not in df["player.name"].unique():
            raise ValueError("Player name not in data.")
        else:
            df_pass = df_pass[(df_pass["type.name"] == "Pass")&(df["player.name"] == name)]
            df_pass = df_pass.dropna(axis='columns', how='all')
            if name in pd.json_normalize(data[0]['tactics']['lineup'])['player.name'].values:
                team = data[0]['team']['name']
                opp = data[1]['team']['name']
            else:
                team = data[1]['team']['name']
                opp = data[0]['team']['name']
    elif sonar is "team":
        if name not in df["team.name"].unique():
            raise ValueError("Team name not in data.")
        else:
            df_pass = df_pass[(df_pass["type.name"] == "Pass")&(df["team.name"] == name)]
            df_pass = df_pass.dropna(axis='columns', how='all')
            if name == data[0]['team']['name']:
                team = name
                opp = data[1]['team']['name']
            else:
                team = name
                opp = data[0]['team']['name']
    else:
        raise ValueError("Only 'player' and 'team' are valid sonar options.")
        
    df1 = df_pass[['pass.length','pass.angle']].copy()
    angle_bins = np.linspace(-np.pi,np.pi+0.001,12) #np.pi is too precise for the angle measurements
    df1['angle_mid'] = pd.cut(df1['pass.angle'],angle_bins,include_lowest=True).apply(lambda x: x.mid)
    df1['x'] = df_pass['location'].apply(lambda x: x[0])
    df1['y'] = df_pass['location'].apply(lambda x: 80-x[1]) # Flip y-coord for plotting StatsBomb data
    df1['x_zone'] = pd.cut(df1['x'], xgrid, include_lowest = True).apply(lambda x: x.mid)
    df1['y_zone'] = pd.cut(df1['y'], ygrid, include_lowest = True).apply(lambda x: x.mid)
    
    # Number of passes in each bin
    counts = df1.groupby(['x_zone','y_zone']).size()
    counts.rename('counts',inplace=True)
    counts_img = counts.reset_index().pivot('y_zone','x_zone','counts')
    
    df1 = df1.merge(counts,right_index=True,left_on=['x_zone','y_zone'])
    
    df2 = df1.groupby(['x_zone','y_zone','angle_mid'],as_index=False)['pass.length'].mean().dropna()
    # Calculate the fraction of passes in that zone that are in each angle bin
    df2['pass_frac'] = (df1.groupby(['x_zone','y_zone','angle_mid']).size()/
                    df1.groupby(['x_zone','y_zone','angle_mid'])['counts'].mean()).rename('pass_frac').dropna().values

    ### Plotting ###
    z_cmap = plt.cm.get_cmap(zone_cmap)
    b_cmap = plt.cm.get_cmap(bar_cmap)
    if zone_vmax is 'count':
        zone_vmax = counts.max()/counts.sum()
        
    zone_norm_range = plt.Normalize(vmin=0,vmax=zone_vmax)

    if legend:
        fig = plt.figure(figsize=(10,12))
        ax = fig.add_axes([0.2,0.1,0.8,0.8])
        _,ax = dp.draw_pitch('w','k','v','f',figax=(fig,ax),alpha=0.3)
    else:
        fig,ax = dp.draw_pitch('w','k','v','f',alpha=0.3)

    ax.imshow(counts_img[::-1].T[::-1],extent=[0,80,0,120], aspect='auto', cmap=z_cmap,alpha=0.8)

    for xzone in df2['x_zone'].unique():
        for yzone in df2['y_zone'].unique():
            alpha = change_range(counts.loc[xzone,yzone],(0,counts.max()),(0.5,1))
            df_zone = df2[(df2['x_zone'] == xzone)&(df2['y_zone'] == yzone)]
            plot_inset(1.3, ax, df_zone, 80-yzone, xzone, alpha=alpha, c_map=b_cmap, zero_loc='N')

    ax.set_aspect('equal')
    
    if legend:
        # Adding the radar legend
        ax2 = fig.add_axes([0.05,0.6,0.15,0.15], projection='polar')
        bars = ax2.bar([0,0.53,0.53*2], [0.25,0.2,0.3], width=0.5, color=b_cmap(0.8))
        for val,bar in zip([0.1,0.5,0.8],bars):
            bar.set_facecolor(b_cmap(val))
        ax2.set_rlim(0,0.25)
        ax2.set_rgrids([0.1,0.2,0.3],['10%','20%','30%'],angle=135,ha='center',va='bottom')
        ax2.set_thetagrids([],labels=[])
        ax2.tick_params(labelsize=12)
        ax2.grid(color='w')
        ax2.spines['polar'].set_visible(False)
        ax2.set_facecolor('0.8')
        ax2.text(0.5,1.2,"Fraction of Passes From Zone",transform=ax2.transAxes,ha='center',va='top',fontsize=14)

        # Adding the sonar colourbar legend
        ax3 = fig.add_axes([0.05,0.55,0.15,0.02])
        norm_range = plt.Normalize(vmin=0,vmax=30)
        cbar = mpl.colorbar.ColorbarBase(ax3,cmap=plt.cm.get_cmap('YlGnBu'), norm=norm_range, 
                                                orientation="horizontal",alpha=0.6)
        cbar.set_ticks([0,10,20,30])
        ax3.tick_params(labelsize=12)
        ax3.text(0.5,1.3,"Average Pass Distance (Yards)",transform=ax3.transAxes,ha='center',va='bottom',fontsize=14)

        # Adding the zone colourbar legend
        ax4 = fig.add_axes([0.05,0.46,0.16,0.02])
        zone_vmax = counts.max()/counts.sum()
        for pos,frac in zip([0,0.25,0.5,0.75],np.linspace(0,round(zone_vmax,2),4)):
            rect = Rectangle((pos,0.05),0.2,0.97,transform=ax4.transAxes, ec='k', fc=z_cmap(zone_norm_range(frac)),alpha=0.8)
            ax4.add_patch(rect)
            ax4.text(pos+0.1,-0.15,"{:.0f}%".format(frac*100),transform=ax4.transAxes,ha='center',va='top',fontsize=12)
        ax4.set_ylim([0,1])
        ax4.axis('off')
        ax4.text(0.5,1.3,"Fraction of Total Passes",transform=ax4.transAxes,ha='center',va='bottom',fontsize=14)

        # Info text
        if sonar is "player":
            ax.text(-0.02,0.99,"{}".format(name),transform=ax.transAxes,fontsize=20,ha='right',va='top')
            ax.text(-0.02,0.96,"{}".format(team),transform=ax.transAxes,fontsize=20,ha='right',va='top')
            ax.text(-0.02,0.93,"vs {}".format(opp),transform=ax.transAxes,fontsize=16,ha='right',va='top')
        elif sonar is "team":
            ax.text(-0.02,0.99,"{}".format(team),transform=ax.transAxes,fontsize=20,ha='right',va='top')
            ax.text(-0.02,0.96,"vs {}".format(opp),transform=ax.transAxes,fontsize=16,ha='right',va='top')
    
    if badge:
        badge_dir = "images/badges/laliga"
        im = Image.open(badge_dir + "/barca.png")
        width, height = im.size
        ax_badge = fig.add_axes([0.1,0.1,0.15,0.15])
        ax_badge.imshow(im,interpolation='hanning')
        ax_badge.axis('off')
            
    plt.show()
    
    #fig.savefig('example_plots/pass_sonar_zones_{}.png'.format(sonar),dpi=100,bbox_inches = 'tight',pad_inches=0.1)
    
    return fig,ax,ax2,ax3,ax4