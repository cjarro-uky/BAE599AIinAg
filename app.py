import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="FIFA World Cup Team Appearances", layout="centered")

# Title and introduction

# Title with FIFA logo
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/FIFA_logo_without_slogan.svg", width=60)
with col2:
    st.title("FIFA World Cup Team Appearances")
st.write("Welcome! This site highlights the 'team_appearances.csv' dataset, which I find interesting.")

# Display image
st.image("20250619_103700.jpg", caption="My Image", use_container_width=True)

# Load and display dataset
st.header("Team Appearances Dataset")
try:
    df = pd.read_csv("team_appearances.csv")

    # Dropdown to select team type
    gender = st.selectbox(
        "Select team type:",
        ("Men's teams", "Women's teams", "Both")
    )

    # Filter dataframe based on selection
    if gender == "Men's teams":
        df_filtered = df[df['tournament_name'].str.contains("Men", case=False, na=False)]
    elif gender == "Women's teams":
        df_filtered = df[df['tournament_name'].str.contains("Women", case=False, na=False)]
    else:
        df_filtered = df.copy()

    # Country statistics table
    stats = df_filtered.groupby(['team_name', 'team_code']).agg(
        games_played = ('match_id', 'count'),
        wins = ('win', 'sum'),
        losses = ('lose', 'sum'),
        ties = ('draw', 'sum')
    ).reset_index()

    def code_to_flag(code):
        if isinstance(code, str) and len(code) == 3:
            return ''.join([chr(127397 + ord(c.upper())) for c in code])
        return ''
    stats['flag'] = stats['team_code'].apply(code_to_flag)

    st.header("Country Statistics")
    st.write("Below are the total games played, wins, losses, ties, and flag for each country:")
    st.dataframe(stats)

    # World Cups Won table (filtered)
    wc_winners = df_filtered[(df_filtered['stage_name'].str.lower() == 'final') & (df_filtered['win'] == 1)]
    cups_won = wc_winners.groupby('team_name').agg(
        cups_won = ('match_id', 'count'),
        years = ('match_date', lambda x: ', '.join(sorted(set(pd.to_datetime(x).dt.year.astype(str)))) )
    ).reset_index()
    cups_won = cups_won[cups_won['cups_won'] > 0]
    if not cups_won.empty:
        st.header("World Cups Won 🏆")
        st.write("Countries that have won at least one World Cup:")
        st.dataframe(cups_won)

    st.header("Team Appearances Dataset")
    st.dataframe(df)
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Calculate statistics for each country
    stats = df.groupby('team_name').agg(
        games_played = ('match_id', 'count'),
        wins = ('win', 'sum'),
        losses = ('lose', 'sum'),
        ties = ('draw', 'sum')
    ).reset_index()

except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Footer
st.markdown("---")
st.write("Created with Streamlit.")
