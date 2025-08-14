---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 7
---

<!-- _class: title -->
# Ayudantía 7
- Carlos Lagos - carlos.lagosc@usm.cl  
- Nangel Coello - nangel.coello@usm.cl  
- Rafael Baeza - rafael.baezam@usm.cl  
- Benjamín Cárdenas - benjamin.cardenas@usm.cl 

---

# Ejercicios

Link Ejercicios: https://vjudge.net/contest/717082

- Apple Division 
- Ferris Wheel 

---

# Apple Division 

El número total de divisiones es $2^n$. Como $n$ es como máximo $20$, podemos recorrer eficientemente todas las divisiones y seleccionar la división óptima en la que la diferencia entre las sumas de los pesos sea mínima. Cada división de las $n$ manzanas corresponde a una cadena de bits de longitud $n$, donde cada bit determina a qué grupo pertenece una manzana. Por ejemplo, si los pesos son $[3, 2, 7, 4, 1]$, la cadena de bits $00101$ significa que el primer grupo tiene los pesos $[3, 2, 4]$ y el segundo grupo tiene los pesos $[7, 1]$.

---

<style scoped>
code,pre{
    font-size:14px;
}
</style>

# Apple Division 

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++) cin >> p[i];

    ll diff = 1e9;
    for (int b = 0; b < (1 << n); b++) {
        ll sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            if (b & (1 << i)) {
                sum1 += p[i];
            } else {
                sum2 += p[i];
            }
        }
        diff = min(diff, abs(sum1 - sum2));
    }

    cout << diff << "\n";
}
```

---

<style scoped>
code,pre{
    font-size:14px;
}
</style>

# Apple Division (opción - backtracking)

```cpp
#include <bits/stdc++.h>
 
using namespace std;
typedef long long ll;
 
ll temp;
 
void solve(vector<ll> &l,ll &max,ll sum = 0,ll i = 0){
    if(i == l.size()){
        if(max > abs(abs(temp - sum) - sum))
            max = abs(abs(temp - sum) - sum);
        return;
    }
    solve(l,max,sum,i + 1);
    solve(l,max,sum + l[i],i + 1);
}
 
int main(){
    ll n;
    vector<ll> l;
    cin >> n;
    l.resize(n);
    ll max = 0;
    for(ll i = 0; i < n; i++){
        cin >> l[i];
        max += l[i];
    }
    temp = max;
    solve(l,max);
    cout << max << endl;
}
```

---

# Ferris Wheel

Podemos resolver el problema utilizando un algoritmo greedy que en cada paso coloca al niño más pesado en una góndola. Si el niño más liviano también puede ser colocado en la misma góndola, se hace, y la góndola tendrá dos niños. De lo contrario, el niño más pesado irá solo en la góndola.

El algoritmo puede implementarse ordenando primero los pesos y luego manteniendo dos punteros: uno al niño más liviano y otro al más pesado. Usando estos punteros, siempre podemos encontrar de manera eficiente al niño más liviano y al más pesado.

El algoritmo funciona porque de todas formas debemos colocar al niño más pesado en una góndola, por lo que podemos comenzar con él. También es óptimo elegir al niño más liviano para que esté en la misma góndola. Si “guardáramos” al niño más liviano para otra góndola, esto nunca produciría una mejor solución.

---

<style scoped>
code,pre{
    font-size:14px;
}
</style>

# Ferris Wheel (C++)

```c++
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;

    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    sort(weights.begin(), weights.end());

    int count = 0;
    int i = 0;
    int j = n - 1;
    while (i <= j) {
        if (i < j && weights[i] + weights[j] <= x) {
            count++;
            i++;
            j--;
        } else {
            count++;
            j--;
        }
    }
    cout << count << "\n";
}
```

---

<style scoped>
code,pre{
    font-size:14px;
}
</style>

# Ferris Wheel (Python)

```python
n, x = map(int, input().split())
ws = list(map(int, input().split()))
ws.sort()
i, j = 0, n - 1
cantidad = 0
while i <= j:
    if ws[i] + ws[j] <= x:
        cantidad += 1
        i += 1
        j -= 1
    else:
        cantidad += 1
        j -= 1
print(cantidad)
```

---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>