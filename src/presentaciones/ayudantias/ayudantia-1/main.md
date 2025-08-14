---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 1
---

<!-- _class: title -->

# Ayudantía 1

Carlos Lagos - [carlos.lagosc@usm.cl](mailto:carlos.lagosc@usm.cl)

---

# Estructura base

```c++
#include <bits/stdc++.h> // #include <iostream>

using namespace std;

int main(){
    /* Aquí va el código principal del programa */
    string nombre; 
    cin >> nombre;
    
    cout << "Hola " << nombre << endl; 
    return 0;
}
```

---

# Compilación

```sh
g++ main.cpp -o main
```

---

# Entrada y salida estándar

La entrada y salida estándar se refiere a la entrada desde la "consola" y salida hacia la "consola".
Se llama salida estándar porque no depende de un archivo y, externamente, esta salida se puede redirigir.

```sh
./main < input.txt
```

```sh
./main > output.txt
```

```sh
./main < input.txt > output.txt
```

---

# Tipos de datos básicos

* **int** → Entero (32 bits)
* **long long** → Entero largo (64 bits)
* **float** → Número decimal de precisión simple (32 bits)
* **double** → Número decimal de precisión doble (64 bits)
* **long double** → Número decimal de precisión extendida (80 o 128 bits según el compilador)
* **bool** → Valor lógico (true o false) (8 bits, aunque solo usa 1 bit efectivo)
* **char** → Carácter (8 bits)

---

# Operaciones C++

* **Suma (`+`)** → Suma dos valores.
* **Resta (`-`)** → Resta un valor de otro.
* **Multiplicación (`*`)** → Multiplica dos valores.
* **División (`/`)** → Divide un valor entre otro (entera si son enteros).
* **Módulo (`%`)** → Resto de la división entera.
* **Incremento (`++`)** → Aumenta en 1 el valor de una variable.
* **Decremento (`--`)** → Disminuye en 1 el valor de una variable.
* **Asignación (`=`)** → Asigna un valor a una variable.
* **Asignaciones combinadas (`+=`, `-=`, `*=`, `/=`, `%=`)** → Operación y asignación en un solo paso.

---

# Operadores de comparación

* **Mayor que (`>`)** → Verdadero si el valor de la izquierda es mayor que el de la derecha.
* **Menor que (`<`)** → Verdadero si el valor de la izquierda es menor que el de la derecha.
* **Mayor o igual que (`>=`)** → Verdadero si el valor de la izquierda es mayor o igual que el de la derecha.
* **Menor o igual que (`<=`)** → Verdadero si el valor de la izquierda es menor o igual que el de la derecha.
* **Igualdad (`==`)** → Verdadero si ambos valores son iguales.
* **Desigualdad (`!=`)** → Verdadero si ambos valores son diferentes.

---

# Operaciones lógicas

* **AND lógico (`&&`)** → Verdadero si ambos operandos son verdaderos.
* **OR lógico (`||`)** → Verdadero si al menos un operando es verdadero.
* **NOT lógico (`!`)** → Invierte el valor lógico (true → false, false → true).

---

# Operaciones bitwise

* **AND bit a bit (`&`)** → Compara cada bit y devuelve 1 si ambos bits son 1.
* **OR bit a bit (`|`)** → Compara cada bit y devuelve 1 si al menos un bit es 1.
* **XOR bit a bit (`^`)** → Devuelve 1 si los bits son diferentes.
* **NOT bit a bit (`~`)** → Invierte cada bit.
* **Desplazamiento a la izquierda (`<<`)** → Mueve los bits a la izquierda, insertando ceros.
* **Desplazamiento a la derecha (`>>`)** → Mueve los bits a la derecha.

---

# Sintaxis básica

* Comentarios:  
  `// una línea`  
  `/* varias líneas */`

* Declaración:  
  `int edad;`  

* Inicialización:  
  `int edad = 20;`

---

# Bloque de código

```cpp
{
    int x = 5;
    cout << x << endl;
}
````

---

# if - else

```cpp
int edad = 18;
if (edad >= 18) {
    cout << "Mayor" << endl;
} else {
    cout << "Menor" << endl;
}
```

---

# while

```cpp
int i = 0;
while (i < 5) {
    cout << i << " ";
    i++;
}
```

---

# do-while

```cpp
int i = 0;
do {
    cout << i << " ";
    i++;
} while (i < 5);
```

---

# for

```cpp
for (int i = 0; i < 5; i++) {
    cout << i << " ";
}
```

---

# break y continue

```cpp
for (int i = 0; i < 5; i++) {
    if (i == 3) break;
    cout << i << " ";
}
```

```cpp
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;
    cout << i << " ";
}
```

---

# Funciones

```cpp
int sumar(int a, int b) {
    return a + b;
}

int main() {
    cout << sumar(3, 4);
}
```

---

# Ejercicio 1

Dado dos numeros enteros positivos a y b (<= 1e9), calcula:

$$
\lceil \frac{a}{b} \rceil
$$

