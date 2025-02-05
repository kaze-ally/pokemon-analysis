import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = "http://127.0.0.1:8000"

def gen_tab():
    st.subheader("Pokémon Distribution by Generation")

    if st.button("Get Generation Analytics"):
        response = requests.get(f"{API_URL}/generation/")

        if response.status_code == 200:
            data = response.json()
            df=pd.DataFrame(data)
            generations = ["1", "2", "3", "4", "5", "6"]
            df["Generation"] = generations
            df = df.set_index("Generation")

            # Create a better bar plot using Seaborn
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x=df.index, y=df["#"], ax=ax, palette="viridis")

            # titles and labels
            ax.set_title("Generation-wise Pokémon Distribution", fontsize=14)
            ax.set_xlabel("Generation", fontsize=12)
            ax.set_ylabel("Number of Pokémon", fontsize=12)

            # Display the plot
            st.pyplot(fig)
            new_columns=["number of pokemons"]
            df.columns=new_columns
            # Show data table
            st.dataframe(df)
        else:
            st.error("Failed to fetch generation data.")
