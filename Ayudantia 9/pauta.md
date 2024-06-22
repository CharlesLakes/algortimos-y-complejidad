# Ayudantia 9

## Fibonacci


Siendo $f_n$ el n-esimo numero de Fibonacci, tenemos:

$$
\begin{pmatrix}
f_{n-1} & f_{n} \\
f_{n} & f_{n+1} 
\end{pmatrix} = 
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}^n
$$

Como las multiplicacioes de matrices so siempre entre matrices $2 \times 2$, podemos considerar el tiempo de multiplicacion como constante. Realizar las $n$ multiplicaciones nos tomaria tiempo $O(n)$.

Hay que notar que la multiplicacion de matrices es asociativa.

Para $n = 4$, por ejemplo, podemos considerar multiplicar la mitad de la derecha y luego la de la izquierda, esto reduce el numero de multiplicaciones a 3:

$$
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}^4 = 
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix} = 
(\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix} \begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix})(\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix}\begin{pmatrix}
0 & 1 \\
1 & 1 
\end{pmatrix})
$$

Notar ahora que ambas mitades son iguales, por lo que solo necesito multiplicar una mitad y multiplicar el resultado por si mismo, terminando con un total de 2 multiplicaciones.

Generalizando, cuando $n = 2^k, k \in \mathbb{N}$ (n es potencia de 2), podemos defiir recursivamete la matriz para n:

$$
M(n) = 
\begin{cases} 
    M, & n = 1 \\
    (M(n/2))^{2}, & n > 1
\end{cases}
$$



De esta forma se realizan $log(n)$ multiplicaciones de matrices.

Para el caso general, es decir, cuando  a no es necesariamente una potencia de 2, en algun punto puede que $n/2$ sea impar. En este caso se realiza division entera (i.e: funcion piso) y luego se multiplica por el resto:

$$
M(n) = 
\begin{cases} 
    M, & n = 1 \\
    (M(n/2))^{2}, & n > 1 & y & n & par \\
    M\times(M(\lfloor n/2\rfloor))^{2}, & n > 1 & y & n & impar \\
\end{cases}
$$

Asi, tenemos un algoritmo que calcula el n-esimo numero de Fibonacci en tiempo $O(log(n))$ 

## GCD y LCM

## Arreglo shifteado
### A)
Como se conoce $k$ y el arreglo se encotraba ordenado antes del shifteo, ecotrar el valor maximo en el arreglo en tiempo $\Theta(1)$ se reduce a buscar en la posicion $k-1$ del arreglo (se indica que se parte del 0), pues en la posicion $k$ se encuentra el minimo.
### B)
En este caso no se conoce el valor de $k$. 
De nuevo aqui hay que notar que previamente al shifteo el arreglo se encontraba ordenado. Esto quiere decir que el sub-arreglo partiendo desde el menor valor hasta el final se encuentra ordenado, y el subarreglo que parte desde la primera posicion y termina con el maximo tambien esta ordeado. Esto quiere decir que el unico elemento mayor al elemento siguiente ( $A[i] > A[i+1]$ ) es el elemeto maximo del arreglo.

Sabiendo esto utilizaremos una modificacion de la busqueda biaria, en lugar de consultar si el elemento se encuetra en la mitad izquierda o derecha, preguntamos si el elemento central es menor o mayor que el limite izquierdo. Si es menor, el maximo se encuentra en la mitad izquierda, si es mayor, el maximo se encuetra en la mitad derecha. Se continua con la mitad correspondiente hasta que queden dos elementos, de los cuales el izquierdo sera el maximo.

Como busqueda biaria, se descarta con cada iteracion la mitad de cada subarreglo, por lo que este algoritmo encuetra el maximo en tiempo $O(log(n))$

### C)

Como podemos encontrar el maximo del arreglo, podemos separar el arreglo en 2 subarreglos ordenados.

$$
A[0..n-1] = \langle A[0], ... , A_{max} , A_{min}, ... A[n-1]  \rangle
$$

Notar que si el elemento que buscamos es $x$, si $x \leq A[n-1]$ (el ultimo elemeto), este se encuentra en el subarreglo de la derecha, en caso contrario, se ecuentra en el sub arreglo de la izquierda. Teniendo esto identificado, se puede realizar una busqueda binaria comun en el subarreglo correspondiente.

Esto tiene tiempo $EncontrarMaximo + BusquedaBinaria = O(log(n)) + O(log(n))  = O(log(n))$
