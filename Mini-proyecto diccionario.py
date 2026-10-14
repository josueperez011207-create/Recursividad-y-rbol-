"""Mini-proyecto Unidad 9: Diccionario Inteligente con un BST.

El árbol guarda objetos Palabra y los ordena alfabéticamente. Para comparar
se ignoran mayúsculas y tildes, así "autonomia" encuentra "autonomía".
"""

import unicodedata


def normalizar(texto):
    """Pasa a minúsculas y quita las tildes para poder comparar."""
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


class Palabra:
    def __init__(self, texto, definicion):
        self.texto = texto
        self.definicion = definicion
        self.clave = normalizar(texto)  # con esto se ordena el árbol


class NodoPalabra:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class DiccionarioBST:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def insertar(self, palabra):
        """Inserta una palabra. Devuelve False si ya estaba en el árbol."""
        if self.raiz is None:
            self.raiz = NodoPalabra(palabra)
            self.cantidad += 1
            return True

        actual = self.raiz
        while True:
            if palabra.clave < actual.palabra.clave:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoPalabra(palabra)
                    break
                actual = actual.izquierdo
            elif palabra.clave > actual.palabra.clave:
                if actual.derecho is None:
                    actual.derecho = NodoPalabra(palabra)
                    break
                actual = actual.derecho
            else:
                return False  # ya existe

        self.cantidad += 1
        return True

    def buscar(self, texto):
        """Busca una palabra exacta. Devuelve la Palabra o None."""
        clave = normalizar(texto)
        actual = self.raiz
        while actual is not None:
            if clave == actual.palabra.clave:
                return actual.palabra
            if clave < actual.palabra.clave:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return None

    def todas_las_palabras(self):
        """Devuelve todas las palabras en orden alfabético (inorden)."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.palabra)
            self._inorden(nodo.derecho, resultado)

    def buscar_por_prefijo(self, prefijo):
        """Devuelve la lista de palabras que empiezan con el prefijo."""
        resultado = []
        self._prefijo(self.raiz, normalizar(prefijo), resultado)
        return resultado

    def _prefijo(self, nodo, prefijo, resultado):
        if nodo is None:
            return
        clave = nodo.palabra.clave
        if clave.startswith(prefijo):
            # Puede haber coincidencias en los dos lados
            self._prefijo(nodo.izquierdo, prefijo, resultado)
            resultado.append(nodo.palabra.texto)
            self._prefijo(nodo.derecho, prefijo, resultado)
        elif clave < prefijo:
            # Todo lo de la izquierda es menor, no puede coincidir
            self._prefijo(nodo.derecho, prefijo, resultado)
        else:
            # Todo lo de la derecha es mayor, no puede coincidir
            self._prefijo(nodo.izquierdo, prefijo, resultado)


# Lista inicial (a propósito sin orden alfabético, para que el árbol
# no quede convertido en una lista enlazada)
PALABRAS_INICIALES = [
    ("manzana", "Fruta redonda de piel roja, verde o amarilla."),
    ("auto", "Vehículo con motor que se usa para transportar personas."),
    ("zapato", "Calzado que cubre el pie."),
    ("nodo", "Elemento de una estructura de datos que guarda un dato."),
    ("aurora", "Luz rosada que aparece en el cielo antes de salir el sol."),
    ("lago", "Gran extensión de agua rodeada de tierra."),
    ("variable", "Espacio de memoria con nombre donde se guarda un valor."),
    ("autonomía", "Capacidad de decidir y actuar sin depender de otros."),
    ("casa", "Edificio donde vive una persona o una familia."),
    ("raíz", "Nodo superior de un árbol, el que no tiene padre."),
    ("dato", "Información que se guarda o se procesa."),
    ("luna", "Satélite natural que gira alrededor de la Tierra."),
    ("compilador", "Programa que traduce código fuente a lenguaje máquina."),
    ("escuela", "Lugar donde se enseña y se aprende."),
    ("audio", "Sonido grabado o reproducido por un aparato."),
    ("grafo", "Estructura formada por nodos unidos por aristas."),
    ("teclado", "Conjunto de teclas para escribir en una computadora."),
    ("río", "Corriente de agua que desemboca en el mar o en un lago."),
    ("bit", "Unidad mínima de información, vale 0 o 1."),
    ("hoja", "Nodo de un árbol que no tiene hijos."),
    ("volcán", "Montaña por donde sale lava del interior de la Tierra."),
    ("autor", "Persona que crea una obra, como un libro o un programa."),
    ("memoria", "Componente donde la computadora guarda datos."),
    ("jardín", "Terreno donde se cultivan plantas y flores."),
    ("función", "Bloque de código que hace una tarea y se reutiliza."),
    ("puente", "Construcción que permite cruzar un río o una carretera."),
    ("elefante", "Mamífero terrestre muy grande con trompa y colmillos."),
    ("pantalla", "Parte del equipo donde se muestran las imágenes."),
    ("biblioteca", "Lugar donde se guardan libros para leer o prestar."),
    ("algoritmo", "Conjunto ordenado de pasos para resolver un problema."),
    ("sol", "Estrella que da luz y calor a la Tierra."),
    ("estudiante", "Persona que se dedica a estudiar."),
    ("ventana", "Abertura en una pared para que entre luz y aire."),
    ("programa", "Conjunto de instrucciones que ejecuta una computadora."),
    ("nube", "Masa de gotas de agua que flota en el cielo."),
    ("cable", "Conductor que transmite electricidad o datos."),
    ("objeto", "Elemento que tiene atributos y métodos en la programación."),
    ("lluvia", "Agua que cae de las nubes en forma de gotas."),
    ("internet", "Red mundial que conecta computadoras de todo el planeta."),
    ("árbol", "Estructura de datos jerárquica formada por nodos."),
    ("isla", "Porción de tierra rodeada de agua por todos lados."),
    ("depurar", "Buscar y corregir los errores de un programa."),
    ("libro", "Conjunto de hojas escritas unidas por un lado."),
    ("byte", "Conjunto de ocho bits."),
    ("montaña", "Elevación natural del terreno de gran altura."),
    ("lenguaje", "Sistema de signos para comunicarse o programar."),
    ("ciclo", "Grupo de instrucciones que se repite varias veces."),
    ("computadora", "Máquina electrónica que procesa información."),
    ("ordenar", "Colocar los elementos siguiendo un criterio."),
    ("palabra", "Conjunto de letras que tiene un significado."),
    ("hijo", "Nodo que depende de otro nodo en un árbol."),
    ("python", "Lenguaje de programación sencillo y muy usado."),
    ("audiencia", "Conjunto de personas que atiende un evento."),
    ("aula", "Salón donde se dan las clases."),
    ("arena", "Granos muy pequeños de roca que hay en las playas."),
]


def cargar_diccionario():
    diccionario = DiccionarioBST()
    for texto, definicion in PALABRAS_INICIALES:
        diccionario.insertar(Palabra(texto, definicion))
    return diccionario


# ----------------------------------------------------------------------
# Interfaz de consola
# ----------------------------------------------------------------------
def mostrar_menu():
    print("\n===== DICCIONARIO INTELIGENTE =====")
    print("1. Buscar una palabra")
    print("2. Autocompletar (buscar por prefijo)")
    print("3. Ver el diccionario completo")
    print("4. Salir")


def opcion_buscar(diccionario):
    texto = input("Escribe la palabra: ").strip()
    if not texto:
        print("No escribiste nada.")
        return
    palabra = diccionario.buscar(texto)
    if palabra is None:
        print(f'La palabra "{texto}" no está en el diccionario.')
    else:
        print(f"\n{palabra.texto}: {palabra.definicion}")


def opcion_prefijo(diccionario):
    prefijo = input("Escribe el inicio de la palabra: ").strip()
    if not prefijo:
        print("Escribe al menos una letra.")
        return
    coincidencias = diccionario.buscar_por_prefijo(prefijo)
    if not coincidencias:
        print(f'No hay palabras que empiecen con "{prefijo}".')
    else:
        print(f'\nPalabras que empiezan con "{prefijo}" '
              f"({len(coincidencias)}):")
        for texto in coincidencias:
            print(f"  - {texto}")


def opcion_ver_todo(diccionario):
    palabras = diccionario.todas_las_palabras()
    print(f"\nDiccionario completo ({len(palabras)} palabras):\n")
    for palabra in palabras:
        print(f"- {palabra.texto}: {palabra.definicion}")


def main():
    diccionario = cargar_diccionario()
    print(f"Se cargaron {diccionario.cantidad} palabras.")

    while True:
        mostrar_menu()
        try:
            opcion = input("Elige una opción: ").strip()
            if opcion == "1":
                opcion_buscar(diccionario)
            elif opcion == "2":
                opcion_prefijo(diccionario)
            elif opcion == "3":
                opcion_ver_todo(diccionario)
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, intenta de nuevo.")
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
