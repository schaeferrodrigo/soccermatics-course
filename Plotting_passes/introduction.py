# %%
import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch , Sbopen

# %%
parser = Sbopen()
idEvent = 69301
df , related, freeze, tactics = parser.event(idEvent)

# %%
team1 , team2 = df.team_name.unique()
print('team 1 is ', team1, 'team 2 is ', team2 )

# %%
def teamPasses(team):
    mask = (df.team_name==team)&(df.type_name=='Pass')
    df_reduced = df.loc[mask,['x', 'y', 'end_x', 'end_y', 'player_name']]
    return df_reduced

# %%
def specificPlayer(team,playerName):
    df = teamPasses(team)
    mask = df.player_name == playerName
    df_reduced = df.loc[mask,['x', 'y', 'end_x', 'end_y' ]]
    return df_reduced

# %%
namePlayer = 'Lucy Bronze'
BronzePasses = specificPlayer(team1, namePlayer)

# %%
pitch = Pitch(line_color='black')
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)




def plotPasses(dataFrame , colorOrigin,colorDirection , axx = ax['pitch'] ):
    
    for i, row in dataFrame.iterrows():
        pitch.scatter(row.x, row.y , alpha = 0.2 , s= 500 , color = colorOrigin, ax = axx)
        pitch.arrows(row.x, row. y , row.end_x, row.end_y, color = colorDirection, ax = axx , width =1)
        
plotPasses(BronzePasses,'blue','blue')

plt.suptitle(f'{namePlayer} against {team2}', fontsize = 30)

# %%
# multiple pass maps

EnglandPasses = teamPasses(team1)


# %%
pitch = Pitch(line_color='black' , pad_top= 20)
fig, ax = pitch.grid( ncols = 4 , nrows = 4, grid_height=0.85, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)


def MultiplePlotsPasses(team):
    df = teamPasses(team)
    players = df['player_name'].unique()
    for name , axx in zip(players,ax['pitch'].flat[:len(players)]):
        axx.text(60,-10, name, ha = 'center', va = 'center', fontsize= '14')
        dfPlayer = specificPlayer(team, name )
        plotPasses(dfPlayer, 'blue', 'blue' , axx)
    for axx in ax['pitch'][-1,16 - len(Players):]:
        axx.remove()

MultiplePlotsPasses(team1)

ax['title'].text(0.5,0.5, 'England passes against Sweden', ha = 'center', va = 'center', fontsize = 30 )

# %%



