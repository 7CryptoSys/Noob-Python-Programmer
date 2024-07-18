import random

palavra = []
chance = 1

areas = int(input("""

      [1] Animais
      [2] Tecnologia
      [3] Plantas
      [4] Carros
      Escolha um numero:"""))

animais = ['cachorro', 'gato', 'elefante', 'leão', 'girafa', 'papagaio', 'tigre', 'macaco', 'zebra', 'coelho',
               'panda', 'leopardo', 'lobo', 'baleia', 'golfinho', 'pinguim', 'cobra', 'rinoceronte', 'esquilo', 'urso']

tecnologias = ['internet', 'smartphone', 'gps', 'wi-fi', 'bluetooth', 'streaming', 'tablet', 
                   'redes sociais', 'realidade virtual', 'cloud', 'robótica', 'impressora 3D', 
                   'backup', 'saas', 'chatbot', 'blockchain', 'e-commerce', 'smartwatch', 'drones', 
                   'inteligência artificial']


plantas = ['orquídea', 'samambaia', 'rosa', 'margarida', 'girassol', 'cacto', 'jasmim', 'violeta',
               'menta', 'lavanda', 'alecrim', 'manjericão', 'peônia', 'lírio', 'hortênsia', 'cipreste',
               'hera', 'bambu', 'papoula', 'gérbera']

carros = ['ferrari', 'lamborghini', 'porsche', 'bmw', 'mercedes-benz', 'audi', 'ford', 'chevrolet',
              'toyota', 'honda', 'nissan', 'mazda', 'subaru', 'volvo', 'tesla', 'volkswagen',
              'hyundai', 'kia', 'jeep', 'land rover']


def generate_choice(category) -> str:
  if areas == 1:
    return random.choice(animais)
  elif areas == 2: 
    return random.choice(tecnologias)
  elif areas == 3:
    return random.choice(plantas)
  elif areas == 4:
    return random.choice(carros)

palavra = generate_choice(areas)
palavra_new = list()
for char in list(palavra):
    palavra_new.append("*")
    
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
                palavra_new[indice] = letras_usuarios
    
    if areas == 2:
      print("Vamos ao jogo da forca a palavra abaixo")
      print(f"Esta palavra tem: {len(palavra)} letras")

      join_new = "".join(palavra_new)
      print(join_new)
      letras_usuarios = list(str(input("Digita a letra: ")))[0]

      if letras_usuarios in list(palavra):
          print("\n\nVocê acertou!\n\n")
        
      for indice in range(0, len(list(palavra))):
          if letras_usuarios == list(palavra)[indice]:
              palavra_new[indice] = letras_usuarios

    if areas == 3:
      print("Vamos ao jogo da forca a palavra abaixo")
      print(f"Esta palavra tem: {len(palavra)} letras")

      join_new = "".join(palavra_new)
      print(join_new)
      letras_usuarios = list(str(input("Digita a letra: ")))[0]

      if letras_usuarios in list(palavra):
          print("\n\nVocê acertou!\n\n")
        
      for indice in range(0, len(list(palavra))):
          if letras_usuarios == list(palavra)[indice]:
              palavra_new[indice] = letras_usuarios

    if areas == 4:
      print("Vamos ao jogo da forca a palavra abaixo")
      print(f"Esta palavra tem: {len(palavra)} letras")

      join_new = "".join(palavra_new)
      print(join_new)
      letras_usuarios = list(str(input("Digita a letra: ")))[0]

      if letras_usuarios in list(palavra):
          print("\n\nVocê acertou!\n\n")
        
      for indice in range(0, len(list(palavra))):
          if letras_usuarios == list(palavra)[indice]:
              palavra_new[indice] = letras_usuarios
