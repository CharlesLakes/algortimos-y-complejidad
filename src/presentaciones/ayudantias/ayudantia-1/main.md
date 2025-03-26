---
marp: true
math: mathjax
theme: beam
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 1
---

# Ayudantía 1

*Introducción a la Biblioteca Estándar de C++: STL*

---

## ¿Qué es la STL?

>Es un conjunto de clases y funciones basadas en plantillas (templates).
>>Implementa **estructuras de datos** y **algoritmos** básicos (listas, pilas, colas, búsqueda, orden, etc).<br>
>>Además agrega objetos iteradores para operar y/o acceder a las estructuras de datos.

---

## Componentes de la STL

La STL se compone de 4 elementos principales:

1. **Contenedores** (Estructuras de datos)  
2. **Algoritmos**  
3. **Iteradores**

---

## Contenedores

- Contenedores de secuencia
Array, Vector, Deque, List, Forward List
- **Adaptadores de contenedores**  
Stack, Queue, Priority Queue
- **Contenedores asociativos**  
Set, Map, Multiset, Multimap
- **Contenedores asocitavos desordenados**
Unordered Set, Unordered Map, Unordered Multiset, Unordered Multimap

---

### Algoritmos Manipulativos (Modifican o reordenan los elementos)


|**Función**|**Operación**|
|-----------|-------------|
|**copy**| Copia elementos de un rango a otro.|
|**fill**| Asigna un valor a todos los elementos de un rango.|
|**transform**| Aplica una función a cada elemento.|
|**replace**| Reemplaza elementos por un nuevo valor.|
|**swap**|Intercambia el contenido de dos variables.|
|**reverse**|Invierte el orden de los elementos.|
|**rotate**|Rota los elementos de un rango.|
|**remove**|Elimina elementos con un valor específico.|
|**unique**| Elimina duplicados consecutivos.|

---
```c++
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

int main(){
    vector<int> ejemplo = {1, 2, 3, 4, 5, 6, 7};
    vector<int> copia_ejemplo(ejemplo.size());

    copy(ejemplo.begin(), ejemplo.end(), copia_ejemplo.begin());
    reverse(copia_ejemplo.begin(), copia_ejemplo.end());

    for(int i : copia_ejemplo) cout << i << ' ';

    return 0;
}

//output: 7 6 5 4 3 2 1
```

---

### Algoritmos No Manipulativos (Operan sin modificar el contenido)

| **Función**| **Operación**|
|------------|--------------|
|**max_element**|Encuentra el elemento máximo.|
|**min_element**|Encuentra el elemento mínimo.|
|**accumulate**|Suma los elementos de un rango.|
|**count**|Cuenta ocurrencias de un elemento.|
|**find**| Busca el primer elemento que cumple una condición.|
|**is_permutation**|Comprueba si dos rangos son permutaciones.|
|**is_sorted**|Verifica si un rango está ordenado.|
|**partial_sum**|Calcula la suma acumulada.|

---

## Iteradores

Objetos similares a punteros que sirven para recorrer los contenedores.

---

## Beneficios de la STL

- **Código genérico y reutilizable:** Escribe algoritmos que funcionan con múltiples tipos.
- **Enfoque en la solución de problemas:** Menos código de bajo nivel y más énfasis en la lógica.
- **Gestión de memoria:** Reduce errores comunes como pérdidas de memoria.

---

## Limitaciones de la STL

- **Sobrecarga de rendimiento:** La generalidad puede afectar la eficiencia en casos específicos.
- **Complejidad al depurar:** Las abstracciones pueden dificultar la identificación de errores.
- **Control de memoria:** Menor control sobre detalles de asignación y liberación.
- **Integración con estructuras personalizadas:** Algunas estructuras a medida pueden requerir soluciones específicas.

---


# ¡Gracias!

Preguntas y comentarios.
