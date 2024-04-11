# Ayudantía 2
## Análisis Amortizado
### Recomendaciones

Al calcular el costo amortizado por operaciones en una estructura de datos, es esencial determinar cuánto tiempo $T(n)$ se necesita en el peor caso para realizar $n$ operaciones y luego promediarlo con la cantidad total de operaciones $n$. Por lo tanto, el costo amortizado por operación se obtiene mediante la expresión $T(n)/n$.

Para realizar este cálculo de manera efectiva, se sugiere analizar cuántas operaciones elementales se llevan a cabo por cada elemento en la estructura de datos. Es decir, es importante examinar el flujo de operaciones para un elemento individual y luego multiplicarlo por la cantidad total de elementos, considerando que en el peor caso todos los elementos seguirán el mismo patrón de operaciones.
