import json
import os

caminho1 = os.path.dirname(os.path.abspath(__file__))
caminho2 = os.path.join(caminho1, 'toprichest.json')
with open (caminho2, 'r', encoding='utf-8') as file:
    dados = json.load(file)

top = int(input('Qual TOP você quer ver? (1 - 10, caso for todos digite 0:)\n'))
os.system('cls')
if top == 0:
    for indice, dado in enumerate (dados, start=1):
        print('\nTop:', dados[indice - 1]['TOP:'])
        print('Nome:', dados[indice - 1]['Nome:'])
        print('Fortuna:', dados[indice - 1]['Fortuna:'],'\n')
else:
    print('Top:', dados[top - 1]['TOP:'])
    print('Nome:', dados[top - 1]['Nome:'])
    print('Fortuna:', dados[top - 1]['Fortuna:'])
