
def open_data(file):
    file = file
    import json
    data_file = json.load(open(file))
    return data_file
    
    
def clean_match_data(data):
    data = data
    import pandas as pd
    i = 0
    ht = []
    at = []
    hts = []
    ats = []
    
    for i in range(0,len(data)):
        if "home_team" in data[i]:
            ht.append(data[i]['home_team']['home_team_name'])
            
        if "away_team" in data[i]:
            at.append(data[i]['away_team']['away_team_name'])
            
        if "home_score" in data[i]:
            hts.append(data[i]['home_score'])
        
        if "away_score" in data[i]:
            ats.append(data[i]['away_score'])
        
    match_basic = pd.DataFrame()
    match_basic['home_team'] = ht
    match_basic['away_team'] = at
    match_basic['home_score'] = hts
    match_basic['away_score'] = ats
    
    return match_basic
    
    
def clean_event_data(data):
    data = data
    import pandas as pd
    
    ind = []
    per = []
    m = []
    s = []
    ty = []
    pos = []
    ptm = []
    pat = []
    tm = []
    pl = []
    x = []
    y = []
    dur = []
    psr = []
    rec = []
    h = []
    out = []
    end_x =[]
    end_y = []
    
    for i in range(0,len(data)):
        if "index" in data[i]:
            ind.append(data[i]['index'])
        else:
            ind.append(0)
        
        if "period" in data[i]:
            per.append(data[i]['period'])
        else:
            per.append(None)
            
        if "minute" in data[i]:
            m.append(data[i]['minute'])
        else:
            m.append(None)
            
        if "second" in data[i]:
            s.append(data[i]['second'])
        else:
            s.append(None)
            
        if "type" in data[i]:
            ty.append(data[i]['type']['name'])
        else:
            ty.append(None)
            
        if "possession" in data[i]:
            pos.append(data[i]['possession'])
        else:
            pos.append(None)
            
        if "possession_team" in data[i]:
            ptm.append(data[i]['possession_team']['name'])
        else:
            ptm.append(None)
            
        if "play_pattern" in data[i]:
            pat.append(data[i]['play_pattern']['name'])
        else:
            pat.append(None)
            
        if "team" in data[i]:
            tm.append(data[i]['team']['name'])
        else:
            tm.append(None)
        
        if "player" in data[i]:
            pl.append(data[i]['player']['name'])
        else:
            pl.append(None)
            
        if "location" in data[i]:
            x.append(data[i]['location'][0])
            y.append(data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)
            
        if "duration" in data[i]:
            dur.append(data[i]['duration'])
        else:
            dur.append(None)
            
        if "under_pressure" in data[i]:
            psr.append(data[i]['under_pressure'])
        else:
            psr.append(None)
            
        if "pass" in data[i]:
            if "recipient" in data[i]['pass']:
                rec.append(data[i]['pass']['recipient']['name'])
            else:
                rec.append(None)
            if "height" in data[i]['pass']:
                h.append(data[i]['pass']['height']['name'])
            else:
                h.append(None)
        else:
            rec.append(None)
            h.append(None)
        
        
        if "pass" in data[i]:
            if "end_location" in data[i]['pass']:
                end_x.append(data[i]['pass']['end_location'][0])
                end_y.append(data[i]['pass']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)    
            if "outcome" in data[i]['pass']:
                out.append(data[i]['pass']['outcome']['name'])
            elif "outcome" not in data[i]['pass']:
                out.append("Complete")
            else:
                out.append(None)
                
        elif "shot" in data[i]:
            if "end_location" in data[i]['shot']:
                end_x.append(data[i]['shot']['end_location'][0])
                end_y.append(data[i]['shot']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
            if "outcome" in data[i]['shot']:
                out.append(data[i]['shot']['outcome']['name'])
            elif "outcome" not in data[i]['shot']:
                out.append("Complete")
            else:
                out.append(None)
                
        elif "carry" in data[i]:
            if "end_location" in data[i]['carry']:
                end_x.append(data[i]['carry']['end_location'][0])
                end_y.append(data[i]['carry']['end_location'][1])
            else:
                end_x.append(None)
                end_y.append(None)
            out.append(None)
        else:
            end_x.append(None)
            end_y.append(None)
            out.append(None)
    
    match_events = pd.DataFrame()
    match_events['m_index'] = ind
    match_events['period'] = per
    match_events['minute'] = m
    match_events['second'] = s
    match_events['type'] = ty
    match_events['pos'] = pos
    match_events['pos_team'] = ptm
    match_events['play_pattern'] = pat
    match_events['team'] = tm
    match_events['player'] = pl
    match_events['x'] = x
    match_events['y'] = y
    match_events['end_x'] = end_x
    match_events['end_y'] = end_y
    match_events['height'] = h
    match_events['duration'] = dur
    match_events['pressure'] = psr
    match_events['outcome'] = out
    match_events['recipient'] = rec
    
    return match_events


def get_shots(data):
    data = data
    import pandas as pd
    
    i = 0
    shot_data = []
    for i in range(0,len(data)):
        if("shot" in data[i]):
            shot_data.append(data[i])
        else:
            pass
    
    i = 0
    ind = []
    per = []
    m = []
    s = []
    ty = []
    ptm = []
    pat = []
    tm = []
    pl = []
    x = []
    y = []
    dur = []
    psr = []
    end_x =[]
    end_y = []
    end_z = []
    ft = []
    ff = []
    opg = []
    sxg = []
    dfl = []
    tec = []
    bp = []
    sty = []
    out = []
    
    for i in range(len(shot_data)):
        if "index" in shot_data[i]:
            ind.append(shot_data[i]['index'])
        else:
            ind.append(0)
    
        if "period" in shot_data[i]:
            per.append(shot_data[i]['period'])
        else:
            per.append(None)
        
        if "minute" in shot_data[i]:
            m.append(shot_data[i]['minute'])
        else:
            m.append(None)
            
        if "second" in shot_data[i]:
            s.append(shot_data[i]['second'])
        else:
            s.append(None)
            
        if "type" in shot_data[i]:
            ty.append(shot_data[i]['type']['name'])
        else:
            ty.append(None)
            
        if "possession_team" in shot_data[i]:
            ptm.append(shot_data[i]['possession_team']['name'])
        else:
            ptm.append(None)
            
        if "play_pattern" in shot_data[i]:
            pat.append(shot_data[i]['play_pattern']['name'])
        else:
            pat.append(None)
            
        if "team" in shot_data[i]:
            tm.append(shot_data[i]['team']['name'])
        else:
            tm.append(None)
            
        if "player" in shot_data[i]:
            pl.append(shot_data[i]['player']['name'])
        else:
            pl.append(None)
            
        if "location" in shot_data[i]:
            x.append(shot_data[i]['location'][0])
            y.append(shot_data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)
            
        if "duration" in shot_data[i]:
            dur.append(shot_data[i]['duration'])
        else:
            dur.append(None)
            
        if "under_pressure" in shot_data[i]:
            psr.append(shot_data[i]['under_pressure'])
        else:
            psr.append(False)
            
        if "end_location" in shot_data[i]['shot']:
            end_x.append(shot_data[i]['shot']['end_location'][0])
            end_y.append(shot_data[i]['shot']['end_location'][1])
            if len(shot_data[i]['shot']['end_location']) == 3:
                end_z.append(shot_data[i]['shot']['end_location'][2])
            else:
                end_z.append(None)
        else:
            end_x.append(None)
            end_y.append(None)
            
        if "first_time" in shot_data[i]['shot']:
            ft.append(shot_data[i]['shot']['first_time'])
        else:
            ft.append(False)
            
        if "freeze_frame" in shot_data[i]['shot']:
            ff.append(shot_data[i]['shot']['freeze_frame'])
        else:
            ff.append(None)
            
        if "open_goal" in shot_data[i]['shot']:
            opg.append(shot_data[i]['shot']['open_goal'])
        else:
            opg.append(False)
            
        if "statsbomb_xg" in shot_data[i]['shot']:
            sxg.append(shot_data[i]['shot']['statsbomb_xg'])
        else:
            sxg.append(None)
        
        if "deflected" in shot_data[i]['shot']:
            dfl.append(shot_data[i]['shot']['deflected'])
        else:
            dfl.append(False)
        
        if "technique" in shot_data[i]['shot']:
            tec.append(shot_data[i]['shot']['technique']['name'])
        else:
            tec.append(None)
            
        if "body_part" in shot_data[i]['shot']:
            bp.append(shot_data[i]['shot']['body_part']['name'])
        else:
            bp.append(None)
            
        if "type" in shot_data[i]['shot']:
            sty.append(shot_data[i]['shot']['type']['name'])
        else:
            sty.append(None)
            
        if "outcome" in shot_data[i]['shot']:
            out.append(shot_data[i]['shot']['outcome']['name'])
        else:
            out.append(None)
    
    shots = pd.DataFrame()
    shots['index'] = ind
    shots['period'] = per
    shots['minute'] = m
    shots['second'] = s
    shots['type'] = ty
    shots['pos_team'] = ptm
    shots['play_pattern'] = pat
    shots['team'] = tm
    shots['player'] = pl
    shots['x'] = x
    shots['y'] = y
    shots['duration'] = dur
    shots['under_pressure'] = psr
    shots['end_x'] = end_x
    shots['end_y'] = end_y
    shots['end_z'] = end_z
    shots['first_time'] = ft
    shots['freeze_frame'] = ff
    shots['open_goal'] = opg
    shots['sb_xg'] = sxg
    shots['deflection'] = dfl
    shots['technique'] = tec
    shots['body_part'] = bp
    shots['shot_type'] = sty
    shots['outcome'] = out
    
    return shots

### Getting Pass Data ###
def get_pass(data):
    data = data
    import pandas as pd
    
    i = 0
    pass_data = []
    for i in range(0,len(data)):
        if("pass" in data[i]):
            pass_data.append(data[i])
        else:
            pass
    
    i = 0
    ind = []
    per = []
    m = []
    s = []
    ty = []
    ptm = []
    pat = []
    tm = []
    pl = []
    x = []
    y = []
    dur = []
    psr = []
    rec = []
    end_x =[]
    end_y = []
    crs = []
    sa = []
    ga = []
    bp = []
    pty = []
    out = []
    tec = []
    
    for i in range(len(pass_data)):
        if "index" in pass_data[i]:
            ind.append(pass_data[i]['index'])
        else:
            ind.append(0)
    
        if "period" in pass_data[i]:
            per.append(pass_data[i]['period'])
        else:
            per.append(None)
        
        if "minute" in pass_data[i]:
            m.append(pass_data[i]['minute'])
        else:
            m.append(None)
            
        if "second" in pass_data[i]:
            s.append(pass_data[i]['second'])
        else:
            s.append(None)
            
        if "type" in pass_data[i]:
            ty.append(pass_data[i]['type']['name'])
        else:
            ty.append(None)
            
        if "possession_team" in pass_data[i]:
            ptm.append(pass_data[i]['possession_team']['name'])
        else:
            ptm.append(None)
            
        if "play_pattern" in pass_data[i]:
            pat.append(pass_data[i]['play_pattern']['name'])
        else:
            pat.append(None)
            
        if "team" in pass_data[i]:
            tm.append(pass_data[i]['team']['name'])
        else:
            tm.append(None)
            
        if "player" in pass_data[i]:
            pl.append(pass_data[i]['player']['name'])
        else:
            pl.append(None)
            
        if "location" in pass_data[i]:
            x.append(pass_data[i]['location'][0])
            y.append(pass_data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)
            
        if "duration" in pass_data[i]:
            dur.append(pass_data[i]['duration'])
        else:
            dur.append(None)
            
        if "under_pressure" in pass_data[i]:
            psr.append(pass_data[i]['under_pressure'])
        else:
            psr.append(None)
            
        if "recipient" in pass_data[i]['pass']:
            rec.append(pass_data[i]['pass']['recipient']['name'])
        else:
            rec.append(None)
            
        if "end_location" in pass_data[i]['pass']:
            end_x.append(pass_data[i]['pass']['end_location'][0])
            end_y.append(pass_data[i]['pass']['end_location'][1])
        else:
            end_x.append(None)
            end_y.append(None)
        
        if "cross" in pass_data[i]['pass']:
            crs.append(pass_data[i]['pass']['cross'])
        else:
            crs.append(False)
        
        if "shot_assist" in pass_data[i]['pass']:
            sa.append(pass_data[i]['pass']['shot_assist'])
        else:
            sa.append(None)
            
        if "goal_assist" in pass_data[i]['pass']:
            ga.append(pass_data[i]['pass']['goal_assist'])
        else:
            ga.append(None)
            
        if "body_part" in pass_data[i]['pass']:
            bp.append(pass_data[i]['pass']['body_part']['name'])
        else:
            bp.append(None)
            
        if "type" in pass_data[i]['pass']:
            pty.append(pass_data[i]['pass']['type']['name'])
        else:
            pty.append('Standard')
            
        if "outcome" in pass_data[i]['pass']:
            out.append(pass_data[i]['pass']['outcome']['name'])
        else:
            out.append('Complete')
            
        if "technique" in pass_data[i]['pass']:
            tec.append(pass_data[i]['pass']['technique']['name'])
        else:
            tec.append(None)
    
    passes = pd.DataFrame()
    passes['index'] = ind
    passes['period'] = per
    passes['minute'] = m
    passes['second'] = s
    passes['type'] = ty
    passes['pos_team'] = ptm
    passes['play_pattern'] = pat
    passes['team'] = tm
    passes['player'] = pl
    passes['x'] = x
    passes['y'] = y
    passes['duration'] = dur
    passes['under_pressure'] = psr
    passes['recipient'] = rec
    passes['end_x'] = end_x
    passes['end_y'] = end_y
    passes['cross'] = crs
    passes['shot_assist'] = sa
    passes['goal_assist'] = ga
    passes['body_part'] = bp
    passes['pass_type'] = pty
    passes['outcome'] = out
    passes['technique'] = tec
    
    return passes


### Pitch drawing function ###
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
            fig,ax = plt.subplots(figsize=(8,12))
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
        
        plt.plot(lx1,ly1,color=line_col,zorder=5)
        
        # boxes, 6 yard box and goals
        
        #outer boxes#
        lx2 = [120,102,102,120]
        ly2 = [18,18,62,62] 
        plt.plot(lx2,ly2,color=line_col,zorder=5)
        
        lx3 = [0,18,18,0]
        ly3 = [18,18,62,62] 
        plt.plot(lx3,ly3,color=line_col,zorder=5)
        
        #goals#
        lx4 = [120,120.2,120.2,120]
        ly4 = [36,36,44,44]
        plt.plot(lx4,ly4,color=line_col,zorder=5)
        
        lx5 = [0,-0.4,-0.4,0]
        ly5 = [36,36,44,44]
        plt.plot(lx5,ly5,color=line_col,zorder=5)
        
        #6 yard boxes#
        lx6 = [120,114,114,120]
        ly6 = [30,30,50,50]
        plt.plot(lx6,ly6,color=line_col,zorder=5)
        
        lx7 = [0,6,6,0]
        ly7 = [30,30,50,50]
        plt.plot(lx7,ly7,color=line_col,zorder=5)
        
        #Halfway line, penalty spots, and kickoff spot
        lx8 = [60,60]
        ly8 = [0,80]
        plt.plot(lx8,ly8,color=line_col,zorder=5)
        
        plt.scatter(108,40,color=line_col,zorder=5) # pen right
        plt.scatter(12,40,color=line_col,zorder=5) # pen left
        plt.scatter(60,40,color=line_col,zorder=5) # kickoff
        
        #Circles
        centreCircle = plt.Circle((60,40),10,lw=1.5,color=line_col,fill=False,zorder=1,alpha=1)
            
        #Arcs
        rightArc = Arc((108,40),height=20,width=20,angle=0,theta1=127,theta2=233,color="black",lw=1.5)
        leftArc = Arc((12,40),height=20,width=20,angle=0,theta1=307,theta2=53,color="black",lw=1.5)
        
        ax.add_patch(centreCircle)
        ax.add_patch(rightArc)
        ax.add_patch(leftArc)
        
    else:
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(12,8))
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
        
        plt.plot(lx1,ly1,color=line_col,zorder=5)
        
        # boxes, 6 yard box and goals
        
        #outer boxes#
        lx2 = [18,18,62,62]
        ly2 = [120,102,102,120] 
        plt.plot(lx2,ly2,color=line_col,zorder=5)
        
        lx3 = [18,18,62,62]
        ly3 = [0,18,18,0] 
        plt.plot(lx3,ly3,color=line_col,zorder=5)
        
        #goals#
        ly4 = [120,120.2,120.2,120]
        lx4 = [36,36,44,44]
        plt.plot(lx4,ly4,color=line_col,zorder=5)
        
        ly5 = [0,-0.2,-0.2,0]
        lx5 = [36,36,44,44]
        plt.plot(lx5,ly5,color=line_col,zorder=5)
        
        #6 yard boxes#
        ly6 = [120,114,114,120]
        lx6 = [30,30,50,50]
        plt.plot(lx6,ly6,color=line_col,zorder=5)
        
        ly7 = [0,6,6,0]
        lx7 = [30,30,50,50]
        plt.plot(lx7,ly7,color=line_col,zorder=5)
        
        #Halfway line, penalty spots, and kickoff spot
        ly8 = [60,60]
        lx8 = [0,80]
        plt.plot(lx8,ly8,color=line_col,zorder=5)
        
        plt.scatter(40,108,color=line_col,zorder=5) # pen right
        plt.scatter(40,12,color=line_col,zorder=5) # pen left
        plt.scatter(40,60,color=line_col,zorder=5) # kickoff
        
        #Circles
        centreCircle = plt.Circle((40,60),10,lw=1.5,color=line_col,fill=False,zorder=1,alpha=1)
            
        #Arcs
        rightArc = Arc((40,108),height=20,width=20,angle=90,theta1=127,theta2=233,color="black",lw=1.5)
        leftArc = Arc((40,12),height=20,width=20,angle=90,theta1=307,theta2=53,color="black",lw=1.5)
        
        ax.add_patch(centreCircle)
        ax.add_patch(rightArc)
        ax.add_patch(leftArc)
        
    return fig,ax


#### Function for rescaling colourbars in xG plots ####
# The values of the points that we will xfrm
def xg_colourbar(xg_vals,colourmap):
    import numpy as np
    import matplotlib
    
    levels = np.concatenate((
        np.linspace(0, 0.1, 5)[:-1],
        np.linspace(0.1, 0.2, 3),
        np.linspace(0.2, 0.8, 6)[1:]
        ))
    levels.sort()

    # Making levels into an array
    levels_array = np.asarray(levels, dtype='float64')

    # Making the linear xfrm array
    xfrm_levels = np.linspace(0.0, max(levels_array),len(levels_array))

    # Defining the colour map of choice. This takes values between 0.0 and 1.0
    cmap = matplotlib.cm.get_cmap(colourmap)

    # Make a list of colours from the colour map. The value passed to the colour map is from an 
    # interpolation where levels_array is x and xfrm_levels is y and this value is normalised by
    # the max such that 0.0<i<1.0 .
    cmap_nonlin = cmap([np.interp(i, levels_array, xfrm_levels) for i in xg_vals] / max(levels_array))
    
    return cmap, cmap_nonlin, levels, xfrm_levels


def xg_size(xg_vals):
    import numpy as np
    import matplotlib
    
    levels = np.concatenate((
        np.linspace(0, 0.1, 5)[:-1],
        np.linspace(0.1, 0.2, 3),
        np.linspace(0.2, 0.8, 6)[1:]
        ))
    levels.sort()

    # Making levels into an array
    levels_array = np.asarray(levels, dtype='float64')

    # Making the linear xfrm array
    xfrm_levels = np.linspace(0.0, max(levels_array),len(levels_array))

    # Calculate the new sizes using interpolation between levels and xfrm_levels
    sizes = [np.interp(i, levels_array, xfrm_levels) for i in xg_vals] / max(levels_array)
    
    return sizes


def shot_map_team(data,team,pitch_col,line_col,xg_display,colourmap):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    
    data = data
    team = team
    pitch_col = pitch_col
    line_col = line_col
    
    shots = get_shots(data)
    
    teams = shots.team.unique()
    
    if team == teams[0]:
        opposition = teams[1]
    else:
        opposition = teams[0]
        
    fig, ax = draw_pitch(pitch_col,line_col,'v','h')
        
    # Shot data
    tshots = shots[shots['team'] == team]
    tshots_h = tshots[(tshots['body_part'] == 'Head')]
    tshots_f = tshots[((tshots['body_part'] == 'Left Foot')|(tshots['body_part'] == 'Right Foot'))&(tshots['shot_type'] != 'Penalty')&(tshots['shot_type'] != 'Free Kick')]
    tshots_pfk = tshots[(tshots['shot_type'] == 'Penalty')|(tshots['shot_type'] == 'Free Kick')]
    tshots_p = tshots[(tshots['shot_type'] == 'Penalty')]
    
    tshots_h_g = tshots_h[tshots_h['outcome'] == 'Goal']
    tshots_f_g = tshots_f[tshots_f['outcome'] == 'Goal']
    tshots_pfk_g = tshots_pfk[tshots_pfk['outcome'] == 'Goal']
    
    xh = tshots_h['x']
    yh = tshots_h['y']
    
    xf = tshots_f['x']
    yf = tshots_f['y']
    
    xpfk = tshots_pfk['x']
    ypfk = tshots_pfk['y']
    
    xh_g = tshots_h_g['x']
    yh_g = tshots_h_g['y']
    
    xf_g = tshots_f_g['x']
    yf_g = tshots_f_g['y']
    
    xpfk_g = tshots_pfk_g['x']
    ypfk_g = tshots_pfk_g['y']
    
    h_xG = tshots_h.sb_xg.values
    f_xG = tshots_f.sb_xg.values
    pfk_xG = tshots_pfk.sb_xg.values
    
    h_g_xG = tshots_h_g.sb_xg.values
    f_g_xG = tshots_f_g.sb_xg.values
    pfk_g_xG = tshots_pfk_g.sb_xg.values
    
    if xg_display.lower().startswith("s"):
        
        size_f = xg_size(f_xG)
        size_h = xg_size(h_xG)
        size_pfk = xg_size(pfk_xG)
        
        size_f_g = xg_size(f_g_xG)
        size_h_g = xg_size(h_g_xG)
        size_pfk_g = xg_size(pfk_g_xG)
    
        # Plot legend
        ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Foot',alpha=0.6)
        ax.scatter(-100,-100,marker='o',c='w',edgecolors='black',s=200,label='Head',alpha=0.6)
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='Penalty/FK',alpha=0.6)
        ax.legend(bbox_to_anchor=(0.99, 0.01),ncol=3,fontsize=14,loc=4,shadow=True)

        # Plotting shots
        ax.scatter(yf, xf, s=size_f*1000, marker='H', c="red", edgecolors="black",zorder=100,alpha=0.9)
        ax.scatter(yh, xh, s=size_h*1000, marker='o', c="red", edgecolors="black",zorder=100,alpha=0.9)
        ax.scatter(ypfk,xpfk,s=size_pfk*1000,marker='s',c='red',edgecolors='black',zorder=100,alpha=0.9)
        
        # Plotting goals
        ax.scatter(yf_g, xf_g, s=size_f_g*1000, marker='H', c="r", edgecolors="black",zorder=101,alpha=0.9,lw=5)
        ax.scatter(yh_g, xh_g, s=size_h_g*1000, marker='o', c="r", edgecolors="black",zorder=101,alpha=0.9)
        ax.scatter(ypfk_g,xpfk_g,s=size_pfk_g*1000,marker='s',c='r',edgecolors='black',zorder=101,alpha=0.9)

        #plt.title(r"$\bf{" + str(team) + "}$" + "\n vs " + str(opposition) + "\n Total " + str(round(sum(tshots.sb_xg),2)) + "xG" ,fontsize=18)
        ax.text(0.0, 1.03, team, ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')
        ax.text(0.0, 1.0, 'vs ' + str(opposition), ha='left', va='bottom', transform=ax.transAxes, fontsize=13)
        if len(tshots_p) > 0:
            ax.text(1.0, 1.03, str(round(sum(tshots.sb_xg)-sum(tshots_p.sb_xg),2)) + ' xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
            ax.text(1.0, 1.0, '(+' + str(len(tshots_p)) + ' Pen)', ha='right', va='bottom', transform=ax.transAxes, fontsize=13)
        else:
            ax.text(1.0, 1.0, str(round(sum(tshots.sb_xg),2)) + 'xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')            

        plt.show()
           
    else:
        ## Colour representing xG
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        
        zo=10
        i = 0
        cmap, cmap_nonlin_f, levels, xfrm_levels = xg_colourbar(f_xG,colourmap)
        cmap_nonlin_h = xg_colourbar(h_xG,colourmap)[1]
        cmap_nonlin_pfk = xg_colourbar(pfk_xG,colourmap)[1]
        
        # Plot legend
        ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Foot',alpha=0.6)
        ax.scatter(-100,-100,marker='o',c='w',edgecolors='black',s=200,label='Head',alpha=0.6)
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='Penalty/FK',alpha=0.6)
        ax.legend(bbox_to_anchor=(0.99, 0.01),ncol=3,fontsize=14,loc=4,shadow=True)
        
        # Plot shots
        ax.scatter(yf,xf,zorder=zo+1,s=200,marker='H',color=cmap_nonlin_f,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(yh,xh,zorder=zo+1,s=200,marker='o',color=cmap_nonlin_h,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(ypfk,xpfk,zorder=zo+1,s=200,marker='s',color=cmap_nonlin_pfk,edgecolors='black',lw=1,alpha=0.8)

        #cax, _ = matplotlib.colorbar.make_axes(ax,orientation='horizontal')
        #cax = inset_axes(ax, width="60%", height="5%", bbox_to_anchor=(150,-50,500,500)) # Allows one to place cb in current axis
        #cax = inset_axes(ax, width="60%", height="5%", loc=8) # Allows one to place cb in current axis without specifying coords
        cax = fig.add_axes([0.55, 0.23, 0.3, 0.04]) # Can just add_axes but then must place manually
        cax.set_title('xG',fontsize=14)
        cax.tick_params(labelsize=12)
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range, orientation="horizontal")
        #cbar.set_ticks(xfrm_levels)
        #cbar.set_ticklabels(["%.2f" % lev for lev in levels])
        cbar.set_ticks([xfrm_levels[i] for i in [0,4,6,-1]])
        cbar.set_ticklabels(["%.2f" % levels[i] for i in [0,4,6,-1]])
        
        ax.text(0.0, 1.03, team, ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')
        ax.text(0.0, 1.0, 'vs ' + str(opposition), ha='left', va='bottom', transform=ax.transAxes, fontsize=13)
        if len(tshots_p) > 0:
            ax.text(1.0, 1.03, str(round(sum(tshots.sb_xg)-sum(tshots_p.sb_xg),2)) + ' xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
            ax.text(1.0, 1.0, '(+' + str(len(tshots_p)) + ' Pen)', ha='right', va='bottom', transform=ax.transAxes, fontsize=13)
        else:
            ax.text(1.0, 1.0, str(round(sum(tshots.sb_xg),2)) + 'xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')

        plt.show()        
        


def shot_map_player(data,player,pitch_col,line_col,xg_display,colourmap):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe
    import matplotlib
    
    data = data
    player = player
    pitch_col = pitch_col
    line_col = line_col
    
    #shots = pd.concat(data,ignore_index=True)
    shots = get_shots(data)
    shots.sort_values('sb_xg',ascending=True,inplace=True) #Sort into xG value ascending order
    
    #shots = data
       
    fig, ax = draw_pitch(pitch_col,line_col,'v','h')
        
    # Shot data
    pshots = shots[shots['player'] == player]
    pshots_h = pshots[(pshots['body_part'] == 'Head')]
    pshots_f = pshots[(pshots['body_part'] == 'Left Foot')|(pshots['body_part'] == 'Right Foot')]
    pshots_h_g = pshots_h[pshots_h['outcome'] == 'Goal']
    pshots_f_g = pshots_f[pshots_f['outcome'] == 'Goal']
    
    xh = pshots_h['x'].values
    yh = pshots_h['y'].values
    
    xf = pshots_f['x'].values
    yf = pshots_f['y'].values
    
    xh_g = pshots_h_g['x'].values
    yh_g = pshots_h_g['y'].values
    
    xf_g = pshots_f_g['x'].values
    yf_g = pshots_f_g['y'].values
    
    h_xG = pshots_h.sb_xg.values
    f_xG = pshots_f.sb_xg.values
    h_g_xG = pshots_h_g.sb_xg.values
    f_g_xG = pshots_f_g.sb_xg.values
    
    if xg_display.lower().startswith("s"):
        ## Size representing xG
        # Plot legend
        ax.scatter(-100,-100,marker='o',c='grey',edgecolors='black',s=200,label='Head',alpha=0.6)
        ax.scatter(-100,-100,marker='s',c='grey',edgecolors='black',s=200,label='Foot',alpha=0.6)
        ax.legend(bbox_to_anchor=(0.70, 0.001),ncol=3,fontsize=14)
        
        # Plotting shots
        plt.scatter(yh, xh, s=h_xG*1000, marker='o', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf, xf, s=f_xG*1000, marker='s', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yh_g, xh_g, s=h_g_xG*1000, marker='o', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf_g, xf_g, s=f_g_xG*1000, marker='s', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        
        plt.title(str(player) + "\n" + str((len(pshots_h_g) + len(pshots_f_g))) + " Goals with Total "+str(round(sum(pshots.sb_xg),2))+"xG in " + str(len(data)) + " games",fontsize=18)
        #plt.title(r'$\bf{{{0}}}$'.format(str(team)))
        plt.show()
    
    else:
        ## Colour representing xG
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        
        zo=10
        i = 0
        cmap, cmap_nonlin, levels, xfrm_levels = xg_colourbar(f_xG,colourmap)
        ax.scatter(yf, xf,zorder=zo+1,s=200,marker='s',color=cmap_nonlin,edgecolors='black',lw=1,alpha=0.8)

        cax, _ = matplotlib.colorbar.make_axes(ax)
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range)
        cbar.set_ticks(xfrm_levels)
        cbar.set_ticklabels(["%.2f" % lev for lev in levels])

        plt.show()
    

    
def shot_map_player_old(data,player,pitch_col,line_col,xg_display):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe
    import matplotlib
    
    data = data
    player = player
    pitch_col = pitch_col
    line_col = line_col
    
    #shots = pd.concat(data,ignore_index=True)
    shots = get_shots(data)
    shots.sort_values('sb_xg',ascending=True,inplace=True) #Sort into xG value ascending order
    
    #shots = data
       
    fig, ax = draw_pitch(pitch_col,line_col,'v','h')
        
    # Shot data
    pshots = shots[shots['player'] == player]
    pshots_h = pshots[(pshots['body_part'] == 'Head')]
    pshots_f = pshots[(pshots['body_part'] == 'Left Foot')|(pshots['body_part'] == 'Right Foot')]
    pshots_h_g = pshots_h[pshots_h['outcome'] == 'Goal']
    pshots_f_g = pshots_f[pshots_f['outcome'] == 'Goal']
    
    xh = pshots_h['x'].values
    yh = pshots_h['y'].values
    
    xf = pshots_f['x'].values
    yf = pshots_f['y'].values
    
    xh_g = pshots_h_g['x'].values
    yh_g = pshots_h_g['y'].values
    
    xf_g = pshots_f_g['x'].values
    yf_g = pshots_f_g['y'].values
    
    xh_xG = pshots_h.sb_xg.values
    xf_xG = pshots_f.sb_xg.values
    xh_g_xG = pshots_h_g.sb_xg.values
    xf_g_xG = pshots_f_g.sb_xg.values
    
    if xg_display.lower().startswith("s"):
        ## Size representing xG
        # Plot legend
        ax.scatter(-100,-100,marker='o',c='grey',edgecolors='black',s=200,label='Head',alpha=0.6)
        ax.scatter(-100,-100,marker='s',c='grey',edgecolors='black',s=200,label='Foot',alpha=0.6)
        ax.legend(bbox_to_anchor=(0.70, 0.001),ncol=3,fontsize=14)
        
        # Plotting shots
        plt.scatter(yh, xh, s=xh_xG*1000, marker='o', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf, xf, s=xf_xG*1000, marker='s', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yh_g, xh_g, s=xh_g_xG*1000, marker='o', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf_g, xf_g, s=xf_g_xG*1000, marker='s', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        
        plt.title(str(player) + "\n" + str((len(pshots_h_g) + len(pshots_f_g))) + " Goals with Total "+str(round(sum(pshots.sb_xg),2))+"xG in " + str(len(data)) + " games",fontsize=18)
        #plt.title(r'$\bf{{{0}}}$'.format(str(team)))
        plt.show()
    
    else:
        ## Colour representing xG
        #cmap = matplotlib.cm.get_cmap('plasma')
        cmap = matplotlib.cm.get_cmap('jet')
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        c_vals_h = [cmap(norm_range(value)) for value in xh_xG]
        c_vals_f = [cmap(norm_range(value)) for value in xf_xG]
        c_vals_f_g = [cmap(norm_range(value)) for value in xf_g_xG]
        
        zo=10
        i = 0
        for i in range(len(pshots_f)):
            plt.scatter(yf[i], xf[i],zorder=i+zo+1,s=200,marker='s',color=c_vals_f[i],edgecolors='black',lw=1,alpha=0.3)
            #plot = plt.scatter(yf[i], xf[i],zorder=0,color=c_vals_f[i])
            plot = plt.scatter(yf[i], xf[i],zorder=0,s=0,c=xf_xG[i], vmin=0, vmax=0.8, cmap=cmap)
        for i in range(len(pshots_f_g)):
            plt.scatter(yf_g[i], xf_g[i],zorder=i+zo+500,s=200,marker='s',color=c_vals_f_g[i],edgecolors='black',lw=1)
            
#        cax, _ = matplotlib.colorbar.make_axes(ax)
#        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range)
        cbar = fig.colorbar(plot)

        plt.show()
        
    return pshots_f, pshots_f_g, xf, yf, xf_g, yf_g, xh_xG, xf_xG, xf_g_xG
    

def shot_map_player_older(data,player,pitch_col,line_col,xg_display):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe
    import matplotlib
    
    data = data
    player = player
    pitch_col = pitch_col
    line_col = line_col
    
    shots = pd.concat(data,ignore_index=True)
    shots.sort_values('sb_xg',ascending=True,inplace=True) #Sort into xG value ascending order
    
    #shots = data
       
    fig,ax = plt.subplots(figsize=(10.4,6.8))
    plt.ylim(50,105)
    plt.xlim(-1,69)
    ax.axis('off')    
    
    ### Plotting pitch ###
    ## TOP ##
    # Sidelines
    lx1 = [0,0,68,68,0]
    ly1 = [0,104,104,0,0]
    # Outer box
    lx2 = [13.84,13.84,54.16,54.16]
    ly2 = [104,87.5,87.5,104]
    # Goal
    lx3 = [30.34,30.34,37.66,37.66]
    ly3 = [104,104.2,104.2,104]
    # 6-yard box
    lx4 = [24.84,24.84,43.16,43.16]
    ly4 = [104,99.5,99.5,104]
    #Half-way line
    lx5 = [0,68]
    ly5 = [52,52]
    ### BOTTOM ###
    # Outer box
    lx6 = [13.84,13.84,54.16,54.16]
    ly6 = [0,16.5,16.5,0]
    # Goal
    lx7 = [30.34,30.34,37.66,37.66]
    ly7 = [0,-0.2,-0.2,0]
    # 6-yard box
    lx8 = [24.84,24.84,43.16,43.16]
    ly8 = [0,4.5,4.5,0]
    # Circles
    circle1 = plt.Circle((34,93.5), 9.15, ls='solid', lw=1.5, color=line_col, fill=False, zorder=1, alpha=1)
    circle2 = plt.Circle((34,10.5), 9.15, ls='solid', lw=1.5, color=line_col, fill=False, zorder=1, alpha=1)
    circle3 = plt.Circle((34,52), 9.15, ls='solid', lw=1.5, color=line_col, fill=False, zorder=2, alpha=1)

    plt.plot(lx1,ly1,color=line_col,zorder=5)
    plt.plot(lx2,ly2,color=line_col,zorder=5)
    plt.plot(lx3,ly3,color=line_col,zorder=5)
    plt.plot(lx4,ly4,color=line_col,zorder=5)
    plt.plot(lx5,ly5,color=line_col,zorder=5)
    plt.plot(lx6,ly6,color=line_col,zorder=5)
    plt.plot(lx7,ly7,color=line_col,zorder=5)
    plt.plot(lx8,ly8,color=line_col,zorder=5)
    
    # Center and penalty spots
    plt.scatter(34,93,color=line_col,zorder=5)
    plt.scatter(34,11,color=line_col,zorder=5)
    plt.scatter(34,52,color=line_col,zorder=5)
    
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    
    ## Rectangles in boxes
    rec1 = plt.Rectangle((20,87.5), 30,16.5,ls='-',color=pitch_col, zorder=1,alpha=1)
    rec2 = plt.Rectangle((20,0), 30,16.5,ls='-',color=pitch_col, zorder=1,alpha=1)
    ## Pitch rectangle
    rec3 = plt.Rectangle((-1,-1), 70,106,color=pitch_col,zorder=0,alpha=1)
    
    ax.add_artist(rec1)
    ax.add_artist(rec2)
    ax.add_artist(rec3)
        
    # Shot data
    pshots = shots[shots['player'] == player]
    pshots_h = pshots[(pshots['body_part'] == 'Head')]
    pshots_f = pshots[(pshots['body_part'] == 'Left Foot')|(pshots['body_part'] == 'Right Foot')]
    pshots_h_g = pshots_h[pshots_h['outcome'] == 'Goal']
    pshots_f_g = pshots_f[pshots_f['outcome'] == 'Goal']
    
    xh = (pshots_h['x'].values / 120) * 104
    yh = (pshots_h['y'].values / 80) * 68
    yh = 68 - yh # Since we are plotting half the pitch vertically, y coords become the new x
    
    xf = (pshots_f['x'].values / 120) * 104
    yf = (pshots_f['y'].values / 80) * 68
    yf = 68 - yf
    
    xh_g = (pshots_h_g['x'].values / 120) * 104
    yh_g = (pshots_h_g['y'].values / 80) * 68
    yh_g = 68 - yh_g # Since we are plotting half the pitch vertically, y coords become the new x
    
    xf_g = (pshots_f_g['x'].values / 120) * 104
    yf_g = (pshots_f_g['y'].values / 80) * 68
    yf_g = 68 - yf_g
    
    xh_xG = pshots_h.sb_xg.values
    xf_xG = pshots_f.sb_xg.values
    xh_g_xG = pshots_h_g.sb_xg.values
    xf_g_xG = pshots_f_g.sb_xg.values
    
    if xg_display.lower().startswith("s"):
        ## Size representing xG
        # Plot legend
        ax.scatter(-100,-100,marker='o',c='grey',edgecolors='black',s=200,label='Head',alpha=0.6)
        ax.scatter(-100,-100,marker='s',c='grey',edgecolors='black',s=200,label='Foot',alpha=0.6)
        ax.legend(bbox_to_anchor=(0.70, 0.001),ncol=3,fontsize=14)
        
        # Plotting shots
        plt.scatter(yh, xh, s=xh_xG*1000, marker='o', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf, xf, s=xf_xG*1000, marker='s', c="grey", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yh_g, xh_g, s=xh_g_xG*1000, marker='o', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        plt.scatter(yf_g, xf_g, s=xf_g_xG*1000, marker='s', c="pink", edgecolors="black",alpha=0.6,zorder=100)
        
        plt.title(str(player) + "\n" + str((len(pshots_h_g) + len(pshots_f_g))) + " Goals with Total "+str(round(sum(pshots.sb_xg),2))+"xG in " + str(len(data)) + " games",fontsize=18)
        #plt.title(r'$\bf{{{0}}}$'.format(str(team)))
        plt.show()
    
    else:
        ## Colour representing xG
        cmap = matplotlib.cm.get_cmap('plasma')
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        c_vals_h = [cmap(norm_range(value)) for value in xh_xG]
        c_vals_f = [cmap(norm_range(value)) for value in xf_xG]
        c_vals_f_g = [cmap(norm_range(value)) for value in xf_g_xG]
        
        zo=10
        i = 0
        for i in range(len(pshots_f)):
            plt.scatter(yf[i], xf[i],zorder=i+zo+1,s=200,marker='s',color=c_vals_f[i],edgecolors='black',lw=1,alpha=0.3)
            #plot = plt.scatter(yf[i], xf[i],zorder=0,color=c_vals_f[i])
            plot = plt.scatter(yf[i], xf[i],zorder=0,c=xf_xG[i], vmin=0, vmax=0.8, cmap=cmap)
        for i in range(len(pshots_f_g)):
            plt.scatter(yf_g[i], xf_g[i],zorder=i+zo+500,s=200,marker='s',color=c_vals_f_g[i],edgecolors='black',lw=1)
            
#        cax, _ = matplotlib.colorbar.make_axes(ax)
#        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range)
        cbar = fig.colorbar(plot)

        plt.show()

    
    
def shot_map(data,home_team,away_team,home_col,away_col,pitch_col,line_col):
    import pandas as pd
    import matplotlib.pyplot as plt
    
    data = data
    home_team = home_team
    away_team = away_team
    pitch_col = pitch_col
    line_col = line_col
    
    shots = get_shots(data)
    
    fig,ax = plt.subplots(figsize=(10.4,6.8))
    plt.xlim(-1,105)
    plt.ylim(-1,69)
    ax.axis('off')
    
    ### Plotting pitch ###
    # side and goal lines #
    lx1 = [0,104,104,0,0]
    ly1 = [0,0,68,68,0]
    # boxes, 6 yard box and goals
    #outer boxes#
    lx2 = [104,87.5,87.5,104]
    ly2 = [13.84,13.84,54.16,54.16] 
    ly3 = [13.84,13.84,54.16,54.16] 
    lx3 = [0,16.5,16.5,0]
    #goals#
    lx4 = [104,104.2,104.2,104]
    ly4 = [30.34,30.34,37.66,37.66]
    lx5 = [0,-0.2,-0.2,0]
    ly5 = [30.34,30.34,37.66,37.66]
    #6 yard boxes#
    lx6 = [104,98.5,98.5,104]
    ly6 = [24.84,24.84,43.16,43.16]
    lx7 = [0,5.5,5.5,0]
    ly7 = [24.84,24.84,43.16,43.16]
    #Halfway line
    lx8 = [52,52]
    ly8 = [0,68]
    # Penalty spots and kickoff spot
    plt.scatter(93,34,color=line_col,zorder=5)
    plt.scatter(11,34,color=line_col,zorder=5)
    plt.scatter(52,34,color=line_col,zorder=5)
    #Circles
    circle1 = plt.Circle((93.5,34), 9.15,ls='solid',lw=1.5,color=line_col, fill=False, zorder=1,alpha=1)
    circle2 = plt.Circle((10.5,34), 9.15,ls='solid',lw=1.5,color=line_col, fill=False, zorder=1,alpha=1)
    circle3 = plt.Circle((52, 34), 9.15,ls='solid',lw=1.5,color=line_col, fill=False, zorder=2,alpha=1)
    # Rectangles in boxes
    rec1 = plt.Rectangle((87.5,20), 16.5,30,ls='-',color=pitch_col, zorder=1,alpha=1)
    rec2 = plt.Rectangle((0, 20), 16.5,30,ls='-',color=pitch_col, zorder=1,alpha=1) 
    # Pitch rectangle
    rec3 = plt.Rectangle((-1,-1), 106,70,color=pitch_col,zorder=0,alpha=1)

    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    ax.add_artist(rec1)
    ax.add_artist(rec2)
    ax.add_artist(rec3)
    
    plt.plot(lx1,ly1,color=line_col,zorder=5)
    plt.plot(lx2,ly2,color=line_col,zorder=5)
    plt.plot(lx3,ly3,color=line_col,zorder=5)
    plt.plot(lx4,ly4,color=line_col,zorder=5)
    plt.plot(lx5,ly5,color=line_col,zorder=5)
    plt.plot(lx6,ly6,color=line_col,zorder=5)
    plt.plot(lx7,ly7,color=line_col,zorder=5)
    plt.plot(lx8,ly8,color=line_col,zorder=5)
    
    ### Shot data ###
    hshots = shots[shots['team'] == home_team]
    ashots = shots[shots['team'] == away_team]
    # Sorting into head and foot
    hshots_h = hshots[hshots['body_part'] == 'Head']
    hshots_f = hshots[(hshots['body_part'] == 'Left Foot')|(hshots['body_part'] == 'Right Foot')]
    ashots_h = ashots[ashots['body_part'] == 'Head']
    ashots_f = ashots[(ashots['body_part'] == 'Left Foot')|(ashots['body_part'] == 'Right Foot')]
    hshots_h_g = hshots_h[hshots_h['outcome'] == 'Goal']
    hshots_f_g = hshots_f[hshots_f['outcome'] == 'Goal']
    ashots_h_g = ashots_h[ashots_h['outcome'] == 'Goal']
    ashots_f_g = ashots_f[ashots_f['outcome'] == 'Goal']
    
    # Recaling x and y data into metres
    xh_h = ((120 - hshots_h.x) / 120) * 104 # Take away from 120 so these points will be on left side of pitch
    yh_h = ((80 - hshots_h.y) / 80) * 68
    xh_f = ((120 - hshots_f.x) / 120) * 104
    yh_f = ((80 - hshots_f.y) / 80) * 68
    
    xa_h = (ashots_h.x / 120) * 104
    ya_h = (ashots_h.y / 80) * 68
    xa_f = (ashots_f.x / 120) * 104
    ya_f = (ashots_f.y / 80) * 68
    
    xh_h_g = ((120 - hshots_h_g.x) / 120) * 104 # Take away from 120 so these points will be on left side of pitch
    yh_h_g = ((80 - hshots_h_g.y) / 80) * 68
    xh_f_g = ((120 - hshots_f_g.x) / 120) * 104
    yh_f_g = ((80 - hshots_f_g.y) / 80) * 68
    
    xa_h_g = (ashots_h_g.x / 120) * 104
    ya_h_g = (ashots_h_g.y / 80) * 68
    xa_f_g = (ashots_f_g.x / 120) * 104
    ya_f_g = (ashots_f_g.y / 80) * 68
    
    hshots_xG = hshots.sb_xg.values
    ashots_xG = ashots.sb_xg.values
    hshots_h_xG = hshots_h.sb_xg.values
    hshots_f_xG = hshots_f.sb_xg.values
    ashots_h_xG = ashots_h.sb_xg.values
    ashots_f_xG = ashots_f.sb_xg.values
    hshots_h_g_xG = hshots_h_g.sb_xg.values
    hshots_f_g_xG = hshots_f_g.sb_xg.values
    ashots_h_g_xG = ashots_h_g.sb_xg.values
    ashots_f_g_xG = ashots_f_g.sb_xg.values
    
    # Plot legend
    ax.scatter(-100,-100,marker='o',c='grey',edgecolors='black',s=200,label='Head',alpha=0.6)
    ax.scatter(-100,-100,marker='s',c='grey',edgecolors='black',s=200,label='Foot',alpha=0.6)
    ax.legend(bbox_to_anchor=(0.70, 0.001),ncol=3,fontsize=14)
    
    # Plotting shots
    # Home shots
    plt.scatter(xh_h, yh_h, s=hshots_h_xG*1000, marker='o', c=home_col, edgecolors="black",zorder=100)
    plt.scatter(xh_f, yh_f, s=hshots_f_xG*1000, marker='s', c=home_col, edgecolors="black",zorder=100)
    # Away shots
    plt.scatter(xa_h, ya_h, s=ashots_h_xG*1000, marker='o', c=away_col, edgecolors="black",zorder=100)
    plt.scatter(xa_f, ya_f, s=ashots_f_xG*1000, marker='s', c=away_col, edgecolors="black",zorder=100)
    # Home goals
    plt.scatter(xh_h_g, yh_h_g, s=ashots_h_g_xG*1000, marker='o', c='Pink', edgecolors="black",zorder=100)
    plt.scatter(xh_f_g, yh_f_g, s=ashots_f_g_xG*1000, marker='s', c='Pink', edgecolors="black",zorder=100)
    # Away goals
    plt.scatter(xa_h_g, ya_h_g, s=ashots_h_g_xG*1000, marker='o', c='Pink', edgecolors="black",zorder=100)
    plt.scatter(xa_f_g, ya_f_g, s=ashots_f_g_xG*1000, marker='s', c='Pink', edgecolors="black",zorder=100)

    plt.title(str(home_team) + " vs " + str(away_team) + "\n xG sum " + str(round(sum(hshots.sb_xg),2)) + ' - ' + str(round(sum(ashots_xG),2)),fontsize=18)
    #plt.title(r'$\bf{{{0}}}$'.format(str(team)))
    plt.show()
    
    