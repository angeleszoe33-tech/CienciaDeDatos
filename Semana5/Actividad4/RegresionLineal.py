# ============================================================================
# ACTIVIDAD 4 — PARTE 1: Regresión Lineal Múltiple
# Predicción de ventas de vehículos según precio y kilometraje
# Curso: QR.LSTI2309TEO — Universidad Tecmilenio
# Autor: Zoe Ángeles | Fecha: 26/04/2026
# Temas: T11 (Análisis preliminar), T12 (Regresión lineal)
# ============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os, warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

# ── 1. CARGA DE DATOS ─────────────────────────────────────────────────────────
# Fuente: Kaggle — Vehicle Sales Data
# https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data
df = pd.read_csv('Datos/vehiculos.csv')
print(f"Dataset cargado: {df.shape[0]:,} registros x {df.shape[1]} columnas")
print(f"\nPrimeras filas:\n{df.head().to_string()}")
print(f"\nNulos:\n{df.isnull().sum()}")

# ── 2. LIMPIEZA ───────────────────────────────────────────────────────────────
df['precio']      = df['precio'].fillna(df['precio'].median())
df['kilometraje'] = df['kilometraje'].fillna(df['kilometraje'].median())
print(f"\nNulos post-limpieza: {df.isnull().sum().sum()}")
print(f"\nEstadísticas:\n{df[['precio','kilometraje','ventas']].describe().round(2).to_string()}")

# ── 3. ANÁLISIS EXPLORATORIO — PAIRPLOT ───────────────────────────────────────
FONDO='#FAFAFA'; AZUL='#185FA5'
g = sns.pairplot(df[['precio','kilometraje','ventas']],
                 plot_kws={'alpha':0.4,'s':12,'color':AZUL},
                 diag_kws={'color':AZUL,'alpha':0.7})
g.figure.suptitle('Pairplot — Precio, Kilometraje y Ventas', y=1.02,
                   fontsize=13, fontweight='bold', color='#2C2C2A')
g.figure.patch.set_facecolor(FONDO)
os.makedirs('Visualizaciones', exist_ok=True)
plt.savefig('Visualizaciones/pairplot_vehiculos.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("\npairplot_vehiculos.png ✓")

# Correlaciones
print(f"\nCorrelaciones:")
print(f"  precio vs ventas:       r = {df['precio'].corr(df['ventas']):.4f}")
print(f"  kilometraje vs ventas:  r = {df['kilometraje'].corr(df['ventas']):.4f}")
print(f"  precio vs kilometraje:  r = {df['precio'].corr(df['kilometraje']):.4f}")

# ── 4. IDENTIFICACIÓN DE VARIABLES ───────────────────────────────────────────
# Variables independientes (X): precio, kilometraje
# Variable dependiente    (y): ventas
X = df[['precio', 'kilometraje']]
y = df['ventas']

# ── 5. DIVISIÓN DE DATOS ──────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nEntrenamiento: {len(X_train)} | Prueba: {len(X_test)}")

# ── 6. MODELADO ───────────────────────────────────────────────────────────────
modelo = LinearRegression()
modelo.fit(X_train, y_train)
print(f"\nEcuación del modelo:")
print(f"  ventas = {modelo.coef_[0]:.6f}·precio + {modelo.coef_[1]:.6f}·km + {modelo.intercept_:.2f}")

# ── 7. PREDICCIÓN ─────────────────────────────────────────────────────────────
y_pred = modelo.predict(X_test)
ejemplos = pd.DataFrame({'precio':[15000,25000,35000,50000],
                          'kilometraje':[10000,40000,80000,150000]})
print(f"\nPredicciones de ejemplo:")
for _, row in ejemplos.iterrows():
    pred = modelo.predict([[row['precio'], row['kilometraje']]])[0]
    print(f"  ${row['precio']:,} | {row['kilometraje']:,} km → {pred:.0f} ventas estimadas")

# ── 8. EVALUACIÓN ─────────────────────────────────────────────────────────────
r2   = r2_score(y_test, y_pred)
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\n=== MÉTRICAS ===")
print(f"R²   = {r2:.4f}  → el modelo explica el {r2*100:.1f}% de la varianza en ventas")
print(f"MAE  = {mae:.2f} ventas")
print(f"MSE  = {mse:.2f}")
print(f"RMSE = {rmse:.2f} ventas")

# Gráfica
NARANJA='#D85A30'; VERDE='#3B6D11'; GRIS='#5F5E5A'
fig, axes = plt.subplots(1,2, figsize=(13,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Regresión Lineal Múltiple — Vehículos', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; ax.set_facecolor(FONDO)
ax.scatter(y_test, y_pred, color=AZUL, alpha=0.55, s=20, edgecolors='white', lw=0.3)
lims = [min(y_test.min(),y_pred.min())-10, max(y_test.max(),y_pred.max())+10]
ax.plot(lims, lims, color=NARANJA, lw=2, ls='--', label='Predicción perfecta')
ax.set_xlabel('Ventas reales', fontsize=11, color='#2C2C2A'); ax.set_ylabel('Ventas predichas', fontsize=11, color='#2C2C2A')
ax.set_title('Real vs Predicho', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.text(0.03,0.97,f'R² = {r2:.4f}\nRMSE = {rmse:.2f}', transform=ax.transAxes, fontsize=10,
        va='top', bbox=dict(boxstyle='round,pad=0.4',facecolor='white',edgecolor='#D3D1C7',alpha=0.9))
ax.tick_params(colors=GRIS, labelsize=9); ax.grid(color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
ax = axes[1]; ax.set_facecolor(FONDO)
res = y_test.values - y_pred
ax.hist(res, bins=25, color=VERDE, alpha=0.82, edgecolor='white', lw=0.4)
ax.axvline(res.mean(), color=NARANJA, lw=2, ls='--', label=f'Media: {res.mean():.1f}')
ax.set_xlabel('Residuos', fontsize=11, color='#2C2C2A'); ax.set_ylabel('Frecuencia', fontsize=11, color='#2C2C2A')
ax.set_title('Distribución de Residuos', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.tick_params(colors=GRIS, labelsize=9); ax.grid(axis='y',color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
plt.tight_layout()
plt.savefig('Visualizaciones/regresion_multiple.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("regresion_multiple.png ✓")
