---
marp: true
math: mathjax
theme: beam
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 6
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
*{
    font-family: "Montserrat", sans-serif !important;
}
</style>

<!-- _class: title -->
# Ayudantía 6

Carlos Lagos - carlos.lagosc@usm.cl

---

# Fuerza bruta y Backtracking

## Problema de las Ocho Reinas

Consiste en colocar 8 reinas en un tablero de ajedrez de 8x8 de manera que ninguna pueda atacar a otra. Las reinas no deben compartir la misma fila, columna o diagonal. Encuentra todas las disposiciones que cumplan con esta condición.

---

# Fuerza bruta y Backtracking

## Fuerza Bruta

Es una búsqueda exhaustiva de todos los posibles candidatos para las soluciones de un problema. Se itera a través de todos los estados posibles para encontrar una o varias soluciones óptimas y factibles.

Para solucionar el problema anterior, podemos usar 8 bucles 'for', uno por cada fila, iterando 8 veces en cada bucle para abarcar todas las columnas.

---

# Fuerza bruta y Backtracking

### Fuerza Bruta - Ejemplo

Ejemplo con 4 reinas y un tablero de 4x4:

```c++
for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
        for(int k = 0; k < 4; k++) {
            for(int l = 0; l < 4; l++) {
                // Se verifica si es factible.
            }
        }
    }
}
```

---

# Fuerza bruta y Backtracking

## Backtracking

El backtracking es una técnica de búsqueda más eficiente que la fuerza bruta. Construye una solución paso a paso, verificando en cada etapa si sigue siendo factible. Si no es posible, retrocede y prueba otra opción, reduciendo así el espacio de búsqueda.

En el problema de las 8 reinas, el backtracking coloca una reina en cada fila y verifica si la colocación es factible. Si una colocación resulta inviable, se retrocede y se prueba con otra opción, optimizando el proceso y evitando soluciones inviables.

---

# Fuerza bruta y Backtracking

### Backtracking - Ejemplo

Ejemplo con 4 reinas y un tablero de 4x4:

```c++
for (int i = 0; i < 4; i++) {
    if (!esFactible(i)) continue;
    for (int j = 0; j < 4; j++) {
        if (!esFactible(i, j)) continue;
        for (int k = 0; k < 4; k++) {
            if (!esFactible(i, j, k)) continue;
            for (int l = 0; l < 4; l++) {
                if (!esFactible(i, j, k, l)) continue;
                // Procesar solución factible
            }
        }
    }
}
```
---

# Ejemplo: Prefi-Primos

Un número es prefi-primo si todos sus prefijos son primos:

- $233$ es prefi-primo, porque $2$, $23$ y $233$ son primos.
- $251$ es primo, pero no prefi-primo, $25$ no es primo.

Sea $f_n=$ la cantidad de prefi-primos de $n$ dígitos.

Sea $n$ un valor acotado por 1 $\leq$ $n$ $\leq$ $10^4$. Calcular $f_n$.

Asuma que existe una forma de hacer test de primalidad en $O(1)$.

---

# Ejemplo: Prefi-Primos

### Opción fuerza bruta

```c++
for (int a = 1; a <= 9; a++)
for (int b = 0; b <= 9; b++)
for (int c = 0; c <= 9; c++)
for (int d = 0; d <= 9; d++)
if (primo(a) && primo(10*a+b) && primo(100*a+10*b+c) )
if (primo(1000*a+100*b+10*c+d))
ret++;
```

¿Que complejidad tendría?

---

# Ejemplo: Prefi-Primos

### Opción fuerza bruta

```c++
for (int a = 1; a <= 9; a++)
for (int b = 0; b <= 9; b++)
for (int c = 0; c <= 9; c++)
for (int d = 0; d <= 9; d++)
if (primo(a) && primo(10*a+b) && primo(100*a+10*b+c) )
if (primo(1000*a+100*b+10*c+d))
ret++;
```

¿Que complejidad tendría?

$O(n \cdot 10^n)$

---

# Ejemplo: Prefi-Primos

### Opción Backtracking

```c++
for (int a = 1; a <= 9; a++)
if (primo(a))
for (int b = 0; b <= 9; b++)
if (primo(10*a+b))
for (int c = 0; c <= 9; c++)
if (primo(100*a+10*b+c))
for (int d = 0; d <= 9; d++)
if (primo(1000*a+100*b+10*c+d))
ret++;
```

¿Que complejidad tendría?


---

# Ejemplo: Prefi-Primos

### Opción Backtracking

```c++
for (int a = 1; a <= 9; a++)
if (primo(a))
for (int b = 0; b <= 9; b++)
if (primo(10*a+b))
for (int c = 0; c <= 9; c++)
if (primo(100*a+10*b+c))
for (int d = 0; d <= 9; d++)
if (primo(1000*a+100*b+10*c+d))
ret++;
```

¿Que complejidad tendría?

$O(n \cdot (f_1 + f_2 + ...+f_n))$

---


# Ejemplo: Prefi-Primos

## Existen MUY POCOS prefi-primos  
$f_1 = 4$  
$f_2 = 9$  
$f_3 = 14$  
$f_4 = 16$  
$f_5 = 15$  
$f_6 = 12$  
$f_7 = 8$  
$f_8 = 5$  
$f_i = 0, \, \forall i \geq 9$

---

# Ejemplo: Prefi-Primos

* El ejemplo anterior es extremo, pasa de $10^8$ operaciones a 664.  
* Aun así, en muchísimos otros ejemplos también se reduce la complejidad asintótica.

---

# Principio de generar y no filtrar.
Supongamos que queremos saber cuántos números cumplen cierta condición.
* Es posible generar todas las posibilidades y filtrar las correctas.
* También podemos generar todas las posibilidades, sin filtrar.

---

# Principio de generar y no filtrar.

Buscando números que deben cumplir ser múltiplos de $x$:  
```c++
for (int i = 1; i <= N; i++) if (i % x == 0) print(i);
```

```c++
for (int i = x; i <= N; i += x) print(i); 
```

---

# Branch and bound

* En cada nodo del árbol de backtracking se computan cotas inferior y superior $L, U$ (con $L \leq U$) a las posibles soluciones desde ese nodo.  
* Se mantiene una variable global `best` con el valor de la mejor solución encontrada.  
* Para un problema de minimización, `best` tiene en todo momento el mínimo $U$ que hemos visto en todo el algoritmo.  
* Para un problema de minimización, si $L \geq \text{best}$ podemos descartar ese nodo y todo su subárbol.  
* Lo esencial: meter un `if (L >= best) return;` al comienzo de la función recursiva.

---

# Tips generales

* En algunos problemas de backtracking puede que tengamos que optimizar lo más posible la constante para que pase en tiempo.
* Usar `next_permutation`.
* Usar operaciones de bits si se puede, esto a veces nos permite hacer operaciones rápidas y usar menos memoria.  
* Evitar usar memoria dinámica (es mejor usar arreglos nativos de C++ que vectores en algunos casos).  

---

# Tips generales

* Si se hace una operación repetida muchas veces, es mejor precomputar y guardarlo en memoria para evitarse ese costo.  
* En algunos problemas, la respuesta se puede reducir a tener precalculados ciertos valores (los cuales son pocos), pero precalcular puede ser caro. Entonces, se puede precalcular en local y hardcodear en el código. (Uno del listado se hace de esta forma).  

---

# Ejercicios

* Dado un conjunto de desde el $1$ al $n$, imprime todos los posibles subconjuntos.
* Genera todas las permutaciones posibles, sin usar `next_permutation`.


---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>