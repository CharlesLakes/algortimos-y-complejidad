# Ayudantia 8

## Dividir y Conquistar

### Desequilibrio

_Me demorare un poco en subir este ejericio debido que es muy largo de explicar_

## Decrecer y Conquistar

### Mínimo $N$ en una Función No Decreciente

Dado que la función tiene un comportamiento no decreciente, nos interesa encontrar el mínimo $i$ tal que $f(i) \geq 0$. Podemos observar que, si tuviéramos un intervalo desde $x$ hasta $y$ y sabemos que la respuesta está dentro de ese intervalo, podríamos buscarla aplicando búsqueda binaria. 

Es decir, si tomamos el punto $\left\lfloor \frac{x + y}{2} \right\rfloor$ y obtenemos que $f\left(\left\lfloor \frac{x + y}{2} \right\rfloor\right) \geq 0$, sabemos que ese punto es una posible respuesta. Sin embargo, podría haber un $i$ menor que también cumpla la condición, por lo que podemos guardar esa respuesta temporalmente y reducir la búsqueda a un intervalo desde $x$ hasta $\left\lfloor \frac{x + y}{2} \right\rfloor - 1$. 

Si en este intervalo encontramos otro punto que cumpla la condición, entonces sabemos que está más a la izquierda en el plano que el anterior. En el caso de que $f\left(\left\lfloor \frac{x + y}{2} \right\rfloor\right)$ sea menor a 0, debido al comportamiento de la función, sabemos que los números a la izquierda de la mitad no nos importan, ya que serán igual o menores que la mitad. Entonces, podemos continuar la búsqueda en el intervalo desde $\left\lfloor \frac{x + y}{2} \right\rfloor + 1$ hasta $y$. Podemos hacer esto recursivamente hasta encontrar la respuesta.

Podemos observar que no tenemos un intervalo inicial para realizar la búsqueda. Para encontrar un intervalo que nos sirva de forma eficiente, podemos realizar una búsqueda exponencial. Es decir, podemos probar por potencias partiendo desde $2^1$ y, cuando encontremos $f(2^i) \geq 0$, entonces sabemos que un intervalo válido sería desde $2^{i-1}$ hasta $2^i$.

#### Complejidad

La complejidad final es $O(\log(n))$.

### Factory Machines

En este problema, podemos realizar búsqueda binaria para encontrar la respuesta.

Para esto, definiremos la siguiente función:

$$ 
f(i) = \text{la cantidad máxima de productos que puedo realizar en } i \text{ segundos} 
$$

Podemos observar de la función anterior que sigue el siguiente comportamiento para todo $i$:

$$ 
f(i - 1) \leq f(i) \leq f(i + 1) 
$$

Es decir, es una función monótona. Entonces, de esta forma, se parece mucho al problema anterior. Sabemos que queremos producir $t$ productos.

Entonces, si $f(i) \geq t$, esto nos indica que en $i$ segundos se puede satisfacer la demanda.

Lo que queremos encontrar es el mínimo $i$ que cumpla la condición $f(i) \geq t$. Podemos utilizar búsqueda binaria y, en el caso de que $f(\text{mitad}) \geq t$, sabemos que mitad es una posible respuesta. Entonces, continuamos la búsqueda desde $x$ hasta $\text{mitad} - 1$. En caso contrario, continuamos la búsqueda en la otra mitad.

Un intervalo posible para realizar la búsqueda puede ser el siguiente: $[1, A_{\text{max}} \cdot t]$.

#### Complejidad

La complejidad para calcular $f(i)$ es $O(n)$. Al realizar búsqueda binaria se evalúa $f$ $O(\log(A_{\text{max}} \cdot t))$ veces, entonces la complejidad final es $O(n \log(A_{\text{max}} \cdot t))$.

#### Código


```python
def busqueda_binaria(izquierda, derecha, maquinas, t):
    if izquierda > derecha:
        return float("inf")
    mitad = (izquierda + derecha) // 2
    produccion = 0
    for maquina in maquinas:
        produccion += mitad // maquina
    if produccion >= t:
        return min(mitad, busqueda_binaria(izquierda, mitad - 1, maquinas, t))
    return busqueda_binaria(mitad + 1, derecha, maquinas, t)
 
n, t = list(map(int, input().split()))
maquinas = list(map(int, input().split()))
 
izquierda = 0
derecha = max(maquinas) * t
 
print(busqueda_binaria(izquierda, derecha, maquinas, t))
```