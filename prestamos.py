dinero_prestamo = float(input("Introduce cantidad de dinero deseado: "))
anos = float(input("Introduce los años a pagar: "))
tasa_interes_anual = 5/100
r = float(tasa_interes_anual/12)
n = float(anos*12)
pago_mensual =  dinero_prestamo*(r*(1+r)**n) / ((1+r)**n - 1)
print("Al mes debes pagar:", pago_mensual, "€")