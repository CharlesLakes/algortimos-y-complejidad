# Ayudantía 6
## Salto, saltito, saltote

**Existe un error en el enunciado ya que $s_i$ siempre es mayor a 0.**

Definiremos la siguiente función:

$$
 f(i) = \text{La cantidad mínima de saltos desde } i \text{ hasta } n 
$$

Podemos observar que si estamos en la posición $n$, la cantidad de pasos para llegar al final es 0.

Para el caso general, si estamos en la posición $i$, podemos saltar a las posiciones desde $i + 1$ hasta $i + s_i$. Si saltamos a cierta posición, la respuesta sería 1 salto más la respuesta de la función desde ese punto al final. Por lo tanto, necesitamos verificar todos los posibles saltos y tomar el mínimo.

$$
f(i) = 
\begin{cases} 
    0, & i = n \\
    \min_{1 \leq j \leq \min(s_i,n - i)} \left( f(i + j) + 1 \right), & i < n
\end{cases}
$$

Podemos convertir lo anterior en una función de llenado.

$$
M[i] = 
\begin{cases} 
    0, & i = n \\
    \min_{1 \leq j \leq \min(s_i,n - i)} \left( M[i + j] + 1 \right), & i < n
\end{cases}
$$

Observamos que para cada valor de $M[i]$, vamos a necesitar el cálculo de los valores en $M$ para $i$ mayores. Por lo tanto, estos valores tienen que estar previamente calculados para poder ser usados. Así que para hacer esto de manera correcta, debemos llenar $M$ desde la derecha hacia la izquierda. La complejidad espacial es $O(n)$, pero en el peor caso, es decir, cuando $s_i$ sea igual a $n$, la complejidad temporal es $O(n^2)$.


## Conteo de Arreglos

Definimos la función $f(i,l)$ como la cantidad de arreglos diferentes considerando el arreglo desde $i$ hasta $n$, teniendo en cuenta que $l$ es el número anterior.

Observamos que dado que solo podemos colocar números del 1 al $m$ en los espacios con 0, $l$ nunca será 0 pero podemos usar $l = 0$ de manera conveniente, es decir, nos indicará que no había nada antes.

Si tomamos una decisión sobre qué elemento colocar en la posición $i$, podemos observar que calcular la función empezando en $i$ sería equivalente a tomar una decisión sobre qué elemento colocar y luego llamar a $f(i + 1, \text{elemento que elegí})$. Podemos simplificar todos los casos posibles de la siguiente manera:

Caso Base:

$$
f(i,l) = 1 \text{, } i = n + 1
$$

$$
f(i,l) = f(i + 1,A[i]) \text{, } A[i] \neq 0 \land l = 0
$$

$$
f(i,l) = \sum_{j = 1}^{m}{f(i + 1,j)} \text{, } A[i] = 0 \land l = 0
$$

$$
f(i,l) = 0 \text{, } A[i] \neq 0 \land l \neq 0 \land |l - A[i]| > 1
$$

$$
f(i,l) = f(i + 1,A[i]) \text{, } A[i] \neq 0 \land l \neq 0 \land |l - A[i]| \leq 1
$$

$$
f(i,l) = \sum_{j = \max(1,l - 1)}^{\min(m,l + 1)}{f(i + 1,j)} \text{, } A[i] = 0 \land l \neq 0
$$

Podemos convertir lo anterior en una expresión de llenado.

Caso Base:

$$
M[i][l] = 1 \text{, } i = n + 1
$$

Casos generales:

$$
M[i][l] = M[i + 1][A[i]] \text{, } A[i] \neq 0 \land l = 0 
$$

$$
M[i][l] = \sum_{j = 1}^{m}{M[i + 1][j]} \text{, } A[i] = 0 \land l = 0
$$

$$
M[i][l] = 0 \text{, } A[i] \neq 0 \land l \neq 0 \land |l - A[i]| > 1 
$$

$$
M[i][l] =  M[i + 1][A[i]] \text{, } A[i] \neq 0 \land l \neq 0 \land |l - A[i]| \leq 1
$$

$$
M[i][l] = \sum_{j = \max(1,l - 1)}^{\min(m,l + 1)}{M[i + 1][j]} \text{, } A[i] = 0 \land l \neq 0
$$

Podemos observar que para cada $M[i][l]$ vamos a utilizar los elementos de la fila $i + 1$. Entonces, siempre necesitamos tenerlo calculado antes. El llenado debe ser desde los valores de $i$ mayores hasta los menores, y en el eje de $l$ da igual.

Podemos observar que la complejidad espacial es $O(NM)$ y la complejidad temporal también es $O(NM)$.

Pueden intentar programar la solución utilizando el siguiente enlace:
* [Array Description](https://cses.fi/problemset/task/1746)

Solución: https://cses.fi/paste/01e5d8fbead934d34fb977/

## mamá me aprendí la tabla del 5

Este problema se encuentra en la capsula subida por Nangel.

# FIN
