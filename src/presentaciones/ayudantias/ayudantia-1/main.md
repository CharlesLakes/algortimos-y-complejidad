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
