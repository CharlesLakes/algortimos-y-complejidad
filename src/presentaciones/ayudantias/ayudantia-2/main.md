---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 1
---

<!-- _class: title -->
# Ayudantía 2
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