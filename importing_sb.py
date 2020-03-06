
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
    eid = []
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
            
        if "id" in data[i]:
            eid.append(data[i]['id'])
        else:
            eid.append(0)
        
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
            
        elif "dribble" in data[i]:
            if "outcome" in data[i]['dribble']:
                out.append(data[i]['dribble']['outcome']['name'])
            elif "outcome" not in data[i]['dribble']:
                out.append(None)
            end_x.append(None)
            end_y.append(None)
            

        else:
            end_x.append(None)
            end_y.append(None)
            out.append(None)
    
    match_events = pd.DataFrame()
    match_events['m_index'] = ind
    match_events['event_id'] = eid
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


def get_player_info(data,player):
    data = data
    player = player
    import pandas as pd
    i = 0
    
    for i in range(0,len(data)):
        if "type" in data[i]:
            if 'Starting XI' in data[i]['type']['name']:
                for j in data[i]['tactics']['lineup']:
                    if player in j['player']['name']:
                        start = 'Yes'
                        pos = j['position']['name']
                        num = j['jersey_number']
                        min_start = 0
                        sec_start = 0
                    else:
                        pass
            
            if 'Substitution' in data[i]['type']['name']:
                if player == data[i]['player']['name']:
                    sub_off = 'Yes'
                    min_end = data[i]['minute']
                    sec_end = data[i]['second']
                else:
                    pass
                
                if player == data[i]['substitution']['replacement']['name']:
                    sub_on = 'Yes'
                    min_start = data[i]['minute']
                    sec_start = data[i]['second']
                else:
                    pass
        else:
            pass

    if 'start' not in locals():
        start = 'No'
        pos = None
        num = None

    if 'sub_on' not in locals():
        sub_on = 'No'
    
    if 'sub_off' not in locals():
        sub_off = 'No'
    
    if 'min_end' not in locals():
        min_end = data[-1]['minute']
        sec_end = data[-1]['second']
        
    player_info = pd.Series(name=player)
    player_info['position'] = pos
    player_info['number'] = num
    player_info['start'] = start
    player_info['sub_off'] = sub_off
    player_info['sub_on'] = sub_on
    
    # Added if incase player doesn't play
    if 'min_start' in locals():
        player_info['min_start'] = min_start
        player_info['sec_start'] = sec_start
        player_info['min_end'] = min_end
        player_info['sec_end'] = sec_end
        player_info['sec_played'] = ((min_end * 60) + sec_end) - ((min_start * 60) + sec_start)
    else:
        player_info['min_start'] = None
        player_info['sec_start'] = None
        player_info['min_end'] = None
        player_info['sec_end'] = None
        player_info['sec_played'] = None        
        
    return player_info


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
    eid = []
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
    drib = []
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
            
        if "id" in shot_data[i]:
            eid.append(shot_data[i]['id'])
        else:
            eid.append(0)
    
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
        
        if "follows_dribble" in shot_data[i]['shot']:
            drib.append(shot_data[i]['shot']['follows_dribble'])
        else:
            drib.append(False)
        
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
    shots['event_id'] = eid
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
    shots['follows_dribble'] = drib
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
    shots = get_shots(data)
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
    eid = []
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
    cut = []
    swi = []
    sa = []
    ga = []
    xA = []
    bp = []
    pty = []
    out = []
    tec = []
    
    for i in range(len(pass_data)):
        if "index" in pass_data[i]:
            ind.append(pass_data[i]['index'])
        else:
            ind.append(0)
            
        if "id" in pass_data[i]:
            eid.append(pass_data[i]['id'])
        else:
            eid.append(0)
    
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
            
        if "cut-back" in pass_data[i]['pass']:
            cut.append(pass_data[i]['pass']['cut-back'])
        else:
            cut.append(False)
            
        if "switch" in pass_data[i]['pass']:
            swi.append(pass_data[i]['pass']['switch'])
        else:
            swi.append(False)
        
        if "shot_assist" in pass_data[i]['pass']:
            sa.append(pass_data[i]['pass']['shot_assist'])
            ga.append(None)
            sa_id = pass_data[i]['pass']['assisted_shot_id']
            xA.append(shots[shots['event_id'] == sa_id]['sb_xg'].values[0])
        elif "goal_assist" in pass_data[i]['pass']:
            ga.append(pass_data[i]['pass']['goal_assist'])
            sa.append(None)
            ga_id = pass_data[i]['pass']['assisted_shot_id']
            xA.append(shots[shots['event_id'] == ga_id]['sb_xg'].values[0])
        else:
            sa.append(None)
            ga.append(None)
            xA.append(None)
            
#         if "goal_assist" in pass_data[i]['pass']:
#             ga.append(pass_data[i]['pass']['goal_assist'])
#         else:
#             ga.append(None)
            
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
    passes['event_id'] = eid
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
    passes['cutback'] = crs
    passes['switch'] = swi
    passes['shot_assist'] = sa
    passes['goal_assist'] = ga
    passes['xA'] = xA
    passes['body_part'] = bp
    passes['pass_type'] = pty
    passes['outcome'] = out
    passes['technique'] = tec
    
    return passes

### Get Carries ###
def get_carry(data):
    data = data
    import pandas as pd
    import numpy as np
    
    i = 0
    carry_data = []
    for i in range(0,len(data)):
        if("carry" in data[i]):
            carry_data.append(data[i])
        else:
            pass
    
    i = 0
    ind = []
    eid = []
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
    end_x = []
    end_y = []
    rev = []
    
    for i in range(len(carry_data)):
        if "index" in carry_data[i]:
            ind.append(carry_data[i]['index'])
        else:
            ind.append(0)
            
        if "id" in data[i]:
            eid.append(carry_data[i]['id'])
        else:
            eid.append(0)
    
        if "period" in carry_data[i]:
            per.append(carry_data[i]['period'])
        else:
            per.append(None)
        
        if "minute" in carry_data[i]:
            m.append(carry_data[i]['minute'])
        else:
            m.append(None)
            
        if "second" in carry_data[i]:
            s.append(carry_data[i]['second'])
        else:
            s.append(None)
            
        if "type" in carry_data[i]:
            ty.append(carry_data[i]['type']['name'])
        else:
            ty.append(None)
            
        if "possession_team" in carry_data[i]:
            ptm.append(carry_data[i]['possession_team']['name'])
        else:
            ptm.append(None)
            
        if "play_pattern" in carry_data[i]:
            pat.append(carry_data[i]['play_pattern']['name'])
        else:
            pat.append(None)
            
        if "team" in carry_data[i]:
            tm.append(carry_data[i]['team']['name'])
        else:
            tm.append(None)
            
        if "player" in carry_data[i]:
            pl.append(carry_data[i]['player']['name'])
        else:
            pl.append(None)
            
        if "location" in carry_data[i]:
            x.append(carry_data[i]['location'][0])
            y.append(carry_data[i]['location'][1])
        else:
            x.append(None)
            y.append(None)
            
        if "duration" in carry_data[i]:
            dur.append(carry_data[i]['duration'])
        else:
            dur.append(None)
            
        if "under_pressure" in carry_data[i]:
            psr.append(carry_data[i]['under_pressure'])
        else:
            psr.append(None)
            
        if "end_location" in carry_data[i]['carry']:
            end_x.append(carry_data[i]['carry']['end_location'][0])
            end_y.append(carry_data[i]['carry']['end_location'][1])
        else:
            end_x.append(None)
            end_y.append(None)
            
        if "related_events" in carry_data[i]:
            rev.append(carry_data[i]['related_events'])
        else:
            rev.append(0)
            
    carries = pd.DataFrame()
    carries['index'] = ind
    carries['event_id'] = eid
    carries['period'] = per
    carries['minute'] = m
    carries['second'] = s
    carries['type'] = ty
    carries['pos_team'] = ptm
    carries['play_pattern'] = pat
    carries['team'] = tm
    carries['player'] = pl
    carries['x'] = x
    carries['y'] = y
    carries['duration'] = dur
    carries['under_pressure'] = psr
    carries['end_x'] = end_x
    carries['end_y'] = end_y
    carries['carry_dist'] = np.sqrt((np.array(end_x) - np.array(x)) ** 2 + (np.array(end_y) - np.array(y)) **2)
    carries['related_events'] = rev
        
    return carries


def get_carry_prog(data, find_success=False, player=None, team=None):
    import numpy as np
    import pandas as pd
    
    carries = get_carry(data)
    
    xg = 120
    yg = 40
    
    d = np.sqrt((120 - carries['x']) ** 2 + (40 - carries['y']) ** 2)
    de = np.sqrt((120 - carries['end_x']) ** 2 + (40 - carries['end_y']) ** 2)
    prog = ((d - de) * 0.914 >= 5.0).values
    
    car_prog = carries[prog&(carries['end_x'] >= 60)]
    
    if player != None:
        car = car_prog[car_prog['player'] == player]
    elif team != None:
        car = car_prog[car_prog['team'] == team]
    else:
        car = car_prog
        
    if find_success == True:
        event_df = clean_event_data(data)
        passes = get_pass(data)
        shots = get_shots(data)
        
        df_index = []
        car_outcome = []
        pass_outcome = []
        shot_outcome = []
        drib_outcome = []
        xG = []
        xA = []
        outcome_id = []
        for index, row in car.iterrows():
            #print('index = ',index)
            for j in row['related_events']:
                event = event_df[event_df['event_id'] == j]
                if event['m_index'].values > row['index']:
                    if event['type'].values == 'Dribble':
                        df_index.append(index)
                        outcome_id.append(event['event_id'].values[0])
                        if event['outcome'].values == 'Complete':
                            car_outcome.append('Successful')
                            drib_outcome.append('Complete')
                        else:
                            car_outcome.append('Unsuccessful')
                            drib_outcome.append('Incomplete')
                        pass_outcome.append(None)
                        shot_outcome.append(None)
                        xG.append(None)
                        xA.append(None)
                        break

                    elif event['type'].values == 'Pass':
                        df_index.append(index)
                        outcome_id.append(event['event_id'].values[0])
                        if event['outcome'].values == 'Complete':
                            car_outcome.append('Successful')
                            pass_event = passes[passes['event_id'] == event['event_id'].values[0]]
                            if pass_event['shot_assist'].any() == True:
                                pass_outcome.append('Shot Assist')
                                xA.append(pass_event['xA'].values[0])
                            elif pass_event['goal_assist'].any() == True:
                                pass_outcome.append('Goal Assist')
                                xA.append(pass_event['xA'].values[0])
                            else:
                                pass_outcome.append('Complete')
                                xA.append(None)
                        else:
                            car_outcome.append('Unsuccessful')
                            pass_outcome.append('Incomplete')
                            xA.append(None)
                        shot_outcome.append(None)
                        drib_outcome.append(None)
                        xG.append(None)
                        break

                    elif event['type'].values == 'Shot':
                        car_outcome.append('Successful')
                        df_index.append(index)
                        outcome_id.append(event['event_id'].values[0])
                        shot_event = shots[shots['event_id'] == event['event_id'].values[0]]
                        shot_outcome.append(shot_event['outcome'].values[0])
                        xG.append(shot_event['sb_xg'].values[0])
                        pass_outcome.append(None)
                        drib_outcome.append(None)
                        xA.append(None)
                        break

                    elif event['type'].values == 'Dispossessed':
                        car_outcome.append('Unsuccessful')
                        df_index.append(index)
                        outcome_id.append(event['event_id'].values[0])
                        shot_outcome.append(None)
                        pass_outcome.append(None)
                        drib_outcome.append(None)
                        xG.append(None)
                        xA.append(None)

                    elif event['type'].values == 'Foul Won':
                        #if event['team'].values == 'Barcelona':
                        if event['pos_team'].values == event['team'].values:
                            car_outcome.append('Successful')
                            df_index.append(index)
                            outcome_id.append(event['event_id'].values[0])
                            shot_outcome.append(None)
                            pass_outcome.append(None)
                            drib_outcome.append(None)
                            xG.append(None)
                            xA.append(None)

                    elif event['type'].values == 'Foul Committed':
                        #if event['player'].values == player:
                        if event['pos_team'].values == event['team'].values:
                            car_outcome.append('Unsuccessful')
                            df_index.append(index)
                            outcome_id.append(event['event_id'].values[0])
                            shot_outcome.append(None)
                            pass_outcome.append(None)
                            drib_outcome.append(None)
                            xG.append(None)
                            xA.append(None)

                    elif event['type'].values == 'Miscontrol':
                        car_outcome.append('Unsuccessful')
                        df_index.append(index)
                        outcome_id.append(event['event_id'].values[0])
                        shot_outcome.append(None)
                        pass_outcome.append(None)
                        drib_outcome.append(None)
                        xG.append(None)
                        xA.append(None)

                    else:
                        pass
                        #car_outcome.append(event['type'].values)

        carry_outcome = pd.DataFrame()
        carry_outcome['index'] = df_index
        carry_outcome['outcome'] = car_outcome
        carry_outcome['pass_outcome'] = pass_outcome
        carry_outcome['shot_outcome'] = shot_outcome
        carry_outcome['dribble_outcome'] = drib_outcome
        carry_outcome['xG'] = xG
        carry_outcome['xA'] = xA
        carry_outcome['outcome_id'] = outcome_id

        carry_outcome.set_index('index',inplace=True)
        del carry_outcome.index.name

        # Add carry_outcome columns and rearrange the column order
        car = pd.concat([car,carry_outcome], axis=1)
        car = car[[c for c in car if c not in ['related_events']] + ['related_events']]
    
    return car
    

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


def shot_map_team(data,team,xg_display,pitch_col='w',line_col='k',colourmap='jet'):
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
    
        
    # Plot legend
    ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Foot',alpha=0.6)
    ax.scatter(-100,-100,marker='o',c='w',edgecolors='black',s=200,label='Head',alpha=0.6)
    ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='Penalty/FK',alpha=0.6)
    ax.legend(bbox_to_anchor=(0.99, 0.01),ncol=3,fontsize=14,loc=4,shadow=True)
    
    zo=10
    if xg_display.lower().startswith("s"):
        
        size_f = xg_size(f_xG)
        size_h = xg_size(h_xG)
        size_pfk = xg_size(pfk_xG)
        
        size_f_g = xg_size(f_g_xG)
        size_h_g = xg_size(h_g_xG)
        size_pfk_g = xg_size(pfk_g_xG)

        # Plotting shots
        ax.scatter(yf, xf, s=size_f*1000, marker='H', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
        ax.scatter(yh, xh, s=size_h*1000, marker='o', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
        ax.scatter(ypfk,xpfk,s=size_pfk*1000,marker='s',c='red',edgecolors='black',zorder=zo+1,alpha=0.9)
        
        # Plotting goals
        ax.scatter(yf_g, xf_g, s=size_f_g*1000, marker='H', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yh_g, xh_g, s=size_h_g*1000, marker='o', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(ypfk_g,xpfk_g,s=size_pfk_g*1000,marker='s',c='r',edgecolors='black',zorder=zo+2,alpha=0.9,lw=3)

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
        
        cmap, cmap_nonlin_f, levels, xfrm_levels = xg_colourbar(f_xG,colourmap)
        cmap_nonlin_h = xg_colourbar(h_xG,colourmap)[1]
        cmap_nonlin_pfk = xg_colourbar(pfk_xG,colourmap)[1]
        cmap_nonlin_f_g = xg_colourbar(f_g_xG,colourmap)[1]
        cmap_nonlin_h_g = xg_colourbar(h_g_xG,colourmap)[1]
        cmap_nonlin_pfk_g = xg_colourbar(pfk_g_xG,colourmap)[1]
        
        # Plot shots
        ax.scatter(yf,xf,zorder=zo+1,s=200,marker='H',color=cmap_nonlin_f,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(yh,xh,zorder=zo+1,s=200,marker='o',color=cmap_nonlin_h,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(ypfk,xpfk,zorder=zo+1,s=200,marker='s',color=cmap_nonlin_pfk,edgecolors='black',lw=1,alpha=0.8)
        
        # Plotting goals
        ax.scatter(yf_g, xf_g, s=200, marker='H', c=cmap_nonlin_f_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yh_g, xh_g, s=200, marker='o', c=cmap_nonlin_h_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(ypfk_g,xpfk_g,s=200,marker='s',c=cmap_nonlin_pfk_g,edgecolors='black',zorder=zo+2,alpha=0.9,lw=3)

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
        
    return fig, ax
        


def shot_map_player(data,player,xg_display,date=None,includepens=False,pitch_col='w',line_col='k',colourmap='jet'):
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
    pshots_f = pshots[((pshots['body_part'] == 'Left Foot')|(pshots['body_part'] == 'Right Foot'))&(pshots['shot_type'] != 'Penalty')&(pshots['shot_type'] != 'Free Kick')]
    pshots_p = pshots[(pshots['shot_type'] == 'Penalty')]
    pshots_fk = pshots[(pshots['shot_type'] == 'Free Kick')]
    
    pshots_h_g = pshots_h[pshots_h['outcome'] == 'Goal']
    pshots_f_g = pshots_f[pshots_f['outcome'] == 'Goal']
    pshots_fk_g = pshots_fk[pshots_fk['outcome'] == 'Goal']
    pshots_p_g = pshots_p[pshots_p['outcome'] == 'Goal']
    
    goals = len(pshots_h_g) + len(pshots_f_g) + len(pshots_fk_g)
    goals_pen = len(pshots_p_g)
    team = pshots['team'].unique()[0]
    
    xh = pshots_h['x'].values
    yh = pshots_h['y'].values
    xf = pshots_f['x'].values
    yf = pshots_f['y'].values
    xfk = pshots_fk['x'].values
    yfk = pshots_fk['y'].values
    xp = pshots_p['x'].values
    yp = pshots_p['y'].values
    
    xh_g = pshots_h_g['x'].values
    yh_g = pshots_h_g['y'].values
    xf_g = pshots_f_g['x'].values
    yf_g = pshots_f_g['y'].values
    xfk_g = pshots_fk_g['x'].values
    yfk_g = pshots_fk_g['y'].values
    xp_g = pshots_p_g['x'].values
    yp_g = pshots_p_g['y'].values
    
    h_xG = pshots_h.sb_xg.values
    f_xG = pshots_f.sb_xg.values
    fk_xG = pshots_fk.sb_xg.values
    p_xG = pshots_p.sb_xg.values
    h_g_xG = pshots_h_g.sb_xg.values
    f_g_xG = pshots_f_g.sb_xg.values
    fk_g_xG = pshots_fk_g.sb_xg.values
    p_g_xG = pshots_p_g.sb_xg.values
    
    # Plot legend
    ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Foot',alpha=0.9)
    ax.scatter(-100,-100,marker='o',c='w',edgecolors='black',s=200,label='Head',alpha=0.9)
    if includepens == True:
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='Penalty/FK',alpha=0.9)
    else:
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='FK',alpha=0.9)
    ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Goal',alpha=0.9,lw=3)
        
    ax.legend(bbox_to_anchor=(0.99, 0.01),ncol=4,fontsize=14,loc=4,shadow=True)
    
    # Add date
    if date != None:
        ax.text(0.0, 1.0, team + ' - ' + str(date), ha='left', va='bottom', transform=ax.transAxes, fontsize=14)
    else:
        ax.text(0.0, 1.0, team, ha='left', va='bottom', transform=ax.transAxes, fontsize=14)
    
    # Player name
    ax.text(0.0, 1.03, player, ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
    
    # Goals and xG
    if len(pshots_p) > 0:
        ax.text(1.0, 1.03, str(goals) + ' Goals : ' + str(round(sum(pshots.sb_xg)-sum(pshots_p.sb_xg),2)) + ' xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(1.0, 1.0, '(+' + str(goals_pen) + ' Goals from ' + str(len(pshots_p)) + ' Pen)', ha='right', va='bottom', transform=ax.transAxes, fontsize=13)
    else:
        ax.text(1.0, 1.0, str(round(sum(pshots.sb_xg),2)) + 'xG', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
    
    zo=10
    ## Size representing xG
    if xg_display.lower().startswith("s"):
        
        size_f = xg_size(f_xG)
        size_h = xg_size(h_xG)
        size_fk = xg_size(fk_xG)
        size_p = xg_size(p_xG)
        
        size_f_g = xg_size(f_g_xG)
        size_h_g = xg_size(h_g_xG)
        size_fk_g = xg_size(fk_g_xG)
        size_p_g = xg_size(p_g_xG)

        # Plotting shots
        ax.scatter(yf, xf, s=size_f*1000, marker='H', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
        ax.scatter(yh, xh, s=size_h*1000, marker='o', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
        ax.scatter(yfk, xfk, s=size_fk*1000, marker='s', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
        
        # Plotting goals
        ax.scatter(yf_g, xf_g, s=size_f_g*1000, marker='H', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yh_g, xh_g, s=size_h_g*1000, marker='o', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yfk_g, xfk_g, s=size_fk_g*1000, marker='s', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        
        if includepens == True:
            ax.scatter(yp, xp, s=size_p*1000, marker='s', c="red", edgecolors="black",zorder=zo+1,alpha=0.9)
            ax.scatter(yp_g, xp_g, s=size_p_g*1000, marker='s', c="r", edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
            
        plt.show()
    
    ## Colour representing xG
    else:
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        
        cmap, cmap_nonlin_f, levels, xfrm_levels = xg_colourbar(f_xG,colourmap)
        cmap_nonlin_h = xg_colourbar(h_xG,colourmap)[1]
        cmap_nonlin_fk = xg_colourbar(fk_xG,colourmap)[1]
        cmap_nonlin_p = xg_colourbar(p_xG,colourmap)[1]
        cmap_nonlin_f_g = xg_colourbar(f_g_xG,colourmap)[1]
        cmap_nonlin_h_g = xg_colourbar(h_g_xG,colourmap)[1]
        cmap_nonlin_fk_g = xg_colourbar(fk_g_xG,colourmap)[1]
        cmap_nonlin_p_g = xg_colourbar(p_g_xG,colourmap)[1]
        
        # Plot shots
        ax.scatter(yf,xf,zorder=zo+1,s=200,marker='H',color=cmap_nonlin_f,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(yh,xh,zorder=zo+1,s=200,marker='o',color=cmap_nonlin_h,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(yfk,xfk,zorder=zo+1,s=200,marker='s',color=cmap_nonlin_fk,edgecolors='black',lw=1,alpha=0.8)
            
        # Plotting goals
        ax.scatter(yf_g, xf_g, s=200, marker='H', c=cmap_nonlin_f_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yh_g, xh_g, s=200, marker='o', c=cmap_nonlin_h_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(yfk_g, xfk_g, s=200, marker='s', c=cmap_nonlin_fk_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        
        if includepens == True:
            ax.scatter(yp,xp,zorder=zo+1,s=200,marker='s',color=cmap_nonlin_p,edgecolors='black',lw=1,alpha=0.8)
            ax.scatter(yp_g, xp_g, s=200, marker='s', c=cmap_nonlin_p_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)

        # Colourbar
        cax = fig.add_axes([0.55, 0.23, 0.3, 0.04]) # Can just add_axes but then must place manually
        cax.set_title('xG',fontsize=14)
        cax.tick_params(labelsize=12)
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range, orientation="horizontal")
        cbar.set_ticks([xfrm_levels[i] for i in [0,4,6,-1]])
        cbar.set_ticklabels(["%.2f" % levels[i] for i in [0,4,6,-1]])
            
        plt.show()
        
    return fig, ax
    
    
def shot_map(data,home_team,away_team,xg_display,date=None,
             includepens=False,home_col='xkcd:blue',away_col='xkcd:red',pitch_col='w',line_col='k',colourmap='jet'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib
    
    data = data
    home_team = home_team
    away_team = away_team
    xg_display = xg_display
    home_col = home_col
    away_col = away_col
    pitch_col = pitch_col
    line_col = line_col
    colourmap = colourmap
    
    shots = get_shots(data)
    
    fig, ax = draw_pitch(pitch_col,line_col,'h','f')
    
    ### Shot data ###
    hshots = shots[shots['team'] == home_team]
    ashots = shots[shots['team'] == away_team]
    
    # Sorting into head, foot, PK/FK, PK (where PK is just used for xG sums and is not plotted)
    hshots_h = hshots[hshots['body_part'] == 'Head']
    hshots_f = hshots[((hshots['body_part'] == 'Left Foot')|(hshots['body_part'] == 'Right Foot'))&(hshots['shot_type'] != 'Penalty')&(hshots['shot_type'] != 'Free Kick')]
    hshots_fk = hshots[(hshots['shot_type'] == 'Free Kick')]
    hshots_p = hshots[(hshots['shot_type'] == 'Penalty')]
    hshots_g = hshots[hshots['outcome'] == 'Goal']
    
    ashots_h = ashots[ashots['body_part'] == 'Head']
    ashots_f = ashots[((ashots['body_part'] == 'Left Foot')|(ashots['body_part'] == 'Right Foot'))&(ashots['shot_type'] != 'Penalty')&(ashots['shot_type'] != 'Free Kick')]
    ashots_fk = ashots[(ashots['shot_type'] == 'Free Kick')]
    ashots_p = ashots[(ashots['shot_type'] == 'Penalty')]
    ashots_g = ashots[ashots['outcome'] == 'Goal']
    
    hshots_h_g = hshots_h[hshots_h['outcome'] == 'Goal']
    hshots_f_g = hshots_f[hshots_f['outcome'] == 'Goal']
    hshots_fk_g = hshots_fk[hshots_fk['outcome'] == 'Goal']
    hshots_p_g = hshots_p[hshots_p['outcome'] == 'Goal']
    
    ashots_h_g = ashots_h[ashots_h['outcome'] == 'Goal']
    ashots_f_g = ashots_f[ashots_f['outcome'] == 'Goal']
    ashots_fk_g = ashots_fk[ashots_fk['outcome'] == 'Goal']
    ashots_p_g = ashots_p[ashots_p['outcome'] == 'Goal']
    
    # Getting coords
    xh_h = (120 - hshots_h.x) # Take away from 120 so these points will be on left side of pitch
    yh_h = hshots_h.y 
    xh_f = (120 - hshots_f.x)
    yh_f = hshots_f.y
    xh_fk = (120 - hshots_fk.x)
    yh_fk = hshots_fk.y
    xh_p = (120 - hshots_p.x)
    yh_p = hshots_p.y
    
    xa_h = ashots_h.x
    ya_h = (80 - ashots_h.y) # Take away from 80 so wings are correct side
    xa_f = ashots_f.x
    ya_f = (80 - ashots_f.y)
    xa_fk = ashots_fk.x
    ya_fk = (80 - ashots_fk.y)
    xa_p = ashots_p.x
    ya_p = (80 - ashots_p.y)

    xh_h_g = (120 - hshots_h_g.x)
    yh_h_g = hshots_h_g.y
    xh_f_g = (120 - hshots_f_g.x)
    yh_f_g = hshots_f_g.y
    xh_fk_g = (120 - hshots_fk_g.x)
    yh_fk_g = hshots_fk_g.y
    xh_p_g = (120 - hshots_p_g.x)
    yh_p_g = hshots_p_g.y
    
    xa_h_g = ashots_h_g.x
    ya_h_g = (80 - ashots_h_g.y)
    xa_f_g = ashots_f_g.x
    ya_f_g = (80 - ashots_f_g.y)
    xa_fk_g = ashots_fk_g.x
    ya_fk_g = (80 - ashots_fk_g.y)
    xa_p_g = ashots_p_g.x
    ya_p_g = (80 - ashots_p_g.y)
    
    hshots_xG = hshots.sb_xg.values
    ashots_xG = ashots.sb_xg.values
    hshots_h_xG = hshots_h.sb_xg.values
    hshots_f_xG = hshots_f.sb_xg.values
    hshots_fk_xG = hshots_fk.sb_xg.values
    hshots_p_xG = hshots_p.sb_xg.values
    ashots_h_xG = ashots_h.sb_xg.values
    ashots_f_xG = ashots_f.sb_xg.values
    ashots_fk_xG = ashots_fk.sb_xg.values
    ashots_p_xG = ashots_p.sb_xg.values
    
    hshots_h_g_xG = hshots_h_g.sb_xg.values
    hshots_f_g_xG = hshots_f_g.sb_xg.values
    hshots_fk_g_xG = hshots_fk_g.sb_xg.values
    hshots_p_g_xG = hshots_p_g.sb_xg.values
    ashots_h_g_xG = ashots_h_g.sb_xg.values
    ashots_f_g_xG = ashots_f_g.sb_xg.values
    ashots_fk_g_xG = ashots_fk_g.sb_xg.values
    ashots_p_g_xG = ashots_p_g.sb_xg.values
    
    # Plot legend
    ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Foot',alpha=0.9)
    ax.scatter(-100,-100,marker='o',c='w',edgecolors='black',s=200,label='Head',alpha=0.9)
    if includepens == True:
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='Penalty/FK',alpha=0.9)
    else:
        ax.scatter(-100,-100,marker='s',c='w',edgecolors='black',s=200,label='FK',alpha=0.9)
    ax.scatter(-100,-100,marker='H',c='w',edgecolors='black',s=200,label='Goal',alpha=0.9,lw=3)
    ax.legend(bbox_to_anchor=(0.5, 0.01),ncol=2,fontsize=14,frameon=False)
    
    # Add date
    if date != None:
        ax.text(0.02, 0.93, str(date), ha='left', va='bottom', transform=ax.transAxes, fontsize=16)
    
    # Team names, goals, xG
    if (len(hshots_p) > 0 and len(ashots_p) > 0):
        # Team names and goals
        ax.text(0.0, 1.0, home_team + ' - ' + str(len(hshots_g)) + ' (' + str(len(hshots_p_g)) + ' Pen)', ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(1.0, 1.0, str(len(ashots_g)) + ' (' + str(len(ashots_p_g)) + ' Pen)' + ' - ' + away_team, ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        # xG totals
        ax.text(0.50, 1.03, str(round(sum(hshots.sb_xg)-sum(hshots_p.sb_xg),2)) + '  xG  ' + str(round(sum(ashots.sb_xg)-sum(ashots_p.sb_xg),2)), ha='center', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(0.43, 1.0, '(+' + str(len(hshots_p)) + ' Pen)', ha='center', va='bottom', transform=ax.transAxes, fontsize=13)
        ax.text(0.57, 1.0, '(+' + str(len(ashots_p)) + ' Pen)', ha='center', va='bottom', transform=ax.transAxes, fontsize=13)
    
    elif (len(hshots_p) > 0 and len(ashots_p) == 0):
        # Team names and goals
        ax.text(0.0, 1.0, home_team + ' - ' + str(len(hshots_g)) + ' (' + str(len(hshots_p_g)) + ' Pen)', ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(1.0, 1.0, str(len(ashots_g)) + ' - ' + away_team, ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        # xG totals
        ax.text(0.50, 1.03, str(round(sum(hshots.sb_xg)-sum(hshots_p.sb_xg),2)) + '  xG  ' + str(round(sum(ashots.sb_xg)-sum(ashots_p.sb_xg),2)), ha='center', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(0.43, 1.0, '(+' + str(len(hshots_p)) + ' Pen)', ha='center', va='bottom', transform=ax.transAxes, fontsize=13)
    
    elif (len(hshots_p) == 0 and len(ashots_p) > 0):
        # Team names and goals
        ax.text(0.0, 1.0, home_team + ' - ' + str(len(hshots_g)), ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(1.0, 1.0, str(len(ashots_g)) + ' (' + str(len(ashots_p_g)) + ' Pen)' + ' - ' + away_team, ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        # xG totals
        ax.text(0.50, 1.03, str(round(sum(hshots.sb_xg)-sum(hshots_p.sb_xg),2)) + '  xG  ' + str(round(sum(ashots.sb_xg)-sum(ashots_p.sb_xg),2)), ha='center', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(0.57, 1.0, '(+' + str(len(ashots_p)) + ' Pen)', ha='center', va='bottom', transform=ax.transAxes, fontsize=13)
    
    else:
        # Team names and goals
        ax.text(0.0, 1.0, home_team + ' - ' + str(len(hshots_g)), ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        ax.text(1.0, 1.0, str(len(ashots_g)) + ' - ' + away_team, ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')
        # xG totals
        ax.text(0.50, 1.0, str(round(sum(hshots.sb_xg)-sum(hshots_p.sb_xg),2)) + '  xG  ' + str(round(sum(ashots.sb_xg)-sum(ashots_p.sb_xg),2)), ha='center', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='semibold')

    
    zo=10
    ## Size representing xG
    if xg_display.lower().startswith("s"):
        
        size_h_f = xg_size(hshots_f_xG)
        size_h_h = xg_size(hshots_h_xG)
        size_fk_h = xg_size(hshots_fk_xG)
        size_p_h = xg_size(hshots_p_xG)
        #size_h_pfk = xg_size(hshots_pfk_xG)
        size_a_f = xg_size(ashots_f_xG)
        size_a_h = xg_size(ashots_h_xG)
        size_a_fk = xg_size(ashots_fk_xG)
        size_a_p = xg_size(ashots_p_xG)
        #size_a_pfk = xg_size(ashots_pfk_xG)
        
        size_h_f_g = xg_size(hshots_f_g_xG)
        size_h_h_g = xg_size(hshots_h_g_xG)
        size_h_fk_g = xg_size(hshots_fk_g_xG)
        size_h_p_g = xg_size(hshots_p_g_xG)
        #size_h_pfk_g = xg_size(hshots_pfk_g_xG)
        size_a_f_g = xg_size(ashots_f_g_xG)
        size_a_h_g = xg_size(ashots_h_g_xG)
        size_a_fk_g = xg_size(ashots_fk_g_xG)
        size_a_p_g = xg_size(ashots_p_g_xG)
        #size_a_pfk_g = xg_size(ashots_pfk_g_xG)
        
        # Plotting shots
        # Home shots
        plt.scatter(xh_f, yh_f, s=size_h_f*1000, marker='H', c=home_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        plt.scatter(xh_h, yh_h, s=size_h_h*1000, marker='o', c=home_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        plt.scatter(xh_fk, yh_fk, s=size_h_h*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        #plt.scatter(xh_pfk, yh_pfk, s=size_h_pfk*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        # Away shots
        plt.scatter(xa_f, ya_f, s=size_a_f*1000, marker='H', c=away_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        plt.scatter(xa_h, ya_h, s=size_a_h*1000, marker='o', c=away_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        plt.scatter(xa_fk, ya_fk, s=size_a_h*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        #plt.scatter(xa_pfk, ya_pfk, s=size_a_pfk*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+1,alpha=0.8)
        # Home goals
        plt.scatter(xh_f_g, yh_f_g, s=size_h_f_g*1000, marker='H', c=home_col, edgecolors="black",zorder=zo+2,lw=3)
        plt.scatter(xh_h_g, yh_h_g, s=size_h_h_g*1000, marker='o', c=home_col, edgecolors="black",zorder=zo+2,lw=3)
        plt.scatter(xh_fk_g, yh_fk_g, s=size_h_fk_g*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+2,lw=3)
        #plt.scatter(xh_pfk_g, yh_pfk_g, s=size_h_pfk_g*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+2,lw=3)
        # Away goals
        plt.scatter(xa_f_g, ya_f_g, s=size_a_f_g*1000, marker='H', c=away_col, edgecolors="black",zorder=zo+2,lw=3)
        plt.scatter(xa_h_g, ya_h_g, s=size_a_h_g*1000, marker='o', c=away_col, edgecolors="black",zorder=zo+2,lw=3)
        plt.scatter(xa_fk_g, ya_fk_g, s=size_a_fk_g*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+2,lw=3)
        #plt.scatter(xa_pfk_g, ya_pfk_g, s=size_a_pfk_g*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+2,lw=3)
        
        if includepens == True:
            plt.scatter(xh_p, yh_p, s=size_h_h*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+1,alpha=0.8)
            plt.scatter(xa_p, ya_p, s=size_a_h*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+1,alpha=0.8)
            plt.scatter(xh_p_g, yh_p_g, s=size_h_p_g*1000, marker='s', c=home_col, edgecolors="black",zorder=zo+2,lw=3)
            plt.scatter(xa_p_g, ya_p_g, s=size_a_p_g*1000, marker='s', c=away_col, edgecolors="black",zorder=zo+2,lw=3)
        
        plt.show()
    
    ## Colour representing xG
    else:
        norm_range = matplotlib.colors.Normalize(vmin=0, vmax=0.80)
        
        cmap, cmap_h_f, levels, xfrm_levels = xg_colourbar(hshots_f_xG,colourmap)
        cmap_h_h = xg_colourbar(hshots_h_xG,colourmap)[1]
        cmap_h_fk = xg_colourbar(hshots_fk_xG,colourmap)[1]
        cmap_h_p = xg_colourbar(hshots_p_xG,colourmap)[1]
        cmap_h_f_g = xg_colourbar(hshots_f_g_xG,colourmap)[1]
        cmap_h_h_g = xg_colourbar(hshots_h_g_xG,colourmap)[1]
        cmap_h_fk_g = xg_colourbar(hshots_fk_g_xG,colourmap)[1]
        cmap_h_p_g = xg_colourbar(hshots_p_g_xG,colourmap)[1]
        
        cmap_a_f = xg_colourbar(ashots_f_xG,colourmap)[1]
        cmap_a_h = xg_colourbar(ashots_h_xG,colourmap)[1]
        cmap_a_fk = xg_colourbar(ashots_fk_xG,colourmap)[1]
        cmap_a_p = xg_colourbar(ashots_p_xG,colourmap)[1]
        cmap_a_f_g = xg_colourbar(ashots_f_g_xG,colourmap)[1]
        cmap_a_h_g = xg_colourbar(ashots_h_g_xG,colourmap)[1]
        cmap_a_fk_g = xg_colourbar(ashots_fk_g_xG,colourmap)[1]
        cmap_a_p_g = xg_colourbar(ashots_p_g_xG,colourmap)[1]
        
        # Plot shots
        ax.scatter(xh_f,yh_f,zorder=zo+1,s=200,marker='H',color=cmap_h_f,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(xh_h,yh_h,zorder=zo+1,s=200,marker='o',color=cmap_h_h,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(xh_fk,yh_fk,zorder=zo+1,s=200,marker='s',color=cmap_h_fk,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(xa_f,ya_f,zorder=zo+1,s=200,marker='H',color=cmap_a_f,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(xa_h,ya_h,zorder=zo+1,s=200,marker='o',color=cmap_a_h,edgecolors='black',lw=1,alpha=0.8)
        ax.scatter(xa_fk,ya_fk,zorder=zo+1,s=200,marker='s',color=cmap_a_fk,edgecolors='black',lw=1,alpha=0.8)          
            
        # Plotting goals
        ax.scatter(xh_f_g,yh_f_g, s=200, marker='H', c=cmap_h_f_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(xh_h_g,yh_h_g, s=200, marker='o', c=cmap_h_h_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(xh_fk_g,yh_fk_g, s=200, marker='s', c=cmap_h_fk_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(xa_f_g,ya_f_g, s=200, marker='H', c=cmap_a_f_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(xa_h_g,ya_h_g, s=200, marker='o', c=cmap_a_h_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        ax.scatter(xa_fk_g,ya_fk_g, s=200, marker='s', c=cmap_a_fk_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)

        if includepens == True:
            ax.scatter(xh_p,yh_p,zorder=zo+1,s=200,marker='s',color=cmap_h_p,edgecolors='black',lw=1,alpha=0.8)
            ax.scatter(xa_p,ya_p,zorder=zo+1,s=200,marker='s',color=cmap_a_p,edgecolors='black',lw=1,alpha=0.8)
            ax.scatter(xh_p_g,yh_p_g, s=200, marker='s', c=cmap_h_p_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
            ax.scatter(xa_p_g,ya_p_g, s=200, marker='s', c=cmap_a_p_g, edgecolors="black",zorder=zo+2,alpha=0.9,lw=3)
        
        # Colourbar
        cax = fig.add_axes([0.55, 0.06, 0.3, 0.04])
        cax.set_title('xG',fontsize=14)
        cax.tick_params(labelsize=12)
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm_range, orientation="horizontal")
        cbar.set_ticks([xfrm_levels[i] for i in [0,4,6,-1]])
        cbar.set_ticklabels(["%.2f" % levels[i] for i in [0,4,6,-1]])


        plt.show()
        
    return fig, ax
    
    
##### Plots for passes #####

def pass_map_player(data,player,region,pitch_col='w',line_col='k'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe
    import matplotlib
    
    data = data
    player = player
    pitch_col = pitch_col
    line_col = line_col
    region = region
    
    passes = get_pass(data)
    if region.lower().startswith("t"):
        pass_op = passes[(passes['pass_type'] == 'Standard')&(passes['player'] == player)&(passes['end_x'] >= 80)]
    elif region.lower().startswith("b"):
        pass_op = passes[(passes['pass_type'] == 'Standard')&(passes['player'] == player)&(passes['end_x'] >= 102)&(passes['end_y'] >= 18)&(passes['end_y'] <= 62)]
    else:
        pass_op = passes[(passes['pass_type'] == 'Standard')&(passes['player'] == player)]
       
    pass_op_s = pass_op[(pass_op['outcome'] == 'Complete')&(pass_op['shot_assist'].isnull())&(pass_op['goal_assist'].isnull())]
    pass_op_u = pass_op[((pass_op['outcome'] == 'Incomplete')|(pass_op['outcome'] == 'Out'))&(pass_op['shot_assist'].isnull())&(pass_op['goal_assist'].isnull())]
    pass_op_sa = pass_op[pass_op['shot_assist'].notnull()]
    pass_op_ga = pass_op[pass_op['goal_assist'].notnull()]
    
    fig, ax = draw_pitch('w','k','h','f')

    arrow_params = {'width': 0.1,'head_width': 1.0,'head_length': 2.0,'length_includes_head': True}

    xs = pass_op_s.x.values
    ys = (80 - pass_op_s.y.values)
    xes = pass_op_s.end_x.values
    yes = (80 - pass_op_s.end_y.values)
    xu = pass_op_u.x.values
    yu = (80 - pass_op_u.y.values)
    xeu = pass_op_u.end_x.values
    yeu = (80 - pass_op_u.end_y.values)
    xsa = pass_op_sa.x.values
    ysa = (80 - pass_op_sa.y.values)
    xesa = pass_op_sa.end_x.values
    yesa = (80 - pass_op_sa.end_y.values)
    xga = pass_op_ga.x.values
    yga = (80 - pass_op_ga.y.values)
    xega = pass_op_ga.end_x.values
    yega = (80 - pass_op_ga.end_y.values)

    ax.text(0.0, 1.0, player, ha='left', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')
    
    if region.lower().startswith("t"):
        ax.text(1.0, 1.0, 'Final Third Passes', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')
    elif region.lower().startswith("b"):
        ax.text(1.0, 1.0, 'Passes into Box', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')
    else:
        ax.text(1.0, 1.0, 'Passes', ha='right', va='bottom', transform=ax.transAxes, fontsize=18, fontweight='demi')

    ax.scatter(-100,-100,marker='o',c='xkcd:lightblue',edgecolors='black',s=200,label='Successful',alpha=0.5)
    ax.scatter(-100,-100,marker='o',c='k',edgecolors='black',s=200,label='Unsuccessful',alpha=0.2)
    ax.scatter(-100,-100,marker='o',c='xkcd:green',edgecolors='black',s=200,label='Shot Assist',alpha=1)
    ax.scatter(-100,-100,marker='o',c='xkcd:crimson',edgecolors='black',s=200,label='Goal Assist',alpha=1)
    ax.legend(loc=3,bbox_to_anchor=(0., -0.08),ncol=4,fontsize=14,frameon=False)

    zo = 10
    ax.scatter(xs,ys,c='xkcd:lightblue',edgecolors='black',zorder=zo,alpha=0.5)
    for i in range(len(xs)):
        ax.arrow(xs[i],ys[i],xes[i]-xs[i],yes[i]-ys[i],color='xkcd:lightblue',**arrow_params,alpha=0.5)
    ax.scatter(xu,yu,c='k',edgecolors='black',zorder=zo,alpha=0.2)
    ax.scatter(xsa,ysa,c='xkcd:green',edgecolors='black',zorder=zo+1,alpha=0.9)
    for i in range(len(xsa)):
        ax.arrow(xsa[i],ysa[i],xesa[i]-xsa[i],yesa[i]-ysa[i],color='xkcd:green',**arrow_params)

    ax.scatter(xga,yga,c='xkcd:crimson',edgecolors='black',zorder=zo+1,alpha=0.9)
    for i in range(len(xga)):
        ax.arrow(xga[i],yga[i],xega[i]-xga[i],yega[i]-yga[i],color='xkcd:crimson',**arrow_params)


    plt.show()
    
    return fig, ax



##### Plots for carries #####

def carry_map_player(data,player,date=None,pitch_col='w',line_col='k'):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib
    
    data = data
    player = player
    pitch_col = pitch_col
    line_col = line_col
    
    carries = get_carry_prog(data,find_success=True,player=player)
    team = carries['team'].unique()[0]
    
    car_s = carries[carries['outcome'] == 'Successful']
    car_u = carries[carries['outcome'] == 'Unsuccessful']
    car_shot = carries[(carries['shot_outcome'] != 'Goal')&(carries['shot_outcome'].notnull())]
    car_goal = carries[(carries['shot_outcome'] == 'Goal')]
    car_pass = car_s[(car_s['pass_outcome'].notnull())]
    car_sa = car_s[(car_s['pass_outcome'] == 'Shot Assist')]
    car_ga = car_s[(car_s['pass_outcome'] == 'Goal Assist')]
    car_drib = car_s[(car_s['dribble_outcome'].notnull())]

    xA_tot = car_s[car_s['xA'].notna()].xA.sum()
    xG_tot = car_s[car_s['xG'].notna()].xG.sum()
    
    fig, ax = draw_pitch('w','k','v','h')

    xs = car_s['x'].values
    ys = car_s['y'].values
    xse = car_s['end_x'].values
    yse = car_s['end_y'].values

    xsh = car_shot['x'].values
    ysh = car_shot['y'].values
    xshe = car_shot['end_x'].values
    yshe = car_shot['end_y'].values

    xg = car_goal['x'].values
    yg = car_goal['y'].values
    xge = car_goal['end_x'].values
    yge = car_goal['end_y'].values

    xsa = car_sa['x'].values
    ysa = car_sa['y'].values
    xsae = car_sa['end_x'].values
    ysae = car_sa['end_y'].values

    xga = car_ga['x'].values
    yga = car_ga['y'].values
    xgae = car_ga['end_x'].values
    ygae = car_ga['end_y'].values

    xd = car_drib['x'].values
    yd = car_drib['y'].values
    xde = car_drib['end_x'].values
    yde = car_drib['end_y'].values

    zo=100
    ax.plot([ys,yse],[xs,xse],'0.85',alpha=0.5,zorder=zo)
    ax.scatter(yse,xse,s=100,facecolor='w',edgecolor='0.85',zorder=zo+1)
    ax.plot([ysh,yshe],[xsh,xshe],'xkcd:green',alpha=1,zorder=zo+2)
    ax.scatter(yshe,xshe,s=100,facecolor='w',edgecolor='xkcd:green',zorder=zo+3)
    ax.plot([yg,yge],[xg,xge],'xkcd:green',alpha=0.5,zorder=zo+2)
    ax.scatter(yge,xge,s=100,facecolor='xkcd:green',edgecolor='xkcd:green',zorder=zo+3)
    ax.plot([ysa,ysae],[xsa,xsae],'xkcd:blue',alpha=1,zorder=zo+2)
    ax.scatter(ysae,xsae,s=100,facecolor='w',edgecolor='xkcd:blue',zorder=zo+3)
    ax.plot([yga,ygae],[xga,xgae],'xkcd:blue',alpha=1,zorder=zo+2)
    ax.scatter(ygae,xgae,s=100,facecolor='xkcd:blue',edgecolor='xkcd:blue',zorder=zo+3)

    ax.scatter(-100,-100,s=100,facecolor='w',edgecolor='xkcd:green',zorder=zo+3,label='Shot')
    ax.scatter(-100,-100,s=100,facecolor='xkcd:green',edgecolor='xkcd:green',zorder=zo+3,label='Goal')
    ax.scatter(-100,-100,s=100,facecolor='w',edgecolor='xkcd:blue',zorder=zo+3,label='Key Pass')
    ax.scatter(-100,-100,s=100,facecolor='xkcd:blue',edgecolor='xkcd:blue',zorder=zo+3,label='Assist')

    ax.legend(loc=4,bbox_to_anchor=(1.0,1.07),ncol=2,frameon=False,fontsize=12,framealpha=0,facecolor=None)
    
    ## Adding Annotations
    ax.text(0.0,1.18,player,transform=ax.transAxes,ha='left',va='bottom',fontsize=18,fontweight='semibold',zorder=zo)
    ax.text(0.0,1.15,team,transform=ax.transAxes,ha='left',va='top',fontsize=16,zorder=zo)
    ax.text(1.0,1.18,'Progressive Carries',transform=ax.transAxes,ha='right',va='bottom',fontsize=18,fontweight='semibold',zorder=zo)
    
    # Add date
    if date != None:
        ax.text(0.0, 1.10, 'La Liga - ' + str(date), ha='left', va='top', transform=ax.transAxes, fontsize=16)
    else:
        ax.text(0.0, 1.10, 'La Liga', ha='left', va='top', transform=ax.transAxes, fontsize=16)

    ax.text(0.82,1.025,'xG: {:.2f}'.format(xG_tot),transform=ax.transAxes,fontsize=16,
            bbox=dict(boxstyle='round,pad=0.4',facecolor='xkcd:green',edgecolor='k',alpha=0.4),ha='right',zorder=zo)
    ax.text(0.98,1.025,'xA: {:.2f}'.format(xA_tot),transform=ax.transAxes,fontsize=16,
            bbox=dict(boxstyle='round,pad=0.4',facecolor='xkcd:blue',edgecolor='k',alpha=0.4),ha='right',zorder=zo)

    plt.show()
    
    return fig, ax