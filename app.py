from flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character_dict = {
            "name": character["name"],
            "status": character["status"]

        }
        characters.append(character_dict)

    return {"characters": characters}