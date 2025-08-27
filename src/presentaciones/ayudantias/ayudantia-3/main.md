---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 3
---

<!-- _class: title -->

# Ayudantía 3

Carlos Lagos - [carlos.lagosc@usm.cl](mailto:carlos.lagosc@usm.cl)

---

# Struct

* En C++, un `struct` funciona igual que una clase.
* La única diferencia es que, por defecto, los miembros son **public**.
* Útil para **estructuras de datos simples**.

---

# Struct

```cpp
struct Punto {
    int x, y;

    // Constructor
    Punto(int _x, int _y) {
        x = _x;
        y = _y;
    }

    void mover(int dx, int dy) {
        x += dx; y += dy;
    }
};
```

---

# Clases

- Una **clase** permite definir un **TDA** (Tipo de Dato Abstracto).  
- Puede contener:
  - **Atributos** (datos).
  - **Métodos** (funciones).  
- Controla la **visibilidad**:  
  - `public`, `private`, `protected`.

---

# Clases

```cpp
class Persona {
private:
    string nombre;
    int edad;
public:
    // Constructor
    Persona(string n, int e) {
        nombre = n;
        edad = e;
    }

    void setNombre(string n) { nombre = n; }
    void setEdad(int e) { edad = e; }
};
```
---

# Deque

```cpp
deque<int> dq;

// insertar
dq.push_back(10);
dq.push_front(20);

// eliminar
dq.pop_back();
dq.pop_front();

// acceso
dq.front();
dq.back();
dq[0]; // acceso random

// otros
dq.size();
dq.clear();
```

---

# List

```cpp
list<int> lst;

// insertar
lst.push_back(10);
lst.push_front(20);
auto it = lst.begin();
advance(it, 1);
lst.insert(it, 15);

// eliminar
lst.pop_back();
lst.pop_front();
lst.erase(it);

// iteradores
lst.begin();
lst.end();

// otros
lst.size();
lst.clear();
```

---

# Priority\_Queue

```cpp
// max-heap (default)
priority_queue<int> pq;

// insertar
pq.push(10);

// acceso / eliminar
pq.top();
pq.pop();

// min-heap
priority_queue<int, vector<int>, greater<int>> pqmin;

// con pares (ordena por first)
priority_queue<pair<int,int>> pqpair;
```

---

# unordered\_set

```cpp
unordered_set<int> s;

// insertar
s.insert(5);
s.insert(10);

// buscar
if(s.count(5)) { /* encontrado */ }

// eliminar
s.erase(5);

// iterar
for(int x : s) { /* ... */ }

// otros
s.size();
s.empty();
s.clear();
```

---

# unordered\_map

```cpp
unordered_map<string,int> mp;

// insertar
mp["uno"] = 1;
mp["dos"] = 2;

// buscar
if(mp.count("uno")) { int val = mp["uno"]; }

// actualizar
mp["uno"]++;

// eliminar
mp.erase("uno");

// iterar
for(auto &kv : mp){
    // kv.first, kv.second
}

// otros
mp.size();
mp.empty();
mp.clear();
```

---

# Resta de iteradores

```cpp
vector<int> v = {1,2,3,4,5};
auto it1 = v.begin();
auto it2 = v.begin() + 3;

int pos = it2 - it1; // = 3
```

---

# Ordenar con función custom

```cpp
bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.second == b.second) return a.first < b.first;
    return a.second < b.second;
}

vector<pair<int,int>> v;
sort(v.begin(), v.end(), cmp);
```

---

# Ejemplo de stable\_sort

```cpp
bool cmp2(pair<int,int> a, pair<int,int> b){
    return a.first < b.first;
}

vector<pair<int,int>> v;
stable_sort(v.begin(), v.end(), cmp2);
```

---

# Ejercicio 1

Dado una lista de **$N$ elementos**, responde **$Q$ consultas**:
¿Cuántos elementos tienen valores $L \leq x \leq R$?

---

# Ejercicio 2
Se entrega una matriz de $N$ filas y $M$ columnas que representa una figura en ASCII.  
Determina si existe alguna diagonal donde **todos los caracteres sean iguales**.

---

# Ejercicio 3
Inicialmente tienes un conjunto con $N$ números.  
Debes procesar $Q$ consultas de dos tipos:  
1. Insertar un número.  
2. Dado un número $X$, imprimir y eliminar el **menor número $\geq X$**.

---

# Ejercicio 4
Dado un grafo no dirigido con $N$ nodos y $M$ aristas (nodos numerados de $1$ a $N$), cuenta cuántas **componentes conexas** existen.  
Usa DFS sobre una **lista de adyacencia**.

---

# Ejercicio 5
Implementa un **TDA Cola** utilizando internamente **dos stacks**.
