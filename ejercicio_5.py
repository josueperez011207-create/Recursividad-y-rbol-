"""Tarea 5: balancear_arbol() para construir un BST de altura mínima."""


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
        # Si el valor ya existe no se hace nada (no hay duplicados)

    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

    def altura(self):
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))


# ----------------------------------------------------------------------
# Ejercicio 5: balancear_arbol(arbol)
# ----------------------------------------------------------------------
def balancear_arbol(arbol):
    """Devuelve un BST nuevo, balanceado, con los mismos elementos."""
    valores = arbol.inorden()  # ya vienen ordenados de menor a mayor
    nuevo = ArbolBinarioBusqueda()
    nuevo.raiz = _construir_balanceado(valores, 0, len(valores) - 1)
    return nuevo


def _construir_balanceado(valores, inicio, fin):
    if inicio > fin:
        return None
    medio = (inicio + fin) // 2
    nodo = NodoArbol(valores[medio])
    nodo.izquierdo = _construir_balanceado(valores, inicio, medio - 1)
    nodo.derecho = _construir_balanceado(valores, medio + 1, fin)
    return nodo


if __name__ == "__main__":
    degenerado = ArbolBinarioBusqueda()
    for v in [1, 2, 3, 4, 5, 6, 7]:
        degenerado.insertar(v)
    print("Altura antes:", degenerado.altura())

    balanceado = balancear_arbol(degenerado)
    print("Altura después:", balanceado.altura())
    print("Inorden nuevo:", balanceado.inorden())
    print("El original no cambió, altura:", degenerado.altura())

    print("Árbol vacío:", balancear_arbol(ArbolBinarioBusqueda()).inorden())
