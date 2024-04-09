import te

te_negro = te.Te()
te_verde = te.Te()

tipo_1 = type(te_negro.preparacion(1))
tipo_2 = type(te_verde.preparacion(2))

print(tipo_1)
print(tipo_2)

if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")