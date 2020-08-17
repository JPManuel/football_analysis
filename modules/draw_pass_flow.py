#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:43:02 2020

@author: Jonathan Manuel
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic_2d, circmean

import draw_pitch as dp


def change_range(value,old_range,new_range):
    return ((value - old_range[0])/(old_range[1]-old_range[0])) * (new_range[1]-new_range[0]) + new_range[0]


def calc_angle(xstart, ystart, xend, yend):
    xstart, ystart, xend, yend = np.array(xstart), np.array(ystart), np.array(xend), np.array(yend)
    xdist = xend - xstart
    ydist = yend - ystart
    angle = np.arctan2(ydist, xdist)
    return angle


def pass_flow(xstart, ystart, xend, yend, xend=None, yend=None, angles=None, bins=(6,4), color=None,
              length=None, vary_length=False, arr_cmap='viridis', bin_cmap='Blues', figax=None,
              fig_width=8, orientation='h'):
    """
    Plot a pass flow map by binning the data and calculating the average angles. The angle of each pass can be provided directly (useful when the data includes pass angle such as StatsBomb) or the angle can be calculated by providing starting and ending coordinates for each pass.

    Parameters
    ----------
    xstart, ystart : array-like
        Starting coordinates for passes.
    ystart : array-like
        DESCRIPTION.
    xend, yend : array-like, default is None
        Ending coordinates for passes. Only necessary when angles are not explicitly provided such that angles can be calculated.
    angles : array-like, default is None
        Angle for every pass. Must be same size as xstart.
    bins : (int,int), default is (6,4)
        The number of bins in each dimension. From a horizontal pitch viewpoint: nx, ny = bins.
    color : A matplotlib colour, default is None
        If None then arrow colour is given by arr_cmap and the number of passes from each bin.
    length : float, default is None
        Arrow length. If None then it is half the bin width.
    vary_length : bool, default is False
        If True the arrow length depends on the number of passes in the corresponding bin.
    arr_cmap : colormap, default is 'viridis'
        Colormap used for the arrows.
    bin_cmap : colormap, default is 'Blues'
        Colormap used for the bins.
    figax : (fig, ax), default is None
        Provide a matplotlib figure and axes instance to plot on. If None then a pitch is drawn using the draw_pitch module.
    fig_width : int or float, default is 8
        Width of the pitch drawn by draw_pitch when figax is not provided.
    orientation : 'h' or 'v', default is 'h'
        Orientation of the pitch drawn by draw_pitch - 'h' is horizontal and 'v' is vertical.

    Returns
    -------
    ax : matplotlib.axes.Axes

    """
    
    if figax is None:
        fig, ax = dp.draw_pitch('w','k',orientation,'f',fig_width=fig_width)
    else:
        fig, ax = figax[0], figax[1]
    
    # Bin the number of passes
    counts, xedge, yedge, bin_num = binned_statistic_2d(xstart, ystart, values=xstart, bins = bins, range = [[0,120],[0,80]], statistic='count', expand_binnumbers=True)
    counts = counts.T # Make x correspond to columns for horizontal pitch plotting
    
    # Create the grid and the grid of bin centres
    x_grid, y_grid = np.meshgrid(xedge,yedge)
    x_mid, y_mid = np.meshgrid(xedge[:-1] + np.diff(xedge) / 2, yedge[:-1] + np.diff(yedge) / 2)
    
    if angles is None:
        if xend is None or yend is None:
            raise ValueError("Provide array-like values for xend and yend.")
        
        angles = calc_angle(xstart, ystart, xend, yend)
        angles_bin, *_ = binned_statistic_2d(xstart, ystart, values=angles, bins=bins, range=[[0,120],[0,80]], statistic=circmean, expand_binnumbers=True)
        angles_bin = angles_bin.T
        
        # If length isn't specified default to half of the shortest side of the bin so arrow doesn't extend beyond bin
        if length is None:
            if np.diff(xedge)[0] <= np.diff(yedge)[0]:
                length = np.diff(xedge)[0] / 2
            else:
                length = np.diff(yedge)[0] / 2
        
        if vary_length is True:
            lengths = change_range(counts,(np.min(counts),np.max(counts)),(length/2,length))
            xdiff = np.multiply(np.cos(angles_bin), lengths)
            ydiff = np.multiply(np.sin(angles_bin), lengths)
        else:
            xdiff = np.cos(angles_bin) * length
            ydiff = np.sin(angles_bin) * length
        
        angles_bin = np.degrees(angles_bin) # Change to degrees for quiver plotting
        
        if color is None:
            if orientation.startswith('h'):
                ax.quiver(x_mid, y_mid, xdiff, ydiff, counts, angles='xy', scale=1, scale_units='xy', cmap=arr_cmap)
                ax.imshow(counts, origin='lower', extent=(0,120,0,80), alpha=0.8, cmap=bin_cmap)
            else:
                ax.quiver(y_mid.T, x_mid.T, -1*np.flip(ydiff.T,1), np.flip(xdiff.T,1), np.flip(counts.T,1), 
                          angles='xy', scale=1, scale_units='xy', cmap=arr_cmap)
                ax.imshow(np.flip(counts.T,1), origin='lower', extent=(0,80,0,120), alpha=0.8, cmap=bin_cmap)
        else:
            if orientation.startswith('h'):
                ax.quiver(x_mid, y_mid, xdiff, ydiff, color=color, angles='xy', scale=1, scale_units='xy')
                ax.imshow(counts, origin='lower', extent=(0,120,0,80), alpha=0.8, cmap=bin_cmap)
            else:
                ax.quiver(y_mid.T, x_mid.T, -1*np.flip(ydiff.T,1), np.flip(xdiff.T,1), color=color, angles='xy', scale=1, scale_units='xy')
                ax.imshow(np.flip(counts.T,1), origin='lower', extent=(0,80,0,120), alpha=0.8, cmap=bin_cmap)
        
    
    else:
        angles_bin, *_ = binned_statistic_2d(xstart, ystart, values=angles, bins = bins, range = [[0,120],[0,80]], statistic=circmean, expand_binnumbers=True)
        angles_bin = np.degrees(angles_bin.T)

        # If length is not specified then set it to be half bin-width
        if length is None:
            length = 1 / (2*bins[0])

        # When providing the angles directly the length of the arrows is simply determined by the U vector
        U = np.full((x_mid.shape[0],x_mid.shape[1]), length)

        # Setting arrow length to zero in bins where there were no passes
        zero_locs = np.where(counts == 0)
        zeros_list = list(zip(zero_locs[0], zero_locs[1]))
        for i in zeros_list:
            U[i] = 0
        
        if color is None:
            if orientation.startswith('h'):
                ax.quiver(x_mid, y_mid, U, 0, counts, angles=angles_bin, scale=1, scale_units='width', cmap=arr_cmap, zorder=10)
                ax.imshow(counts, origin='lower', extent=(0,120,0,80), alpha=0.8, cmap=bin_cmap)
            else:
                ax.quiver(y_mid.T, x_mid.T, np.flip(U.T,1), 0, np.flip(counts.T,1), angles=np.flip(angles_bin.T,1)+90, scale=1, scale_units='width', cmap=arr_cmap, zorder=10)
                ax.imshow(np.flip(counts.T,1), origin='lower', extent=(0,80,0,120), alpha=0.8, cmap=bin_cmap)
        else:
            if orientation.startswith('h'):
                ax.quiver(x_mid, y_mid, U, 0, color=color, angles=angles_bin, scale=1, scale_units='width', zorder=10)
                ax.imshow(counts, origin='lower', extent=(0,120,0,80), alpha=0.8, cmap=bin_cmap)
            else:
                ax.quiver(y_mid.T, x_mid.T, np.flip(U.T,1), 0, color=color, angles=np.flip(angles_bin.T,1)+90, scale=1, scale_units='width', zorder=10)
                ax.imshow(np.flip(counts.T,1), origin='lower', extent=(0,80,0,120), alpha=0.8, cmap=bin_cmap)

    plt.show()
    
    return ax