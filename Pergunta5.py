string_original = "Ramonie"  # exemplo de string original

string_invertida = ""  # string que irá armazenar a string invertida

# percorre a string original de trás para frente, adicionando cada caractere na string invertida
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

print(string_invertida)  # imprime a string invertida
