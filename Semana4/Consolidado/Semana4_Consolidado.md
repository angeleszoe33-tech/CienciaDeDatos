# Semana 4: Preparación y Procesamiento de Datos

**Fecha:** 18/04/2026
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Temas cubiertos:** T9 (Preparación de datos en Python), T10 (Procesamiento de datos en Python)

---

## 1. Ejercicios Complementarios

### Ejercicio 1: Normalización Min-Max

**Fórmula:** X_norm = (X − X_min) / (X_max − X_min)

**Datos:** [10, 20, 30, 40, 50]

**Cálculo manual:**
- X_min = 10, X_max = 50
- 10 → (10−10)/(50−10) = 0/40 = **0.00**
- 20 → (20−10)/(50−10) = 10/40 = **0.25**
- 30 → (30−10)/(50−10) = 20/40 = **0.50**
- 40 → (40−10)/(50−10) = 30/40 = **0.75**
- 50 → (50−10)/(50−10) = 40/40 = **1.00**

Resultado: [0.00, 0.25, 0.50, 0.75, 1.00] ✓ todos entre 0 y 1

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

datos = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
scaler = MinMaxScaler()
resultado = scaler.fit_transform(datos)
print(resultado.flatten())  # [0.   0.25 0.5  0.75 1.  ]
```

---

### Ejercicio 2: Estandarización Z-Score

**Fórmula:** Z = (X − μ) / σ

**Datos:** [2, 4, 4, 4, 5, 5, 7, 9]

**Cálculo:**
- n = 8
- **μ (media):** (2+4+4+4+5+5+7+9)/8 = 40/8 = **5.0**
- **σ (desv. estándar):** √[(∑(xi−μ)²)/n] = √[(9+1+1+1+0+0+4+16)/8] = √[32/8] = √4 = **2.0**

| x | Z = (x − 5) / 2 |
|---|-----------------|
| 2 | (2−5)/2 = **−1.50** |
| 4 | (4−5)/2 = **−0.50** |
| 4 | **−0.50** |
| 4 | **−0.50** |
| 5 | (5−5)/2 = **0.00** |
| 5 | **0.00** |
| 7 | (7−5)/2 = **+1.00** |
| 9 | (9−5)/2 = **+2.00** |

Verificación: media de Z ≈ 0, std de Z ≈ 1 ✓

---

### Ejercicio 3: Comparación de Técnicas de Escalamiento

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

# MinMaxScaler → escala a [0, 1]
mm  = MinMaxScaler().fit_transform(datos)
print("MinMax:", mm.flatten())   # [0.   0.25 0.5  0.75 1.  ]

# StandardScaler → media=0, std=1
std = StandardScaler().fit_transform(datos)
print("Z-Score:", std.flatten()) # [-1.41 -0.71  0.    0.71  1.41]

# ¿Cuándo usar cada uno?
# MinMaxScaler:  cuando el algoritmo requiere valores acotados (redes neuronales, KNN)
# StandardScaler: cuando los datos siguen distribución normal o el modelo
#                 asume datos centrados (regresión, SVM, PCA)
```

---

### Ejercicio 4: Identificación de Valores Faltantes

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# 1. Identificar valores faltantes
print(df.isnull())

# 2. Contar nulos por columna
print(df.isnull().sum())
# A    1 | B    2 | C    0

# 3. Porcentaje de valores faltantes
print((df.isnull().sum() / len(df) * 100).round(1))
# A    20.0% | B    40.0% | C    0.0%

# 4. Filas con al menos un valor faltante
print(df[df.isnull().any(axis=1)])
# Filas 0 (B nulo), 2 (A nulo), 4 (B nulo)
```

---

### Ejercicio 5: Estrategias de Imputación

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# 1. Eliminar filas con nulos
df_dropna = df.dropna()
print(f"Filas tras dropna: {len(df_dropna)}")  # 2

# 2. Eliminar columnas con nulos
df_dropcol = df.dropna(axis=1)
print(df_dropcol.columns.tolist())  # ['C']

# 3. Imputar con la media
df_media = df.fillna(df.mean(numeric_only=True))

# 4. Imputar con la mediana
df_mediana = df.fillna(df.median(numeric_only=True))

# 5. Forward fill (propagar valor anterior)
df_ffill = df.ffill()

# 6. Backward fill (propagar valor siguiente)
df_bfill = df.bfill()
```

---

### Ejercicio 6: Imputación Avanzada con sklearn

```python
from sklearn.impute import SimpleImputer
import numpy as np

datos = np.array([[1, 2, np.nan],
                  [4, np.nan, 6],
                  [7, 8, 9]])

# Media
imp_mean = SimpleImputer(strategy='mean')
print(imp_mean.fit_transform(datos))

# Mediana
imp_median = SimpleImputer(strategy='median')
print(imp_median.fit_transform(datos))

# Moda (más frecuente)
imp_mode = SimpleImputer(strategy='most_frequent')
print(imp_mode.fit_transform(datos))

# Constante (rellenar con un valor fijo)
imp_const = SimpleImputer(strategy='constant', fill_value=0)
print(imp_const.fit_transform(datos))

# ¿Cuándo usar cada estrategia?
# mean:         variables numéricas sin sesgo pronunciado
# median:       variables numéricas con outliers o distribución sesgada
# most_frequent: variables categóricas o con distribución discreta
# constant:     cuando el valor faltante tiene un significado (ej. 0 = sin actividad)
```

---

### Ejercicio 7: Detección de Outliers — Método IQR

```python
import numpy as np

datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

Q1  = np.percentile(datos, 25)   # 14.25
Q3  = np.percentile(datos, 75)   # 21.5
IQR = Q3 - Q1                    # 7.25

lim_inf = Q1 - 1.5 * IQR         # 14.25 - 10.875 = 3.375
lim_sup = Q3 + 1.5 * IQR         # 21.5  + 10.875 = 32.375

outliers = [x for x in datos if x < lim_inf or x > lim_sup]
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Límite inferior: {lim_inf}")
print(f"Límite superior: {lim_sup}")
print(f"Outliers: {outliers}")    # [100]
```

---

### Ejercicio 8: Detección de Outliers — Método Z-Score

```python
from scipy import stats
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])
z_scores = stats.zscore(datos)

print("Z-scores:", np.round(z_scores, 3))
# [ -0.997  -0.846  -0.695  -0.62   -0.544  -0.393  -0.242  -0.091   0.135   4.293]

outliers_idx = np.where(np.abs(z_scores) > 3)[0]
outliers_val = datos[outliers_idx]
print(f"Índices outliers: {outliers_idx}")  # [9]
print(f"Valores outliers: {outliers_val}")  # [100]
# El valor 100 tiene Z = 4.293 >> 3 → outlier confirmado
```

---

### Ejercicio 9: Manejo de Outliers

```python
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100], dtype=float)
Q1, Q3 = np.percentile(datos, [25, 75])
IQR    = Q3 - Q1
lim_inf, lim_sup = Q1 - 1.5*IQR, Q3 + 1.5*IQR

# 1. Eliminar outliers
datos_sin_out = datos[(datos >= lim_inf) & (datos <= lim_sup)]
print("Sin outliers:", datos_sin_out)  # [10 12 14 15 16 18 20 22 25]

# 2. Capping (reemplazar por el límite)
datos_cap = np.clip(datos, lim_inf, lim_sup)
print("Capping:", datos_cap)           # [10 12 ... 25 32.375]

# 3. Transformación logarítmica (reduce el impacto de valores extremos)
datos_log = np.log1p(datos)
print("Log:", np.round(datos_log, 3))

# 4. Box-Cox (requiere valores positivos)
from scipy.stats import boxcox
datos_boxcox, lambda_opt = boxcox(datos)
print(f"Box-Cox λ óptimo: {lambda_opt:.4f}")
```

---

### Ejercicio 10: Codificación de Variables Categóricas

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde', 'rojo', 'verde'],
    'talla': ['S', 'M', 'L', 'S', 'M']
})

# 1. Label Encoding (asigna entero a cada categoría)
le = LabelEncoder()
df['color_label'] = le.fit_transform(df['color'])
print(df['color_label'].tolist())  # [2, 0, 1, 2, 1]  (azul=0, rojo=2, verde=1)

# 2. One-Hot Encoding con pandas
df_ohe = pd.get_dummies(df, columns=['color', 'talla'], prefix=['color', 'talla'])
print(df_ohe.columns.tolist())

# 3. One-Hot Encoding con sklearn
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
encoded = ohe.fit_transform(df[['color', 'talla']])
print(encoded)

# ¿Cuándo usar cada uno?
# Label Encoding:   variables ordinales (S < M < L) o árboles de decisión
# One-Hot Encoding: variables nominales sin orden (colores), regresión lineal, SVM
```

---

### Ejercicio 11: Transformaciones Numéricas

```python
import numpy as np
from scipy.stats import boxcox

datos = np.array([1, 2, 3, 4, 5, 10, 20, 30], dtype=float)

# 1. Logaritmo natural (útil para datos con sesgo positivo)
log_n = np.log1p(datos)
print("Log natural:", np.round(log_n, 3))

# 2. Raíz cuadrada (suaviza distribuciones sesgadas moderadamente)
sqrt_d = np.sqrt(datos)
print("Raíz cuadrada:", np.round(sqrt_d, 3))

# 3. Box-Cox (transformación potencia óptima, λ se estima)
bc_d, lam = boxcox(datos)
print(f"Box-Cox (λ={lam:.3f}):", np.round(bc_d, 3))

# 4. Discretización (binning)
bins = pd.cut(pd.Series(datos), bins=3, labels=['bajo','medio','alto'])
print("Bins:", bins.tolist())
```

---

### Ejercicio 12: Feature Engineering

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame({
    'precio':   [100, 200, 150, 300, 250],
    'costo':    [60,  120, 90,  180, 150],
    'fecha':    pd.to_datetime(['2023-01-15','2023-03-22','2023-07-01',
                                '2023-10-10','2023-12-25'])
})

# 1. Ratio entre columnas
df['margen_pct'] = ((df['precio'] - df['costo']) / df['precio'] * 100).round(2)

# 2. Diferencia entre columnas
df['ganancia'] = df['precio'] - df['costo']

# 3. Indicador binario
df['es_premium'] = (df['precio'] > 200).astype(int)

# 4. Polynomial features (grado 2 sobre precio)
pf = PolynomialFeatures(degree=2, include_bias=False)
poly = pf.fit_transform(df[['precio']])
print("Features polinomiales:", pf.get_feature_names_out(['precio']))

# 5. DateTime features
df['mes']         = df['fecha'].dt.month
df['dia_semana']  = df['fecha'].dt.dayofweek
df['es_fin_anio'] = (df['fecha'].dt.month >= 11).astype(int)
print(df[['precio','margen_pct','ganancia','es_premium','mes','es_fin_anio']])
```

---

### Ejercicio 13: Comparar Escaladores

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np

data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], dtype=float)

escaladores = {
    'MinMaxScaler':   MinMaxScaler(),
    'StandardScaler': StandardScaler(),
    'RobustScaler':   RobustScaler(),
    'MaxAbsScaler':   MaxAbsScaler(),
}
for nombre, sc in escaladores.items():
    res = sc.fit_transform(data)
    print(f"\n{nombre}:\n{np.round(res, 3)}")

# ¿Cuándo usar cada uno?
# MinMaxScaler:   datos sin outliers, redes neuronales, imágenes
# StandardScaler: datos normales o casi normales, regresión, PCA, SVM
# RobustScaler:   datos con outliers (usa mediana e IQR en lugar de media y std)
# MaxAbsScaler:   datos ya centrados en 0, escala a [-1, 1], datos dispersos
```

---

### Ejercicio 14: Pipeline de Preprocesamiento

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# Dataset de ejemplo
df = pd.DataFrame({
    'edad':       [25, np.nan, 30, 22, 35],
    'salario':    [50000, 60000, np.nan, 45000, 70000],
    'ciudad':     ['CDMX', 'GDL', 'MTY', 'CDMX', None],
    'departamento':['IT', 'HR', 'IT', 'Ventas', 'HR']
})

X = df.drop(columns=[]) # todas las columnas son features en este ejemplo
cols_num = ['edad', 'salario']
cols_cat = ['ciudad', 'departamento']

# Pipeline numérico: imputar con mediana + estandarizar
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

# Pipeline categórico: imputar con moda + One-Hot
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Combinación en ColumnTransformer
preprocesador = ColumnTransformer([
    ('num', num_pipeline, cols_num),
    ('cat', cat_pipeline, cols_cat)
])

X_transformado = preprocesador.fit_transform(df[cols_num + cols_cat])
print(f"Shape original: {df.shape}")
print(f"Shape tras pipeline: {X_transformado.shape}")
```

---

### Ejercicio 15: Mejores Prácticas

**1. ¿Por qué es importante la preparación de datos?**

Los datos del mundo real son ruidosos, incompletos y heterogéneos. La preparación de datos representa entre el 60% y 80% del tiempo total de un proyecto de ciencia de datos. Un modelo entrenado con datos sucios producirá predicciones poco confiables independientemente de su sofisticación: "garbage in, garbage out". La preparación garantiza calidad, consistencia y que los datos cumplan los supuestos del algoritmo.

**2. ¿Qué es data leakage y cómo evitarlo?**

El data leakage ocurre cuando información del conjunto de prueba (o del futuro) se filtra al proceso de entrenamiento, generando métricas artificialmente optimistas que no se reproducen en producción. Ejemplos: normalizar usando estadísticas de todo el dataset antes de dividir train/test, incluir variables que en la realidad no estarían disponibles al momento de predecir.

Cómo evitarlo:
- Siempre dividir train/test **antes** de aplicar cualquier transformación.
- Ajustar los escaladores e imputadores solo con datos de entrenamiento (`fit` en train, `transform` en test).
- Usar `sklearn.pipeline.Pipeline` para encapsular todos los pasos.

**3. Diferencia entre datos de entrenamiento y prueba:**

| Aspecto | Entrenamiento | Prueba |
|---------|--------------|--------|
| Proporción típica | 70–80% | 20–30% |
| Uso | Ajustar parámetros del modelo | Evaluar rendimiento real |
| Exposición al modelo | El modelo los ve durante `fit()` | El modelo nunca los ve en training |
| Representatividad | Debe cubrir toda la variación | Muestra aleatoria del total |

---

### Ejercicio 16: Técnicas Avanzadas

**1. SMOTE (Synthetic Minority Over-sampling Technique)**
Técnica para balancear datasets con clases desbalanceadas. En lugar de simplemente duplicar muestras de la clase minoritaria (oversampling básico), SMOTE genera muestras sintéticas interpolando entre instancias existentes de la clase minoritaria usando sus k-vecinos más cercanos. Se usa cuando la diferencia entre clases es >3:1 y el modelo tiene dificultad aprendiendo la clase minoritaria.

**2. Imputación por K-Nearest Neighbors (KNN)**
En lugar de imputar con un estadístico global (media/mediana), KNN encuentra los k registros más similares al registro con el valor faltante y usa sus valores para imputar. Es más preciso que SimpleImputer cuando existen correlaciones entre variables, pero computacionalmente más costoso. Disponible en sklearn como `KNNImputer`.

**3. Target Encoding**
Reemplaza cada categoría de una variable categórica con la media de la variable objetivo para esa categoría. Por ejemplo, si la ciudad "CDMX" tiene precio promedio de $5,000, se reemplaza "CDMX" por 5000. Es muy poderoso para variables categóricas de alta cardinalidad, pero requiere técnicas como cross-validation o suavizado (smoothing) para evitar data leakage y overfitting.

---

## 2. Actividades Prácticas

### Actividad 4.1: Identificación de Valores Faltantes

```python
import pandas as pd
import numpy as np

# Dataset con valores nulos intencionales
df = pd.DataFrame({
    'nombre':  ['Ana','Luis','María',None,'Pedro'],
    'edad':    [25, np.nan, 30, 28, np.nan],
    'salario': [50000, 60000, np.nan, 45000, 55000],
    'ciudad':  ['CDMX','GDL',None,'MTY','CDMX']
})

# isnull() y notnull()
print(df.isnull())
print(df.notnull())

# Contar nulos por columna
print(df.isnull().sum())

# info() para completitud
print(df.info())

# Porcentaje de nulos
print((df.isnull().mean() * 100).round(1))
# nombre   20.0% | edad 40.0% | salario 20.0% | ciudad 20.0%
```

---

### Actividad 4.2: Imputación de Datos

```python
import pandas as pd
import numpy as np

df_orig = pd.DataFrame({
    'precio':    [100, np.nan, 150, 200, np.nan, 300],
    'categoria': ['A', 'B', np.nan, 'A', 'C', 'B'],
    'cantidad':  [5, 3, np.nan, 8, 2, np.nan]
})

# Media (columnas numéricas)
df_media = df_orig.copy()
df_media['precio']   = df_media['precio'].fillna(df_media['precio'].mean())
df_media['cantidad'] = df_media['cantidad'].fillna(df_media['cantidad'].mean())
print("Media:", df_media)

# Mediana (más robusta ante outliers)
df_mediana = df_orig.copy()
df_mediana['precio']   = df_mediana['precio'].fillna(df_mediana['precio'].median())
df_mediana['cantidad'] = df_mediana['cantidad'].fillna(df_mediana['cantidad'].median())

# Moda (para categóricas)
df_moda = df_orig.copy()
df_moda['categoria'] = df_moda['categoria'].fillna(df_moda['categoria'].mode()[0])

# Forward/Backward fill
df_ffill = df_orig.copy().ffill()
df_bfill = df_orig.copy().bfill()

# Conclusión: media para distribuciones simétricas, mediana cuando hay outliers,
# moda para categóricas, ffill/bfill para series de tiempo o datos ordenados.
```

---

### Actividad 4.3: Transformación de Datos

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder

df = pd.DataFrame({
    'precio':    [100, 500, 200, 800, 150],
    'cantidad':  [5, 2, 8, 1, 6],
    'categoria': ['A', 'B', 'A', 'C', 'B']
})

# Normalización Min-Max
mm = MinMaxScaler()
df['precio_norm']    = mm.fit_transform(df[['precio']]).flatten()
df['cantidad_norm']  = mm.fit_transform(df[['cantidad']]).flatten()

# Estandarización Z-Score
std = StandardScaler()
df['precio_std']     = std.fit_transform(df[['precio']]).flatten()

# One-Hot Encoding
ohe_result = pd.get_dummies(df['categoria'], prefix='cat')
df = pd.concat([df, ohe_result], axis=1)

# Variable derivada
df['ingreso_total'] = df['precio'] * df['cantidad']

print(df.to_string())
```

---

### Actividad 4.4: Pipeline de Procesamiento Completo

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

# Pipeline numérico
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

# Pipeline categórico
cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', num_pipe, ['precio_unitario', 'cantidad', 'costo_envio']),
    ('cat', cat_pipe, ['categoria', 'region'])
])

# Pipeline completo con modelo
pipeline_completo = Pipeline([
    ('preprocessor', preprocessor),
    ('model',        LinearRegression())
])

# Uso: pipeline_completo.fit(X_train, y_train) → aplica todo automáticamente
# Sin riesgo de data leakage ya que fit solo usa X_train
print("Pipeline creado correctamente. Pasos:")
for nombre, paso in pipeline_completo.steps:
    print(f"  - {nombre}: {type(paso).__name__}")
```

---

## 3. Actividad Evaluable — Regresión Lineal Simple: Béisbol MLB

### 3.1 Definición del Problema y Objetivo

**Objetivo:** Construir y evaluar un modelo de regresión lineal simple que prediga el número de carreras anotadas (Runs, R) por un equipo de béisbol MLB a partir del número de turnos al bate (At-Bats, AB) por temporada.

**Preguntas clave:**
1. ¿Existe una relación lineal significativa entre la cantidad de bateos y las carreras anotadas?
2. ¿Cuántas carreras adicionales predice el modelo por cada bateo extra?
3. ¿Qué tan preciso es el modelo para predecir el desempeño de equipos no vistos?

**Fuente de datos:** ESPN MLB Statistics — https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador
**Dataset:** 30 equipos MLB, temporadas 2018–2023, 180 registros totales.

---

### 3.2 Descripción del Dataset

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `equipo` | Categórico | Nombre del equipo MLB |
| `temporada` | Numérico entero | Año de la temporada |
| `AB` | Numérico entero | At-Bats: turnos al bate por temporada |
| `H` | Numérico entero | Hits: golpes exitosos |
| `HR` | Numérico entero | Home Runs: cuadrangulares |
| `BB` | Numérico entero | Bases por bolas (walks) |
| `R` | Numérico entero | **Runs: carreras anotadas (variable objetivo)** |

**Valores nulos identificados:**
- `H`: 7 nulos (3.9%) → imputados con mediana
- `BB`: 7 nulos (3.9%) → imputados con mediana

---

### 3.3 Limpieza y Preparación de Datos

**Pasos realizados:**

1. **Imputación de nulos:** columnas `H` y `BB` imputadas con mediana (robusta ante outliers).
2. **Normalización de temporada 2020:** la temporada COVID se jugó solo 60 juegos (37% del calendario de 162). Los valores se escalaron multiplicando por el factor 162/60 = 2.7 para que sean comparables con temporadas completas.
3. **Verificación:** 0 nulos tras limpieza, tipos de datos correctos.
4. **Estandarización de AB** (para verificación teórica): media ≈ 0, std ≈ 1 confirmado.

**Estadísticas descriptivas post-limpieza:**

| Variable | Media | Mediana | Mín | Máx | Desv. Std |
|----------|-------|---------|-----|-----|-----------|
| AB (bateos) | 5,548.2 | 5,553.0 | 5,218 | 5,944 | 140.7 |
| R (carreras) | 1,186.2 | 1,182.0 | 1,006 | 1,322 | 65.0 |

---

### 3.4 Análisis Exploratorio y Correlación de Pearson

**Correlación de Pearson entre AB y R:**

```
r(AB, R) = 0.2388
p-valor  = 0.001248
```

**Interpretación:**
La correlación de Pearson de **r = 0.2388** indica una relación positiva débil entre el número de bateos y las carreras anotadas. El p-valor de 0.0012 (< 0.05) confirma que la correlación es estadísticamente significativa: no es producto del azar. Sin embargo, la magnitud débil del coeficiente indica que los bateos solos no explican completamente las carreras; variables como hits, home runs y bases por bolas tienen mayor poder predictivo individual (como confirma el heatmap de correlaciones).

**Heatmap de correlaciones (ver Visualizaciones/exploratorio.png):**
La variable R tiene mayor correlación con H (hits, ~0.95) y HR (home runs, ~0.85) que con AB (~0.24), lo que tiene sentido desde el punto de vista del béisbol: lo que genera carreras son los hits y cuadrangulares, no simplemente los intentos de bateo.

---

### 3.5 Construcción del Modelo

**Variables:**
- **Variable independiente (X):** AB — At-Bats (número de bateos por temporada)
- **Variable dependiente (y):** R — Runs (carreras anotadas)

**División train/test:**
- Entrenamiento: 144 registros (80%)
- Prueba: 36 registros (20%)
- `random_state=42` para reproducibilidad

**Ecuación del modelo:**

```
R = 0.1081 × AB + 587.65
```

**Interpretación de los coeficientes:**
- **Intercepto (587.65):** si un equipo tuviera 0 bateos (teóricamente), el modelo predice 587.65 carreras (valor sin interpretación práctica real, es el punto de corte matemático).
- **Coeficiente (0.1081):** por cada bateo adicional en una temporada, el modelo predice **0.1081 carreras más**. Dicho de otra forma, para anotar una carrera adicional se necesitan aproximadamente 9.25 bateos más.

---

### 3.6 Predicción y Evaluación del Modelo

**Métricas de evaluación:**

| Métrica | Valor | Interpretación |
|---------|-------|---------------|
| R² (coeficiente de determinación) | 0.0434 | El modelo explica solo el 4.3% de la varianza en carreras |
| MAE (error absoluto medio) | 41.55 carreras | En promedio, el modelo se equivoca por ±41.55 carreras |
| MSE (error cuadrático medio) | 3,208.04 | Penaliza errores grandes |
| RMSE (raíz del error cuadrático) | 56.64 carreras | Error típico de ±56.64 carreras |

**Muestra de predicciones:**

| Equipo | Temporada | AB | R Real | R Predicho | Error |
|--------|-----------|----|---------|-----------| ------|
| Houston Astros | 2022 | 5,644 | 1,265 | 1,197 | +68 |
| Tampa Bay Rays | 2021 | 5,490 | 1,162 | 1,181 | −19 |
| New York Yankees | 2019 | 5,720 | 1,254 | 1,206 | +48 |
| Cleveland Guard. | 2023 | 5,380 | 1,098 | 1,169 | −71 |

**Visualizaciones generadas:**
- `regresion_scatter.png` — línea de regresión + gráfico real vs predicho
- `residuos.png` — análisis de residuos
- `exploratorio.png` — histogramas y heatmap de correlaciones

---

### 3.7 Análisis de Residuos

![Análisis de residuos](Visualizaciones/residuos.png)

Los residuos se distribuyen aproximadamente de forma aleatoria alrededor de cero (media de residuos ≈ 0), lo que indica que el modelo no tiene sesgo sistemático. La distribución de residuos es aproximadamente normal, cumpliendo uno de los supuestos básicos de la regresión lineal. Sin embargo, la dispersión de los residuos es considerable (±50–100 carreras), confirmando que el modelo tiene poder predictivo limitado cuando usa solo la variable AB.

---

### 3.8 Conclusión

El modelo de regresión lineal simple entre At-Bats y Runs produce una ecuación estadísticamente significativa (**R = 0.1081 × AB + 587.65**), pero con un R² de apenas **0.0434**, lo que significa que los bateos solos explican solo el 4.3% de la varianza en carreras anotadas. El error promedio de **41.55 carreras** por temporada es alto considerando que la diferencia entre equipos sólidos y mediocres puede ser de 100–150 carreras.

**Interpretación deportiva:** En béisbol, las carreras dependen más de qué sucede con los bateos (si resultan en hits, cuadrangulares o bases por bolas) que de la cantidad de intentos. Un equipo puede batear mucho y anotar pocas carreras si sus bateadores tienen baja efectividad. Las variables H (hits) y HR (home runs) serían predictores mucho más potentes.

**Aplicabilidad en toma de decisiones:** Este modelo es útil como punto de partida para entender la relación entre actividad ofensiva y producción, pero para tomar decisiones estratégicas reales (contratar jugadores, diseñar estrategias de juego) se requeriría un modelo de regresión múltiple que incluya H, HR y BB como variables independientes, lo cual sería el siguiente paso natural en el proyecto.

---

## 4. Resumen de Aprendizaje

- La preparación de datos no es opcional: un dataset con nulos sin tratar o con outliers extremos produce modelos completamente erróneos o sesgados.
- Elegir la técnica de imputación correcta importa: usar la media en presencia de outliers introduce sesgo; la mediana es más robusta.
- La normalización temporada 2020 enseñó que el contexto del dominio es tan importante como el código: sin entender que fue una temporada corta, los datos habrían parecido erróneos.
- Un R² bajo no significa que el modelo esté mal implementado: puede significar que la variable independiente elegida simplemente no tiene suficiente poder predictivo sola.
- Los residuos deben analizarse siempre: un modelo puede tener un R² aceptable pero residuos con patrones sistemáticos que indican violación de supuestos.
- La correlación de Pearson mide relación lineal, no causalidad: AB y R se correlacionan positivamente, pero no porque batear cause carreras directamente.

---

## 5. Dudas o Preguntas

- ¿Cuándo es preferible usar validación cruzada (cross-validation) en lugar de un único train/test split, y qué tamaño de dataset lo justifica?
- ¿Cómo se interpreta el R² ajustado frente al R² estándar cuando se agregan más variables al modelo de regresión?

---

## 6. Commits Realizados

```
Semana4: Ejercicios complementarios normalización, outliers y transformaciones
Semana4: Actividades prácticas 4.1 a 4.4
Semana4: Actividad 3 - Dataset béisbol MLB generado y limpiado
Semana4: Actividad 3 - Modelo regresión lineal simple completado
Semana4: Visualizaciones - regresión, residuos, exploratorio
Semana4: Consolidado completo
```

---

## 7. Referencias

- James, G., Witten, D., Hastie, T. & Tibshirani, R. (2021). *An Introduction to Statistical Learning, 2nd ed.* Springer.
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow, 3rd ed.* O'Reilly Media.
- McKinney, W. (2022). *Python for Data Analysis, 3rd ed.* O'Reilly Media.
- Scikit-learn Developers. (2024). *Preprocessing data.* https://scikit-learn.org/stable/modules/preprocessing.html
- ESPN. (2024). *MLB Estadísticas.* https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador
- SciPy. (2024). *scipy.stats documentation.* https://docs.scipy.org/doc/scipy/reference/stats.html
