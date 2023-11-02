import ficha15_02


def test():
    print('ARREGLOS: ÚLTIMO Y PRIMERO')
    print('*'*80)
    n = ficha15_02.validar_tamanio()
    v = ficha15_02.crear(n)
    print('*'*80)
    rep = ficha15_02.contar_repeticiones(v)
    print('El último número se repite',rep,'veces en el vector')
    menores = ficha15_02.buscar_menores(v)
    print('Los valores menores al primer elemento son:',menores)


if __name__ == "__main__":
    test()
