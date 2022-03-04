import os
import gato, cachorro, papagaio


os.system('cls')

gato = gato.Gato('skar', 3, 7)
cachorro = cachorro.Cachorro('bob', 5, 10)
papagaio = papagaio.Papagaio('raimundo', 7, 2)

gato.miar()
cachorro.latir()
papagaio.falar()