import pandas as pd
game_df = pd.read_csv("data/nba_games_merge.csv")
player_df = pd.read_csv("data/player_data_merge.csv", encoding='latin-1')
roster_df = pd.read_csv("data/roster_data_merge.csv", encoding='latin1')

player_position_df = player_df.merge(roster_df, how='left', on=['Season', 'Player', 'Tm'])
player_position_df = player_position_df.drop(player_position_df.columns[0], axis='columns')
player_position_df = player_position_df.drop(player_position_df.columns[-2], axis='columns')

game_player_position_df = player_position_df.merge(game_df, how='left', on=['ID'])
game_player_position_df = game_player_position_df.rename(columns={'date_x': 'date'})
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-2], axis='columns')
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-4], axis='columns')
game_player_position_df = game_player_position_df.drop(game_player_position_df.columns[-3], axis='columns')

analysis_list = []

game_ID = ''
pg_pt = 0
sg_pt = 0
sf_pt = 0
pf_pt = 0
c_pt = 0
pg = ''
sg = ''
sf = ''
pf = ''
c = ''
pg_store_pt = 0
sg_store_pt = 0
sf_store_pt = 0
pf_store_pt = 0
c_store_pt = 0
pg_store = ''
sg_store = ''
sf_store = ''
pf_store = ''
c_store = ''
date = ''
Tm = ''
home = 0
won = True
game = []

for index in game_player_position_df.index:
    if game_player_position_df['ID'][index]!=game_ID:
        if pg == '':
            pg = pg_store
        if sg == '':
            sg = sg_store
        if sf == '':
            sf = sf_store
        if pf == '':
            pf = pf_store
        if c == '':
            c = c_store
        game.append(game_ID)
        game.append(date)
        game.append(Tm)
        game.append(home)
        game.append(won)
        game.append(pg)
        game.append(sg)
        game.append(sf)
        game.append(pf)
        game.append(c)
        analysis_list.append(game)
        game = []
        game_ID = game_player_position_df['ID'][index]
        pg = ''
        sg = ''
        sf = ''
        pf = ''
        c = ''
        pg_store = ''
        sg_store = ''
        sf_store = ''
        pf_store = ''
        c_store = ''
        pg_pt = 0
        sg_pt = 0
        sf_pt = 0
        pf_pt = 0
        c_pt = 0
        pg_store_pt = 0
        sg_store_pt = 0
        sf_store_pt = 0
        pf_store_pt = 0
        c_store_pt = 0
        date = game_player_position_df['date'][index]
        Tm = game_player_position_df['Tm'][index]
        home = game_player_position_df['home'][index]
        won = game_player_position_df['won'][index]
        if game_player_position_df['Pos'][index]=='PG':
            if game_player_position_df['SP'][index]>pg_pt:
                pg = game_player_position_df['Player'][index]
                pg_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>sg_store_pt:
                    sg_store = game_player_position_df['Player'][index]
                    sg_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SG':
            if game_player_position_df['SP'][index]>sg_pt:
                sg = game_player_position_df['Player'][index]
                sg_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>pg_store_pt:
                    pg_store = game_player_position_df['Player'][index]
                    pg_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>sf_store_pt:
                    sf_store = game_player_position_df['Player'][index]
                    sf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SF':
            if game_player_position_df['SP'][index]>sf_pt:
                sf = game_player_position_df['Player'][index]
                sf_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>sg_store_pt:
                    sg_store = game_player_position_df['Player'][index]
                    sg_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>pf_store_pt:
                    pf_store = game_player_position_df['Player'][index]
                    pf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='PF':
            if game_player_position_df['SP'][index]>pf_pt:
                pf = game_player_position_df['Player'][index]
                pf_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>c_store_pt:
                    c_store = game_player_position_df['Player'][index]
                    c_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>sf_store_pt:
                    sf_store = game_player_position_df['Player'][index]
                    sf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='C':
            if game_player_position_df['SP'][index]>c_pt:
                c = game_player_position_df['Player'][index]
                c_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>pf_store_pt:
                    pf_store = game_player_position_df['Player'][index]
                    pf_store_pt = game_player_position_df['SP'][index]
    else:
        if game_player_position_df['Pos'][index]=='PG':
            if game_player_position_df['SP'][index]>pg_pt:
                pg = game_player_position_df['Player'][index]
                pg_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>sg_store_pt:
                    sg_store = game_player_position_df['Player'][index]
                    sg_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SG':
            if game_player_position_df['SP'][index]>sg_pt:
                sg = game_player_position_df['Player'][index]
                sg_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>pg_store_pt:
                    pg_store = game_player_position_df['Player'][index]
                    pg_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>sf_store_pt:
                    sf_store = game_player_position_df['Player'][index]
                    sf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='SF':
            if game_player_position_df['SP'][index]>sf_pt:
                sf = game_player_position_df['Player'][index]
                sf_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>sg_store_pt:
                    sg_store = game_player_position_df['Player'][index]
                    sg_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>pf_store_pt:
                    pf_store = game_player_position_df['Player'][index]
                    pf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='PF':
            if game_player_position_df['SP'][index]>pf_pt:
                pf = game_player_position_df['Player'][index]
                pf_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>c_store_pt:
                    c_store = game_player_position_df['Player'][index]
                    c_store_pt = game_player_position_df['SP'][index]
                elif game_player_position_df['SP'][index]>sf_store_pt:
                    sf_store = game_player_position_df['Player'][index]
                    sf_store_pt = game_player_position_df['SP'][index]
        if game_player_position_df['Pos'][index]=='C':
            if game_player_position_df['SP'][index]>c_pt:
                c = game_player_position_df['Player'][index]
                c_pt = game_player_position_df['SP'][index]
            else:
                if game_player_position_df['SP'][index]>pf_store_pt:
                    pf_store = game_player_position_df['Player'][index]
                    pf_store_pt = game_player_position_df['SP'][index]

#finally initialise dataframe stating column names and passing through list
analysis_df = pd.DataFrame(analysis_list, columns=['ID', 'date', 'Tm', 'home', 'won', 'PG', 'SG', 'SF', 'PF', 'C'],
                      index=list(range(0, len(analysis_list))))

analysis_df.to_csv('analysis_new.csv')