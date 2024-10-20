document.getElementById("character-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const race = document.getElementById("race").value;
    const characterClass = document.getElementById("class").value;
    const level = parseInt(document.getElementById("level").value);
    const strength = parseInt(document.getElementById("strength").value);
    const dexterity = parseInt(document.getElementById("dexterity").value);
    const constitution = parseInt(document.getElementById("constitution").value);
    const intelligence = parseInt(document.getElementById("intelligence").value);
    const wisdom = parseInt(document.getElementById("wisdom").value);
    const charisma = parseInt(document.getElementById("charisma").value);
    const health_points = parseInt(document.getElementById("health_points").value);

    const newCharacter = {
        name,
        race,
        character_class: characterClass,
        level,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        health_points,
    };

    const response = await fetch("http://localhost:8000/characters", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newCharacter),
    });

    if (response.ok) {
        const createdCharacter = await response.json();
        console.log("Character created:", createdCharacter);
        loadCharacters(); // Atualizar a lista
    } else {
        console.error("Error creating character:", response.statusText);
    }
});

// Função para carregar personagens
async function loadCharacters() {
    const response = await fetch("http://localhost:8000/characters");
    const characters = await response.json();
    const characterList = document.getElementById("character-list");
    characterList.innerHTML = "";

    characters.forEach(character => {
        const li = document.createElement("li");
        li.textContent = `${character.name} - ${character.race} - ${character.character_class}`;
        characterList.appendChild(li);
    });
}

// Carregar personagens ao iniciar
loadCharacters();
