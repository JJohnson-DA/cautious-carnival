import streamlit as st
import pandas as pd


players = pd.read_csv("players.csv")

st.markdown("# Let's Pick Some Teams.")

with st.form("form"):
    st.subheader("Who's Playing?")
    all_players = st.checkbox("Use All Players", value=True)
    chosen_players_text = st.text_input(
        "OR...",
        placeholder="Enter names seperated by commas (ex. Scott, Adam, Lainy, Ryan).",
    )
    chosen_players = [x.strip() for x in chosen_players_text.split(",")]
    # chosen_players = st.multiselect(label="Select Players", options=players["Name"])

    if all_players:
        temp = players.shape[0]
    else:
        temp = len(chosen_players)

    select_opts = list(
        filter(None, [x if temp % x == 0 else None for x in range(2, temp)])
    )
    st.subheader("How Many Teams?")

    number_of_teams = int(
        st.select_slider(
            "",
            value=2,
            options=[1, 2, 3, 4, 5, 6],
            help="Select 1 team to get a randomized order of all player names.",
        ),
    )
    submit = st.form_submit_button("Create Teams")

if submit:
    if all_players:
        randomized = players.sample(n=players.shape[0]).reset_index(drop=True)

    else:
        randomized = (
            players[[x in chosen_players for x in players.Name]]
            .sample(n=len(chosen_players))
            .reset_index(drop=True)
        )

    if randomized.shape[0] % number_of_teams != 0:
        st.warning(
            "Players per team is not even, add more players or lower the number of teams."
        )
    else:
        players_per_team = randomized.shape[0] // number_of_teams

        cols = st.columns(number_of_teams)

        for i in range(1, number_of_teams + 1):
            with cols[i - 1]:
                subset = randomized.iloc[:players_per_team]
                randomized = randomized.drop(range(0, players_per_team)).reset_index(
                    drop=True
                )
                st.subheader(f"Team {i}")
                st.write(", ".join([str(x) for x in subset.Name]))
