---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 4
---

<!-- _class: title -->

# Ayudantía 4

Carlos Lagos - [carlos.lagosc@usm.cl](mailto:carlos.lagosc@usm.cl)

---

# `getline` vs `cin`

- **`cin`**  
  - Lee hasta el primer espacio o salto de línea.  
  - Útil para enteros, doubles o palabras.  
  - ⚠️ Problema: al combinar con `getline` deja el salto de línea (`\n`) en el buffer.

- **`getline`**  
  - Lee una línea completa (hasta `\n`).  
  - Útil para strings con espacios.  
  - ⚠️ Problema: puede leer una cadena vacía si antes se usó `cin`.

---

# Cómo evitar el problema (`cin` + `getline`)

- Usar `cin.ignore()` para limpiar el buffer:  

```cpp
int n;
cin >> n;
cin.ignore(); // elimina el salto de línea pendiente
string s;
getline(cin, s);
````

* Alternativa: usar `ws` (whitespace) al combinar:

```cpp
int n;
cin >> n;
string s;
getline(cin >> ws, s); // ignora espacios y saltos antes de leer
```

---

# Sobrecarga de operadores fuera de la clase/struct

```cpp
struct Vector2D {
    int x, y;
};

Vector2D operator+(const Vector2D &v1, const Vector2D &v2) {
    return {v1.x + v2.x, v1.y + v2.y};
}

Vector2D operator-(const Vector2D &v1, const Vector2D &v2) {
    return {v1.x - v2.x, v1.y - v2.y};
}

// Producto cruzado
int operator^(const Vector2D &v1, const Vector2D &v2) { return v1.x * v2.y - v1.y * v2.x; }

// Producto punto
int operator*(const Vector2D &v1, const Vector2D &v2) { return v1.x * v2.x + v1.y * v2.y; }

// Comparación (orden lexicográfico por y, luego x)
bool operator<(const Vector2D &v1, const Vector2D &v2) {
    if (v1.y == v2.y) return v1.x < v2.x;
    return v1.y < v2.y;
}
```

---

# Sobrecarga de operadores dentro de la clase/struct

```cpp
struct Vector2D {
    int x, y;

    Vector2D operator+(const Vector2D &o) const {
        return {x + o.x, y + o.y};
    }

    Vector2D operator-(const Vector2D &o) const {
        return {x - o.x, y - o.y};
    }

    int operator^(const Vector2D &o) const {
        return x * o.y - y * o.x;
    }

    int operator*(const Vector2D &o) const {
        return x * o.x + y * o.y;
    }

    bool operator<(const Vector2D &o) const {
        if (y == o.y) return x < o.x;
        return y < o.y;
    }
};
```

---

# Ejercicio 1: Ángulo entre vectores

Se te dan dos vectores en el plano:

$$
u = (u_x, u_y), \quad v = (v_x, v_y)
$$

Debes calcular el ángulo entre ellos:

$$
\theta = \arccos \left( \frac{u \cdot v}{|u||v|} \right)
$$

* Entrada: dos pares de enteros $(u_x, u_y), (v_x, v_y)$.
* Salida: el ángulo en radianes con al menos 6 decimales.

---

# Ejercicio 2: Ordenar puntos

Se te da un punto pivote $p$ y un conjunto de $n$ puntos en el plano.

Debes ordenar los puntos según el **ángulo polar** respecto a $p$, en sentido antihorario.

* Entrada: $n$ seguido de $p$ y los $n$ puntos.
* Salida: los puntos ordenados según el ángulo respecto a $p$.

---

# Ejercicio 3: Fracciones

Implementa una estructura para manejar fracciones irreducibles:

$$
\frac{a}{b}, \quad b \neq 0
$$

Debes soportar:

1. Suma, resta, multiplicación y división de fracciones.
2. Comparación de fracciones (para usarlas en un `sort`).

* Entrada: una lista de $n$ fracciones.
* Salida: las mismas fracciones ordenadas de menor a mayor.

---

# Ejercicio 4: Conjunto dinámico de fracciones

Se tiene un conjunto de fracciones irreducibles:  

$$
\frac{a}{b}, \quad b \neq 0
$$

y se deben procesar $q$ operaciones de dos tipos:

1. **Insertar** una fracción $\frac{a}{b}$ en el conjunto e imprimir la fracción máxima.  
2. **Eliminar** la fracción máxima actual del conjunto e imprimir el nuevo máximo (o indicar que el conjunto está vacío).  

