import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def find_top_10():
    st.subheader("Top 10 Pokémon by Stat")
    
    # Use dropdown 
    selected_stat = st.selectbox("Select Stat", ["HP", "Attack", "Defense","Sp_Atk", "Sp_Def", "Speed"])

    if st.button("Show Top 10"):
        response = requests.get(f"{API_URL}/top_10/{selected_stat}")

        if response.status_code == 200:
            data = response.json()
            if not data:
                st.warning("No Pokémon found.")
            else:
                df = pd.DataFrame(data)
                # Display as a bar chart
                st.bar_chart(df.set_index("Name")[selected_stat])
                
                # Show detailed table
                st.dataframe(df)
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
