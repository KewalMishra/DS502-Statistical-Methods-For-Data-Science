import pandas as pd
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
from PIL import Image
from helper import load_data, load_old_data, draw_pitch_mpl, draw_pitch_plotly

def feature_engineering():    
    st.title('Feature engineering :factory_worker:')

    st.header('Pitch coordinates transformation')
    st.markdown('###')
    st.text('''The pitch coordinates in the dataset are transformed to map 
onto a standard soccer pitch with dimensions of 53 m and 34 m.
      ''')

    code = '''
    xStart = -53
    xEnd = 53
    yStart = -34
    yEnd = 34
    xLength = xEnd - xStart
    yLength = yEnd - yStart

    # Covert Default Coordinates
    df_Shots['position_xM'] = (xLength/2)-(df_Shots['position_x'])
    df_Shots['position_yM'] = (df_Shots['position_y'] / df_Shots['position_y'].max()
                            ) * (yLength/2)
    '''

    # Create an expander with the code snippet
    with st.expander("Click to show code"):
        st.code(code, language='python')
    data = load_data()
    df_op_Shots = data[(data['play_type'] == 'Open Play')].copy()
    df_op_Shots = df_op_Shots[df_op_Shots['BodyPart'] != 'Other']
    df_op_Shots = df_op_Shots[df_op_Shots['Interference_on_Shooter'] != 'Unknown']
    df= df_op_Shots

    ## Define bins
    bins= [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,110]
    df['distance_to_goalM_binned'] = pd.cut(df['distance_to_goalM'], bins)

    ## Create ID attribute
    df['idx'] = range(1, len(df) + 1)

    ## Group and Aggregate data
    df_grouped = (df.groupby('distance_to_goalM_binned')
                    .agg({'idx': 'count',
                        'isGoal': 'sum'
                        }
                        )
                    .reset_index()
                    .rename(columns={'idx': 'shots',
                                    'isGoal': 'goals'
                                    }
                        )
                    .sort_values(by='distance_to_goalM_binned', ascending=True)
                )

    ## Clean binned attribute
    df_grouped['distance_to_goalM_binned'] = df_grouped['distance_to_goalM_binned'].astype(str).str.replace('(', '').str.replace(']', '').str.replace(', ', '-')

    ## Create 'ratio_Goals_shots' attribute
    df_grouped['ratio_goals_shots'] = df_grouped['goals'] / df_grouped['shots']

    ## Assign final DataFrame to specific DataFrame
    df_distance = df_grouped

    ## Display DataFrame

    show_data = st.checkbox('Show Data')
    if show_data:
        st.table(df_distance.head(10))

    st.subheader('Visualise the probability of scoring from different points')
    options = st.selectbox('Point of analysis',[
        'Distance to the Goal',
        'Y Coordinate',
        'Distance to the Center of the Pitch',
        'Angle of the Shot',
        'Number of Intervening Opponents',
        'Number of Intervening Teammates',
        'Interference on Shooter',
        'Header Distance to the Goal'
    ])
    if options == 'Y Coordinate':
        image = Image.open('fe2.png')
        st.image(image)
    if options == 'Distance to the Center of the Pitch':
        image = Image.open('fe3.png')
        st.image(image)
    if options == 'Angle of the Shot':
        image = Image.open('fe4.png')
        st.image(image)
    if options == 'Number of Intervening Opponents':
        image = Image.open('fe5.png')
        st.image(image)
    if options == 'Number of Intervening Teammates':
        image = Image.open('fe6.png')
        st.image(image)
    if options == 'Interference on Shooter':
        image = Image.open('fe7.png')
        st.image(image)
    if options == 'Header Distance to the Goal':
        image = Image.open('fe8.png')
        st.image(image)

    if options == 'Distance to the Goal':
        df = df_distance
        x_axis_bar = df['distance_to_goalM_binned']
        y_axis_bar = df['shots']
        x_axis_line = df['distance_to_goalM_binned']
        y_axis_line = df['ratio_goals_shots']

        ## Set background colour
        background = 'aliceblue'

        ## Create figure 
        fig, ax = plt.subplots(figsize=(15, 8))
        fig.set_facecolor(background)

        ## Set Gridlines 
        ax.grid(linewidth=0.25, color='k', zorder=1)

        ## Create Bar Chart
        ax.bar(x_axis_bar,
            y_axis_bar,
            edgecolor='midnightblue',
            color='steelblue'
            )


        ## Set subplot face colour
        ax.patch.set_facecolor(background)

        ## Twin object for two different y-axis on the sample plot
        ax2 = ax.twinx()

        ## Create Line Chart
        ax2.plot(x_axis_line,
                y_axis_line,
                color='orange',
                linewidth='3',
                marker='o',
                markersize='10',
                label='Goals to Shots Ratio'
                )

        ## Axis
        plt.xlim(('0-2', '60-110'))
        plt.ylim((0))

        ## Set title
        ax.set_title('Distance to the Goal Line in Meters',
                    loc='center',
                    color='midnightblue', 
                    fontweight='bold',
                    fontfamily='DejaVu Sans',
                    fontsize=22,
                    )

        ## Set Gridlines 
        ax.grid(linewidth=0.25, color='k', zorder=1)

        ## X and Y Labels
        ax.set_xlabel('Distance (Bucketed)', color='midnightblue', fontfamily='DejaVu Sans', fontsize=16)
        ax.set_ylabel('No. Shots', color='midnightblue', fontfamily='DejaVu Sans', fontsize=16)
        ax2.set_ylabel('Probability to Score', color='midnightblue', fontfamily='DejaVu Sans', fontsize=16)

        ## Show figure
        plt.tight_layout()
        st.write(fig)
