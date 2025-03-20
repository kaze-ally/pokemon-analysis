import streamlit as st
import db_pokemon
from f_poke import find_pokemon_tab
from top_10 import find_top_10
from gen import gen_tab
from type import type_tab
from stats import stat_tab
API_URL="http://127.0.0.1:8000"
st.title("Pokemon Analysis System")
tab1,tab2,tab3,tab4,tab5=st.tabs(["find_pokemon","top_10","stats","type","generation"])
with tab1:
    find_pokemon_tab()
with tab2:
    find_top_10()
with tab3:
    stat_tab()
with tab4:
    type_tab()
with tab5:
    gen_tab()
