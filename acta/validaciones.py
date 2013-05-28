#-*- coding: utf-8 -*-


def cedula_valida(cedula):
	if not cedula.isdigit() or len(cedula) != 10:
		return False
	valores = [ int(cedula[x]) * (2 - x % 2) for x in range(9) ]
	suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
	return int(cedula[9]) == 10 - int(str(suma)[-1:])

