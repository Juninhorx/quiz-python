import json
import time

def verificaResposta(resposta):
  opcoes_validas = ["A", "B", "C", "D", "DESISTO"]
  if resposta in opcoes_validas:
      return True
  else:
      return False
  

with open('questions.json', 'r', encoding='utf-8') as file:
    quetoesJson = json.load(file)

questoes = quetoesJson['questoes']

pontos = 0
nQuestoes = 0

print('####### QUIZ #######')
usuario = input('Para começar, digite o seu nome: ')
print(f'\nOlá {usuario}, responda 15 questôes sobre o tema "ESPORTES". \n')

for i, questao in enumerate(questoes, 1):
    time.sleep(1)
    nQuestoes += 1
    print(f"Questão {i}: {questao['pergunta']} \n")
    print("a)", questao['alternativaA'])
    print("b)", questao['alternativaB'])
    print("c)", questao['alternativaC'])
    print("d)", questao['alternativaD'], '\n')

    altResposta = input('Resposta: ').upper()
    resposta_correta = questao['resposta_correta']

    if verificaResposta(altResposta) == False:
        print('\nRESPOSTA INVÁLIDA! \n RESPONDA COM: \n "A"\n "B"\n "C"\n "D"\n "DESISTO \n"')
        altResposta = input('Resposta: ').upper()
        
    if (altResposta == resposta_correta):
        time.sleep(1)
        print(f'\n{usuario} sua resposta está CORRETA. \n')
        pontos += 1
    elif (altResposta == 'DESISTO'):
        print('\n Você desistiu!')
        quit()
    else:
        time.sleep(1)
        print(f'\n{usuario} sua resposta está ERRADA. \n')

percentual = (100 / nQuestoes) * pontos

print('Fim de Jogo!\n')
print(f'Você acertou {pontos} questôes! \n')
if percentual >= 85:
    print(f'VOCÊ VENCEU! Com {percentual:.1f}% de acertos!')
    print('\n \n')
    quit()
print(f'VOCÊ PERDEU! Com {percentual:.1f}% de acertos.')
print('\n \n')

        

