
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def find_pokemon_tab():
    st.subheader("Find Pokémon by Type")
    
    # Use dropdowns 
    pokemon_types = ["None","Fire", "Water", "Grass", "Electric", "Flying", "Normal","Psychic", 'Ghost',"Ground", "Rock", "Ice", "Bug", "Dragon", "Dark", "Steel", "Fairy","Poison","Fighting"]
    pokemon_type_1 = ["Fire", "Water", "Grass", "Electric", "Flying","Normal","Psychic","Ghost", "Ground", "Rock", "Ice", "Bug", "Dragon", "Dark", "Steel", "Fairy","Poison","Fighting"]
    selected_type_1 = st.selectbox("Select Primary Type", pokemon_type_1)
    selected_type_2 = st.selectbox("Select Secondary Type", pokemon_types)

    if st.button("Find Pokémon"):
        payload = {"T1": selected_type_1, "T2": selected_type_2}
        response = requests.post(f"{API_URL}/find_pokemon/", json=payload)

        if response.status_code == 404:
            response = requests.get(f"{API_URL}/find_pokemon/{selected_type_1}/{selected_type_2}")

        if response.status_code == 200:
            try:
                data = response.json()
                if not data:
                    st.warning("No Pokémon found for the given types.")
                else:
                    df = pd.DataFrame(data)
                    st.dataframe(df) 

                    # Display Pokémon images if names are available and correctly pronounced
                    for index, row in df.iterrows():
                        pokemon_name = row["Name"]
                        st.image(f"https://img.pokemondb.net/sprites/home/normal/{pokemon_name.lower()}.png", caption=pokemon_name)
            except Exception as e:
                st.error(f"Error parsing JSON: {e}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")



      