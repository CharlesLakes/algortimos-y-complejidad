---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía Final
---

<!-- _class: title -->
# Ayudantía Final
- Carlos Lagos - carlos.lagosc@usm.cl  
- Nangel Coello - nangel.coello@usm.cl  
- Rafael Baeza - rafael.baezam@usm.cl  
- Benjamín Cárdenas - benjamin.cardenas@usm.cl 

---

# Conceptos

Indique qué características debe tener un problema computacional para ser clasificado en las siguientes clases:

* $P$
* $NP$
* $NP-Hard$
* $NP-Completo$

---

# Análisis

<style scoped>
    code,pre{
        width:80%;
    }
</style>

<div style="display:flex;padding:10px;">

<div style="width:50%;display:flex;align-items:center;text-align:center;">

Dado el siguiente código, indicar, en notación asintótica $O$, el costo temporal y espacial en el **peor caso** del siguiente programa, en función de $n$ y $m$.


</div>


<div style="width:50%;display:flex;align-items:center;justify-content:center;">

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n,m;
    cin >> n >> m;
    vector<int> as(n),bs(m);
    for(int i = 0; i < n; i++) cin >> as[i];
    for(int i = 0; i < m; i++) cin >> bs[i];

    (bs.begin(),bs.end());

    as[0] = min(as[0],bs[0] - as[0]);

    for(int i = 1; i < n; i++) {
        int temp = as[i] + as[i - 1];
        auto it = lower_bound(bs.begin(),bs.end(),temp);
        if(it != bs.end()) {
            int v = *it;
            if(as[i] >= as[i - 1]) as[i] = min(as[i],v - as[i]);
            else as[i] = v - as[i];
        }
    }

    bool check = true;
    for(int i = 1; i < n; i++)
        check = check && as[i - 1] <= as[i];

    if(check) cout << "YES" << endl;
    else cout << "NO" << endl;

    return 0;
}
```

</div>

</div>

---

# Resolución

## Enunciado

Carlos va muy atrasado a las clases de la universidad, pero necesita dinero para la locomoción. Sabe que tiene una fila de monedas dispuestas una al lado de la otra, donde $a_1$ representa el valor de la moneda en la primera posición y $a_n$ el valor en la última. 

Como está apurado, quiere tomar un **subsegmento** (es decir, un grupo de monedas contiguas) rápidamente. Sin embargo, antes de hacerlo, se pregunta: 

> ¿Cuál es el subsegmento cuya suma total de monedas es la mayor posible? 

Cabe destacar que, en su mundo, las monedas pueden tener valores **negativos**.

---

# Resolución

## Entrada

- La primera línea contiene un entero $n$, que representa la cantidad de monedas.
- La segunda línea contiene $n$ enteros separados por espacios, donde cada entero representa el valor de una moneda.

## Salida

Un único entero que representa el **mayor monto total** que Carlos puede obtener al tomar un subsegmento de monedas.

---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>