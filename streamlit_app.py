import streamlit as st
import pandas as pd
import numpy as np

st.title(":blue[Players stats]")

# List creation
player=["Barella", "Lukaku", "Cuadrado", "Orsolini", "Locatelli"]
goals=[3, 11, 0, 11, 1]
assists=[6, 8, 2, 3, 2]
matches=[27, 29, 18, 23, 29]
distance=[12, 9, 8, 10, 6]
pass_accuracy=[86, 72, 84, 73, 89]

# Dataframe creation
player_dataframe={
    "player": player,
    "goals_scored": goals,
    "assists": assists,
    "matches_played": matches,
    "distance": distance,
    "pass_accuracy": pass_accuracy
}
df=pd.DataFrame(player_dataframe)

# Bar chart for goals
st.title('Goals')
st.bar_chart(df, x="player", y="goals_scored", x_label="Player's name", y_label="Goals scored")

# Line chart for matches and assists
st.title('Matches')
st.line_chart(df, x="player", y="matches_played", x_label="Player's name", y_label="Matches played")

st.title('Assists')
st.line_chart(df, x="player", y="assists", x_label="Player's name", y_label="Assists")

# Area chart for pass accuracy and average distance covered
st.title('Accuracy')
st.area_chart(df, x="player", y="pass_accuracy", x_label="Player's name", y_label="Pass accuracy [%]")

st.title('Distance covered')
st.area_chart(df, x="player", y="distance", x_label="Player's name", y_label="Distance covered [km]")

# Interactive element
chosen_player=st.selectbox('Choose a player to see his stats', player)
for n in range(len(player)):
    if chosen_player==player[n]:
        st.write(f'**Stats of {player[n]}**  \n'
                    f'Number of goals scored: {goals[n]}  \n'
                    f'Number of assists: {assists[n]}  \n'
                    f'Number of matches played: {matches[n]}  \n'
                    f'Distance covered: {distance[n]} km  \n'
                    f'Pass accuracy: {pass_accuracy[n]}%')

# Comparison
comparison=st.multiselect('**Choose more players to do a comparison**', player)
comparison_df=df[df['player'].isin(comparison)]
st.dataframe(comparison_df)