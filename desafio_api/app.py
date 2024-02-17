from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)
# https://rickandmortyapi.com/documentation/#rest
# 1. DEFINIÇÕES
# A API possui três endpoints: um para listar os personagens, um para
# listar as localizações e dimensões e um para listar os episódios. Durante
# a aula, utilizamos apenas o endpoint de personagens.
# O objetivo deste exercício é adicionar novas funcionalidades ao projeto.
# Você deverá adicionar uma página para listar as localizações e os
# episódios, além de melhorar a página de perfil do personagem.
# Para isso, você deverá:
# 1. Criar uma nova rota para listar as localizações. A rota deverá ser
# acessível através do caminho /locations. A página deverá ser
# renderizada através do template locations.html. A página deverá
# conter uma tabela com as seguintes informações: nome, tipo e
# dimensão. A tabela deverá conter um link para a página de perfil
# da localização.
@app.route("/locations.html")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response_data = urllib.request.urlopen(url)
    data = json.loads(response_data.read())

    locations_data = []

    for location in data["results"]:
        id = location["id"]
        name = location["name"]
        dimension = location["dimension"]
        type = location["type"]
        locations_data.append({"id": id, "name": name, "dimension": dimension, "type": type})
    return render_template("locations.html", locations=locations_data)

@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response_data = urllib.request.urlopen(url)
    data = json.loads(response_data.read())

    character_names = []
    for character_url in data["residents"]:
        character_response = urllib.request.urlopen(character_url)
        character_data = json.loads(character_response.read())
        character_names.append(character_data["name"])

    return render_template("location.html", location=data, character_names=character_names)