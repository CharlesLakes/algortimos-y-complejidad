# Ayudantía 2
## Análisis Amortizado
### Recomendaciones

Al calcular el costo amortizado por operaciones en una estructura de datos, es esencial determinar cuánto tiempo $T(n)$ se necesita en el peor caso para realizar $n$ operaciones y luego promediarlo con la cantidad total de operaciones $n$. Por lo tanto, el costo amortizado por operación se obtiene mediante la expresión $T(n)/n$.

Para realizar este cálculo de manera efectiva, se sugiere analizar cuántas operaciones elementales se llevan a cabo por cada elemento en la estructura de datos. Es decir, es importante examinar el flujo de operaciones para un elemento individual y luego multiplicarlo por la cantidad total de elementos, considerando que en el peor caso todos los elementos seguirán el mismo patrón de operaciones.

### Cuack! (no hablo de patos)

#### Implementación

Una solución viable es emplear dos pilas para implementar el Quack, una estructura que combina las características de una cola y una pila. Para cada operación de inserción (PUSH), los elementos se colocan en la primera pila. Al realizar una operación de extracción desde la base (PULL), se verifica si la segunda pila está vacía. En tal caso, se trasladan todos los elementos de la primera pila a la segunda y se extrae el elemento de la cima de la segunda pila. Si la segunda pila contiene elementos antes de realizar PULL, simplemente se extrae el elemento de la cima de dicha pila.

Para implementar la operación de eliminación desde la cima (POP), se realiza una verificación inicial en la primera pila para determinar si contiene elementos. En caso afirmativo, se extrae el elemento de la cima de la pila 1. Sin embargo, si la primera pila está vacía pero la segunda contiene elementos, se descartan los elementos de la base de la segunda pila. Para llevar a cabo este proceso, se utiliza un contador que registra la cantidad de elementos a considerar en la segunda pila. Este contador se incrementa en 1 cada vez que se introduce un elemento en la segunda pila. Al ejecutar un POP, simplemente se disminuye en uno este contador. En el escenario donde la segunda pila queda sin elementos considerados, es posible extraer todos los elementos previamente ignorados de la pila.

#### Análisis

Se puede observar que el caso más desfavorable ocurre cuando se insertan $n/2$ elementos en la estructura y luego se aplica un PULL, lo que provoca que los $n/2$ elementos pasen a la segunda pila. Después, se realizan $n/2 - 1$ operaciones de POP. Al analizar el flujo de cada elemento en este caso, se observa que por cada elemento se llevan a cabo las siguientes operaciones: ingreso a la primera pila, traslado de la primera a la segunda pila, ignorancia (disminución del contador de considerados en 1) y finalmente extracción de la estructura. Por lo tanto, por cada elemento se realizan $4$ operaciones, lo que da un total de $4\cdot\frac{n}{2}$ operaciones en total.

Así, el promedio sería el siguiente:

$$
\frac{T(n)}{n} = \frac{4\cdot\frac{n}{2}}{n} = 2 \in O(1) 
$$

Por lo tanto, el costo amortizado por operación es $O(1)$.

_PD: Los cálculos pueden variar, ya que dependen de qué operaciones elementales se consideren para el conteo temporal y si se encuentra un caso igual de desfavorable._

### BACKUP

_Podemos asumir que copiar un solo elemento en otro lugar es O(1)._

El peor caso que se puede considerar es que las $k$ operaciones sean solo de inserción, ya que si hay extracción, la cantidad de elementos que se copiarán en otro sector de memoria será menor.

Como podemos observar, cada elemento tendrá el siguiente flujo:
- Entrará un elemento a la pila.
- Se realizará una copia del elemento.

$$
\frac{T(n)}{n} = \frac{2k}{k} = 2 \in O(1)
$$

Con lo anterior, podemos demostrar que el costo amortizado por operación es $O(1)$.

### Las potencias

