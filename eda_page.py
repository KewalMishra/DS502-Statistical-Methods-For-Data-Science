import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Arc
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go
import numpy as np
# import missingno as msno
from helper import load_data, draw_pitch_mpl, draw_pitch_plotly

def eda():
    st.sidebar.markdown('#')
    st.title('Exploratory Data Analysis on football dataset')

    # Define Standard Pitch Lengths
    xStart = -53
    xEnd = 53
    yStart = -34
    yEnd = 34
    xLength = xEnd - xStart
    yLength = yEnd - yStart

    data = load_data()

    football_field1 = st.selectbox("Type of Shots",['Outcome','Play type','Set-piece'])
    
    if football_field1 == 'Outcome':
        df_Goals = data[(data['outcome'] == 'Goal') | (data['outcome']=='owngoal')]
        df_NotGoals = data[(data['outcome'] == 'Blocked') | (data['outcome'] == 'GoalFrame') | (data['outcome'] == 'Missed') | (data['outcome'] == 'Saved')]

        title_font='Arial'
        main_font='Arial'

        ## Set background colour
        background = 'green'     #'city-blue'    # 

        ## Figure
        fig = draw_pitch_plotly(colour=background, size=1, len_field=106, wid_field=68)

        ## No-Goals
        fig.add_trace(go.Scatter(x=df_NotGoals['position_xM_std'],
                                y=df_NotGoals['position_yM_std'],
                                mode='markers',
                                name='No Goal',
                                hovertemplate=('<b>X-coordinate</b>: %{x:.2f}<br>'+\
                                                '<b>Y-coordinate</b>: %{y:.2f}<br>'
                                            ),
                                marker=dict(size=4,
                                            color='red'
                                            )
                                )
                    )

        ### Goals
        fig.add_trace(go.Scatter(x=df_Goals['position_xM_std'],
                                y=df_Goals['position_yM_std'],
                                mode='markers',
                                name='Goal',
                                hovertemplate=('<b>X-coordinate</b>: %{x:.2f}<br>'+\
                                                '<b>Y-coordinate</b>: %{y:.2f}<br>'
                                            ),
                                marker=dict(size=4,
                                            color='green'
                                            )
                                )
                    )

        ## Update figure layout
        fig.update_layout(title={'text': 'Shot positions',
                                'y':0.95,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                        legend_title='Outcome',
                        font_family=main_font,
                        font_color='white',
                        title_font_family=title_font,
                        title_font_color='white',
                        title_font_size=22,
                        legend_title_font_color='white',
                        legend={'traceorder':'reversed'},
                        hoverlabel=dict(bgcolor='white',
                                        font_size=13,
                                        font_family=main_font
                                        )
                        )
        st.write(fig)

    if football_field1 == 'Play type':

        # Create dataframe 
        df_op = data[data['play_type']=='Open Play']
        df_Goals = data[(data['outcome'] == 'Goal') | (data['outcome']=='owngoal')]

        # Visualise shots

        ## Define fonts
        title_font='Arial'
        main_font='Arial'

        ## Set background colour
        background = 'green'    # aliceblue


        ## Draw the pitch
        fig = draw_pitch_plotly(colour=background, size=1, len_field=106, wid_field=68)


        ## Add scatter plot points to existing figure

        ### No Goal
        fig.add_trace(go.Scatter(x=df_op['position_xM_std'],
                                y=df_op['position_yM_std'],
                                mode='markers',
                                name='Open-Play',

                                marker=dict(size=4,
                                            color='red'
                                            )
                                )
                    )

        ### Goals
        fig.add_trace(go.Scatter(x=df_Goals['position_xM_std'],
                                y=df_Goals['position_yM_std'],
                                mode='markers',
                                name='Goal',
                                hovertemplate=('<b>X-coordinate</b>: %{x:.2f}<br>'+\
                                                '<b>Y-coordinate</b>: %{y:.2f}<br>'
                                            ),
                                marker=dict(size=4,
                                            color='green'
                                            )
                                )
                    )


        ## Update figure layout
        fig.update_layout(title={'text': 'Shots from Open Play',
                                'y':0.95,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                        legend_title='Outcome',
                        font_family=main_font,
                        font_color='white',
                        title_font_family=title_font,
                        title_font_color='white',
                        title_font_size=22,
                        legend_title_font_color='white',
                        legend={'traceorder':'reversed'},
                        #width=795,
                        #height=510,
                        hoverlabel=dict(bgcolor='white',
                                        font_size=13,
                                        font_family=main_font
                                        )
                        )



        ## Show figure
        st.write(fig)

    if football_field1 == 'Set-piece':
        df_pk = data[data['play_type']=='Penalty']
        df_fk = data[data['play_type'] == 'Direct freekick']
        df_corners = data[(data['play_type'] == 'Direct Corner') | (data['play_type'] == 'Direct corner')]
        df_Goals = data[(data['outcome'] == 'Goal') | (data['outcome']=='owngoal')]

        # Visualise shots

        ## Define fonts
        title_font='Arial'
        main_font='Arial'

        ## Set background colour
        background = 'green'    # aliceblue


        ## Draw the pitch
        fig = draw_pitch_plotly(colour=background, size=1, len_field=106, wid_field=68)


        ## Add scatter plot points to existing figure

        ### Penalties
        fig.add_trace(go.Scatter(x=df_pk['position_xM_std'],
                                y=df_pk['position_yM_std'],
                                mode='markers',
                                name='Penalties',

                                marker=dict(size=4,
                                            color='red'
                                            )
                                )
                    )

        ### Free-Kicks
        fig.add_trace(go.Scatter(x=df_fk['position_xM_std'],
                                y=df_fk['position_yM_std'],
                                mode='markers',
                                name='Free-Kicks',

                                marker=dict(size=4,
                                            color='yellow'
                                            )
                                )
                    )

        ### Corners
        fig.add_trace(go.Scatter(x=df_corners['position_xM_std'],
                                y=df_corners['position_yM_std'],
                                mode='markers',
                                name='Corners',

                                marker=dict(size=4,
                                            color='blue'
                                            )
                                )
                    )


        ### Goals
        fig.add_trace(go.Scatter(x=df_Goals['position_xM_std'],
                                y=df_Goals['position_yM_std'],
                                mode='markers',
                                name='Goal',
                                hovertemplate=('<b>X-coordinate</b>: %{x:.2f}<br>'+\
                                                '<b>Y-coordinate</b>: %{y:.2f}<br>'
                                            ),
                                marker=dict(size=4,
                                            color='green'
                                            )
                                )
                    )


        ## Update figure layout
        fig.update_layout(title={'text': 'Shots from Set-Pieces',
                                'y':0.95,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                        legend_title='Outcome',
                        font_family=main_font,
                        font_color='white',
                        title_font_family=title_font,
                        title_font_color='white',
                        title_font_size=22,
                        legend_title_font_color='white',
                        legend={'traceorder':'reversed'},
                        #width=795,
                        #height=510,
                        hoverlabel=dict(bgcolor='black',
                                        font_size=13,
                                        font_family=main_font
                                        )
                        )



        ## Show figure
        st.write(fig)

    st.markdown('####')
    
    daily_avg_sent_exp = st.expander('Data insight')
    daily_avg_sent_exp.write('More than 11,000 Shots in the Dataset.')

    st.markdown('###')
    show_data = st.checkbox('Show Data')
    if show_data:
        st.table(data.head(5))

    background = 'aliceblue' #"white"

# Two dimensional histogram
    df_op_Shots = data[(data['play_type'] == 'Open Play')].copy()

    
    H_Shot = np.histogram2d(df_op_Shots['position_xM_std'], df_op_Shots['position_yM_std'], bins=50, range=[[0, xLength], [0, yLength]])
    df_op_goals = df_op_Shots[df_op_Shots['isGoal'] == 1]
    H_Goal = np.histogram2d(df_op_goals['position_xM_std'], df_op_goals['position_yM_std'], bins=50, range=[[0, xLength], [0, yLength]])
    
    fig, ax = plt.subplots(figsize=(16.5, 10.5))
    fig.set_facecolor(background)
    cmap=plt.cm.Reds

    # Get the colormap colors
    my_cmap = cmap(np.arange(cmap.N))

    # Set alpha
    my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

    # Create new colormap
    my_cmap = ListedColormap(my_cmap)
    ## Draw the pitch
    draw_pitch_mpl(x_min=0,
                x_max=xLength,
                y_min=0,
                y_max=yLength,
                orientation="vertical", # "horizontal"
                aspect="fll",
                pitch_color=background,
                line_color="midnightblue",
                ax=ax
                )

    ## Heat map
    pos=ax.imshow(H_Goal[0]/H_Shot[0],
                extent=[-1, yLength, xLength, -1],
                aspect='auto',
                cmap=my_cmap,
                #vmin=0,
                #vmax=0.5
                )

    ## Colour bar
    fig.colorbar(pos, ax=ax)

    ## Set title
    ax.set_title('Proportion of Shots Resulting in a\nGoal Before Outlier Removal',
                loc='center',
                color='midnightblue', 
                fontweight='bold',
                fontfamily='DejaVu Sans',
                fontsize=16,
                )


    ## Show figure
    plt.tight_layout()
    plt.gca().set_aspect('equal', adjustable='box')
    st.markdown('####')
    st.write(fig)
    st.markdown('####')
    daily_avg_sent_exp = st.expander('Data insight')
    daily_avg_sent_exp.write('''
    There are data points far away from the goal that almost certainly wrong, the other might indeed have happened in a match and are therefore right, just like the Xabi Alonso goal against Luton where the goalkeeper was out of position, causing Xabi to shoot from a position that he otherwise would not shoot from. For example, it appears that a goal was scored from the edge of the of the attacking team's box. There is also a goal from the halfway line.

Reasons for this could be:
*    The data in correctly entered,
*    Coordinate system flipped for the particular shot (unlikely).

The data is required to be smooth so that the model doesn't think there's a 100% chance of scoring when shooting from the edge of the goalkeepers box.

There are three options to deal with these outliers:
1.    Delete the outliers;
2.    Use our experience and tell the model that the probability to score from this position is realistically 0. This means we change the target but leave the features as is; and
3.    Assume that the shot happened closer to the goal, but we still assume that it went in. This means that we change the features but leave the target.

In our situation, the second strategy would make the most sense.

There are sophisticated ways to filter out these shots when a full set of Event data is available. For example, with full event data, we could determine the percentage likelihood of shooting from a position by looking at all actions on a pitch, and seeing how many times a player shoots relative to other actions. If the player 99 times out of 100 passes the ball instead of shooting for said position, we can set the chance that the player scorores to zero. With this logic, we can assume that all shots happening in any of the cells with < 1% shooting probability did not result in a goal.
''')