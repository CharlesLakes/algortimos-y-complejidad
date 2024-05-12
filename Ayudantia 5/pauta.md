# Ayudantía 5
## Problema de Corte de Cuerda

### Explicación

Podemos establecer una relación de recurrencia al observar que en cada caso podemos elegir un $i$ desde 1 hasta $n$, lo que indica el segmento que vamos a recortar. Por ejemplo, si recortamos 3 unidades de una longitud total de 10, al hacerlo la opción restante sería multiplicar 3 por la respuesta de la multiplicación máxima desde 7. Así, podemos definir una función $f(n)$ que devuelva la multiplicación mínima de los segmentos con una longitud inicial de $n$. Al asumir que esto funciona, podemos generar la siguiente expresión recursiva:

$$
f(n) = 
\begin{cases} 
    1, & n = 0 \\
    \max_{1 \leq i \leq n}{(i \cdot f(n - i))}, & n > 0
\end{cases}
$$

Ahora podemos convertir lo anterior en una expresión de llenado:

$$
M[n] = 
\begin{cases} 
    1, & n = 0 \\
    \max_{1 \leq i \leq n}{(i \cdot M[n - i])}, & n > 0
\end{cases}
$$

Podemos observar que para el cálculo del valor $M[n]$, con $n > 0$, siempre usamos un valor con $n$ menor para su cálculo. Por lo tanto, como necesitaremos usarlo, debe estar calculado previamente. Podemos visualizar este proceso de llenado como una lista desde el 0 hacia la derecha.

Notamos que la memoria utilizada pertenece a $\Theta(n)$ y como en cada valor de la DP se accede a valores menores hasta M[0], entonces el costo temporal pertenece a $\Theta(N^2)$.

## Robomonkey Shines

Consideremos una matriz $C[i][j]$ que contiene la cantidad de monedas en la coordenada $(i,j)$. Para cada posición, tenemos dos opciones: avanzar hacia abajo o hacia la derecha, siempre y cuando no nos salgamos del tablero.

Definamos la función $f(i,j)$ como la cantidad máxima de monedas que podemos tomar empezando desde $(i,j)$ y terminando en $(m,n)$.

Teniendo en cuenta lo que responde la función, podemos establecer una ecuación de recurrencia.

$$
f(i,j) = 
\begin{cases} 
    C[i][j], & i = m \land j = n \\
    C[i][j] + f(i + 1,j), & j = n \land i < m \\
    C[i][j] + f(i,j + 1), & i = m \land j < n \\
    C[i][j] + \max{(f(i + 1,j),f(i,j + 1))}, & i < m  \land j < n
\end{cases}
$$

Ahora podemos convertir lo anterior en una expresión de llenado.

$$
M[i][j] = 
\begin{cases} 
    C[i][j], & i = m \land j = n \\
    C[i][j] + M[i + 1][j], & j = n \land i < m \\
    C[i][j] + M[i][j + 1], & i = m \land j < n \\
    C[i][j] + \max{(M[i + 1][j],M[i][j + 1])}, & i < m  \land j < n
\end{cases}
$$

Observamos que para cada valor de $i$ y $j$ necesitamos el contenido de la DP de la derecha o abajo. Además, hay que tener en cuenta que el caso base estará almacenado en la posición $(m,n)$ de $M$. Debido a esto, necesitaremos llenar la tabla de derecha a izquierda (es decir, desde los valores mayores a los menores) y de abajo a la derecha (es decir, desde los valores mayores a los menores). Al construir de esta forma, siempre tendremos calculados previamente los valores que necesitamos.

Observamos que el espacio utilizado se debe al almacenamiento en una matriz de dimensiones $M \times N$, lo que implica un espacio de $O(NM)$. Además, en cada cálculo de los valores realizamos a lo sumo dos operaciones, es decir, verificamos si avanzamos hacia la derecha o hacia abajo. Por lo tanto, la complejidad temporal sería $O(NM)$.


## Viaje por el río Mapocho

Dado que solo podemos avanzar en el viaje, primero observamos el caso base: el costo de ir desde la posición $n$ hasta la posición $n$ es 0, ya que no necesitamos movernos. Este será nuestro caso base. Para los casos recursivos, si estamos en la posición $i$, siempre podríamos avanzar a la posición siguiente. Sin embargo, si decidimos avanzar a la posición $j$, el costo sería $f_{i,j}$ más el costo mínimo desde $j$ hasta $n$. Por lo tanto, podemos definir la siguiente recurrencia:

$$C(i) \text{: Costo de ir de la estación } i \text{ a la estación } n$$

$$f_{i,j} \text{: Costo arbitrario de ir de la estación } i \text{ a } j$$

$$
C(i) =
\begin{cases}
\min_{i < j \leq n}(C(j) + f_{i,j}) & \text{si } i \neq n \\
0 & \text{si } i = n
\end{cases}
$$

Podemos convertir lo anterior en una función de llenado:

$$
M[i] =
\begin{cases}
\min_{i < j \leq n}(M[j] + f_{i,j}) & \text{si } i \neq n \\
0 & \text{si } i = n
\end{cases}
$$

Observamos que para calcular los valores de $M$ para los casos no base, siempre necesitamos acceder al valor de los elementos que están adelante hacia $n$. Por lo tanto, para calcular todos los valores de $M$, debemos empezar llenando de derecha a izquierda (es decir, desde $i$ mayores hasta los menores). Además, notamos que para el cálculo de los valores de $M[i]$, en el peor caso necesitamos recorrer todos los elementos hacia adelante. Por ende, la complejidad temporal es $O(n^2)$.
