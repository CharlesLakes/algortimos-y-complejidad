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
