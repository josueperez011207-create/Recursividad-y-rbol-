"""Tarea 2: recorrido por niveles (BFS) usando una cola."""

from queue import Queue


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
    # Ejercicio 2: recorrido por niveles
    # ------------------------------------------------------------------
    def recorrido_niveles(self):
        resultado = []
        if self.raiz is None:
            return resultado

        cola = Queue()
        cola.put(self.raiz)
        while not cola.empty():
            nodo = cola.get()
            resultado.append(nodo.valor)
            if nodo.izquierdo is not None:
                cola.put(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.put(nodo.derecho)
        return resultado


if __name__ == "__main__":
    bst = ArbolBinarioBusqueda()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(v)
    print("Por niveles:", bst.recorrido_niveles())

    bst2 = ArbolBinarioBusqueda()
    for v in [10, 5, 15, 2, 7, 12, 17]:
        bst2.insertar(v)
    print("Por niveles (otro árbol):", bst2.recorrido_niveles())

    print("Árbol vacío:", ArbolBinarioBusqueda().recorrido_niveles())
