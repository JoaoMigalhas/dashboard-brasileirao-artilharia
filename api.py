import pandas as pd
import json
import requests

#configurar aA API

API_KEY = "{sua chave aqui}" #coloque sua chave aqui

headers = {"X-Auth-Token": API_KEY}

url = "https://api.football-data.org/v4/competitions/BSA/scorers"

print("Fazendo requisicao...")

response = requests.get(url, headers=headers)

print(f"Exibir status do GET: {response.status_code}")

if response.status_code != 200:
    print("Erro ao conectar!")
    print(response.json())
else:
    print("Deu certo!")

    data = response.json()

    print("Estrutura dos dados:")
    print(json.dumps(data, indent=2, ensure_ascii=False))


    jogadores = []

    for item in data["scorers"]:

        jogadores.append({
            "jogador": item["player"]["name"],
            "time": item["team"]["name"],
            "gols": item["goals"],
            "assistencias": item.get("assists") or 0,
            "jogos": item["playedMatches"]
        })


    df = pd.DataFrame(jogadores)

    print("Previa dos dados:")
    print(df.head(10))

    df.to_csv("data/jogadores.csv", index=False)

