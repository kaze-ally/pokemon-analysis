from fastapi import FastAPI, HTTPException
from datetime import date
import db_pokemon
from typing import List
from pydantic import BaseModel
app=FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

class GenerationRecord(BaseModel):
    Generation: int
    Count: int

@app.get("/generation/")
def get_gen():
    df_gen=db_pokemon.gen()
    return df_gen


@app.get("/find_pokemon/{Type1}/{Type2}")
def get_pokemon(Type1,Type2):
    sorted_pokemon=db_pokemon.get_pokemon(Type1,Type2)
    return sorted_pokemon



@app.get("/top_10/{stat}")
def get_top(stat):
    df_top=db_pokemon.get_top_10(stat)
    return df_top

@app.post("/stats/")
def get_heat():
    df_stat=db_pokemon.get_stat()
    return df_stat

@app.post("/type/")
def get_gen():
    df_type=db_pokemon.type_()
    return df_type

