"""Tarea 4: método es_completo() en el Árbol Binario de Búsqueda."""


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

    # ------------------------------------------------------------------
    # Ejercicio 4: es_completo()
    # ------------------------------------------------------------------
    def es_completo(self):
        """True si todos los nodos internos tienen exactamente 2 hijos."""
        return self._es_completo_rec(self.raiz)

    def _es_completo_rec(self, nodo):
        if nodo is None:
            return True
        # Una hoja cumple la condición
        if nodo.izquierdo is None and nodo.derecho is None:
            return True
        # Nodo con un solo hijo: no cumple
        if nodo.izquierdo is None or nodo.derecho is None:
            return False
        return (self._es_completo_rec(nodo.izquierdo)
                and self._es_completo_rec(nodo.derecho))


if __name__ == "__main__":
    completo = ArbolBinarioBusqueda()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        completo.insertar(v)
    print("[50, 30, 70, 20, 40, 60, 80] ->", completo.es_completo())

    incompleto = ArbolBinarioBusqueda()
    for v in [50, 30, 70, 20]:
        incompleto.insertar(v)
    print("[50, 30, 70, 20] ->", incompleto.es_completo())

    print("Árbol vacío ->", ArbolBinarioBusqueda().es_completo())
