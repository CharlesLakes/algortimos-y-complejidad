# Ayudantía 1
## Análisis Asintótico: Parte 1
### Verdadero o Falso: $100n^2 + 200n + 15 \in O(n^2)$

$$
\lim_{n \to \infty}\frac{n^2+3n+10}{n^2}= \lim_{n \to \infty} \left( 1 + \frac{3}{n} + \frac{10}{n^2} \right) = 1
$$

Es verdadero debido a que tiende a 100 y no a infinito, por ende pertenece a $O(n^2)$.

### Verdadero o Falso: $3n \in O(n \cdot log(n))$

$$
\lim_{n \to \infty}\frac{3n}{n \cdot log(n)} = \lim_{n \to \infty}\frac{3}{log(n)} = 0
$$

Es verdadero debido a que tiende a 0 y es diferente a infinito, por ende pertenece a $O(n \cdot log(n))$

### Verdadero o Falso:  $\sqrt{n} \in \theta (n)$

$$
\lim_{n \to \infty } \frac{\sqrt{n}}{n} =  
\lim_{n \to \infty } \frac{n^{0.5}}{n} = 
\lim_{n \to \infty } \frac{1}{n^{0.5}} = 0
$$

Es falso debido a que tiende a 0 y para pertenecer a $\theta$ tiene que tender a una real diferente de cero e infinito.

### Verdadero o Falso: $ln(n) \in O(\sqrt{n})$

$$
\lim_{n \to \infty} \frac{ln(n)}{\sqrt{n}}
$$

Podemos utilizar l'hopital:

$$
\lim_{n \to \infty} \frac{ln(n)}{\sqrt{n}} = 
\lim_{n \to \infty} \frac{\frac{1}{n}}{\frac{1}{2} n^{-\frac{1}{2}}} =
\lim_{n \to \infty} \frac{2n^{\frac{1}{2}}}{n} = 
\lim_{n \to \infty} \frac{2}{\sqrt{n}} = 0
$$

Es verdadero debido a que tiene a 0 por ende si pertenece a $O(\sqrt{n})$.

### Verdadero o Falso: $a^n \in \theta (b^n)$, con $a \neq b$

$$
\lim_{n \to \infty} \frac{a^n}{b^n} =
\lim_{n \to \infty} \left( \frac{a}{b} \right)^n
$$

Para este problema podemos tener en cuando estos dos casos:
#### Caso 1: $a > b$
Para este caso $\frac{a}{b}$ seria estrictamente mayor a 1, por lo que si este numero se eleva con un $n$ tendiendo al infinito provoca que $\left( \frac{a}{b} \right)^n$ tienda a infinito. Entonces para este caso no pertenecería a $\theta(b^n)$


#### Caso 2: $a < b$
Para este caso $\frac{a}{b}$ seria estrictamente menor a 1, por lo que si este numero se eleva con un $n$ tendiendo al infinito provoca que $\left( \frac{a}{b} \right)^n$ tienda a 0. Entonces para este caso no pertenecería a $\theta(b^n)$

#### Conclusión
Teniendo en cuenta estos dos casos podemos concluir de que la expresión es falsa.

### Verdadero o Falso: $ln(n) \in \omega(n^{\frac{1}{4}})$
Usaremos l'hopital:

$$
\lim_{n \to \infty} \frac{ln(n)}{n^{\frac{1}{4}}} = 
\lim_{n \to \infty} \frac{\frac{1}{n}}{\frac{1}{4} n^{-3/4}} = 
\lim_{n \to \infty} \frac{4n^{\frac{3}{4}}}{n} = 
\lim_{n \to \infty} \frac{4}{n^{1/4}} = 0 
$$

La aseveración es falsa debido que para pertenecer a $\in \omega(n^{\frac{1}{4}})$ tendría que tender a infinito.


### Verdadero o Falso: $n! \in \theta((n + 1)!)$

$$
\lim_{n \to \infty} \frac{n!}{(n + 1)!} = 
\lim_{n \to \infty} \frac{n!}{(n + 1) \cdot n!} = 
\lim_{n \to \infty} \frac{1}{(n + 1)} = 0
$$

Es falso debido que para pertenecer a $\theta((n + 1)!)$ el limite tiene que ser diferente de 0 e infinito.

### Verdadero o Falso: $n\sqrt{n} \in o(n^2)$

## Análisis Asintótico: Parte 2

Suponiendo que $T_1 \in O(f)$ $∧$ $T2 \in O(f)$ determinar si cada una de las
siguientes sentencias son verdaderas o falsas.

### Verdadero o Falso: $T_1 + T_2 \in O(f)$

$$
\lim_{n \to \infty} \frac{T_1 + T_2}{f} =
\lim_{n \to \infty} \frac{T_1}{f} + \lim_{n \to \infty} \frac{T_2}{f} = 
k_1 +k_2
$$

Por el enunciado sabemos que $k_1$ y $k_2$ es diferente de infinito porque pertenece a $O(f)$, entonces la suma de ambos nunca sera infinito. Podemos concluir que es verdadera la afirmación.

### Verdadero o Falso: $T_1 - T_2 \in O(f)$
Primero hay que tener en cuenta que siempre $T_1 \geq T_2$ , porque no podemos tener tiempo de ejecución negativo.

$$
\lim_{n \to \infty} \frac{T_1 - T_2}{f} =
\lim_{n \to \infty} \frac{T_1}{f} + \lim_{n \to \infty} \frac{T_2}{f} = 
k_1 - k_2
$$

Por el enunciado sabemos que $k_1$ y $k_2$ es diferente de infinito porque pertenece a $O(f)$, entonces la resta entre ambos nunca sera infinito. Podemos concluir que es verdadera la afirmación.
### Verdadero o Falso: $T_1 \in O(T_2)$

$$
\lim_{n \to \infty} \frac{T_1}{T_2} = \textbf{Desconocido}
$$

Debido a que saber que $T_1$ y $T_2$ pertenezca a $O(f)$, no nos da información del comportamiento de cada uno, por ende podríamos buscar un contra ejemplo. 
Podríamos analizar el siguiente caso:
* $T_1 = n$
* $T_2 = 30$
* $f = n^2$
Para el caso anterior podemos observar que tanto $T_1$ y $T_2$ pertenecen a $O(f)$ pero $T_1$ no pertenecería a $O(T_2)$

### Verdadero o Falso: $T_1/T_2$

$$
\lim_{n \to \infty} \frac{\frac{T_1}{T_2}}{1} = 
\lim_{n \to \infty} \frac{T_1}{T_2} = \textbf{Desconocido}
$$

Podemos observar que ahora estamos en el mismo caso que antes por ende podríamos usar el mismo contra ejemplo.

## Mejor caso, peor caso y caso promedio
Como se comento en la ayudantía para este ejercicio podemos asumir que $n$ es un cuadrado perfecto. Ademas solo puedes considerar la cantidad de comparaciones.

### ¿Que hace el algoritmo?

Al analizar el algoritmo podemos darnos cuentas de que lo que estamos haciendo es dividir la lista con largo $n$ en $\sqrt{n}$ pedazos de largo $\sqrt{n}$. La idea general del algoritmo es pasar por cada pedazo desde el mas a la izquierda hasta el mas a la derecha. Por cada bloque verificamos si el ultimo elemento de ese bloque es menor  a el numero que estamos buscando, en el caso que no se cumpla significa que pertenece a ese bloque. Al encontrar el pedazo recorremos ese pedazo de izquierda a derecha hasta encontrar el numero.

### ¿Cual es el mejor caso?

El mejor caso es cuando el numero el cual estamos buscando se encuentra al principio de la lista. Esto provocaría que este en el primer bloque por ende el primer $while$ solo se evaluaría una vez y seria $falso$ por ende se saldría de este bucle.

Luego cuando comienza el $while$ para buscar el elemento en ese bloque al estar en la primera posición solo se ejecutoriara una única vez y se saldría del bucle.

Si consideramos solo las relaciones de orden $\triangleleft$ y ⊴ realizaríamos 2 comparaciones por ende el mejor caso pertenece a $\theta (1)$

### ¿Cual es el peor caso?
El peor caso es cuando el numero que estamos buscando se encuentra en la ultima posición de la lista. Esto provocaría que se recorran todos los bloques hasta el ultimo y luego en ese bloque tendrías que pasar elemento por elemento hasta el final. 

En este caso el primer $while$ se ejecutaría $\sqrt{n}$ veces y el segundo también, entonces si solo contamos las relaciones de orden  $\triangleleft$ y ⊴ realizaríamos $2\sqrt{n}$ comparaciones y esto pertenece a $\theta (\sqrt{n})$.

### ¿Cual es el caso promedio?

#### Caso 1: Numero encontrado con éxito
Calcularemos la sumatoria de los tiempos de casos de exito.
Los casos de exito son en los que si existe el numero en la lista, por ende hay $n$ posibilidades.

$$
\sum_{i = 1}^{\sqrt{n}}
\sum_{j = 1}^{\sqrt{n}} (i + j) =
\sum_{i = 1}^{\sqrt{n}} \left( \sqrt{n} \cdot i + \frac{\sqrt{n} \cdot (\sqrt{n} + 1)}{2} \right) = \\
\sqrt{n} \cdot \frac{\sqrt{n} \cdot (\sqrt{n} + 1)}{2}
+ n\frac{\sqrt{n} + 1}{2} = \\
n \cdot \frac{\sqrt{n} + 1}{2} + n \cdot \frac{\sqrt{n} + 1}{2} = \frac{n}{2} \cdot \left( 2\sqrt{n} + 2 \right) = n\sqrt{n} + n
$$

#### Caso 2: Numero encontrado sin éxito
Calcularemos la sumatoria de los tiempos de casos sin éxito.
Para este caso tenemos que tener en cuenta que siempre en un caso de fracaso vamos a entrar a un bloque o no entraremos a ningúno, lo recorreremos todo y no encontraremos el numero. Podemos observar que hay $\sqrt{n}$  + 1 posibilidades, por lo cual podemos expresar la siguiente sumatoria:

$$
\sqrt{n} + \sum_{i = 1}^{\sqrt{n}} (i +  \sqrt{n}) = 
\sqrt{n} +\frac{\sqrt{n} \cdot (\sqrt{n} + 1)}{2} +  n = \\
\sqrt{n} + \frac{n + \sqrt{n}}{2} + n 
$$

#### Conclusión
Si juntamos ambas expresiónes para promediarlo obtenemos lo siguiente:

$$
T(n) = \frac{n\sqrt{n} + n + \sqrt{n} + \frac{n + \sqrt{n}}{2} + n}{n + \sqrt{n} + 1} = \\
\frac{2n\sqrt{n} + 4n + 2\sqrt{n} + n + \sqrt{n}}{2n + 2\sqrt{n} + 2} = \\
\frac{2n\sqrt{n} + 5n + 3\sqrt{n}}{2n + 2\sqrt{n} + 2} = \\
\frac{\sqrt{n} \cdot (2n + 5\sqrt{n} + 3)}{2n + 2\sqrt{n} + 2} \leq 
\frac{\sqrt{n} \cdot (2n + 5\sqrt{n} + 3)}{2n + 5\sqrt{n} + 3} = \sqrt{n} \in \theta(n)
$$

Podemos observar que al sacar el caso promedio total tomando en cuanta el caso de exito y de fracaso es un calculo muy complejo, pero en muchos ejericios solo te piden el caso promedio de solo exito o de solo fracaso, lo cual lo hace un poco mas simple. :smile:
