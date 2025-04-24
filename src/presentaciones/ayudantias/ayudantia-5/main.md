---
marp: true
math: mathjax
paginate: true
footer: Algoritmos y Complejidad
header: Ayudantía 5
---

<!-- _class: title -->
# Ayudantía 4
- Carlos Lagos - carlos.lagosc@usm.cl  
- Nangel Coello - nangel.coello@usm.cl  
- Rafael Baeza - rafael.baezam@usm.cl  
- Benjamín Cárdenas - benjamin.cardenas@usm.cl 

---

<style scoped>
    p,li{
        font-size:23px;
    }
    pre{
        font-size:18px;
    }
</style>


# Costo Temporal y Espacial

<div style="display:flex; justify-content: center;">


<div style="width:50%;">

<!-- 
    Temporal: O(nlog(n))
    Memoria: O(n)
-->

```c++
int minCostHuffman(vector<int> arr){
    int cost = 0;
    priority_queue<int> pq;

    for(int a: arr)
        pq.push(-a);

    while(pq.size() >= 2){
        int value1 = -pq.top();
        pq.pop();

        int value2 = -pq.top();
        pq.pop();

        int sum = value1 + value2;

        cost += sum;

        pq.push(sum);
    }

    return cost;
}
```

</div>

<div style="width:50%; display: flex; justify-content: center;flex-direction:column; padding:10px;">

- ¿Cuál es la complejidad temporal del algoritmo? ¿Mejor caso? ¿Peor Caso?
- ¿Cuál es la complejidad espacial del algoritmo?

</div>

</div>


---

<style scoped>
    p,li{
        font-size:23px;
    }
    pre{
        font-size:18px;
    }
</style>

# Costo Temporal y Espacial (D&C)


<div style="display:flex; justify-content: center;">


<div style="width:50%;">

<!-- 
    T(n) = T(n/3) + O(1)
    Temporal: O(log(n))
    Memoria: O(log(n)) (stack)
-->

```c++
int busquedaTernaria(vector<int> &arr, int x, int izq, int der) {
    if (izq > der) return -1;

    int tercio = (der - izq) / 3;
    int mid1 = izq + tercio;
    int mid2 = der - tercio;

    if (arr[mid1] == x) return mid1;
    if (arr[mid2] == x) return mid2;

    if (x < arr[mid1]) {
        return busquedaTernaria(arr, x, izq, mid1 - 1);
    } else if (x > arr[mid2]) {
        return busquedaTernaria(arr, x, mid2 + 1, der);
    } else {
        return busquedaTernaria(arr, x, mid1 + 1, mid2 - 1);
    }
}
```

</div>

<div style="width:50%; display: flex; justify-content: center;flex-direction:column; padding:10px;">

- ¿Cuál es la complejidad temporal del algoritmo? ¿Peor Caso?
- ¿Cuál es la complejidad espacial del algoritmo?

</div>

</div>

---

<style scoped>
    p,li{
        font-size:23px;
    }
    pre{
        font-size:18px;
    }
</style>

# Correctitud: Invariante de ciclo

<div style="display:flex; justify-content: center;">


<div style="width:50%;">

El siguiente código calcula cuántos subarreglos de un arreglo tienen una suma impar. Para lograrlo, recorre todas las posibles combinaciones de subarreglos dentro del arreglo original. Por cada posición de inicio $i$, se acumulan las sumas desde esa posición hasta el final del arreglo ($j = i$ a $n - 1$). Si la suma acumulada del subarreglo $[i, j]$ es impar, se incrementa un contador. Finalmente, el total de subarreglos con suma impar se retorna como resultado.  

</div>

<div style="width:50%; display: flex; justify-content: center;flex-direction:column; padding:10px;">

```c++
int count_sum_odd_subarray(vector<int> arr){
    int n = arr.size();
    int ans = 0;
    
    for(int i = 0; i < n; i++){
        int acum = 0;
        int preans = 0;
        for(int j = i; j < n; j++){
            acum += arr[j];
            if(acum % 2 != 0)
                preans++; 
        }
        ans += preans;
    }
    return ans;
}
```

</div>

</div>

---

<div align="center">
<h2 style="font-size:400px;">FIN</h2>
</div>