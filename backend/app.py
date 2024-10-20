from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
import math
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permita todas as origens ou especifique
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE_PATH = 'characters.json'

class CharacterModel(BaseModel):
    name: str
    race: str
    character_class: str
    level: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    health_points: int
    inventory: List[str] = []
    skills: dict = {}
    trained_skills: List[str] = []

def load_characters():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_characters(characters):
    with open(FILE_PATH, 'w') as file:
        json.dump(characters, file, indent=4)

@app.get("/characters", response_model=List[CharacterModel])
async def get_characters():
    return load_characters()

@app.post("/characters", response_model=CharacterModel)
async def create_character(character: CharacterModel):
    characters = load_characters()
    new_character = character.dict()
    characters.append(new_character)
    save_characters(characters)
    return new_character

@app.get("/characters/{char_id}", response_model=CharacterModel)
async def get_character(char_id: int):
    characters = load_characters()
    if 0 <= char_id < len(characters):
        return characters[char_id]
    raise HTTPException(status_code=404, detail="Character not found")

@app.put("/characters/{char_id}", response_model=CharacterModel)
async def update_character(char_id: int, character: CharacterModel):
    characters = load_characters()
    if 0 <= char_id < len(characters):
        updated_character = character.dict()
        characters[char_id] = updated_character
        save_characters(characters)
        return updated_character
    raise HTTPException(status_code=404, detail="Character not found")
