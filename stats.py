import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = "http://127.0.0.1:8000"

def stat_tab():
    st.subheader("Pokémon Stats Correlation Analysis")

    if st.button("Get Stats Analytics"):
        response = requests.post(f"{API_URL}/stats/")

        if response.status_code == 200:
            df = pd.DataFrame(response.json())

            # Select only stats column
            num_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed']
            correlation_matrix = df[num_cols].corr()

            # Create a heatmap for correlation analysis
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=1, ax=ax, annot_kws={"size": 10})

    
            ax.set_title("Correlation Between Pokémon Stats", fontsize=14)
        
            st.pyplot(fig)
        else:
            st.error("Failed to fetch stats data.")
