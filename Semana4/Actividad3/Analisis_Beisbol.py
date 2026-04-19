# ============================================================================
# ACTIVIDAD 3 — Ciencia de Datos | Universidad Tecmilenio
# Regresión Lineal Simple — Datos MLB Béisbol
# Predicción de Carreras (R) a partir de At-Bats (AB)
# Autor: Zoe Ángeles | Fecha: 18/04/2026
# Temas: T9 (Preparación de datos), T10 (Procesamiento de datos)
# ============================================================================

# ── PARTE 1: IMPORTACIÓN DE LIBRERÍAS ────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
print("Librerías importadas correctamente.")

# ── PARTE 2: CARGA DE DATOS ───────────────────────────────────────────────────
# Fuente: ESPN MLB Statistics (https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador)
# Dataset: temporadas 2018-2023, 30 equipos MLB, 180 registros
df_raw = pd.read_csv('Datos/beisbol_mlb.csv')
print(f"\nDataset cargado: {df_raw.shape[0]} registros x {df_raw.shape[1]} columnas")
print(f"\nPrimeras 5 filas:\n{df_raw.head().to_string()}")
print(f"\nTipos de datos:\n{df_raw.dtypes}")
print(f"\nValores nulos:\n{df_raw.isnull().sum()}")
print(f"\nEstadísticas descriptivas:\n{df_raw.describe().round(2).to_string()}")

# ── PARTE 3: LIMPIEZA Y PREPARACIÓN ──────────────────────────────────────────
df = df_raw.copy()

# Convertir columnas con nulos a float para poder imputar
df['H']  = df['H'].astype(float)
df['BB'] = df['BB'].astype(float)

# Imputación con mediana (robusta ante outliers)
df['H']  = df['H'].fillna(df['H'].median())
df['BB'] = df['BB'].fillna(df['BB'].median())

# Normalizar temporada 2020 (60 juegos → equivalente 162 juegos)
# La temporada COVID se jugó solo 37% del calendario normal
mask_2020 = df['temporada'] == 2020
factor    = 162.0 / 60.0
for col in ['AB', 'H', 'HR', 'BB', 'R']:
    df[col] = df[col].astype(float)
    df.loc[mask_2020, col] = (df.loc[mask_2020, col] * factor).round(0)

df[['AB', 'H', 'HR', 'BB', 'R']] = df[['AB', 'H', 'HR', 'BB', 'R']].astype(int)

print(f"\nValores nulos tras limpieza: {df.isnull().sum().sum()}")
print(f"\nEstadísticas post-limpieza:\n{df[['AB','R']].describe().round(2).to_string()}")

# Estandarización de At-Bats para verificación (no se usa en el modelo final)
scaler   = StandardScaler()
AB_scaled = scaler.fit_transform(df[['AB']])
print(f"\nAB estandarizado — Media: {AB_scaled.mean():.4f}, Std: {AB_scaled.std():.4f}")

# ── PARTE 4: ANÁLISIS EXPLORATORIO Y CORRELACIÓN ─────────────────────────────
pearson_r, p_val = stats.pearsonr(df['AB'], df['R'])
print(f"\n=== CORRELACIÓN DE PEARSON ===")
print(f"r(AB, R) = {pearson_r:.4f}")
print(f"p-valor  = {p_val:.6f}")
print(f"Significancia estadística: {'Sí (p < 0.05)' if p_val < 0.05 else 'No'}")

print(f"\nMatriz de correlaciones:")
print(df[['AB','H','HR','BB','R']].corr().round(4).to_string())

# ── PARTE 5: CONSTRUCCIÓN DEL MODELO ─────────────────────────────────────────
# Variable independiente (X): AB — At-Bats (número de bateos por temporada)
# Variable dependiente   (y): R  — Runs (número de carreras anotadas)
X = df[['AB']]
y = df['R']

# División train/test: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print(f"\nRegistros de entrenamiento: {len(X_train)}")
print(f"Registros de prueba:        {len(X_test)}")

# Entrenamiento
modelo = LinearRegression()
modelo.fit(X_train, y_train)
print(f"\nModelo entrenado:")
print(f"  Intercepto (b0): {modelo.intercept_:.2f}")
print(f"  Coeficiente (b1): {modelo.coef_[0]:.4f}")
print(f"  Ecuación: R = {modelo.coef_[0]:.4f} × AB + {modelo.intercept_:.2f}")

# ── PARTE 6: PREDICCIÓN Y EVALUACIÓN ─────────────────────────────────────────
y_pred = modelo.predict(X_test)

r2   = r2_score(y_test, y_pred)
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\n=== MÉTRICAS DE EVALUACIÓN ===")
print(f"R² (coeficiente de determinación): {r2:.4f}")
print(f"MAE  (error absoluto medio):        {mae:.2f} carreras")
print(f"MSE  (error cuadrático medio):      {mse:.2f}")
print(f"RMSE (raíz del error cuadrático):   {rmse:.2f} carreras")

# Tabla comparativa real vs predicho
comparacion = pd.DataFrame({
    'Equipo':     df.loc[X_test.index, 'equipo'].values,
    'Temporada':  df.loc[X_test.index, 'temporada'].values,
    'AB':         X_test['AB'].values,
    'R_real':     y_test.values,
    'R_predicho': y_pred.round(0).astype(int),
    'Error':      (y_test.values - y_pred.round(0)).astype(int)
})
print(f"\nMuestra de predicciones:\n{comparacion.head(10).to_string(index=False)}")

# ── PARTE 7: VISUALIZACIONES ──────────────────────────────────────────────────
import os
os.makedirs('Visualizaciones', exist_ok=True)

FONDO='#FAFAFA'; AZUL='#185FA5'; NARANJA='#D85A30'; VERDE='#3B6D11'
MORADO='#534AB7'; GRIS='#5F5E5A'
def estilo(ax):
    ax.set_facecolor(FONDO)
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.grid(color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
    for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)

# Gráfica 1: Scatter + Real vs Predicho
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Regresión Lineal Simple — Bateos vs Carreras (MLB)', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; estilo(ax)
ax.scatter(X_train, y_train, color=AZUL,   alpha=0.5, s=22, label='Entrenamiento (80%)')
ax.scatter(X_test,  y_test,  color=NARANJA, alpha=0.8, s=40, label='Prueba (20%)')
x_line = np.linspace(df['AB'].min(), df['AB'].max(), 300).reshape(-1,1)
ax.plot(x_line, modelo.predict(x_line), color=VERDE, linewidth=2.5,
        label=f'y = {modelo.coef_[0]:.4f}x + {modelo.intercept_:.0f}')
ax.set_xlabel('At-Bats (Bateos por temporada)', fontsize=11, color='#2C2C2A', labelpad=8)
ax.set_ylabel('Runs (Carreras anotadas)', fontsize=11, color='#2C2C2A', labelpad=8)
ax.set_title('Línea de Regresión', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.text(0.03, 0.97, f'r = {pearson_r:.4f}\nR² = {r2:.4f}',
        transform=ax.transAxes, fontsize=10, color='#2C2C2A', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#D3D1C7', alpha=0.9))
ax = axes[1]; estilo(ax)
ax.scatter(y_test, y_pred, color=MORADO, alpha=0.75, s=45, edgecolors='white', linewidths=0.5)
lims = [min(y_test.min(), y_pred.min())-30, max(y_test.max(), y_pred.max())+30]
ax.plot(lims, lims, color=NARANJA, linewidth=2, linestyle='--', label='Predicción perfecta')
ax.set_xlabel('Carreras reales', fontsize=11, color='#2C2C2A', labelpad=8)
ax.set_ylabel('Carreras predichas', fontsize=11, color='#2C2C2A', labelpad=8)
ax.set_title('Real vs Predicho', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.text(0.03, 0.97, f'MAE  = {mae:.1f}\nRMSE = {rmse:.1f}',
        transform=ax.transAxes, fontsize=10, color='#2C2C2A', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#D3D1C7', alpha=0.9))
plt.tight_layout()
plt.savefig('Visualizaciones/regresion_scatter.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("  regresion_scatter.png ✓")

# Gráfica 2: Residuos
residuos = y_test.values - y_pred
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Análisis de Residuos', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; estilo(ax)
ax.scatter(y_pred, residuos, color=AZUL, alpha=0.75, s=40, edgecolors='white', linewidths=0.5)
ax.axhline(0, color=NARANJA, linewidth=2, linestyle='--', label='Residuo = 0')
ax.set_xlabel('Valores predichos', fontsize=11, color='#2C2C2A')
ax.set_ylabel('Residuos (Real − Predicho)', fontsize=11, color='#2C2C2A')
ax.set_title('Residuos vs Predichos', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax = axes[1]; estilo(ax)
ax.grid(axis='y', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
ax.hist(residuos, bins=18, color=VERDE, alpha=0.82, edgecolor='white', linewidth=0.5)
ax.axvline(residuos.mean(), color=NARANJA, lw=2, ls='--', label=f'Media: {residuos.mean():.1f}')
ax.set_xlabel('Residuos', fontsize=11, color='#2C2C2A')
ax.set_ylabel('Frecuencia', fontsize=11, color='#2C2C2A')
ax.set_title('Distribución de Residuos', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
plt.tight_layout()
plt.savefig('Visualizaciones/residuos.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("  residuos.png ✓")

# Gráfica 3: Exploratorio
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Análisis Exploratorio — Variables Clave MLB', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
for ax, (col, color, titulo) in zip(axes[:2], [
    ('AB', AZUL,  'Distribución de At-Bats'),
    ('R',  VERDE, 'Distribución de Carreras'),
]):
    estilo(ax)
    ax.hist(df[col], bins=25, color=color, alpha=0.82, edgecolor='white', linewidth=0.4)
    ax.axvline(df[col].mean(),   color=NARANJA, lw=2, ls='--', label=f'Media: {df[col].mean():.0f}')
    ax.axvline(df[col].median(), color=GRIS,    lw=1.8, ls=':', label=f'Mediana: {df[col].median():.0f}')
    ax.set_title(titulo, fontsize=11, fontweight='500', color='#2C2C2A')
    ax.set_ylabel('Frecuencia', fontsize=10, color='#2C2C2A')
    ax.legend(fontsize=8.5, framealpha=0.9, edgecolor='#D3D1C7')
ax = axes[2]
cm = df[['AB','H','HR','BB','R']].corr()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(cm, annot=True, fmt='.2f', cmap=cmap, center=0, vmin=-1, vmax=1,
            square=True, linewidths=0.5, linecolor='#F1EFE8',
            annot_kws={'size':9,'weight':'500'}, ax=ax, cbar_kws={'shrink':0.8})
ax.set_title('Correlaciones entre Variables', fontsize=11, fontweight='500', color='#2C2C2A', pad=10)
ax.tick_params(colors='#2C2C2A', labelsize=9)
plt.tight_layout()
plt.savefig('Visualizaciones/exploratorio.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("  exploratorio.png ✓")

print("\nAnálisis completo.")
