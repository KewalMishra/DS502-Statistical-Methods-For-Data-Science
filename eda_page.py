import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from helper import load_data, draw_pitch_mpl, draw_pitch_plotly

def eda():
    st.sidebar.markdown('#')
    st.title('Exploratory Dataa Analysis on football dataset')

    data = load_data()

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

    st.markdown('####')
    
    daily_avg_sent_exp = st.expander('Data insight')
    daily_avg_sent_exp.write('More than 11,000 Shots in the Dataset.')

    st.markdown('###')
