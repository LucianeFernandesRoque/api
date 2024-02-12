from flask import Flask
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
@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    dict = json.loads(response.read())
    
    return json.dumps(dict)