# class ActionProximoJogo(Action):
#     def name(self) -> str:
#         return "action_proximo_jogo"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict) -> list:
#
#         response = requests.get("http://localhost:3000/matches")
#         data = response.json()
#
#         if data:
#             jogo = data[0]
#             resposta = f"O próximo jogo da FURIA é contra {jogo['team1']['name']} no evento {jogo.get('event', {}).get('name', 'desconhecido')}."
#         else:
#             resposta = "A FURIA não tem jogos agendados no momento."
#
#         dispatcher.utter_message(text=resposta)
#         return []
#
# class ActionResultadosRecentes(Action):
#     def name(self) -> str:
#         return "action_resultados_recentes"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict) -> list:
#         response = requests.get("http://localhost:3000/results")
#         data = response.json()
#         resposta = data
#         dispatcher.utter_message(text=resposta)
#         return []


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import os

DATA_SERVER_URL = os.getenv("DATA_SERVER_URL")

class ActionInformLineup(Action):
    def name(self) -> str:
        return "action_inform_lineup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        try:
            response = requests.get(f"{DATA_SERVER_URL}/team")
            team_data = response.json()

            jogadores = [
                p["name"]
                for p in team_data.get("players", [])
                if p.get("type") == "Starter"
            ]

            if jogadores:
                nomes = ", ".join(jogadores)
                resposta = f"A line-up atual da FURIA é composta por: {nomes}."
            else:
                resposta = "Não consegui encontrar a line-up atual da FURIA."

        except Exception as e:
            print(f"Erro ao buscar line-up: {e}")
            resposta = "Ocorreu um erro ao tentar obter a line-up da FURIA."

        dispatcher.utter_message(text=resposta)
        return []

class ActionFallbackLLM(Action):
    def name(self):
        return "action_fallback_llm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        user_msg = next(
            (e['text'] for e in reversed(tracker.events) if e.get('event') == 'user' and e.get('text')),
            "Desculpe, não consegui entender sua pergunta."
        )

        #user_msg = tracker.latest_message.get("text")
        print(f"📤 Enviando para o servidor Node.js: {user_msg}")

        try:
            print(user_msg)
            response = requests.post(f"{DATA_SERVER_URL}/llm", json={
                "question": f"{user_msg.strip()} (sobre o time de CS:GO da FURIA)."
            })

            if response.status_code == 200:
                resposta = response.json()
                dispatcher.utter_message(text=resposta.get("answer", "Não entendi a resposta da IA."))
            else:
                print(f"⚠️ Erro no servidor Node.js: {response.status_code} - {response.text}")
                dispatcher.utter_message(text="Tive um problema para responder agora. Tente novamente em breve.")

        except Exception as e:
            print(f"❌ Erro ao consultar seu backend: {e}")
            dispatcher.utter_message(text="Não consegui falar com o servidor. Tente novamente mais tarde.")

        return []
