---
marp: true
math: mathjax
theme: beam
paginate: true
footer: Algoritmos y Complejidad
---

<!-- _class: title -->
# Capsula 1: Fuerza bruta
Carlos Lagos - carlos.lagosc@usm.cl
Nangel Coello - nangel.coello@usm.cl

---
<!-- _header: Fuerza bruta -->

# Fuerza bruta

## ¿Qué es?
<p align="justify">

La fuerza bruta es un enfoque simple para resolver un problema, a menudo basado directamente en el enunciado del problema y la definición de los conceptos involucrados. Suele ser la manera más simple de resolver un problema, pero no necesariamente la más eficiente. No conlleva ningún tipo de inteligencia, solo resuelve los problemas. Es útil para problemas con instancias pequeñas.

</p>

## ¿Para qué sirve?
Es un excelente punto de partida, ya que permite establecer una solución inicial para comprender el problema y determinar cuáles son las operaciones repetitivas que podrían evitarse.

---
<!-- _header: Recursividad -->

# Recursividad

En matemáticas, la recursividad se refiere a una función definida en términos de sí misma, es decir, una función que se llama a sí misma. Al diseñar una función recursiva, es fundamental considerar que no se genere un bucle infinito. Por lo tanto, se debe establecer una condición de terminación, también conocida como caso base, que permita que la recursión llegue a su fin en un punto determinado, evitando así la recursión infinita.

**Fuerza bruta recursiva:** Implica implementar una solución utilizando un enfoque recursivo que sigue un método de fuerza bruta.

---

<!-- _header: Fuerza bruta recursiva -->

# Combinaciones de Dados

Tu tarea consiste en contar el número de formas de construir la suma $n$ lanzando un dado una o más veces. Cada lanzamiento produce un resultado entre 1 y 6.

Por ejemplo, si $n=3$, hay 4 formas:

- $1+1+1$
- $1+2$
- $2+1$
- $3$

Debes diseñar un algoritmo recursivo para resolver este problema.

---
<style scoped>
.page{
    font-size:23px;
}
</style>
<!-- _header: Fuerza bruta recursiva -->

# Combinaciones de Monedas

<div class="page">

Considera un sistema monetario que consiste en $n$ monedas. Cada moneda tiene un valor entero positivo. Tu tarea es calcular el número de formas distintas en las que puedes obtener una suma de dinero $x$ utilizando las monedas disponibles.

Por ejemplo, si las monedas son $\{2, 3, 5\}$ y la suma deseada es 9, hay 8 formas:

- $2+2+5$
- $2+5+2$
- $5+2+2$
- $3+3+3$
- $2+2+2+3$
- $2+2+3+2$
- $2+3+2+2$
- $3+2+2+2$

</div>