import pandas as pd
game_df = pd.read_csv("data/nba_games_merge.csv")
player_df = pd.read_csv("data/player_data_merge.csv", encoding='latin-1')
roster_df = pd.read_csv("data/roster_data_merge.csv", encoding='latin1')

player_position_df = player_df.merge(roster_df, how='left', on=['Season', 'Player', 'Tm'])
player_position_df = player_position_df.drop(player_position_df.columns[0], axis='columns')
player_position_df = player_position_df.drop(player_position_df.columns[-2], axis='columns')

#player_position_df.to_csv('game_player_position.csv')

game_player_position_df = player_position_df.merge(game_df, how='left', on=['ID'])
game_player_position_df = game_player_position_df.rename(columns={'date_x': 'date'})
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-2], axis='columns')
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-4], axis='columns')
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-3], axis='columns')

#game_player_position_df.to_csv('game_player_position.csv')


#initialise final list that starts off empty; will be converted to dataframe
analysis_list = []

#initalise variables to store game ID, playing time and position and name; starts off blank
game_ID = ''
pg_pt1 = 0
sg_pt1 = 0
sf_pt1 = 0
pf_pt1 = 0
c_pt1 = 0
pg1 = ''
sg1 = ''
sf1 = ''
pf1 = ''
c1 = ''
pg_pt2 = 0
sg_pt2 = 0
sf_pt2 = 0
pf_pt2 = 0
c_pt2 = 0
pg2 = ''
sg2 = ''
sf2 = ''
pf2 = ''
c2 = ''
pg_pt3 = 0
sg_pt3 = 0
sf_pt3 = 0
pf_pt3 = 0
c_pt3 = 0
pg3 = ''
sg3 = ''
sf3 = ''
pf3 = ''
c3 = ''
date = ''
Tm = ''
home = 0
won = True

#initalise list that will store a row of the final list; starts off empty
game = []
#create loop that iterates through rows of dataframe
for index in game_player_position_df.index:

#if statement stating that if the game ID is new aka it is not the same as the value currently stored in game ID, first add name variables 
#to the list then add the list to final list then set the list back to empty as well as the name and playing time variables and then add 
#date, team, home flag and result to the list. Else, check position to check playing time variable against seconds played column; if 
#seconds played is greater, replace name.
    if game_player_position_df['ID'][index]!=game_ID:
        game.append(game_ID)
        game.append(date)
        game.append(Tm)
        game.append(home)
        game.append(won)
        game.append(pg1)
        game.append(sg1)
        game.append(sf1)
        game.append(pf1)
        game.append(c1)
        game.append(pg2)
        game.append(sg2)
        game.append(sf2)
        game.append(pf2)
        game.append(c2)
        game.append(pg3)
        game.append(sg3)
        game.append(sf3)
        game.append(pf3)
        game.append(c3)
        analysis_list.append(game)
        game = []
        game_ID = game_player_position_df['ID'][index]
        pg1 = ''
        sg1 = ''
        sf1 = ''
        pf1 = ''
        c1 = ''
        pg2 = ''
        sg2 = ''
        sf2 = ''
        pf2 = ''
        c2 = ''
        pg3 = ''
        sg3 = ''
        sf3 = ''
        pf3 = ''
        c3 = ''
        pg_pt1 = 0
        sg_pt1 = 0
        sf_pt1 = 0
        pf_pt1 = 0
        c_pt1 = 0
        pg_pt2 = 0
        sg_pt2 = 0
        sf_pt2 = 0
        pf_pt2 = 0
        c_pt2 = 0
        pg_pt3 = 0
        sg_pt3 = 0
        sf_pt3 = 0
        pf_pt3 = 0
        c_pt3 = 0
        date = game_player_position_df['date'][index]
        Tm = game_player_position_df['Tm'][index]
        home = game_player_position_df['home'][index]
        won = game_player_position_df['won'][index]
        if game_player_position_df['Pos'][index]=='PG':
            if game_player_position_df['SP'][index]>pg_pt1:
                pg1 = game_player_position_df['Player'][index]
                pg_pt1 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SG':
            if game_player_position_df['SP'][index]>sg_pt1:
                sg1 = game_player_position_df['Player'][index]
                sg_pt1 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SF':
            if game_player_position_df['SP'][index]>sf_pt1:
                sf1 = game_player_position_df['Player'][index]
                sf_pt1 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='PF':
            if game_player_position_df['SP'][index]>pf_pt1:
                pf1 = game_player_position_df['Player'][index]
                pf_pt1 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='C':
            if game_player_position_df['SP'][index]>c_pt1:
                c1 = game_player_position_df['Player'][index]
                c_pt1 = game_player_position_df['SP'][index]
    else:
        if game_player_position_df['Pos'][index]=='PG' and game_player_position_df['SP'][index] > 0:
            if game_player_position_df['SP'][index]>pg_pt1:
                pg3 = pg2
                pg2 = pg1
                pg_pt3 = pg_pt2
                pg_pt2 = pg_pt1
                pg1 = game_player_position_df['Player'][index]
                pg_pt1 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>pg_pt2:
                pg3 = pg2
                pg_pt3 = pg_pt2
                pg2 = game_player_position_df['Player'][index]
                pg_pt2 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>pg_pt3:
                pg3 = game_player_position_df['Player'][index]
                pg_pt3 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SG' and game_player_position_df['SP'][index] > 0:
            if game_player_position_df['SP'][index]>sg_pt1:
                sg3 = sg2
                sg2 = sg1
                sg_pt3 = sg_pt2
                sg_pt2 = sg_pt1
                sg1 = game_player_position_df['Player'][index]
                sg_pt1 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>sg_pt2:
                sg3 = sg2
                sg_pt3 = sg_pt2
                sg2 = game_player_position_df['Player'][index]
                sg_pt2 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>sg_pt3:
                sg3 = game_player_position_df['Player'][index]
                sg_pt3 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SF' and game_player_position_df['SP'][index] > 0:
            if game_player_position_df['SP'][index]>sf_pt1:
                sf3 = sf2
                sf2 = sf1
                sf_pt3 = sf_pt2
                sf_pt2 = sf_pt1
                sf1 = game_player_position_df['Player'][index]
                sf_pt1 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>sf_pt2:
                sf3 = sf2
                sf_pt3 = sf_pt2
                sf2 = game_player_position_df['Player'][index]
                sf_pt2 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>sf_pt3:
                sf3 = game_player_position_df['Player'][index]
                sf_pt3 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='PF' and game_player_position_df['SP'][index] > 0:
            if game_player_position_df['SP'][index]>pf_pt1:
                pf3 = pf2
                pf2 = pf1
                pf_pt3 = pf_pt2
                pf_pt2 = pf_pt1
                pf1 = game_player_position_df['Player'][index]
                pf_pt1 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>pf_pt2:
                pf3 = pf2
                pf_pt3 = pf_pt2
                pf2 = game_player_position_df['Player'][index]
                pf_pt2 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>pf_pt3:
                pf3 = game_player_position_df['Player'][index]
                pf_pt3 = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='C' and game_player_position_df['SP'][index] > 0:
            if game_player_position_df['SP'][index]>c_pt1:
                c3 = c2
                c2 = c1
                c_pt3 = c_pt2
                c_pt2 = c_pt1
                c1 = game_player_position_df['Player'][index]
                c_pt1 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>c_pt2:
                c3 = c2
                c_pt3 = c_pt2
                c2 = game_player_position_df['Player'][index]
                c_pt2 = game_player_position_df['SP'][index]
            elif game_player_position_df['SP'][index]>c_pt3:
                c3 = game_player_position_df['Player'][index]
                c_pt3 = game_player_position_df['SP'][index]

#finally initialise dataframe stating column names and passing through list
analysis_df = pd.DataFrame(analysis_list, columns=['ID', 'date', 'Tm', 'home', 'won', 'PG1', 'SG1', 'SF1', 'PF1', 'C1', 'PG2', 'SG2', 
                                                   'SF2', 'PF2', 'C2', 'PG3', 'SG3', 'SF3', 'PF3', 'C3'], index=list(range(0, 
                                                                                                                           len(analysis_list))))

analysis_df.to_csv('analysis_v2.csv')