"""Tarea 1: método eliminar(valor) en el Árbol Binario de Búsqueda."""


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

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)

    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

    # ------------------------------------------------------------------
    # Ejercicio 1: eliminar(valor)
    # ------------------------------------------------------------------
    def eliminar(self, valor):
        """Elimina el valor del árbol. Devuelve True si lo encontró."""
        if not self.buscar(valor):
            return False
        self.raiz = self._eliminar_rec(self.raiz, valor)
        return True

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
        else:
            # Caso 1 y 2: sin hijos o con un solo hijo.
            # Si no tiene hijo izquierdo se devuelve el derecho (que puede
            # ser None) y si no tiene derecho se devuelve el izquierdo.
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: dos hijos. Se busca el sucesor inorden (el mínimo
            # del subárbol derecho), se copia su valor y se borra el sucesor.
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)

        return nodo


if __name__ == "__main__":
    bst = ArbolBinarioBusqueda()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(v)
    print("Árbol inicial:", bst.inorden())

    bst.eliminar(20)   # caso 1: hoja
    print("Sin el 20 (hoja):", bst.inorden())

    bst.eliminar(30)   # caso 2: un hijo (el 40)
    print("Sin el 30 (un hijo):", bst.inorden())

    bst.eliminar(50)   # caso 3: dos hijos (la raíz)
    print("Sin el 50 (dos hijos):", bst.inorden())
    print("Nueva raíz:", bst.raiz.valor)

    print("Eliminar un valor que no existe:", bst.eliminar(999))
