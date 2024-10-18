---
marp: true
math: mathjax
theme: beam
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 7
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
*{
    font-family: "Montserrat", sans-serif !important;
}
</style>

<!-- _class: title -->
# Ayudantía 7

Carlos Lagos - carlos.lagosc@usm.cl
Matias Francia - matias.francia@usm.cl

Problemas: https://vjudge.net/group/algoco2024

---

# Greedy

Supongamos que queremos resolver un problema P que tiene una solución
óptima, a la que llamaremos $R_o$. Denotaremos por $R_g$ una solución
construida mediante una estrategia codiciosa (greedy).  
Una estrategia Greedy consiste en construir una solución eligiendo los
óptimos locales en cada paso, según los criterios establecidos por la
estrategia.

En algoritmos y complejidad, dado que las soluciones deben resolver el
problema de manera exacta, buscamos que la solución greedy $R_g$ sea igual
a la solución óptima $R_o$. Esto se cumple para ciertos problemas,
dependiendo de la estrategia utilizada. Para garantizar esto, es necesario
demostrar que la estrategia greedy es óptima.

---

# Helpful Maths

<p>Xenia, la matemática principiante, es una estudiante de tercer año en la escuela primaria. Ahora está aprendiendo la operación de suma.</p><p>El maestro ha escrito la suma de varios números. Los alumnos deben calcular la suma. Para facilitar el cálculo, la suma solo contiene los números 1, 2 y 3. Aún así, eso no es suficiente para Xenia. Ella apenas comienza a contar, por lo que solo puede calcular una suma si los sumandos están en orden no decreciente. Por ejemplo, no puede calcular la suma 1+3+2+1, pero puede calcular las sumas 1+1+2 y 3+3.</p><p>Tienes la suma que fue escrita en la pizarra. Reorganiza los sumandos y imprime la suma de tal manera que Xenia pueda calcularla.</p>

---

# Add All 

¡Sí! El nombre del problema refleja tu tarea; simplemente debes sumar un conjunto de números. Pero puede que te sientas condescendiente al escribir un programa en C/C++ solo para sumar un conjunto de números. Un problema así simplemente cuestionaría tu erudición. Así que, vamos a añadirle un toque de ingenio.
Ahora, la operación de suma requiere un costo, y el costo es la suma de los dos números a sumar. Por ejemplo, para sumar 1 y 10, necesitas un costo de 11. Si quieres sumar 1, 2 y 3, hay varias maneras de hacerlo.

<table>
    <tr>
        <td>1 + 2 = 3, costo = 3<br>3 + 3 = 6, costo = 6<br>Total = 9</td>
        <td>1 + 3 = 4, costo = 4<br>2 + 4 = 6, costo = 6<br>Total = 10</td>
        <td>2 + 3 = 5, costo = 5<br>1 + 5 = 6, costo = 6<br>Total = 11</td>
    </tr>
</table>

---

# Ferris Wheel 

Hay $n$ niños que quieren subir a una rueda de la fortuna, y tu tarea es asignar una góndola a cada uno. Cada góndola puede llevar uno o dos niños, pero el peso total en una góndola no puede exceder $x$. Conoces el peso de cada niño.
¿Cuál es el número mínimo de góndolas necesarias para acomodar a todos los niños?

---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>