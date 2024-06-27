Unknown_words = {
                "Vate": "adivino, poeta",
                "Mesticia": "aflicción, pena, tristeza",
                "Yerto": "tieso, rígido, áspero",
                "Popar": "despreciar o tener en poco a alguien",
                "Escozor": "sensación parecida a la causada por quemadura",
                "Licurgo": "inteligente, astuto, hábil",
                }
print("Hola usuario, vamos a ver que palabras no conoces, ahora vas a escribir palabras que no conozcas")

for i in range(5):
    word = input("escribe la palabra que no conozcas")
    if word in Unknown_words.keys():
        print(Unknown_words[word])
    else:
        print("Esa palabra no la conozco")
