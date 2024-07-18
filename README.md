# Hangman game
Para este código de jogo da forca, eu usei repetição while, a biblioteca random e seus modulos, join e choice além de usar def, e listas contendo 20 nomes de animais, carros, coisas sobre tecnologia e plantas, usei for e range e append, nesta parte do codigo eu defino quais serão as condições caso uma categoria seja escolhida, e depois eu declaro que a váriavel "Palavra" que contem uma tupla, eu transformo em list e falo que ela será a função ''generate_choice" crio a váriavel "palavras_new" e defino como uma lista que vai manter as palavras escondidas, e em ''for char in list(palavra) será adicionado (append) um * sendo a palavra censurada, exemplo: Palavra tem 20 caracteres, então será 20 *

### Example

 ```py
while chance != 15:
    chance += 1

    if areas == 1:
        print("Vamos ao jogo da forca a palavra abaixo")
        print(f"Esta palavra tem: {len(palavra)} letras")

        join_new = "".join(palavra_new)
        print(join_new)
        letras_usuarios = list(str(input("Digita a letra: ")))[0]

        if letras_usuarios in list(palavra):
            print("\n\nVocê acertou!\n\n")
        
        for indice in range(0, len(list(palavra))):
            if letras_usuarios == list(palavra)[indice]:
                palavra_new[indice] = letras_usuarios ```
 
 
            
