palavra = "ATGCATGAATGTAG"

trio = []
for i in range(0, len(palavra), 3):
    trio.append(palavra[i:i+3])  # Adiciona a substring de 3 caracteres


print(' '.join(trio))
