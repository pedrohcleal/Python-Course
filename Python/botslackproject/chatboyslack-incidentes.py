from extrairdados import *
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)  #carrega a token do bot

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel= '#botslack', text=f"""
Olá Service Desk e compania, a seguir dados do Ajudaki:
Incidentes ->
Chamados: 
Em andamento: {andamento:.0f}
Em espera: {espera:.0f}
Sem Atribuição: {sem_atrib:.0f}

Estado:
Critíco: {criticos:.0f}
Moderado: {moderados:.0f}
Baixo: {baixos:.0f} 

Requisições ->


""")

