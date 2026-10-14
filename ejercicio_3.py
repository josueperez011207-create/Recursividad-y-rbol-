"""Tarea 3: suma de todos los elementos de un BST sin modificarlo."""


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


# ----------------------------------------------------------------------
# Ejercicio 3: suma_arbol(arbol)
# ----------------------------------------------------------------------
def suma_arbol(arbol):
    total = 0
    if arbol.raiz is None:
        return total

    # Se usa una pila para recorrer el árbol sin tocar sus nodos
    pila = [arbol.raiz]
    while pila:
        nodo = pila.pop()
        total += nodo.valor
        if nodo.izquierdo is not None:
            pila.append(nodo.izquierdo)
        if nodo.derecho is not None:
            pila.append(nodo.derecho)
    return total


if __name__ == "__main__":
    bst = ArbolBinarioBusqueda()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(v)
    print("Suma:", suma_arbol(bst))                 # 350
    print("La raíz sigue siendo:", bst.raiz.valor)  # 50

    print("Suma de un árbol vacío:", suma_arbol(ArbolBinarioBusqueda()))
