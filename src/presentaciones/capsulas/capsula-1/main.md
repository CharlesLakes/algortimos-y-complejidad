---
marp: true
math: mathjax
theme: beam
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 1
---

<!-- _class: title -->
# Capsula 1
- Carlos Lagos - carlos.lagosc@usm.cl  
- Nangel Coello - nangel.coello@usm.cl  
- Rafael Baeza - rafael.baezam@usm.cl  
- Benjamín Cárdenas - benjamin.cardenas@usm.cl  

---

# Análisis Asintótico

- **$f(n) \in O(g(n))$**: $f$ crece a lo sumo como una función $g$
- **$f(n) \in o(g(n))$**: $f$ crece estrictamente menor a $g$
- **$f(n) \in \Omega(g(n))$**: $f$ crece al menos como una función $g$
- **$f(n) \in \omega(g(n))$**: $f$ crece estrictamente mayor a $g$
- **$f(n) \in \Theta(g(n))$**: $f$ tiene el mismo crecimiento asintótico que $g$

---

# Análisis Asintótico

## Definición formal

- **$f(n) \in O(g(n))$**: Si $\exists \, c > 0, \, \exists \, n_0 > 0 \text{ tal que } \forall \, n \geq n_0, \quad f(n) \leq c \cdot g(n)$

- **$f(n) \in o(g(n))$**: Si $\forall \, c > 0, \, \exists \, n_0 > 0 \text{ tal que } \forall \, n \geq n_0, \quad f(n) < c \cdot g(n)$

---

# Análisis Asintótico

## Definición formal

- **$f(n) \in \Omega(g(n))$**: Si $\exists \, c > 0, \, \exists \, n_0 > 0 \text{ tal que } \forall \, n \geq n_0, \quad f(n) \geq c \cdot g(n)$

- **$f(n) \in \omega(g(n))$**: Si $\forall \, c > 0, \, \exists \, n_0 > 0 \text{ tal que } \forall \, n \geq n_0, \quad f(n) > c \cdot g(n)$

---

# Análisis Asintótico

## Definición formal

- **$f(n) \in \Theta(g(n))$**: Si $\exists \, c_1, c_2 > 0, \, \exists \, n_0 > 0 \text{ tal que } \forall \, n \geq n_0, \quad c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$

---

# Análisis Asintótico
## Análisis a través de límites

- **$f(n) \in O(g(n))$:**
  $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = k, \quad k \in \mathbb{R}^+ \cup \{0\}, \quad k \neq \infty$$

- **$f(n) \in o(g(n))$:**
  $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$$


---

# Análisis Asintótico
## Análisis a través de límites

- **$f(n) \in \Omega(g(n))$:**
  $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = k, \quad k \in \mathbb{R}^+$$

- **$f(n) \in \omega(g(n))$:**
  $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$$


---

# Análisis Asintótico
## Análisis a través de límites

- **$f(n) \in \Theta(g(n))$:**
  $$\lim_{n \to \infty} \frac{f(n)}{g(n)} = k, \quad k \in \mathbb{R}^+, \quad k \neq \infty$$

---

# Análisis Asintótico

## Ejercicios

1. Verdadero o Falso: $n^2 + 3n + 10 \in O(n^2)$

2. Verdadero o Falso:  $\sqrt{n} \in \theta (n)$

3. Verdadero o Falso: $a^n \in \theta (b^n)$, con $a \neq b$

4. Verdadero o Falso: $\ln(n) \in \omega(n^{\frac{1}{4}})$

5. Verdadero o Falso: $n\sqrt{n} \in o(n^2)$

---

# Análisis Asintótico

1. Verdadero o Falso: $n^2 + 3n + 10 \in O(n^2)$

$$
\lim_{n \to \infty}\frac{n^2+3n+10}{n^2}= \lim_{n \to \infty} \left( 1 + \frac{3}{n} + \frac{10}{n^2} \right) = 1
$$

Es verdadero debido a que tiende a 1 y no a infinito, por ende pertenece a $O(n^2)$.

---

# Análisis Asintótico

2. Verdadero o Falso:  $\sqrt{n} \in \theta (n)$

$$
\lim_{n \to \infty } \frac{\sqrt{n}}{n} =  
\lim_{n \to \infty } \frac{n^{0.5}}{n} = 
\lim_{n \to \infty } \frac{1}{n^{0.5}} = 0
$$

Es falso debido a que tiende a 0 y para pertenecer a $\theta$ tiene que tender a un valor diferente de cero e infinito.

---

# Análisis Asintótico

3. Verdadero o Falso: $a^n \in \theta (b^n)$, con $a \neq b$

$$
\lim_{n \to \infty} \frac{a^n}{b^n} =
\lim_{n \to \infty} \left( \frac{a}{b} \right)^n
$$

**Caso 1: $a > b$**
Para este caso $\frac{a}{b}$ sería estrictamente mayor a 1, por lo que si este número se eleva con un $n$ tendiendo al infinito provoca que $\left( \frac{a}{b} \right)^n$ tienda a infinito. Entonces para este caso no pertenecería a $\theta(b^n)$.

**Caso 2: $a < b$** 
Para este caso $\frac{a}{b}$ sería estrictamente menor a 1, por lo que si este número se eleva con un $n$ tendiendo al infinito provoca que $\left( \frac{a}{b} \right)^n$ tienda a 0. Entonces para este caso no pertenecería a $\theta(b^n)$.

---

# Análisis Asintótico

4. Verdadero o Falso: $\ln(n) \in \omega(n^{\frac{1}{4}})$

Usaremos L'Hôpital:

$$
\lim_{n \to \infty} \frac{\ln(n)}{n^{\frac{1}{4}}} = 
\lim_{n \to \infty} \frac{\frac{1}{n}}{\frac{1}{4} n^{-3/4}} = 
\lim_{n \to \infty} \frac{4n^{\frac{3}{4}}}{n} = 
\lim_{n \to \infty} \frac{4}{n^{1/4}} = 0 
$$

La aseveración es falsa, ya que para pertenecer a $\omega(n^{\frac{1}{4}})$ tendría que tender a infinito.

---

# Análisis Asintótico

5. Verdadero o Falso: $n\sqrt{n} \in o(n^2)$

$$
\lim_{n \to \infty} \frac{n\sqrt{n}}{n^2} = 
\lim_{n \to \infty} \frac{\sqrt{n}}{n} = 
\lim_{n \to \infty} \frac{n^{\frac{1}{2}}}{n} = 
\lim_{n \to \infty} \frac{1}{n^{\frac{1}{2}}} = 0
$$

Es verdadero, ya que el límite es diferente de infinito.

---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>