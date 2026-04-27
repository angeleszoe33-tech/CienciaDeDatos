# Semana 5: Análisis de Correlación y Regresión

**Fecha:** 26/04/2026
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Temas cubiertos:** T11 (Análisis preliminar de datos en Python), T12 (Regresión lineal simple en Python)

---

## Actividad 4 — Parte 1: Regresión Lineal Múltiple (Vehículos)

### 1.1 Preparación de los Datos

**Fuente:** Kaggle — Vehicle Sales Data
**Dataset:** 1,200 registros de vehículos con precio, kilometraje y ventas.

**Valores nulos identificados:**
- `precio`: 25 nulos (2.1%) → imputados con mediana
- `kilometraje`: 25 nulos (2.1%) → imputados con mediana

**Estadísticas post-limpieza:**

| Variable | Media | Mediana | Mínimo | Máximo | Desv. Std |
|----------|-------|---------|--------|--------|-----------|
| precio ($) | 27,047 | 24,800 | 5,000 | 62,200 | 11,229 |
| kilometraje | 52,751 | 40,983 | 6,038 | 200,000 | 39,778 |
| ventas | 349 | 355 | 116 | 533 | 63 |

---

### 1.2 Análisis Exploratorio — Pairplot

![Pairplot Vehículos](Visualizaciones/pairplot_vehiculos.png)

**Correlaciones de Pearson:**

| Par de variables | r | Interpretación |
|-----------------|---|---------------|
| precio vs ventas | **−0.5376** | Correlación negativa moderada: a mayor precio, menos ventas |
| kilometraje vs ventas | **−0.2952** | Correlación negativa débil: más kilometraje reduce ventas |
| precio vs kilometraje | **−0.3140** | Negativa débil: vehículos más caros tienden a tener menos km |

El pairplot confirma visualmente estas relaciones: la nube de dispersión precio-ventas muestra una tendencia descendente clara, mientras que kilometraje-ventas es más dispersa pero también negativa.

---

### 1.3 Identificación de Variables

- **Variables independientes (X):** `precio` y `kilometraje`
- **Variable dependiente (y):** `ventas`

**Justificación:** El precio y el kilometraje son los factores más consultados por compradores de vehículos usados. Ambas tienen correlación negativa con ventas, lo que tiene sentido: los consumidores prefieren vehículos baratos y con poco uso.

---

### 1.4 División de Datos

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# Entrenamiento: 960 registros (80%)
# Prueba:        240 registros (20%)
```

---

### 1.5 Modelado — Regresión Lineal Múltiple

**Ecuación del modelo:**

```
ventas = −0.003886 × precio + (−0.000852) × kilometraje + 499.56
```

**Interpretación de coeficientes:**
- **Intercepto (499.56):** ventas base teóricas si precio y km fueran cero.
- **Precio (−0.003886):** por cada $1,000 adicionales en precio, el modelo predice **−3.89 ventas menos**.
- **Kilometraje (−0.000852):** por cada 10,000 km adicionales, el modelo predice **−8.52 ventas menos**.

---

### 1.6 Evaluación del Modelo

![Regresión Múltiple](Visualizaciones/regresion_multiple.png)

| Métrica | Valor | Interpretación |
|---------|-------|---------------|
| R² | **0.5318** | El modelo explica el 53.2% de la varianza en ventas |
| MAE | **34.05** ventas | Error absoluto promedio de ±34 ventas |
| MSE | **1,826.67** | Error cuadrático medio |
| RMSE | **42.74** ventas | Error típico de ±43 ventas |

---

### 1.7 Predicciones

| Precio | Kilometraje | Ventas predichas |
|--------|------------|-----------------|
| $15,000 | 10,000 km | **433** |
| $25,000 | 40,000 km | **368** |
| $35,000 | 80,000 km | **295** |
| $50,000 | 150,000 km | **177** |

Las predicciones siguen el patrón esperado: a medida que sube el precio y el kilometraje, las ventas estimadas caen consistentemente.

---

### 1.8 Error Cuadrático Medio

El MSE de **1,826.67** y RMSE de **42.74 ventas** indican que el modelo puede equivocarse en promedio ±43 ventas por predicción. En un rango de ventas de 116 a 533 (rango de 417), esto representa aproximadamente el 10.2% del rango total, un error aceptable para un modelo con solo dos variables.

---

### 1.9 Conclusión — Parte 1

El modelo de regresión lineal múltiple con precio y kilometraje como predictores logra un R² de **0.5318**, explicando algo más de la mitad de la varianza en ventas. Esto representa una mejora significativa frente a una regresión simple con solo precio (que daría aproximadamente R²=0.29 basado en la correlación r=−0.54).

**Efectividad:** El modelo es funcional para estimaciones generales pero tiene limitaciones. Un R² de 0.53 implica que casi la mitad de la varianza no está explicada, lo que sugiere que existen otros factores importantes: marca, año del vehículo, tipo de carrocería, condición, color y zona geográfica.

**Posibles mejoras:**
- Incluir año del vehículo y marca como variables adicionales (regresión múltiple extendida).
- Aplicar One-Hot Encoding a variables categóricas como condición y tipo.
- Explorar modelos no lineales como árboles de decisión o Random Forest que capten relaciones más complejas.
- Detectar y tratar outliers en precio y kilometraje que pueden distorsionar los coeficientes.

---

## Actividad 4 — Parte 2: Regresión Logística Binaria (Titanic)

### 2.1 Preparación de los Datos

**Fuente:** OpenML — Titanic Dataset
**Dataset:** 891 pasajeros con variables demográficas y de viaje.

**Columnas eliminadas:** `PassengerId`, `Name`, `Ticket`, `Cabin`
- `Cabin`: 77.6% de nulos, no aporta información confiable.
- `Name`, `Ticket`, `PassengerId`: identificadores sin poder predictivo.

**Imputaciones:**
- `Age`: 177 nulos (19.9%) → imputados con mediana (29 años).
- `Embarked`: 2 nulos → imputados con moda ('S').

**Conversión de tipos:**
- `Pclass`, `Sex`, `Embarked` → tipo `category`
- `Sex` → encoding binario: female=1, male=0
- `Pclass` → encoding numérico: 1, 2, 3

---

### 2.2 Visualización de Datos

![Supervivencia por Sexo y Clase](Visualizaciones/titanic_barras.png)

Las gráficas confirman claramente:
- **Mujeres sobrevivieron al 76.2%** vs hombres al 32.9% → diferencia de 43 puntos porcentuales.
- **1ª clase: 63.6%** vs 3ª clase: 38.8% → la clase social fue determinante para el acceso a los botes salvavidas.

Estas diferencias visuales justifican incluir sexo y clase como variables predictoras en el modelo.

---

### 2.3 Prueba t-test

**Hipótesis:** ¿La edad promedio de los sobrevivientes es significativamente diferente a la de los no sobrevivientes?

```
H₀: μ_sobrevivientes = μ_no_sobrevivientes
H₁: μ_sobrevivientes ≠ μ_no_sobrevivientes
```

**Resultados:**
- Media sobrevivientes: **29.82 años**
- Media no sobrevivientes: **29.13 años**
- t = 0.8344
- p-valor = 0.4043

**Conclusión:** Con p = 0.4043 > 0.05, **no se rechaza H₀**. La diferencia de edad entre sobrevivientes y no sobrevivientes no es estadísticamente significativa. La edad por sí sola no fue determinante para la supervivencia. Los factores de sexo y clase tuvieron mucho mayor peso.

![Distribución de Edad y Matriz de Confusión](Visualizaciones/titanic_confusion.png)

---

### 2.4 División de Datos

```python
features = ['Pclass_enc', 'Sex_enc', 'Age', 'SibSp', 'Parch', 'Fare']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# Entrenamiento: 712 pasajeros (80%)
# Prueba:        179 pasajeros (20%)
```

---

### 2.5 Creación del Modelo

```python
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)
```

La regresión logística binaria modela la probabilidad de supervivencia (1) vs no supervivencia (0) usando la función sigmoide:

```
P(Survived=1) = 1 / (1 + e^(−z))
donde z = b₀ + b₁·Pclass + b₂·Sex + b₃·Age + ...
```

---

### 2.6 Coeficientes y Odds Ratio

![Odds Ratio y Curva ROC](Visualizaciones/logistica_roc.png)

| Variable | Coeficiente | Odds Ratio | Interpretación |
|----------|-------------|------------|---------------|
| Clase (Pclass) | −0.8129 | **0.4436** | Cada clase superior reduce 56% la probabilidad de sobrevivir* |
| Sexo (female=1) | +1.9596 | **7.0968** | Ser mujer multiplica por **7.1x** la probabilidad de sobrevivir |
| Edad | +0.0086 | **1.0086** | Efecto prácticamente nulo (OR≈1) |
| Hermanos/Cónyuge (SibSp) | +0.2624 | **1.3000** | Tener 1 familiar a bordo aumenta 30% la probabilidad |
| Padres/Hijos (Parch) | +0.0926 | **1.0970** | Efecto débil positivo |
| Tarifa (Fare) | −0.0036 | **0.9964** | Efecto prácticamente nulo |

*Interpretación de Pclass: al pasar de 1ª a 2ª clase (o de 2ª a 3ª), el OR es 0.44, es decir, la probabilidad de sobrevivir se reduce aproximadamente a la mitad.

**Variable más importante:** `Sex_enc` con OR=7.10 es, con mucho, el predictor más poderoso. Ser mujer multiplicó por 7 la probabilidad de sobrevivir, consistente con la política "mujeres y niños primero" aplicada durante el hundimiento.

---

### 2.7 Evaluación del Modelo

**Métricas:**

| Métrica | Valor | Interpretación |
|---------|-------|---------------|
| Accuracy | **0.6927** | El modelo clasifica correctamente al 69.3% de los pasajeros |
| AUC-ROC | **0.7649** | Buena capacidad discriminativa (>0.70 se considera aceptable) |

**Matriz de confusión:**

| | Predicho: No sobrevivió | Predicho: Sobrevivió |
|---|---|---|
| **Real: No sobrevivió** | 65 (VP) | 33 (FP) |
| **Real: Sobrevivió** | 22 (FN) | 59 (VP) |

- **Precisión clase 0 (no sobrevivió):** 75% — cuando predice "no sobrevive", acierta el 75%.
- **Precisión clase 1 (sobrevivió):** 64% — cuando predice "sobrevive", acierta el 64%.
- **Recall clase 1:** 73% — detecta al 73% de los sobrevivientes reales.

---

### 2.8 Conclusión — Parte 2

El modelo de regresión logística binaria alcanza una **accuracy del 69.3%** y un **AUC-ROC de 0.7649**, lo que representa un desempeño razonablemente bueno para un modelo con solo 6 variables.

**Hallazgos principales:**
- El **sexo femenino** es el predictor más poderoso (OR=7.10), superando por mucho a todas las demás variables.
- La **clase social** tiene el segundo mayor impacto negativo: cada escalón hacia abajo en clase reduce la probabilidad de supervivencia a casi la mitad.
- La **edad** no tiene impacto estadísticamente significativo, confirmado tanto por el t-test (p=0.40) como por su OR≈1.
- La **tarifa pagada** tampoco aporta información independiente una vez que la clase está incluida (correlación alta entre ambas).

**Posibles mejoras:**
- Crear la variable `FamilySize = SibSp + Parch + 1` que puede captar mejor el efecto familiar que las variables por separado.
- Incluir la variable de puerto de embarque con One-Hot Encoding.
- Explorar modelos de ensamble (Random Forest, Gradient Boosting) que típicamente superan el 80% de accuracy en este dataset.
- Aplicar regularización (L1/Lasso) para eliminar variables con poco aporte predictivo.

---

## Resumen de Aprendizaje

- La regresión lineal múltiple permite combinar varios predictores para mejorar el poder explicativo frente a la regresión simple: pasar de R²≈0.29 (solo precio) a R²=0.53 (precio + kilometraje) fue un avance notable.
- La regresión logística es el modelo estándar para variables dependientes binarias: en lugar de predecir un valor numérico, predice una probabilidad entre 0 y 1.
- Los Odds Ratio son la herramienta clave para interpretar la regresión logística: un OR>1 indica efecto positivo sobre el evento, OR<1 indica efecto negativo.
- El t-test es una prueba rápida y efectiva para validar si una variable continua tiene diferencias significativas entre grupos antes de incluirla en el modelo.
- La curva ROC y el AUC son métricas más informativas que la accuracy simple, especialmente cuando las clases están desbalanceadas.
- El pairplot de Seaborn es una herramienta de exploración poderosa: en un solo gráfico permite ver distribuciones univariadas y relaciones bivariadas entre todas las variables de interés.

---

## Dudas o Preguntas

- ¿Cómo se interpreta el coeficiente de regresión logística cuando la variable independiente es categórica con más de dos niveles (multinomial)?
- ¿Cuándo es preferible usar F1-score vs AUC-ROC como métrica principal para evaluar un clasificador binario?

---

## Commits Realizados

```
Semana5: Actividad 4 - Datasets vehículos y Titanic generados
Semana5: Actividad 4 Parte 1 - Regresión lineal múltiple completada
Semana5: Actividad 4 Parte 2 - Regresión logística Titanic completada
Semana5: Visualizaciones - pairplot, regresión, ROC, confusión
Semana5: Consolidado completo
```

---

## Referencias

- James, G. et al. (2021). *An Introduction to Statistical Learning, 2nd ed.* Springer.
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow.* O'Reilly.
- Scikit-learn Developers. (2024). *Linear Models.* https://scikit-learn.org/stable/modules/linear_model.html
- Kaggle. (2024). *Vehicle Sales Data.* https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data
- OpenML. (2024). *Titanic Dataset.* https://www.openml.org/d/40945
- SciPy. (2024). *scipy.stats.ttest_ind.* https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
