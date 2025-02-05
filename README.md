
# Pokemon Analysis System

# Overview

This project is a Pokemon Analysis System built using Streamlit for the frontend and FastAPI for the backend. It allows users to analyze Pokemon stats, find top-performing Pokemon, visualize type distributions, and interact with an API for data retrieval.

## Features

### Streamlit App (Frontend)

Find Pokemon by Type: Search Pokemon based on their primary and secondary types.

Top 10 Pokemon by Stat: View the top 10 Pokemon based on user-selected stats (HP, Attack, Defense, etc.).

Stats Correlation Analysis: Analyze how different Pokemon stats correlate using heatmaps.

Type Distribution: View pie charts for primary and secondary type distributions.

Generation Breakdown: Check how many Pokemon exist in each generation.

### FastAPI (Backend)

GET /generation/ - Retrieves the count of Pokemon per generation.

GET /find_pokemon/{Type1}/{Type2} - Finds Pokemon based on primary and secondary type.

GET /top_10/{stat} - Fetches the top 10 Pokemon based on a selected stat.

POST /stats/ - Provides Pokemon stats for heatmap analysis.

POST /type/ - Returns the type distribution of Pokemon.

## 📂 Dataset  
The dataset contains Pokémon species and their base stats, including HP, Attack, Defense, Speed, etc. 

