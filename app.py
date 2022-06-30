import streamlit as st
from random import shuffle

st.markdown("# Let's Pick Some Teams.")

with st.form("form"):
    st.subheader("Who's Playing?")

    # Get player names from user
    chosen_players_text = st.text_input(
        "",
        placeholder="Enter names seperated by commas (ex. Scott, Adam, Lainy, Ryan).",
    )

    # Split names into list
    chosen_players = [x.strip() for x in chosen_players_text.split(",")]

    # select_opts = list(
    #     filter(
    #         None, [x if num_players % x == 0 else None for x in range(2, num_players)]
    #     )
    # )

    st.subheader("How Many Teams?")

    # Get number of teams from user
    number_of_teams = int(
        st.select_slider(
            "",
            value=2,
            options=[
                1,
                2,
                3,
                4,
                5,
                6,
            ],  # this needs to be swapped for dynamically created list
            help="Select 1 team to get a randomized order of all player names.",
        ),
    )
    submit = st.form_submit_button("Create Teams")

if submit:
    # Randomize order of players
    shuffle(chosen_players)

    # Check that teams would be even numbers
    if len(chosen_players) % number_of_teams != 0:
        st.warning(
            "Players per team is not even, add more players or change the number of teams."
        )
    else:
        # Determine players per team
        players_per_team = len(chosen_players) // number_of_teams

        # Create column structure to display teams
        cols = st.columns(number_of_teams)

        # loop through players
        for i in range(1, number_of_teams + 1):
            # Iterate over the correct column
            with cols[i - 1]:
                # Slice off the first n players
                subset = chosen_players[0:players_per_team]
                # Trim down the player list
                chosen_players = chosen_players[players_per_team:]
                # Display Team
                st.subheader(f"Team {i}")
                st.write(", ".join([str(x) for x in subset]))
