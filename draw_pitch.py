#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:51:59 2020

Function for draw a football pitch.

Distances are in yards as it was orignally built based off the Statsbomb data.

@author: Jonathan Manuel
"""

def draw_pitch(pitch_col, line_col, orientation,view):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Arc
    
    orientation = orientation # Horizontal or vertical
    view = view # full or half pitch
    line_col = line_col
    pitch_col = pitch_col
    
    # Using pitch dimensions 120yd x 80yd (110m x 75m)
    if orientation.lower().startswith("h"):
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(9,12))
            plt.xlim(59,121)
            plt.ylim(-1,81)
        else:
            fig,ax = plt.subplots(figsize=(12,8))
            plt.xlim(-1,121)
            plt.ylim(-1,81)
        ax.axis('off') # this hides the x and y ticks

        # side and goal lines #
        lx1 = [0,120,120,0,0]
        ly1 = [0,0,80,80,0]
        
        plt.plot(lx1,ly1,color=line_col,lw=1.5,zorder=1)
        
        # boxes, 6 yard box and goals
        
        #outer boxes#
        lx2 = [120,102,102,120]
        ly2 = [18,18,62,62] 
        plt.plot(lx2,ly2,color=line_col,lw=1.5,zorder=1)
        
        lx3 = [0,18,18,0]
        ly3 = [18,18,62,62] 
        plt.plot(lx3,ly3,color=line_col,lw=1.5,zorder=1)
        
        #goals#
        lx4 = [120,120.4,120.4,120]
        ly4 = [36,36,44,44]
        plt.plot(lx4,ly4,color=line_col,lw=1.5,zorder=1)
        
        lx5 = [0,-0.4,-0.4,0]
        ly5 = [36,36,44,44]
        plt.plot(lx5,ly5,color=line_col,lw=1.5,zorder=1)
        
        #6 yard boxes#
        lx6 = [120,114,114,120]
        ly6 = [30,30,50,50]
        plt.plot(lx6,ly6,color=line_col,lw=1.5,zorder=1)
        
        lx7 = [0,6,6,0]
        ly7 = [30,30,50,50]
        plt.plot(lx7,ly7,color=line_col,lw=1.5,zorder=1)
        
        #Halfway line, penalty spots, and kickoff spot
        lx8 = [60,60]
        ly8 = [0,80]
        plt.plot(lx8,ly8,color=line_col,lw=1.5,zorder=1)
        
        plt.scatter(108,40,s=30,color=line_col,zorder=1) # pen right
        plt.scatter(12,40,s=30,color=line_col,zorder=1) # pen left
        plt.scatter(60,40,s=30,color=line_col,zorder=1) # kickoff
        
        #Circles
        centreCircle = plt.Circle((60,40),10,color=line_col,lw=1.5,fill=False,zorder=1,alpha=1)
            
        #Arcs
        rightArc = Arc((108,40),height=20,width=20,angle=0,theta1=127,theta2=233,color=line_col,lw=1.5,zorder=1)
        leftArc = Arc((12,40),height=20,width=20,angle=0,theta1=307,theta2=53,color=line_col,lw=1.5,zorder=1)
        
        ax.add_patch(centreCircle)
        ax.add_patch(rightArc)
        ax.add_patch(leftArc)
        
    else:
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(12,9))
            plt.ylim(59,121)
            plt.xlim(-1,81)
        else:
            fig,ax = plt.subplots(figsize=(8,12))
            plt.ylim(-1,121)
            plt.xlim(-1,81)
        ax.axis('off') # this hides the x and y ticks
        
        # side and goal lines #
        lx1 = [0,0,80,80,0]
        ly1 = [0,120,120,0,0]
        
        plt.plot(lx1,ly1,color=line_col,lw=1.5,zorder=1)
        
        # boxes, 6 yard box and goals
        
        #outer boxes#
        lx2 = [18,18,62,62]
        ly2 = [120,102,102,120] 
        plt.plot(lx2,ly2,color=line_col,lw=1.5,zorder=1)
        
        lx3 = [18,18,62,62]
        ly3 = [0,18,18,0] 
        plt.plot(lx3,ly3,color=line_col,lw=1.5,zorder=1)
        
        #goals#
        ly4 = [120,120.2,120.2,120]
        lx4 = [36,36,44,44]
        plt.plot(lx4,ly4,color=line_col,lw=1.5,zorder=1)
        
        ly5 = [0,-0.2,-0.2,0]
        lx5 = [36,36,44,44]
        plt.plot(lx5,ly5,color=line_col,lw=1.5,zorder=1)
        
        #6 yard boxes#
        ly6 = [120,114,114,120]
        lx6 = [30,30,50,50]
        plt.plot(lx6,ly6,color=line_col,lw=1.5,zorder=1)
        
        ly7 = [0,6,6,0]
        lx7 = [30,30,50,50]
        plt.plot(lx7,ly7,color=line_col,lw=1.5,zorder=1)
        
        #Halfway line, penalty spots, and kickoff spot
        ly8 = [60,60]
        lx8 = [0,80]
        plt.plot(lx8,ly8,color=line_col,lw=1.5,zorder=1)
        
        plt.scatter(40,108,color=line_col,s=30,zorder=1) # pen right
        plt.scatter(40,12,color=line_col,s=30,zorder=1) # pen left
        plt.scatter(40,60,color=line_col,s=30,zorder=1) # kickoff
        
        #Circles
        centreCircle = plt.Circle((40,60),10,color=line_col,lw=1.5,fill=False,zorder=1,alpha=1)
            
        #Arcs
        rightArc = Arc((40,108),height=20,width=20,angle=90,theta1=127,theta2=233,color=line_col,lw=1.5,zorder=1)
        leftArc = Arc((40,12),height=20,width=20,angle=90,theta1=307,theta2=53,color=line_col,lw=1.5,zorder=1)
        
        ax.add_patch(centreCircle)
        ax.add_patch(rightArc)
        ax.add_patch(leftArc)
        
    return fig,ax