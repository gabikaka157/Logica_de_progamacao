distancia= float(input('em km, qual a distancia da sua viagem '))
if distancia<=200:
    print("o valor da sua passagem sera {} reais".format(distancia*0.50))
else:
    print("o valor da sua passagem sera {} reais".format(distancia*0.45))