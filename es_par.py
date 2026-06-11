def es_par(numero):
    """
    Determina si un número entero es par.

    Args:
        numero (int): Número entero que se desea evaluar.

    Returns:
        bool: True si el número es par, False si es impar.

    Raises:
        TypeError: Si el valor ingresado no es un número entero.
    """
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("El valor debe ser un número entero")

    return numero % 2 == 0



