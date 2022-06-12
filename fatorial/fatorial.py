num = int(input("Digite um número: "))
i = 1
fatorial = num 

while i < num : 
    fatorial *= (num-i)
    i += 1 
print("O fatorial de", num, "é: ",fatorial)