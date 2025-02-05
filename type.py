import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = "http://127.0.0.1:8000"

def fetch_response():
    """Fetch Pokémon type distribution data from the API."""
    response = requests.post(f"{API_URL}/type/")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None

def type_tab():
    st.subheader("Pokémon Type Distribution")

    # User selects the type of analysis
    option = st.radio("Select an analysis:", [
        "Primary Type Distribution",
        "Secondary Type Distribution",
        "Both Type Analysis"
    ])

    df = fetch_response()

    if df is not None:
        if option == "Primary Type Distribution":
            df_type_1 = df["Type 1"].value_counts().reset_index()
            df_type_1.columns = ["Type", "Count"]

            # Create a pie chart for Primary Type Distribution
            fig, ax = plt.subplots(figsize=(7, 7))
            ax.pie(df_type_1["Count"], labels=df_type_1["Type"], autopct='%1.1f%%', colors=sns.color_palette("tab10"))
            ax.set_title("Primary Type Distribution")

            st.pyplot(fig)

        elif option == "Secondary Type Distribution":
            df_type_2 = df["Type 2"].value_counts().reset_index()
            df_type_2.columns = ["Type", "Count"]

            # Create a pie chart for Secondary Type Distribution
            fig, ax = plt.subplots(figsize=(7, 7))
            ax.pie(df_type_2["Count"], labels=df_type_2["Type"], autopct='%1.1f%%', colors=sns.color_palette("tab10"))
            ax.set_title("Secondary Type Distribution")

            st.pyplot(fig)

        elif option== "Both Type Analysis":
            fig, ax = plt.subplots(figsize=(24, 12))
            
            type1_counts = df["Type 1"].value_counts()
            type2_counts = df["Type 2"].value_counts()

            # Combine both counts into a single DataFrame
            type_counts = pd.DataFrame({"Primary Type": type1_counts, "Secondary Type": type2_counts})

            # Plot the grouped bar chart
            type_counts.plot(kind="bar", stacked=False, width=0.8, figsize=(12, 6), colormap="viridis",ax=ax,
            xlabel="Pokémon Type",ylabel="count",legend="TYPe Category")

            ax.set_title("Comparison of Primary and Secondary Pokémon Types", fontsize=14)
            st.pyplot(fig)
    else:
        st.error("Failed to fetch type data.")
