from fila import *


f = criar_fila()
enfileirar(f, "XYZ")
enfileirar(f, "ABC")
enfileirar(f, "KKK")
mostrar_fila(f)
v1 = desenfileirar(f)
enfileirar(f, "IF")
mostrar_fila(f)