# Ayudantía 3
## Problema de Reducción Numérica

### Explicación

Definimos la función $D(n,i)$, la cual extrae el i-ésimo dígito de derecha a izquierda.

$$
D(n,i) = \left \lfloor \frac{n}{10^{i - 1}} \right \rfloor \mod 10
$$

La cantidad de pasos para llegar desde 0 hasta 0 son 0 pasos, por ende, podemos usar esto como caso base. Ahora, para el caso cuando $ n > 0 $, podemos observar que nunca nos conviene usar el dígito con valor 0, ya que si lo usamos en un movimiento nos dejaría en el mismo lugar. Podemos notar que si a $ n $ le resto un dígito diferente de 0, siempre decrece. Por ejemplo, imaginemos que del número 56 tomamos el número 5; si elegimos el 5, la cantidad de pasos mínimos sería equivalente a 1 más la respuesta de los pasos mínimos del 51. También existe la posibilidad de elegir el 6, en cuyo caso la cantidad de pasos mínimos es 1 más la cantidad mínima de pasos del 50. Así, podemos observar una relación de recurrencia.

$$
f(n) = 
\begin{cases} 
    0, & n = 0 \\
    \min_{\substack{1 \leq i \text{ } \land \text{ } 0 < \left \lfloor \frac{n}{10^{i - 1}} \right \rfloor \text{ } \land \text{ } D(n,i) \neq 0 }} {\left (f(n - D(n,i)) + 1 \right )}, & n > 0
\end{cases}
$$

### Codigo

```py
def D(n,i):
    return (n // (10**(i - 1))) % 10

def f(n):
    if n == 0:
        return 0
    minimo = float("inf") # Representa al infinito
    
    i = 1
    while n // (10**(i - 1)) > 0:
        digito = D(n,i)
        if digito != 0:
            minimo = min(minimo,f(n - digito) + 1)
        i += 1

    return minimo
```

### Programación Dinámica

Esta ayudantía no trataba sobre programación dinámica, pero de igual forma podemos optimizar esta solución utilizando programación dinámica. Simplemente tendríamos que convertirla en una expresión de llenado y memorizar cada respuesta. Si quieres intentarlo, dejo el enlace del juez de donde se extrajo el problema.

Link: [Removing Digits](https://cses.fi/problemset/task/1637)

Para probarlo, debes iniciar sesión y enviar el código que lo resuelva.

_Python tiene un límite de recursión, por lo que la implementación puede generar un error de tiempo en algunos casos de prueba. Sin embargo, si los demás casos están bien, significa que tu solución es correcta. Otra opción es convertirla a bottom-up o cambiar el lenguaje_.

Soluciones:
- [Top-Down (C++)](https://cses.fi/paste/5a6297baa8b0b8328cfd28/)
- [Bottom-Up (Python)](https://cses.fi/paste/b4855b5cb3c6aadd76a04d/)

## Problema de Reducción Numérica

### Explicación

Podemos establecer una relación de recurrencia al observar que en cada caso podemos elegir un $ i $ desde 1 hasta $ n $, lo que indica el segmento que vamos a recortar. Por ejemplo, si recorto 3 unidades de una longitud total de 10, entonces al recortar 3 unidades, la opción restante es multiplicar 3 por la respuesta de la multiplicación máxima desde 7. Así, podemos definir una función $ f(n) $ que devuelva la multiplicación mínima de los segmentos con una longitud inicial de $ n $. Al asumir que esto funciona, podemos generar la siguiente expresión recursiva.


$$
f(n) = 
\begin{cases} 
    1, &  n = 0 \\
    \max_{1 \leq i \leq n}{(i \cdot f(n - i))}, & n > 0
\end{cases}
$$

### Programación Dinámica

Al igual que en el ejercicio anterior, podemos aplicar programación dinámica a este problema. Te dejo como reto la tarea de implementar el código correspondiente.

Aquí está el texto corregido y en formato Markdown compatible con Obsidian:

## Mirnyy

Podemos analizar el algoritmo para unir dos arreglos ordenados y generar otro ordenado. Una forma de hacerlo sería concatenar ambos arreglos y luego ordenarlos utilizando algún algoritmo conocido, pero estos algoritmos son O(nlog(n)), lo cual no cumple con la complejidad requerida. Una forma más eficiente de unirlos es utilizando dos indicadores: uno que empiece al inicio de A y otro al inicio de B. Si el elemento que se está indicando en A es menor o igual que el que se indica en B, podemos agregar ese elemento a otro arreglo; en caso contrario, se agrega el de B.

```python
def mediana(A, B):
    resultado = None
    med = (len(A) + len(B) + 1) // 2
    posA, posB, pos = 0, 0, 0

    while posA < len(A) and posB < len(B):
        if A[posA] <= B[posB]:
            if pos == med - 1:
                resultado = A[posA]
            posA += 1
        else:
            if pos == med - 1:
                resultado = B[posB]
            posB += 1
        pos += 1

    while posA < len(A):
        if pos == med - 1:
            resultado = A[posA]
        posA += 1
        pos += 1

    while posB < len(B):
        if pos == med - 1:
            resultado = B[posB]
        posB += 1
        pos += 1
    
    return resultado
```

El código anterior une dos listas ordenadas y asegura que la resultante se mantenga ordenada en O(n). Podemos calcular la mediana fácilmente de lo resultante, pero aún así esto no cumple con lo que se pide en el enunciado, ya que usamos O(n) en memoria. Sin embargo, si observamos detenidamente, dado que conocemos la posición de la mediana, no necesitamos guardar todo el arreglo resultante. Simplemente debemos añadir la verificación de cuando la variable \( pos \) es igual a la posición de la mediana y guardar ese valor.

```python
def mediana(A, B):
    resultado = None
    med = (len(A) + len(B) + 1) // 2
    posA, posB, pos = 0, 0, 0

    while posA < len(A) and posB < len(B):
        if A[posA] <= B[posB]:
            if pos == med - 1:
                resultado = A[posA]
            posA += 1
        else:
            if pos == med - 1:
                resultado = B[posB]
            posB += 1
        pos += 1

    while posA < len(A):
        if pos == med - 1:
            resultado = A[posA]
        posA += 1
        pos += 1

    while posB < len(B):
        if pos == med - 1:
            resultado = B[posB]
        posB += 1
        pos += 1
    
    return resultado
```

# FIN

Avísame por correo si encuentras algún error o algo por el estilo.
