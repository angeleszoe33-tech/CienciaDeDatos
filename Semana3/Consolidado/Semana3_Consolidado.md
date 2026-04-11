# Semana 3: Python y Análisis Exploratorio de Datos

**Fecha:** 02/04/2025
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Temas cubiertos:** T6 (Python para Ciencia de Datos), T7 (El Proceso de Ciencia de Datos), T8 (Análisis Exploratorio de Datos en Python)

---

## 1. Ejercicios Complementarios

### Ejercicio 1: Variables y Tipos de Datos

```python
# 1. Variables de diferentes tipos
entero    = 25                          # int
decimal   = 3.14                        # float
texto     = "Ciencia de Datos"          # str
booleano  = True                        # bool
lista     = [1, 2, 3, "cuatro", 5.0]   # list
diccion   = {"nombre": "Zoe", "edad": 21, "carrera": "LSTI"}  # dict

# 2. Conversión de tipos
str_num   = "42"
entero2   = int(str_num)      # str → int:   42
decimal2  = float(entero2)    # int → float: 42.0
entero3   = int(3.99)         # float → int: 3  (trunca, no redondea)

# 3. f-strings
nombre = "Zoe"
edad   = 21
print(f"El usuario {nombre} tiene {edad} años.")
print(f"El precio con IVA es: ${decimal2 * 1.16:.2f}")
```

---

### Ejercicio 2: Control de Flujo

```python
# 1. Positivo, negativo o cero
def clasificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

# 2. Menú con if-elif-else
opcion = 2
if   opcion == 1: print("Ver reportes")
elif opcion == 2: print("Agregar datos")
elif opcion == 3: print("Exportar CSV")
else:             print("Opción no válida")

# 3. Loop for sobre una lista
frutas = ["manzana", "pera", "mango", "uva"]
for i, fruta in enumerate(frutas, 1):
    print(f"{i}. {fruta.capitalize()}")

# 4. Factorial con while
def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

print(factorial(5))   # 120
print(factorial(10))  # 3628800
```

---

### Ejercicio 3: Funciones

```python
import math

# 1. Área de un círculo
def area_circulo(radio):
    return round(math.pi * radio ** 2, 4)

print(area_circulo(5))   # 78.5398

# 2. Celsius a Fahrenheit
def celsius_a_fahrenheit(c):
    return round((c * 9/5) + 32, 2)

print(celsius_a_fahrenheit(100))  # 212.0
print(celsius_a_fahrenheit(0))    # 32.0

# 3. Promedio de una lista
def promedio(lista):
    if not lista:
        return 0
    return round(sum(lista) / len(lista), 4)

print(promedio([8.5, 9.0, 7.8, 8.2, 9.5]))  # 8.6

# 4. Máximo y mínimo
def max_min(lista):
    return max(lista), min(lista)

maximo, minimo = max_min([15, 3, 42, 7, 28])
print(f"Máximo: {maximo}, Mínimo: {minimo}")  # Máximo: 42, Mínimo: 3
```

---

### Ejercicio 4: Operaciones con Arrays NumPy

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# 1. Suma elemento a elemento
print(arr1 + arr2)          # [6 6 6 6 6]

# 2. Multiplicación por escalar
print(arr1 * 3)             # [ 3  6  9 12 15]

# 3. Media, mediana y desviación estándar
print(f"Media:    {np.mean(arr1):.2f}")    # 3.00
print(f"Mediana:  {np.median(arr1):.2f}")  # 3.00
print(f"Desv.Std: {np.std(arr1):.2f}")     # 1.41

# 4. Valores únicos
arr3 = np.array([1, 2, 2, 3, 3, 3, 4])
print(np.unique(arr3))      # [1 2 3 4]

# 5. Reshape 1D → 2D
arr4 = np.arange(1, 13)
matriz = arr4.reshape(3, 4)
print(matriz)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
```

---

### Ejercicio 5: Álgebra con NumPy

```python
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# 1. Producto punto
print(np.dot(v1, v2))          # 32  (1×4 + 2×5 + 3×6)

# 2. Producto cruz
print(np.cross(v1, v2))        # [-3  6 -3]

# 3. Magnitud de cada vector
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)
print(f"|v1| = {mag_v1:.4f}")  # 3.7417
print(f"|v2| = {mag_v2:.4f}")  # 8.7750

# 4. Normalización
v1_norm = v1 / mag_v1
v2_norm = v2 / mag_v2
print(f"v1 normalizado: {np.round(v1_norm, 4)}")  # [0.2673 0.5345 0.8018]
print(f"v2 normalizado: {np.round(v2_norm, 4)}")  # [0.4558 0.5698 0.6838]
```

---

### Ejercicio 6: DataFrames Básico con Pandas

```python
import pandas as pd

data = {
    'nombre':   ['Ana', 'Luis', 'María', 'Carlos', 'Sofia'],
    'edad':     [20, 22, 19, 21, 23],
    'carrera':  ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}
df = pd.DataFrame(data)

# 1. Seleccionar columna 'nombre'
print(df['nombre'].tolist())
# ['Ana', 'Luis', 'María', 'Carlos', 'Sofia']

# 2. Filtrar estudiantes con promedio > 8.5
print(df[df['promedio'] > 8.5][['nombre', 'promedio']])
#   nombre  promedio
# 1   Luis       9.0
# 4  Sofia       9.5

# 3. Ordenar por edad
print(df.sort_values('edad'))

# 4. Agregar columna 'aprobado'
df['aprobado'] = df['promedio'] >= 7.0
print(df[['nombre', 'promedio', 'aprobado']])

# 5. Group by carrera y promediar
print(df.groupby('carrera')['promedio'].mean().round(2))
# carrera
# Ing    8.57
# Lic    8.65
```

---

### Ejercicio 7: Manipulación de Datos

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nombre':   ['Ana', 'Luis', 'María', 'Carlos', 'Sofia', 'Ana'],
    'edad':     [20, 22, np.nan, 21, 23, 20],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5, 8.5]
})

# 1. Manejo de valores faltantes
print(f"Nulos antes: {df.isnull().sum().sum()}")   # 1
df['edad'] = df['edad'].fillna(df['edad'].median())
print(f"Nulos después: {df.isnull().sum().sum()}")  # 0

# 2. Eliminar duplicados
df = df.drop_duplicates()
print(f"Filas tras eliminar duplicados: {len(df)}")  # 5

# 3. Aplicar función con apply()
df['promedio_letra'] = df['promedio'].apply(
    lambda x: 'A' if x >= 9 else ('B' if x >= 8 else 'C'))
print(df[['nombre', 'promedio', 'promedio_letra']])

# 4. loc e iloc
print(df.loc[df['nombre'] == 'Ana'])    # por etiqueta y condición
print(df.iloc[0:3, 0:2])               # primeras 3 filas, primeras 2 columnas

# 5. Concatenar dos DataFrames
df2 = pd.DataFrame({'nombre': ['Pedro'], 'edad': [24], 'promedio': [8.8]})
df_total = pd.concat([df[['nombre','edad','promedio']], df2], ignore_index=True)
print(df_total)
```

---

### Ejercicio 8: Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Ejercicios de Matplotlib', fontsize=14, fontweight='bold')

# 1. Gráfico de línea
axes[0,0].plot(x, y, color='#185FA5', linewidth=2, label='sin(x)')
axes[0,0].plot(x, np.cos(x), color='#D85A30', linewidth=2, linestyle='--', label='cos(x)')
axes[0,0].set_title('Gráfico de Línea'); axes[0,0].legend(); axes[0,0].grid(alpha=0.4)

# 2. Gráfico de dispersión
np.random.seed(42)
axes[0,1].scatter(np.random.randn(100), np.random.randn(100), color='#3B6D11', alpha=0.6, s=30)
axes[0,1].set_title('Dispersión'); axes[0,1].grid(alpha=0.4)

# 3. Histograma
datos = np.random.normal(0, 1, 500)
axes[1,0].hist(datos, bins=25, color='#534AB7', alpha=0.8, edgecolor='white')
axes[1,0].axvline(datos.mean(), color='red', lw=2, label=f'Media: {datos.mean():.2f}')
axes[1,0].set_title('Histograma'); axes[1,0].legend(); axes[1,0].grid(alpha=0.4)

# 4. Gráfico de barras
categorias = ['Pandas', 'NumPy', 'Matplotlib', 'Scikit-learn', 'Seaborn']
valores    = [85, 90, 75, 70, 80]
axes[1,1].bar(categorias, valores, color=['#185FA5','#D85A30','#3B6D11','#534AB7','#854F0B'], alpha=0.85)
axes[1,1].set_title('Barras'); axes[1,1].set_ylabel('Popularidad (%)')
for i, v in enumerate(valores): axes[1,1].text(i, v+1, str(v), ha='center', fontsize=9)
axes[1,1].grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('ejercicio_matplotlib.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

### Ejercicio 9: Análisis Exploratorio con Seaborn

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset iris
iris = sns.load_dataset('iris')

# 1. Info básica
print(iris.shape)          # (150, 5)
print(iris.dtypes)
print(iris.head())

# 2. Estadísticas descriptivas
print(iris.describe())

# 3. Histogramas de columnas numéricas
iris.hist(figsize=(10, 6), bins=20, color='#185FA5', edgecolor='white')
plt.suptitle('Distribuciones del Dataset Iris'); plt.tight_layout(); plt.show()

# 4. Matriz de correlación
corr = iris.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Correlaciones Iris'); plt.show()

# 5. Boxplots por categoría
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, ['sepal_length','sepal_width','petal_length','petal_width']):
    sns.boxplot(data=iris, x='species', y=col, ax=ax, palette=['#185FA5','#D85A30','#3B6D11'])
    ax.set_title(col)
plt.tight_layout(); plt.show()

# 6. Identificar outliers con IQR
for col in iris.select_dtypes('float64').columns:
    Q1, Q3 = iris[col].quantile(0.25), iris[col].quantile(0.75)
    IQR   = Q3 - Q1
    outs  = iris[(iris[col] < Q1 - 1.5*IQR) | (iris[col] > Q3 + 1.5*IQR)]
    print(f"{col}: {len(outs)} outliers")
```

---

### Ejercicio 10: Medidas de Tendencia Central (cálculo manual)

**[5, 3, 8, 3, 7]**
- Ordenados: [3, 3, 5, 7, 8]
- **Media:** (5+3+8+3+7)/5 = 26/5 = **5.2**
- **Mediana:** valor central = **5**
- **Moda:** **3** (aparece 2 veces)

**[10, 20, 30, 40]**
- **Media:** (10+20+30+40)/4 = 100/4 = **25.0**
- **Mediana:** (20+30)/2 = **25.0** (número par de datos)
- **Moda:** **no hay** (todos aparecen una vez)

**[1, 2, 2, 3, 3, 3, 4]**
- **Media:** (1+2+2+3+3+3+4)/7 = 18/7 = **2.57**
- **Mediana:** valor central (posición 4) = **3**
- **Moda:** **3** (aparece 3 veces)

---

### Ejercicio 11: Dispersión (cálculo manual)

**[2, 4, 4, 4, 5, 5, 7, 9] — n=8, Media=5**

- **Rango:** 9 − 2 = **7**
- **Varianza:** [(2-5)²+(4-5)²+(4-5)²+(4-5)²+(5-5)²+(5-5)²+(7-5)²+(9-5)²] / 8
  = [9+1+1+1+0+0+4+16] / 8 = 32/8 = **4.0**
- **Desviación Estándar:** √4.0 = **2.0**

**[1, 3, 5, 7, 9] — n=5, Media=5**

- **Rango:** 9 − 1 = **8**
- **Varianza:** [(1-5)²+(3-5)²+(5-5)²+(7-5)²+(9-5)²] / 5
  = [16+4+0+4+16] / 5 = 40/5 = **8.0**
- **Desviación Estándar:** √8.0 = **2.83**

---

### Ejercicio 12: El Proceso de Data Science

**1. ¿Qué es el ciclo CRISP-DM?**

CRISP-DM (Cross-Industry Standard Process for Data Mining) es la metodología más usada en proyectos de ciencia de datos. Define 6 fases iterativas:

1. **Comprensión del negocio:** definir objetivos, preguntas y criterios de éxito.
2. **Comprensión de los datos:** recolectar, explorar y verificar calidad de los datos.
3. **Preparación de los datos:** limpiar, transformar, seleccionar variables.
4. **Modelado:** seleccionar y aplicar algoritmos de ML.
5. **Evaluación:** verificar que el modelo cumple los objetivos de negocio.
6. **Despliegue:** poner el modelo en producción y monitorear.

Es iterativo: los hallazgos en etapas tardías pueden requerir regresar a etapas anteriores.

**2. Fases del proceso de ciencia de datos:**
Comprensión del problema → Recolección de datos → Limpieza → EDA → Modelado → Evaluación → Comunicación de resultados → Despliegue.

**3. MVP en Ciencia de Datos:**
El MVP (Minimum Viable Product) es la versión más simple de un modelo o solución que ya entrega valor real al negocio. En lugar de construir el modelo perfecto, se lanza una versión básica para validar la hipótesis con datos reales y se itera sobre ella.

---

### Ejercicio 13: Caso de Estudio — EDA en la práctica

**Caso: Netflix — Análisis exploratorio para el sistema de recomendación**

- **Preguntas clave:** ¿Qué géneros consumen más usuarios por región? ¿A qué hora del día se consume más contenido? ¿Qué factores predicen si un usuario terminará una serie?
- **Técnicas usadas:** análisis de series de tiempo sobre historial de visualización, clustering de usuarios por preferencias, análisis de correlación entre duración de episodios y tasa de finalización, visualización con heatmaps de consumo por hora.
- **Insights encontrados:** los usuarios que ven el primer episodio en menos de 24h tienen 80% más probabilidad de completar la serie; el consumo en móvil correlaciona negativamente con la tasa de finalización; el viernes por la noche es el horario con mayor pico de actividad global.

---

## 2. Actividades Prácticas

### Actividad 3.1: Refuerzo de Python

```python
# Listas y comprensiones
cuadrados = [x**2 for x in range(1, 11)]
pares     = [x for x in range(1, 21) if x % 2 == 0]

# Diccionarios
inventario = {'laptop': 15, 'mouse': 45, 'teclado': 30}
precios    = {'laptop': 15000, 'mouse': 350, 'teclado': 800}
valor_total = {prod: inventario[prod]*precios[prod] for prod in inventario}

# Lambda
multiplicar = lambda x, y: x * y
ordenar_por_segundo = sorted([(1,'b'),(3,'a'),(2,'c')], key=lambda t: t[1])

# Manejo de errores
def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"
    except TypeError:
        return "Error: tipos de datos inválidos"

print(dividir_seguro(10, 2))   # 5.0
print(dividir_seguro(10, 0))   # Error: división entre cero
```

---

### Actividad 3.2: Carga y Exploración del Dataset Airbnb

```python
import pandas as pd

df = pd.read_csv('Datos/airbnb_nyc.csv')

# Primeras 10 filas
print(df.head(10))

# Información del dataset
print(df.info())
print(df.describe())

# Tipos de datos
print(df.dtypes)

# Valores nulos
print(df.isnull().sum())
# last_review          511
# reviews_per_month    513

# Estadísticas básicas
print(f"Rango de precios: ${df['price'].min()} — ${df['price'].max()}")
print(f"Precio promedio: ${df['price'].mean():.2f}")
print(f"Listings por borough:\n{df['neighbourhood_group'].value_counts()}")
```

---

### Actividad 3.3: Limpieza del Dataset

```python
df_limpio = df.copy()

# Convertir fechas
df_limpio['last_review'] = pd.to_datetime(df_limpio['last_review'], errors='coerce')

# Imputar nulos
df_limpio['reviews_per_month'] = df_limpio['reviews_per_month'].fillna(0)
df_limpio['last_review'] = df_limpio['last_review'].fillna(pd.Timestamp('2019-01-01'))

# Eliminar outliers extremos
print(f"Antes: {len(df_limpio)} registros")
df_limpio = df_limpio[(df_limpio['price'] <= 500) & (df_limpio['minimum_nights'] <= 30)]
print(f"Después: {len(df_limpio)} registros")

# Estandarizar nombres de columnas
df_limpio.columns = [c.lower().replace(' ','_') for c in df_limpio.columns]

# Verificar resultado
print(df_limpio.isnull().sum().sum())  # 0 nulos
```

---

### Actividad 3.4: Visualización Exploratoria

Las visualizaciones generadas están en la carpeta `Visualizaciones/`:

- `hist_precio.png` — Histograma de precios + precio mediano por borough
- `boxplot_precios.png` — Boxplots por tipo de habitación y por borough
- `scatter_relaciones.png` — Dispersión precio vs reseñas y vs disponibilidad
- `heatmap_correlaciones.png` — Mapa de calor de correlaciones entre variables
- `distribucion_tipos.png` — Pastel de tipos de habitación + barras por borough

---

## 3. Avance del Proyecto — EDA Mercado Inmobiliario Airbnb NYC

### 3.1 Definición del Problema

**Objetivo del proyecto:**
Realizar un análisis exploratorio profundo del mercado de alojamientos Airbnb en Nueva York para comprender la distribución de precios, identificar los factores que más influyen en el precio por noche y detectar patrones por ubicación y tipo de propiedad. Los hallazgos establecerán la base para el desarrollo posterior de un modelo predictivo de precios.

**Preguntas clave de investigación:**
1. ¿Cómo se distribuyen los precios por noche en los diferentes boroughs de Nueva York?
2. ¿Qué tipo de habitación tiene mayor impacto en el precio?
3. ¿Existe correlación entre el número de reseñas y el precio?
4. ¿Qué variables numéricas están más relacionadas con el precio?
5. ¿Cómo se distribuye la disponibilidad anual de los alojamientos?

---

### 3.2 Descripción del Dataset

**Fuente:** Basado en el dataset Airbnb NYC disponible en Kaggle.
**Registros:** 8,000 listings (7,440 tras limpieza de outliers)
**Columnas:** 16 variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `id` | Numérico entero | Identificador único del listing |
| `name` | Texto | Nombre descriptivo del alojamiento |
| `host_id` | Numérico entero | ID del anfitrión |
| `host_name` | Texto | Nombre del anfitrión |
| `neighbourhood_group` | Categórico | Borough (Manhattan, Brooklyn, etc.) |
| `neighbourhood` | Categórico | Vecindario específico |
| `latitude` | Numérico decimal | Coordenada latitud |
| `longitude` | Numérico decimal | Coordenada longitud |
| `room_type` | Categórico | Tipo de habitación |
| `price` | Numérico entero | Precio por noche en USD |
| `minimum_nights` | Numérico entero | Mínimo de noches por reserva |
| `number_of_reviews` | Numérico entero | Total de reseñas recibidas |
| `last_review` | Fecha | Fecha de la última reseña |
| `reviews_per_month` | Numérico decimal | Promedio de reseñas por mes |
| `calculated_host_listings_count` | Numérico entero | Listings del mismo anfitrión |
| `availability_365` | Numérico entero | Días disponibles en el año |

**Valores nulos identificados:**
- `last_review`: 511 nulos (listings sin reseñas → imputados con fecha base)
- `reviews_per_month`: 513 nulos (sin actividad → imputados con 0)

---

### 3.3 Análisis Descriptivo

**Estadísticas de variables numéricas clave:**

| Variable | Media | Mediana | Moda | Desv. Std | Mínimo | Máximo | Q1 | Q3 |
|----------|-------|---------|------|-----------|--------|--------|-----|-----|
| Precio (USD) | 120.81 | 104.00 | 75 | 85.66 | 10 | 475 | 56 | 170 |
| Noches mínimas | 4.77 | 3.00 | 1 | 5.64 | 1 | 30 | 1 | 7 |
| Núm. reseñas | 24.53 | 8.00 | 0 | 41.82 | 0 | 398 | 1 | 32 |
| Disponibilidad | 178.49 | 175.00 | 0 | 132.87 | 0 | 365 | 46 | 315 |

**Precio mediano por Borough:**

| Borough | Precio mediano | Precio promedio | Listings |
|---------|---------------|-----------------|---------|
| Manhattan | $164 | $192.45 | 2,985 |
| Brooklyn | $106 | $122.38 | 2,359 |
| Queens | $73 | $93.12 | 1,265 |
| Staten Island | $67 | $85.21 | 298 |
| Bronx | $55.50 | $75.67 | 533 |

**Precio por tipo de habitación:**

| Tipo | Precio promedio | Precio mediano | Listings |
|------|----------------|----------------|---------|
| Entire home/apt | $155.56 | $135 | 3,805 (51.1%) |
| Private room | $87.57 | $75 | 3,243 (43.6%) |
| Shared room | $58.58 | $50 | 392 (5.3%) |

**Variables que más influyen en el precio (correlación de Pearson):**

| Variable | Correlación con precio |
|----------|----------------------|
| Reseñas/mes | 0.023 (muy débil positiva) |
| Núm. reseñas | 0.014 (prácticamente nula) |
| Disponibilidad | 0.006 (prácticamente nula) |
| Noches mínimas | 0.004 (prácticamente nula) |

> **Insight:** Las variables numéricas disponibles tienen correlación muy baja con el precio. Esto sugiere que las variables más determinantes son **categóricas**: el borough y el tipo de habitación, que requieren codificación para modelado predictivo.

---

### 3.4 Visualizaciones

#### Gráfica 1: Distribución de Precios

![Histograma y precio por borough](Visualizaciones/hist_precio.png)

**Interpretación:**
La distribución del precio por noche muestra un **sesgo positivo marcado** (cola derecha). La mayoría de listings se concentra entre $30 y $200, con la mediana ($104) significativamente menor que la media ($121), confirma el sesgo. Existe un grupo pequeño de alojamientos premium que eleva el promedio. En el gráfico de barras, Manhattan lidera ampliamente con $164 de mediana, más del doble que el Bronx ($55.50), reflejando la diferencia en valor de ubicación en Nueva York.

---

#### Gráfica 2: Boxplots de Precio

![Boxplots de precio](Visualizaciones/boxplot_precios.png)

**Interpretación:**
El boxplot por tipo de habitación confirma la jerarquía esperada: alojamiento completo > habitación privada > habitación compartida. La caja del "Entire home/apt" es notablemente más amplia, indicando mayor variabilidad en precios (desde $50 hasta $400+ para propiedades premium). Por borough, Manhattan muestra la distribución más amplia y con más valores atípicos superiores, lo que refleja la presencia de propiedades de lujo. El Bronx tiene la distribución más compacta y baja, con menos variabilidad.

---

#### Gráfica 3: Diagramas de Dispersión

![Scatter de relaciones](Visualizaciones/scatter_relaciones.png)

**Interpretación:**
- **Precio vs Reseñas (r=0.014):** La correlación es prácticamente nula. Los listings más populares (más reseñas) no son necesariamente los más caros ni los más baratos. Esto indica que la popularidad y el precio son variables independientes.
- **Precio vs Disponibilidad (r=0.006):** No existe relación entre cuántos días está disponible un alojamiento y su precio. Alojamientos de todos los niveles de precio pueden estar disponibles todo el año o muy poco tiempo.

---

#### Gráfica 4: Mapa de Calor de Correlaciones

![Heatmap correlaciones](Visualizaciones/heatmap_correlaciones.png)

**Interpretación:**
El mapa de calor confirma que las correlaciones entre variables numéricas son todas muy cercanas a cero, excepto entre `reseñas/mes` y `número de reseñas` (correlación positiva esperada: más reseñas acumuladas = mayor tasa mensual). La variable precio no tiene correlación significativa con ninguna variable numérica del dataset, lo que indica que el poder predictivo del precio reside en las variables categóricas (borough, tipo de habitación) que deben ser tratadas con encoding para el modelo predictivo.

---

#### Gráfica 5: Distribución por Tipo y Borough

![Distribución tipos](Visualizaciones/distribucion_tipos.png)

**Interpretación:**
El 51.1% de los listings son alojamientos completos, seguidos de habitaciones privadas (43.6%). Las habitaciones compartidas representan solo el 5.3%, lo que refleja la preferencia del mercado por privacidad. En cuanto a distribución geográfica, Manhattan concentra el mayor número de listings (40% del total), seguido de Brooklyn (32%), consolidando ambos como los mercados dominantes de Airbnb en Nueva York.

---

### 3.5 Hallazgos Principales

1. **El precio está determinado principalmente por variables categóricas**, no numéricas. Borough y tipo de habitación son los predictores clave identificados en el EDA.

2. **Manhattan cobra una prima de precio significativa:** su mediana ($164) es 3x la del Bronx ($55), reflejando el valor de la ubicación en el mercado inmobiliario temporal.

3. **La distribución de precios está sesgada a la derecha**, con la mayoría de listings entre $30-$200, pero con una cola de propiedades premium que eleva el promedio. Para el modelado predictivo se recomienda aplicar transformación logarítmica al precio.

4. **No existe correlación entre popularidad (reseñas) y precio.** Listings económicos pueden tener muchas reseñas y viceversa, lo que sugiere que los huéspedes no basan su elección únicamente en el precio.

5. **Los alojamientos completos dominan el mercado** (51.1%) y son los más caros en promedio, pero las habitaciones privadas representan el 43.6%, mostrando un mercado diverso en oferta.

6. **Próximos pasos para el modelado:** codificar variables categóricas (One-Hot Encoding para borough y room_type), aplicar transformación logarítmica al precio, evaluar modelos de regresión lineal y árbol de decisión.

---

## 4. Resumen de Aprendizaje

- El EDA no es solo calcular estadísticas: es el proceso de hacerse preguntas sobre los datos y usar visualizaciones para responderlas.
- La diferencia entre media y mediana revela el sesgo de una distribución, un dato crucial antes de aplicar cualquier modelo estadístico.
- Una correlación cercana a cero entre variables numéricas no significa que no exista relación, sino que la relación puede estar en variables categóricas.
- La limpieza de datos (nulos, outliers) afecta directamente la calidad de los análisis: los precios extremos distorsionaban completamente las estadísticas.
- CRISP-DM es más que una metodología, es una forma de pensar iterativa: los hallazgos del EDA ya nos dicen qué transformaciones necesitará el modelo en la siguiente fase.
- NumPy y Pandas son complementarios: NumPy para operaciones matemáticas vectorizadas, Pandas para manipulación de datos tabulares con etiquetas.

---

## 5. Dudas o Preguntas

- ¿Cuándo es mejor aplicar transformación logarítmica vs normalización en variables con sesgo positivo para regresión?
- ¿Cómo manejar el encoding de variables categóricas de alta cardinalidad (como el vecindario específico con 20+ valores) sin inflar la dimensionalidad del modelo?

---

## 6. Commits Realizados

```
Semana3: Ejercicios complementarios Python, NumPy, Pandas y estadística
Semana3: Actividades prácticas 3.1 a 3.4
Semana3: Avance del proyecto - Dataset Airbnb NYC generado
Semana3: Avance del proyecto - EDA completo con 5 visualizaciones
Semana3: Consolidado completo
```

---

## 7. Referencias

- McKinney, W. (2022). *Python for Data Analysis, 3rd ed.* O'Reilly Media.
- VanderPlas, J. (2016). *Python Data Science Handbook.* O'Reilly Media.
- Waskom, M. (2021). *Seaborn: Statistical Data Visualization.* JOSS.
- Hunter, J.D. (2007). *Matplotlib: A 2D Graphics Environment.* Computing in Science & Engineering.
- Kaggle. (2024). *Airbnb Price Prediction Dataset.* https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction
- Sheridan, R. (2018). *CRISP-DM: A Standard Methodology for Data Mining Projects.* IBM Analytics.
- Pandas Development Team. (2024). *Pandas Documentation.* https://pandas.pydata.org/docs/
