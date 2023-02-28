import Metodosinterno as burbuja

B = burbuja.MetodosInterno()

arreglo = [87,39,96,19,45,21,16,62]

"""
Estado inicial:
87|39|96|19|45|21|16|62 <-0

Primera iteración:
aux = 39
39<87
final
Intercambio ->  39|87|96|19|45|21|16|62

Segunda Iteración:
aux = 96
96<87 no
96<39 no

Tercera Iteración:
aux = 19
19<96
19<87
19<39
final
intercambio ->  19|39|87|96|45|21|16|62 

Cuarta Iteración:
aux = 45
45<96
45<87
45<39 no
intercambio -> 19|39|45|87|96|21|16|62

Quinta Iteración:
aux = 21
21<96
21<87
21<45
21<39
21<19 no
intercambio -> 19|21|39|45|87|96|16|62

Sexta Iteración:
aux = 16
16<96
16<87
16<45
16<39
16<21
16<19
final
intercambio -> 16|19|21|39|45|87|96|62

Séptima Iteración:
aux = 62
62<96
62<87
62<45 no
Intercambio -> 16|19|21|39|45|62|87|96

"""
