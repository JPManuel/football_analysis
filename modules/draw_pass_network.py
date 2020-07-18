#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:57:45 2020

@author: Jonathan Manuel
"""

#import sys, os
#sys.path.append(os.path.abspath("modules"))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.colors import Normalize
from matplotlib import cm

import importing_sb as imsb
import draw_pitch as dp

def change_range(value,old_range,new_range):
    return ((value - old_range[0])/(old_range[1]-old_range[0])) * (new_range[1]-new_range[0]) + new_range[0]

def find_pair_counts(players,df):
    players_counted = []
    player1 = []
    player2 = []
    count = []
    for i in players:
        for j in players:
            if j in players_counted:
                continue
            if i == j:
                continue
            if j in df.loc[i].index and i in df.loc[j].index:
                player1.append(i)
                player2.append(j)
                count.append(df.loc[i,j]+df.loc[j,i])
            elif j in df[i].index and i not in df.loc[j].index:
                player1.append(i)
                player2.append(j)
                count.append(df.loc[i,j])
            elif j not in df.loc[i].index and i in df.loc[j].index:
                player1.append(i)
                player2.append(j)
                count.append(df.loc[j,i])

        players_counted.append(i)
        
    df_pair = pd.DataFrame({'player1':player1,'player2':player2,'total':count})
        
    return df_pair

class Player(object):
    def __init__(self, player, dict_num, df):
        self.name = player
        self.number = dict_num[player]
        self.get_loc(player,df)
        self.pass_count = df.groupby('player').size()[player]
        
    def get_loc(self,player,df):
        loc1 = df[df['player'] == player][['x','y']]
        loc2 = df[df['recipient'] == player][['end_x','end_y']].rename(columns={'end_x':'x','end_y':'y'})
        loc = pd.concat([loc1,loc2]).mean()
        self.loc = (loc['x'],loc['y'])
                  
def draw_pass_network_sb(data_dir,match_id,team="home",comp="",season="",date="",edge_type="combined",colours=False,size=False,pass_count_threshold=5,nc='#004d98',ec='k',tc='k',ns=50,n_cmap='Greens',e_cmap='Blues'):
    """
    Plot a passing network.
    
    Parameters
    ----------
        data_dir: Directory in which the StatsBomb event data can be found. Something like "open-data/data/events/".
        match_id: The match id of the match for which passes will be plotted. This must be (and is by default) the name of the corresponding StatsBomb event json file.
    """
    
    data = imsb.open_data(data_dir + '{}.json'.format(match_id))
    
    if team == 'home':
        team_name = data[0]['team']['name']
        opp_name = data[1]['team']['name']
        players = [player['player']['name'] for player in data[0]['tactics']['lineup']]
        numbers = [number['jersey_number'] for number in data[0]['tactics']['lineup']]
    if team == 'away':
        team_name = data[1]['team']['name']
        opp_name = data[0]['team']['name']
        players = [player['player']['name'] for player in data[1]['tactics']['lineup']]
        numbers = [number['jersey_number'] for number in data[1]['tactics']['lineup']]
    
    dict_num = {players[i]:numbers[i] for i in range(len(players))}
    
    df = imsb.get_pass(data)
    df['y'] = df['y'].apply(lambda y: 80-y) # Flipping y coord for plotting
    df['end_y'] = df['end_y'].apply(lambda y: 80-y) # Flipping y coord for plotting
    df = df[df['outcome'] == 'Complete'] # Taking only complete passes
    df = df[df['pass_type'] == 'Standard'] # Only standard, open play passes
    df = df[df['team'] == team_name] # Only Barca passes
    df = df[df['player'].isin(players)] # keep passers only in starting 11
    df = df[df['recipient'].isin(players)] # keep recipients only in starting 11
    df.drop(['index','event_id','minute','second','type','duration','cross','cutback','switch','technique'],axis=1,
           inplace=True)
    
    # Passes played by each player
    df_player_count = df.groupby(['player','recipient']).size()
    
    # Pass count between pairs of players
    df_pair_count = find_pair_counts(players,df_player_count)
    
    max_play_count = df.groupby('player').size().max()
    min_play_count = df.groupby('player').size().min()
    max_pair_count = df_pair_count['total'].max()
    min_pair_count = df_pair_count['total'].min()
    max_pair_count_separate = df_player_count.max()
    max_edge_width = 5
    min_edge_width = 0.1
    arr_shift = 1
    ns_max = 90
    ns_min = 50
    
    
    fig,ax = dp.draw_pitch('w','k','h','f',alpha=0.3)
    
    if edge_type == "combined":
        ### Count total passes between pairs ###
        if colours is False:
            # Plot nodes
            for i in players:
                p = Player(i, dict_num,df)
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=nc,mec='k',zorder=10)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
            # Plot edges
            for i,row in df_pair_count.iterrows():
                if row['total'] < pass_count_threshold:
                    continue
                p1 = Player(row['player1'], dict_num,df)
                p2 = Player(row['player2'], dict_num,df)
                loc = [[p1.loc[0],p2.loc[0]],[p1.loc[1],p2.loc[1]]]
                num_passes = row['total']
                lw = change_range(num_passes,(0,max_pair_count),(min_edge_width,max_edge_width))
                alpha = change_range(num_passes,(0,max_pair_count),(0,1))
                ax.plot(loc[0],loc[1],c=ec,ls='-',lw=lw,alpha=alpha,zorder=9)
                
        elif colours is True:
            # Plot nodes
            node_norm = Normalize(0,max_play_count)
            node_cmap = cm.get_cmap(n_cmap)
            for i in players:
                p = Player(i, dict_num, df)
                node_colour = node_cmap(node_norm(p.pass_count))
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ns_inner = ns-20
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=node_colour,mec='k',mew=0.5,zorder=10)
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns_inner,c='w',mec='k',mew=0.5,zorder=11)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)

            # Plot edges
            edge_norm = Normalize(0,max_pair_count)
            edge_cmap = cm.get_cmap(e_cmap)
            for i,row in df_pair_count.iterrows():
                if row['total'] < pass_count_threshold:
                    continue
                p1 = Player(row['player1'], dict_num, df)
                p2 = Player(row['player2'], dict_num, df)
                loc = [[p1.loc[0],p2.loc[0]],[p1.loc[1],p2.loc[1]]]
                num_passes = row['total']
                edge_colour = edge_cmap(edge_norm(num_passes))
                line_width = change_range(num_passes,(0,max_pair_count),(min_edge_width,max_edge_width))
                ax.plot(loc[0],loc[1],'k-',lw=line_width,c=edge_colour,zorder=9)
    
        else:
            print("Please enter True or False for colours.")
            
    else:
        ### Separate passes played and received ###
        if colours is False:
            # Plot nodes
            for i in players:
                p = Player(i, dict_num, df)
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=nc,zorder=10)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
                
            # Plot edges
            for i,value in df_player_count.iteritems():
                if value < pass_count_threshold:
                    continue

                pas = Player(i[0], dict_num,df)
                rec = Player(i[1], dict_num,df)

                lw = change_range(value,(0,max_pair_count_separate),(min_edge_width,max_edge_width))
                alpha = change_range(value,(0,max_pair_count_separate),(0,1))

                # Shift arrow vertically if diff in x > diff in y
                if abs(rec.loc[0]-pas.loc[0]) > abs(rec.loc[1]-pas.loc[1]):
                    # Passes played by the player will always be on left of passes received
                    if pas.loc[0] <= rec.loc[0]:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]+arr_shift),xytext=(pas.loc[0],pas.loc[1]+arr_shift),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]-arr_shift),xytext=(pas.loc[0],pas.loc[1]-arr_shift),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))

                # Shift arrow horizontally if diff in x <= diff in y
                elif abs(rec.loc[0]-pas.loc[0]) <= abs(rec.loc[1]-pas.loc[1]):
                    # Again ensuring passes played by the player will always be on left of passes received
                    if pas.loc[1] > rec.loc[1]:
                        ax.annotate("",xy=(rec.loc[0]+arr_shift,rec.loc[1]),xytext=(pas.loc[0]+arr_shift,pas.loc[1]),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0]-arr_shift,rec.loc[1]),xytext=(pas.loc[0]-arr_shift,pas.loc[1]),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
            
        elif colours is True:
            # Plot nodes
            node_norm = Normalize(0,max_play_count)
            node_cmap = cm.get_cmap(n_cmap)
            for i in players:
                p = Player(i, dict_num, df)
                node_colour = node_cmap(node_norm(p.pass_count))
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ns_inner = ns-20
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=node_colour,mec='k',mew=0.5,zorder=10)
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns_inner,c='w',mec='k',mew=0.5,zorder=11)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
                
            # Plot edges
            edge_norm = Normalize(0,max_pair_count_separate)
            edge_cmap = cm.get_cmap(e_cmap)
            for i,value in df_player_count.iteritems():
                if value < pass_count_threshold:
                    continue

                pas = Player(i[0], dict_num, df)
                rec = Player(i[1], dict_num, df)
                
                ec = edge_cmap(edge_norm(value))
                lw = change_range(value,(0,max_pair_count_separate),(min_edge_width,max_edge_width))
                alpha = change_range(value,(0,max_pair_count_separate),(0,1))

                # Shift arrow vertically if diff in x > diff in y
                if abs(rec.loc[0]-pas.loc[0]) > abs(rec.loc[1]-pas.loc[1]):
                    # Passes played by the player will always be on left of passes received
                    if pas.loc[0] <= rec.loc[0]:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]+arr_shift),xytext=(pas.loc[0],pas.loc[1]+arr_shift),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]-arr_shift),xytext=(pas.loc[0],pas.loc[1]-arr_shift),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))

                # Shift arrow horizontally if diff in x <= diff in y
                elif abs(rec.loc[0]-pas.loc[0]) <= abs(rec.loc[1]-pas.loc[1]):
                    # Again ensuring passes played by the player will always be on left of passes received
                    if pas.loc[1] > rec.loc[1]:
                        ax.annotate("",xy=(rec.loc[0]+arr_shift,rec.loc[1]),xytext=(pas.loc[0]+arr_shift,pas.loc[1]),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0]-arr_shift,rec.loc[1]),xytext=(pas.loc[0]-arr_shift,pas.loc[1]),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
        
        else:
            print("Please enter True or False for colours.")
            
    ax.text(0,88,"{} - Pass Network".format(team_name),fontsize=20,fontweight='bold')
    ax.text(0,83,"vs {} | {} | {}".format(opp_name,comp,date),fontsize=16)
    
    if colours is True:
        nc_ex = [node_cmap(node_norm(min_play_count)),node_cmap(node_norm((max_play_count-min_play_count)/2)),
                 node_cmap(node_norm(max_play_count))]
        nc_ex_val = [min_play_count,(max_play_count-min_play_count)/2,max_play_count]
        x_ex = [3,5,7]
        y_ex = [5,5,5]
        ax2 = fig.add_axes([0.71,0.90,0.2,0.05])
        ax2.set_xlim(0,10)
        ax2.set_ylim(0,10)
        ax2.axis('off')
        ax2.text(5,12,"Pass number by player",ha='center',fontsize=13)
        for i in range(len(x_ex)):
            ax2.plot(x_ex[i],y_ex[i],'.',markersize=ns_min,c=nc_ex[i],mec='k',mew=0.5,zorder=10)
            ax2.plot(x_ex[i],y_ex[i],'.',markersize=(3/5)*ns_min,c='w',mec='k',mew=0.5,zorder=10)
            ax2.text(x_ex[i],-4,"{:.0f}".format(np.ceil(nc_ex_val[i])),ha='center',fontsize=12)
            
        ec_ex = [edge_cmap(edge_norm(min_pair_count)),edge_cmap(edge_norm((max_pair_count-min_pair_count)/2)),
                 edge_cmap(edge_norm(max_pair_count))]
        ec_ex_val = [min_pair_count,(max_pair_count-min_pair_count)/2,max_pair_count]
        x_ex = [[1,3],[4,6],[7,9]]
        y_ex = [[5,5],[5,5],[5,5]]
        ax3 = fig.add_axes([0.51,0.90,0.2,0.05])
        ax3.set_xlim(0,10)
        ax3.set_ylim(0,10)
        ax3.axis('off')
        ax3.text(5,12,"Pass number between players",ha='center',fontsize=13)
        for i in range(len(x_ex)):
            ax3.plot(x_ex[i],y_ex[i],'-',markersize=ns,c=ec_ex[i],lw=4,zorder=10,
                     path_effects=[pe.Stroke(linewidth=6,foreground='k'), pe.Normal()])
            ax3.text(x_ex[i][0]+1,-1,"{:.0f}".format(np.ceil(ec_ex_val[i])),ha='center',fontsize=12)
            
    plt.show()
    
def draw_pass_network(df,dict_num,team_name="home",opp_name="opp",comp="test",season="test",date="test",edge_type="combined",colours=False,size=False,nc='#004d98',ec='k',tc='k',ns=50,n_cmap='Greens',e_cmap='Blues',
                     pass_count_threshold=5):
    """
    Plot a passing network from a dataframe.
    
    Parameters
    ----------
        df: A dataframe of the passes to be plotted. Must contain the columns "player", "recipient", "x", "y", "end_x", "end_y".
        dict_num: A dictionary where the keys are the player names and the value is the corresponding player shrit number.
    """
    
    players = df['player'].unique()
    
    # Passes played by each player
    df_player_count = df.groupby(['player','recipient']).size()
    
    # Pass count between pairs of players
    df_pair_count = find_pair_counts(players,df_player_count)
    
    max_play_count = df.groupby('player').size().max()
    min_play_count = df.groupby('player').size().min()
    max_pair_count = df_pair_count['total'].max()
    min_pair_count = df_pair_count['total'].min()
    max_pair_count_separate = df_player_count.max()
    max_edge_width = 5
    min_edge_width = 0.1
    arr_shift = 1
    ns_max = 90
    ns_min = 50
    
    
    fig,ax = dp.draw_pitch('w','k','h','f',alpha=0.3)
    
    if edge_type == "combined":
        ### Count total passes between pairs ###
        if colours is False:
            # Plot nodes
            for i in players:
                p = Player(i, dict_num,df)
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=nc,mec='k',zorder=10)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
            # Plot edges
            for i,row in df_pair_count.iterrows():
                if row['total'] < pass_count_threshold:
                    continue
                p1 = Player(row['player1'], dict_num,df)
                p2 = Player(row['player2'], dict_num,df)
                loc = [[p1.loc[0],p2.loc[0]],[p1.loc[1],p2.loc[1]]]
                num_passes = row['total']
                lw = change_range(num_passes,(0,max_pair_count),(min_edge_width,max_edge_width))
                alpha = change_range(num_passes,(0,max_pair_count),(0,1))
                ax.plot(loc[0],loc[1],c=ec,ls='-',lw=lw,alpha=alpha,zorder=9)
                
        elif colours is True:
            # Plot nodes
            node_norm = Normalize(0,max_play_count)
            node_cmap = cm.get_cmap(n_cmap)
            for i in players:
                p = Player(i, dict_num, df)
                node_colour = node_cmap(node_norm(p.pass_count))
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ns_inner = ns-20
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=node_colour,mec='k',mew=0.5,zorder=10)
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns_inner,c='w',mec='k',mew=0.5,zorder=11)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)

            # Plot edges
            edge_norm = Normalize(0,max_pair_count)
            edge_cmap = cm.get_cmap(e_cmap)
            for i,row in df_pair_count.iterrows():
                if row['total'] < pass_count_threshold:
                    continue
                p1 = Player(row['player1'], dict_num, df)
                p2 = Player(row['player2'], dict_num, df)
                loc = [[p1.loc[0],p2.loc[0]],[p1.loc[1],p2.loc[1]]]
                num_passes = row['total']
                edge_colour = edge_cmap(edge_norm(num_passes))
                line_width = change_range(num_passes,(0,max_pair_count),(min_edge_width,max_edge_width))
                ax.plot(loc[0],loc[1],'k-',lw=line_width,c=edge_colour,zorder=9)
    
        else:
            print("Please enter True or False for colours.")
            
    else:
        ### Separate passes played and received ###
        if colours is False:
            # Plot nodes
            for i in players:
                p = Player(i, dict_num, df)
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=nc,zorder=10)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
                
            # Plot edges
            for i,value in df_player_count.iteritems():
                if value < pass_count_threshold:
                    continue

                pas = Player(i[0], dict_num,df)
                rec = Player(i[1], dict_num,df)

                lw = change_range(value,(0,max_pair_count_separate),(min_edge_width,max_edge_width))
                alpha = change_range(value,(0,max_pair_count_separate),(0,1))

                # Shift arrow vertically if diff in x > diff in y
                if abs(rec.loc[0]-pas.loc[0]) > abs(rec.loc[1]-pas.loc[1]):
                    # Passes played by the player will always be on left of passes received
                    if pas.loc[0] <= rec.loc[0]:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]+arr_shift),xytext=(pas.loc[0],pas.loc[1]+arr_shift),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]-arr_shift),xytext=(pas.loc[0],pas.loc[1]-arr_shift),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))

                # Shift arrow horizontally if diff in x <= diff in y
                elif abs(rec.loc[0]-pas.loc[0]) <= abs(rec.loc[1]-pas.loc[1]):
                    # Again ensuring passes played by the player will always be on left of passes received
                    if pas.loc[1] > rec.loc[1]:
                        ax.annotate("",xy=(rec.loc[0]+arr_shift,rec.loc[1]),xytext=(pas.loc[0]+arr_shift,pas.loc[1]),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0]-arr_shift,rec.loc[1]),xytext=(pas.loc[0]-arr_shift,pas.loc[1]),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
            
        elif colours is True:
            # Plot nodes
            node_norm = Normalize(0,max_play_count)
            node_cmap = cm.get_cmap(n_cmap)
            for i in players:
                p = Player(i, dict_num, df)
                node_colour = node_cmap(node_norm(p.pass_count))
                if size is True:
                    ns = change_range(p.pass_count,(0,max_play_count),(ns_min,ns_max))
                ns_inner = ns-20
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns,c=node_colour,mec='k',mew=0.5,zorder=10)
                ax.plot(p.loc[0],p.loc[1],'.',markersize=ns_inner,c='w',mec='k',mew=0.5,zorder=11)
                ax.annotate(p.number,p.loc,c=tc,ha='center',va='center',size=12,fontweight='bold',
                            path_effects=[pe.withStroke(linewidth=2,foreground='w')],zorder=12)
                
            # Plot edges
            edge_norm = Normalize(0,max_pair_count_separate)
            edge_cmap = cm.get_cmap(e_cmap)
            for i,value in df_player_count.iteritems():
                if value < pass_count_threshold:
                    continue

                pas = Player(i[0], dict_num, df)
                rec = Player(i[1], dict_num, df)
                
                ec = edge_cmap(edge_norm(value))
                lw = change_range(value,(0,max_pair_count_separate),(min_edge_width,max_edge_width))
                alpha = change_range(value,(0,max_pair_count_separate),(0,1))

                # Shift arrow vertically if diff in x > diff in y
                if abs(rec.loc[0]-pas.loc[0]) > abs(rec.loc[1]-pas.loc[1]):
                    # Passes played by the player will always be on left of passes received
                    if pas.loc[0] <= rec.loc[0]:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]+arr_shift),xytext=(pas.loc[0],pas.loc[1]+arr_shift),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0],rec.loc[1]-arr_shift),xytext=(pas.loc[0],pas.loc[1]-arr_shift),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))

                # Shift arrow horizontally if diff in x <= diff in y
                elif abs(rec.loc[0]-pas.loc[0]) <= abs(rec.loc[1]-pas.loc[1]):
                    # Again ensuring passes played by the player will always be on left of passes received
                    if pas.loc[1] > rec.loc[1]:
                        ax.annotate("",xy=(rec.loc[0]+arr_shift,rec.loc[1]),xytext=(pas.loc[0]+arr_shift,pas.loc[1]),
                                    arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                    shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
                    else:
                        ax.annotate("",xy=(rec.loc[0]-arr_shift,rec.loc[1]),xytext=(pas.loc[0]-arr_shift,pas.loc[1]),
                                            arrowprops=dict(arrowstyle='-|>,head_length={},head_width={}'.format(0.2*lw,0.1*lw),
                                                            shrinkA=20,shrinkB=15,lw=lw,color=ec,alpha=alpha))
        
        else:
            print("Please enter True or False for colours.")
            
    ax.text(0,88,"{} - Pass Network".format(team_name),fontsize=20,fontweight='bold')
    ax.text(0,83,"vs {} | {} | {}".format(opp_name,comp,date),fontsize=16)
    
    if colours is True:
        nc_ex = [node_cmap(node_norm(min_play_count)),node_cmap(node_norm((max_play_count-min_play_count)/2)),
                 node_cmap(node_norm(max_play_count))]
        nc_ex_val = [min_play_count,(max_play_count-min_play_count)/2,max_play_count]
        x_ex = [3,5,7]
        y_ex = [5,5,5]
        ax2 = fig.add_axes([0.71,0.90,0.2,0.05])
        ax2.set_xlim(0,10)
        ax2.set_ylim(0,10)
        ax2.axis('off')
        ax2.text(5,12,"Pass number by player",ha='center',fontsize=13)
        for i in range(len(x_ex)):
            ax2.plot(x_ex[i],y_ex[i],'.',markersize=ns_min,c=nc_ex[i],mec='k',mew=0.5,zorder=10)
            ax2.plot(x_ex[i],y_ex[i],'.',markersize=(3/5)*ns_min,c='w',mec='k',mew=0.5,zorder=10)
            ax2.text(x_ex[i],-4,"{:.0f}".format(np.ceil(nc_ex_val[i])),ha='center',fontsize=12)
            
        ec_ex = [edge_cmap(edge_norm(min_pair_count)),edge_cmap(edge_norm((max_pair_count-min_pair_count)/2)),
                 edge_cmap(edge_norm(max_pair_count))]
        ec_ex_val = [min_pair_count,(max_pair_count-min_pair_count)/2,max_pair_count]
        x_ex = [[1,3],[4,6],[7,9]]
        y_ex = [[5,5],[5,5],[5,5]]
        ax3 = fig.add_axes([0.51,0.90,0.2,0.05])
        ax3.set_xlim(0,10)
        ax3.set_ylim(0,10)
        ax3.axis('off')
        ax3.text(5,12,"Pass number between players",ha='center',fontsize=13)
        for i in range(len(x_ex)):
            ax3.plot(x_ex[i],y_ex[i],'-',markersize=ns,c=ec_ex[i],lw=4,zorder=10,
                     path_effects=[pe.Stroke(linewidth=6,foreground='k'), pe.Normal()])
            ax3.text(x_ex[i][0]+1,-1,"{:.0f}".format(np.ceil(ec_ex_val[i])),ha='center',fontsize=12)
            
    plt.show()