import json
from contato_gemma31b_copy import contato_lm_json

#Etapa 1
lista_de_resenhas =[]
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

'''print(lista_de_resenhas)
print("/n/n")
print(len(lista_de_resenhas))'''

#Etapa 2 e 3
lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = contato_lm_json(resenha)
    resenha_dic = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dic)

#Etapa 4

def contador_un(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_de_dicionarios_str = []

    for dicionario in lista_de_dicionarios:
        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas = contador_positivas + 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas = contador_negativas + 1
        else:
            contador_neutras = contador_neutras + 1
        
        lista_de_dicionarios_str.append(str(dicionario))

    
    textos_unid = "\\".join(lista_de_dicionarios_str)
    return contador_positivas, contador_negativas, contador_neutras, textos_unid

#Etapa 5
pos, neg, neut, textos = contador_un(lista_de_resenhas_json)

print(f"Positivas: {pos} \n Negativas: {neg} \n Neutras: {neut}")
print(textos)
print(lista_de_resenhas_json)