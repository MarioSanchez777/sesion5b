print("digite una entrada cualquiera\n")
try:
  entrada = int(input())
  if type(entrada) == "<class 'int'>":
    print(entrada)
except:
  print("no es entero")
print("fin de la ejecucion")