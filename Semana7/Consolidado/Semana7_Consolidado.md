# Semana 7: Proyecto Final — Análisis Predictivo del Mercado Inmobiliario Airbnb NYC

**Fecha:** 08/05/2026
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Ponderación:** 35%
**Temas:** T16 (Regresión logística binaria Pt. 1), T17 (Regresión logística binaria Pt. 2), T18 (Estrategias de comunicación de datos)

---

## Ejercicios Complementarios

### Regresión Logística — Teoría

**1. ¿Qué es la regresión logística y en qué se diferencia de la lineal?**

La regresión logística es un modelo de clasificación que predice la probabilidad de que una observación pertenezca a una clase (0 o 1). A diferencia de la regresión lineal que predice valores continuos, la logística aplica la función sigmoide para acotar la salida entre 0 y 1:

```
P(y=1) = 1 / (1 + e^(−z))    donde z = b₀ + b₁x₁ + b₂x₂ + ...
```

Se usa cuando la variable dependiente es binaria (sobrevivió/no sobrevivió, compró/no compró, fraude/no fraude).

**2. ¿Qué son los Odds y el Odds Ratio?**

- **Odds:** razón entre la probabilidad de que ocurra un evento y la probabilidad de que no ocurra. `Odds = P / (1−P)`. Si P=0.75, Odds = 0.75/0.25 = 3 (es 3 veces más probable que ocurra).
- **Odds Ratio (OR):** razón entre los odds de dos grupos. OR=2 significa que un grupo tiene el doble de odds que el otro. OR>1: efecto positivo; OR<1: efecto negativo; OR=1: sin efecto.

**3. Interpretación práctica de OR:**
Si en el Titanic el OR del sexo femenino es 7.10, significa que las mujeres tenían 7.1 veces más odds de sobrevivir que los hombres, manteniendo constantes las demás variables.

---

### Matriz de Confusión

Dada la siguiente matriz de confusión de un modelo de clasificación:

```
               Predicho: No    Predicho: Sí
Real: No            85              15
Real: Sí            20              80
```

**Cálculos:**
- **Total:** 200
- **VP (Verdaderos Positivos):** 80
- **VN (Verdaderos Negativos):** 85
- **FP (Falsos Positivos):** 15
- **FN (Falsos Negativos):** 20

**Métricas:**
- **Accuracy:** (80+85)/200 = **82.5%**
- **Precisión:** 80/(80+15) = **84.2%** — de los que predijo positivo, acertó el 84.2%
- **Recall (Sensibilidad):** 80/(80+20) = **80.0%** — detectó el 80% de los positivos reales
- **F1-Score:** 2×(0.842×0.800)/(0.842+0.800) = **0.820**

**Interpretación:** El modelo es balanceado: no sacrifica recall por precisión ni viceversa. Un F1=0.82 es muy aceptable para clasificación binaria.

---

### Curva ROC y AUC

**¿Qué es la curva ROC?**
La curva ROC (Receiver Operating Characteristic) grafica la Tasa de Verdaderos Positivos (sensibilidad) contra la Tasa de Falsos Positivos (1-especificidad) para todos los umbrales de clasificación posibles.

**¿Qué es el AUC?**
El AUC (Area Under the Curve) mide el área bajo la curva ROC. Va de 0 a 1:
- AUC = 1.0: clasificador perfecto
- AUC = 0.5: equivale a clasificar al azar (línea diagonal)
- AUC > 0.7: modelo aceptable
- AUC > 0.8: modelo bueno
- AUC > 0.9: modelo excelente

**Ventaja sobre accuracy:** el AUC no se ve afectado por clases desbalanceadas, a diferencia de la accuracy que puede ser engañosa cuando hay muchos más casos de una clase que de otra.

---

## Actividades Prácticas

### Actividad 7.1: Regresión Logística — Introducción

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Dataset sintético binario
X, y = make_classification(n_samples=500, n_features=4, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Coeficientes: {modelo.coef_[0].round(3)}")
print(f"Intercepto: {modelo.intercept_[0]:.3f}")
```

---

### Actividad 7.2: Implementación con Dataset Real

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import numpy as np

# Usando el dataset Titanic de la Semana 5
df = pd.read_csv('../Semana5/Actividad4/Datos/titanic.csv')
df = df.drop(columns=['PassengerId','Name','Ticket','Cabin'])
df['Age']      = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna('S')
df['Sex_enc']  = (df['Sex']=='female').astype(int)

features = ['Pclass','Sex_enc','Age','SibSp','Parch','Fare']
X = df[features]; y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)
y_pred      = modelo.predict(X_test)
y_pred_prob = modelo.predict_proba(X_test)[:,1]

print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_pred_prob):.4f}")
```

---

### Actividad 7.3: Métricas de Evaluación Completas

```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                              f1_score, roc_auc_score, confusion_matrix)
import numpy as np

def evaluar_clasificador(y_real, y_pred, y_prob=None):
    print(f"Accuracy:  {accuracy_score(y_real,y_pred):.4f}")
    print(f"Precision: {precision_score(y_real,y_pred):.4f}")
    print(f"Recall:    {recall_score(y_real,y_pred):.4f}")
    print(f"F1-Score:  {f1_score(y_real,y_pred):.4f}")
    if y_prob is not None:
        print(f"AUC-ROC:   {roc_auc_score(y_real,y_prob):.4f}")
    cm = confusion_matrix(y_real, y_pred)
    print(f"Matriz de confusión:\n{cm}")
    VP,FN,FP,VN = cm[1,1],cm[1,0],cm[0,1],cm[0,0]
    print(f"  VP={VP} VN={VN} FP={FP} FN={FN}")

# Cuándo usar cada métrica:
# Accuracy:  datasets balanceados, visión general
# Precision: cuando el costo de FP es alto (spam, fraude)
# Recall:    cuando el costo de FN es alto (cáncer, fraude financiero)
# F1-Score:  balance entre precision y recall, datasets desbalanceados
# AUC-ROC:   comparar modelos sin importar el umbral de clasificación
```

---

### Actividad 7.4: Comunicación de Resultados

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, confusion_matrix
import numpy as np

def graficar_resultados(y_real, y_pred, y_prob, titulo='Modelo'):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle(f'Resultados — {titulo}', fontsize=13, fontweight='bold')

    # 1. Matriz de confusión
    cm = confusion_matrix(y_real, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['No','Sí'], yticklabels=['No','Sí'])
    axes[0].set_title('Matriz de Confusión')
    axes[0].set_xlabel('Predicho'); axes[0].set_ylabel('Real')

    # 2. Curva ROC
    fpr, tpr, _ = roc_curve(y_real, y_prob)
    from sklearn.metrics import roc_auc_score
    auc = roc_auc_score(y_real, y_prob)
    axes[1].plot(fpr, tpr, color='#185FA5', lw=2, label=f'AUC={auc:.3f}')
    axes[1].plot([0,1],[0,1], color='gray', lw=1, ls='--')
    axes[1].set_title('Curva ROC'); axes[1].legend()
    axes[1].set_xlabel('Tasa FP'); axes[1].set_ylabel('Tasa VP')

    # 3. Distribución de probabilidades
    axes[2].hist([y_prob[y_real==0], y_prob[y_real==1]],
                 bins=20, label=['No (0)','Sí (1)'],
                 color=['#D85A30','#185FA5'], alpha=0.7)
    axes[2].set_title('Distribución de Probabilidades Predichas')
    axes[2].set_xlabel('P(y=1)'); axes[2].legend()

    plt.tight_layout()
    plt.savefig(f'resultados_{titulo.lower().replace(" ","_")}.png', dpi=150)
    plt.show()
```

---

## Proyecto Final — Parte 1: Modelo de Regresión Lineal Múltiple

### 1.1 Descripción del Proyecto

Este proyecto continúa el análisis exploratorio iniciado en la Semana 3 con el dataset de Airbnb NYC. En esa fase se identificaron patrones clave en la distribución de precios y se detectó que las variables categóricas (borough y tipo de habitación) son las más relevantes para el precio. En esta fase final se construye y evalúa un modelo predictivo de regresión lineal múltiple para predecir el precio por noche de un alojamiento Airbnb en Nueva York.

**Dataset:** Airbnb NYC — 8,000 listings, temporada 2019
**Fuente:** https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction

---

### 1.2 Limpieza de Datos

**Valores nulos identificados y tratamiento:**

| Variable | Nulos | Estrategia | Justificación |
|----------|-------|-----------|---------------|
| `reviews_per_month` | 505 (6.3%) | Imputar con 0 | Sin reseñas = sin actividad mensual |
| `number_of_reviews` | 200 (2.5%) | Imputar con 0 | Listings nuevos sin reseñas |

**Detección de outliers — Método IQR:**
- Q1 precio = $60, Q3 = $176, IQR = $116
- Límite inferior: $60 − 1.5×$116 = −$114 (no aplica, precio mínimo $10)
- Límite superior: $176 + 1.5×$116 = **$350**
- Outliers de precio eliminados: 663 registros (precio > $350)
- Outliers de minimum_nights eliminados: listings con > 30 noches mínimas

**Registros finales para análisis:** 7,337 (91.7% del dataset original)

**Estadísticas post-limpieza:**

| Variable | Media | Mediana | Mín | Máx | Desv. Std |
|----------|-------|---------|-----|-----|-----------|
| Precio (USD) | $120.50 | $108.00 | $10 | $349 | $79.40 |
| Noches mínimas | 4.6 | 3.0 | 1 | 30 | 5.5 |
| Núm. reseñas | 24.8 | 8.0 | 0 | 398 | 41.5 |
| Disponibilidad | 178.0 | 175.0 | 0 | 365 | 132.4 |

![Distribución de Precios](Visualizaciones/distribucion_precio.png)

La distribución del precio muestra sesgo positivo moderado. La mediana ($108) es menor que la media ($120), indicando una cola derecha de alojamientos de precio medio-alto. Post-limpieza el rango es más manejable para el modelo.

---

### 1.3 Identificación de Variables

**Variable dependiente (y):** `price` — precio por noche en USD

**Variables independientes (X):**

| Variable | Tipo | Justificación |
|----------|------|--------------|
| `neighbourhood_group` (encoded) | Categórica → numérica | El borough es el factor geográfico más importante |
| `room_type` (encoded) | Categórica → numérica | Tipo de alojamiento determina directamente el precio |
| `minimum_nights` | Numérica | Afecta el perfil del alojamiento (turístico vs largo plazo) |
| `number_of_reviews` | Numérica | Proxy de popularidad y actividad del listing |
| `reviews_per_month` | Numérica | Indicador de demanda reciente |
| `calculated_host_listings_count` | Numérica | Distingue anfitriones profesionales de particulares |
| `availability_365` | Numérica | Refleja estrategia de precios del anfitrión |

---

### 1.4 Análisis de Multicolinealidad — VIF

Para garantizar que las variables independientes no están altamente correlacionadas entre sí (lo que inflaría los coeficientes), se calculó el Factor de Inflación de Varianza (VIF):

| Variable | VIF | Evaluación |
|----------|-----|-----------|
| Borough (ng_enc) | 2.95 | ✅ Sin problema |
| Tipo habitación (rt_enc) | 1.66 | ✅ Sin problema |
| Noches mínimas | 1.49 | ✅ Sin problema |
| Núm. reseñas | 2.13 | ✅ Sin problema |
| Reseñas/mes | 1.39 | ✅ Sin problema |
| Listings host | 1.43 | ✅ Sin problema |
| Disponibilidad | 2.80 | ✅ Sin problema |

**Conclusión:** Todos los VIF < 5, muy por debajo del umbral crítico de 10. No existe multicolinealidad problemática en el modelo.

---

### 1.5 Análisis de Correlación — Pairplot

![Pairplot Variables](Visualizaciones/pairplot_final.png)

**Correlaciones con el precio:**

| Variable | r con precio | Interpretación |
|----------|-------------|---------------|
| Tipo habitación (rt_enc) | **−0.386** | Correlación negativa moderada (habitaciones completas tienen rt menor pero precio mayor) |
| Núm. reseñas | −0.012 | Prácticamente nula |
| Disponibilidad | −0.009 | Prácticamente nula |
| Noches mínimas | −0.006 | Prácticamente nula |
| Reseñas/mes | −0.005 | Prácticamente nula |
| Listings host | −0.000 | Prácticamente nula |
| Borough (ng_enc) | +0.004 | Prácticamente nula |

Las variables numéricas tienen correlación muy baja con el precio, lo que ya se identificó en el EDA de la Semana 3. El mayor poder predictivo proviene de las variables categóricas codificadas (tipo de habitación y borough).

![Heatmap de Correlaciones](Visualizaciones/heatmap_final.png)

---

### 1.6 División de Datos

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
# Entrenamiento: 5,869 registros (80%)
# Prueba:        1,468 registros (20%)
```

La división 80/20 garantiza suficientes datos de entrenamiento para que el modelo aprenda patrones, mientras se reserva un conjunto de prueba representativo para evaluación imparcial.

---

### 1.7 Construcción y Entrenamiento del Modelo

**Ecuación del modelo:**

```
precio = 0.3073 × borough + (−52.8024) × tipo_habitación
       + 0.0760 × noches_min + (−0.0407) × num_reseñas
       + (−0.1816) × reseñas_mes + 0.2306 × listings_host
       + (−0.0113) × disponibilidad + 151.18
```

**Interpretación de coeficientes clave:**

- **Tipo de habitación (−52.80):** es el predictor más fuerte. Cada incremento en el encoding (de habitación completa a privada a compartida) reduce el precio en ~$52.80. Refleja directamente la jerarquía de valor: alojamiento completo > habitación privada > compartida.
- **Borough (+0.31):** efecto pequeño en la codificación numérica lineal, pero presente.
- **Noches mínimas (+0.08):** listings que exigen más noches tienden a tener precios ligeramente mayores.
- **Reseñas (−0.04) y Reseñas/mes (−0.18):** listings muy populares con muchas reseñas tienden a ser más asequibles (confirmando que popularidad y precio son independientes).

![Importancia de Características](Visualizaciones/importancia_features.png)

---

### 1.8 Evaluación del Modelo

![Predicciones vs Reales](Visualizaciones/predicciones_residuos.png)

| Métrica | Valor | Interpretación |
|---------|-------|---------------|
| **R²** | **0.1214** | El modelo explica el 12.1% de la varianza en precios |
| **R² ajustado** | **0.1172** | Penaliza variables adicionales; muy cercano al R², confirma que todas las variables aportan |
| **MAE** | **$60.60** | El modelo se equivoca en promedio ±$60.60 por noche |
| **MSE** | **5,436.49** | Error cuadrático medio |
| **RMSE** | **$73.73** | Error típico de ±$73.73 por noche |

**Análisis de residuos:** Los residuos se distribuyen aproximadamente de forma normal y centrada en 0, lo que confirma que el modelo no tiene sesgo sistemático. Sin embargo, la dispersión de ±$70–80 es considerable, reflejando el bajo R².

---

### 1.9 Predicciones

| Tipo de alojamiento | Precio predicho |
|--------------------|----------------|
| Manhattan / Alojamiento completo | **$151/noche** |
| Brooklyn / Habitación privada | **$94/noche** |
| Queens / Alojamiento completo | **$151/noche** |
| Bronx / Habitación compartida | **$40/noche** |

Los valores predichos siguen el patrón esperado del mercado: Manhattan y alojamientos completos tienen precios más altos, mientras que habitaciones compartidas en boroughs más alejados son las más económicas.

---

### 1.10 Error Cuadrático Medio (MSE)

**MSE = 5,436.49 | RMSE = $73.73**

En términos prácticos, el modelo puede predecir el precio de un Airbnb con un error promedio de ±$73.73 por noche. Dado que los precios del dataset van de $10 a $349, este error representa aproximadamente el 21.6% del rango total. Para un modelo de regresión lineal con solo 7 variables en un mercado altamente heterogéneo como el inmobiliario temporal, este nivel de error es esperable.

---

## Proyecto Final — Parte 2: Comunicación de Resultados

### Narrativa: Insights del Mercado Airbnb NYC

**¿Qué dicen los datos sobre el mercado de Airbnb en Nueva York?**

El análisis de 7,337 listings activos en Nueva York revela un mercado profundamente segmentado por dos factores: la ubicación geográfica (borough) y el tipo de alojamiento. Estas dos variables son responsables de la mayor parte de la variación en precios, mientras que factores operativos como el número de reseñas o la disponibilidad tienen un impacto marginal.

**La geografía manda:** Manhattan lidera con una mediana de $162/noche, casi el triple que el Bronx ($56). Brooklyn, con una mediana de $104, se consolida como la alternativa popular de precio moderado para visitantes que buscan un equilibrio entre costo y experiencia auténtica.

![Boxplot por Tipo y Borough](Visualizaciones/boxplot_final.png)

**El tipo de alojamiento es el predictor más poderoso:** con un coeficiente de −52.80, cada escalón de alojamiento completo → habitación privada → compartida reduce el precio en aproximadamente $53. Esto refleja la preferencia del mercado por la privacidad y el espacio completo, que se traduce directamente en disposición a pagar.

**¿Por qué el R² es bajo?** Un R² de 0.12 no significa que el modelo esté mal construido. Significa que el precio de un Airbnb depende de factores que van más allá de las variables disponibles en este dataset: fotografías del listing, calidad del anfitrión, amenidades específicas (vista al parque, aire acondicionado, cocina equipada), y las dinámicas de oferta y demanda en tiempo real. Para capturar estos factores se requeriría información adicional o técnicas de modelado más sofisticadas.

**Recomendaciones para anfitriones basadas en el modelo:**
1. **Ubicación primero:** un listing en Manhattan generará sistemáticamente más ingresos que uno en Staten Island con características idénticas.
2. **Tipo de propiedad importa más que el precio de lista:** ofrecer el alojamiento completo, aunque sea más pequeño, tiene mayor impacto en el precio que ajustar las reseñas o la disponibilidad.
3. **Las reseñas no elevan el precio:** la popularidad no justifica cobrar más. Los listings con más reseñas tienden a ser más asequibles, probablemente porque la competencia en volumen requiere precios competitivos.

**Próximos pasos para mejorar el modelo:**
- Incluir variables de texto (análisis de sentimiento de las descripciones) mediante NLP.
- Aplicar modelos de ensamble (Random Forest, Gradient Boosting) que capten relaciones no lineales y pueden lograr R² > 0.50 en este tipo de datos.
- Incorporar datos de estacionalidad: los precios de Airbnb varían significativamente entre temporada alta (verano, Navidad) y baja.
- Añadir variables de proximidad a puntos de interés turístico mediante datos geoespaciales.

---

## Resumen de Aprendizaje del Curso

A lo largo de las 7 semanas del curso se construyó un pipeline completo de ciencia de datos:

**Semana 1-2:** Fundamentos conceptuales de ciencia de datos, Big Data (5 V) y arquitecturas NoSQL con MongoDB. Se diseñó una solución completa para DeportivaMX.

**Semana 3:** EDA profundo del dataset Airbnb NYC — identificación de patrones, distribuciones y correlaciones que orientaron todo el trabajo posterior.

**Semana 4:** Regresión lineal simple con datos de béisbol MLB — primer modelo predictivo, comprensión de R², residuos y métricas de evaluación.

**Semana 5:** Regresión lineal múltiple (vehículos) y regresión logística (Titanic) — modelos más complejos, odds ratios, curva ROC y AUC.

**Semana 7 (Proyecto Final):** Modelo predictivo de precios Airbnb NYC con limpieza avanzada, análisis de multicolinealidad (VIF), evaluación completa y comunicación de resultados con narrativa de negocio.

**Lección más importante:** La ciencia de datos no es solo código y modelos. Es la capacidad de transformar datos en decisiones: entender qué pregunta hacer, preparar los datos correctamente, elegir el modelo apropiado, evaluarlo con honestidad y comunicar los hallazgos de forma que cualquier persona pueda actuar sobre ellos.

---

## Dudas o Preguntas

- ¿Cómo se aplicaría análisis de series de tiempo para capturar la estacionalidad de precios en plataformas como Airbnb?
- ¿Cuándo es preferible usar un modelo de Gradient Boosting vs una red neuronal para regresión en datasets de tamaño mediano (~10,000 registros)?

---

## Commits Realizados

```
Semana7: Dataset Airbnb limpio generado (7,337 registros)
Semana7: Limpieza.py - manejo de nulos y outliers completado
Semana7: Modelo.py - regresión lineal múltiple entrenada y evaluada
Semana7: 6 visualizaciones generadas
Semana7: Presentacion - narrativa y recomendaciones de negocio
Semana7: Consolidado completo - Proyecto Final
```

---

## Referencias

- James, G., Witten, D., Hastie, T. & Tibshirani, R. (2021). *An Introduction to Statistical Learning, 2nd ed.* Springer.
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow, 3rd ed.* O'Reilly.
- Kaggle. (2024). *Airbnb Price Prediction NYC.* https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction
- Scikit-learn Developers. (2024). *sklearn.linear_model.LinearRegression.* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- Pandas Development Team. (2024). *Pandas Documentation.* https://pandas.pydata.org/docs/
- Seaborn. (2024). *Statistical Data Visualization.* https://seaborn.pydata.org/
- Statsmodels. (2024). *Variance Inflation Factor.* https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html
