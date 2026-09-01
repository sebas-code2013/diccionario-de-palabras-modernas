meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "67" : "expresion sin sentido que se utilizo como humor",
            "BRAINROT": "se refiere a un genero de contenido hiperestimulante para los niños",
            "AURA" : "significa que una persona hiso algo que la vuelve muy genial",
            "FARMEAR" : "generar mucho de algo"
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("fatal error: palabra no encontrada")
