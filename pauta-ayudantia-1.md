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

* Verdadero o Falso: $ln(n) \in O(\sqrt{n})$
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
