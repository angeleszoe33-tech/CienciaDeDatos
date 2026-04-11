# ============================================================================
# PROYECTO — AVANCE SEMANA 3
# Análisis Exploratorio de Datos: Mercado Inmobiliario Airbnb NYC
# Curso: QR.LSTI2309TEO — Universidad Tecmilenio
# Autor: Zoe Ángeles
# Temas: T6 (Python para Ciencia de Datos), T7 (Proceso de DS), T8 (EDA)
# ============================================================================

# ── PARTE 1: IMPORTACIÓN DE LIBRERÍAS Y CARGA DE DATOS ──────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("Librerías importadas correctamente.")
print(f"  Pandas:  {pd.__version__}")
print(f"  NumPy:   {np.__version__}")

# Carga del dataset
df_raw = pd.read_csv('Datos/airbnb_nyc.csv')
print(f"\nDataset cargado: {df_raw.shape[0]:,} registros x {df_raw.shape[1]} columnas")

# Vista inicial
print("\n--- Primeras 5 filas ---")
print(df_raw.head().to_string())
print("\n--- Tipos de datos ---")
print(df_raw.dtypes)
print("\n--- Valores nulos por columna ---")
print(df_raw.isnull().sum())

# ── PARTE 2: LIMPIEZA Y PREPARACIÓN DE DATOS ────────────────────────────────
df = df_raw.copy()

# Convertir fecha
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# Imputar nulos: reviews_per_month con 0 (sin reseñas = sin actividad mensual)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df['last_review']       = df['last_review'].fillna(pd.Timestamp('2019-01-01'))

# Eliminar outliers extremos de precio (> $500/noche) y minimum_nights > 30
registros_antes = len(df)
df = df[(df['price'] <= 500) & (df['minimum_nights'] <= 30)]
print(f"\nRegistros eliminados por outliers: {registros_antes - len(df)}")
print(f"Registros finales para análisis: {len(df):,}")

# Estado del dataset limpio
print("\n--- Info post-limpieza ---")
print(df.info())

# ── PARTE 3: ANÁLISIS DESCRIPTIVO ───────────────────────────────────────────
print("\n" + "="*60)
print("ANÁLISIS DESCRIPTIVO")
print("="*60)

# Estadísticas generales
print("\n--- Estadísticas descriptivas completas ---")
print(df.describe(include='all').to_string())

# Variables numéricas clave
cols_num = ['price', 'minimum_nights', 'number_of_reviews',
            'reviews_per_month', 'availability_365']
resumen = pd.DataFrame({
    'Media':          df[cols_num].mean().round(2),
    'Mediana':        df[cols_num].median().round(2),
    'Moda':           df[cols_num].mode().iloc[0].round(2),
    'Desv. Estándar': df[cols_num].std().round(2),
    'Mínimo':         df[cols_num].min().round(2),
    'Máximo':         df[cols_num].max().round(2),
    'Q1':             df[cols_num].quantile(0.25).round(2),
    'Q3':             df[cols_num].quantile(0.75).round(2),
})
print("\n--- Resumen estadístico variables numéricas ---")
print(resumen.to_string())

# Precio por borough
print("\n--- Precio por Borough ---")
precio_borough = df.groupby('neighbourhood_group')['price'].agg(
    Media='mean', Mediana='median', Mínimo='min', Máximo='max', Listings='count'
).round(2).sort_values('Mediana', ascending=False)
print(precio_borough.to_string())

# Precio por tipo de habitación
print("\n--- Precio por Tipo de Habitación ---")
precio_tipo = df.groupby('room_type')['price'].agg(
    Media='mean', Mediana='median', Listings='count'
).round(2).sort_values('Media', ascending=False)
print(precio_tipo.to_string())

# Variables que más influyen en el precio
print("\n--- Correlaciones con el precio ---")
cols_corr = ['price','minimum_nights','number_of_reviews',
             'reviews_per_month','calculated_host_listings_count','availability_365']
print(df[cols_corr].corr()['price'].sort_values(ascending=False).round(3))

# ── PARTE 4: VISUALIZACIONES ─────────────────────────────────────────────────
print("\n" + "="*60)
print("GENERANDO VISUALIZACIONES")
print("="*60)

import os
os.makedirs('Visualizaciones', exist_ok=True)

FONDO  = '#FAFAFA'; AZUL = '#185FA5'; NARANJA = '#D85A30'
VERDE  = '#3B6D11'; MORADO = '#534AB7'; GRIS = '#5F5E5A'
PALETA = ['#185FA5','#D85A30','#3B6D11','#534AB7','#854F0B']

def estilo(ax):
    ax.set_facecolor(FONDO)
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.grid(axis='y', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
    for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)

# Gráfica 1 — Histograma + barras precio por borough
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Distribución del Precio por Noche', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; estilo(ax)
ax.hist(df['price'], bins=50, color=AZUL, alpha=0.8, edgecolor='white', linewidth=0.4)
ax.axvline(df['price'].mean(),   color=NARANJA, lw=2, ls='--', label=f'Media: ${df["price"].mean():.0f}')
ax.axvline(df['price'].median(), color=VERDE,   lw=2, ls=':',  label=f'Mediana: ${df["price"].median():.0f}')
ax.set_xlabel('Precio por noche (USD)', fontsize=10, color='#2C2C2A')
ax.set_ylabel('Frecuencia', fontsize=10, color='#2C2C2A')
ax.set_title('Histograma de Precio', fontsize=11, fontweight='500', color='#2C2C2A')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax = axes[1]; estilo(ax)
order_b = df.groupby('neighbourhood_group')['price'].median().sort_values(ascending=False)
bars = ax.bar(order_b.index, order_b.values, color=PALETA, alpha=0.85, edgecolor='white')
for bar, val in zip(bars, order_b.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5, f'${val:.0f}', ha='center', va='bottom', fontsize=9, color='#2C2C2A', fontweight='500')
ax.set_title('Precio Mediano por Borough', fontsize=11, fontweight='500', color='#2C2C2A')
ax.set_xlabel('Borough', fontsize=10, color='#2C2C2A'); ax.set_ylabel('USD', fontsize=10, color='#2C2C2A')
plt.tight_layout(); plt.savefig('Visualizaciones/hist_precio.png', dpi=180, bbox_inches='tight', facecolor=FONDO); plt.close()
print("  hist_precio.png ✓")

# Gráfica 2 — Boxplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Análisis de Precios — Boxplots', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
for ax, (col, title, order_key) in zip(axes, [
    ('room_type',           'Precio por Tipo de Habitación', None),
    ('neighbourhood_group', 'Precio por Borough',           None),
]):
    estilo(ax)
    groups = df.groupby(col)['price'].median().sort_values(ascending=False).index
    data   = [df[df[col]==g]['price'].values for g in groups]
    colors = [AZUL, NARANJA, VERDE] if col=='room_type' else PALETA
    bp = ax.boxplot(data, patch_artist=True, widths=0.5,
                    medianprops=dict(color='white', linewidth=2.5),
                    whiskerprops=dict(color=GRIS, linewidth=1.2),
                    capprops=dict(color=GRIS, linewidth=1.5),
                    flierprops=dict(marker='o', markersize=2.5, alpha=0.3, linestyle='none'))
    for patch, c in zip(bp['boxes'], colors): patch.set_facecolor(c); patch.set_alpha(0.75)
    ax.set_xticklabels(groups, fontsize=8.5, color='#2C2C2A', rotation=10)
    ax.set_title(title, fontsize=11, fontweight='500', color='#2C2C2A')
    ax.set_ylabel('Precio por noche (USD)', fontsize=10, color='#2C2C2A')
plt.tight_layout(); plt.savefig('Visualizaciones/boxplot_precios.png', dpi=180, bbox_inches='tight', facecolor=FONDO); plt.close()
print("  boxplot_precios.png ✓")

# Gráfica 3 — Scatter plots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Relaciones entre Variables Clave', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; estilo(ax)
ax.grid(axis='both', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
rt_colors = {'Entire home/apt': AZUL, 'Private room': NARANJA, 'Shared room': VERDE}
for rt, c in rt_colors.items():
    sub = df[df['room_type']==rt]
    ax.scatter(sub['number_of_reviews'], sub['price'], color=c, alpha=0.25, s=12, label=rt)
ax.set_xlabel('Número de Reseñas', fontsize=10, color='#2C2C2A'); ax.set_ylabel('Precio (USD)', fontsize=10, color='#2C2C2A')
ax.set_title('Precio vs Número de Reseñas', fontsize=11, fontweight='500', color='#2C2C2A')
corr1 = df['number_of_reviews'].corr(df['price'])
ax.text(0.03, 0.97, f'r = {corr1:.3f}', transform=ax.transAxes, fontsize=10, color='#2C2C2A', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#D3D1C7', alpha=0.9))
ax.legend(fontsize=8.5, framealpha=0.9, edgecolor='#D3D1C7')
ax = axes[1]; estilo(ax)
ax.grid(axis='both', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
ax.scatter(df['availability_365'], df['price'], color=MORADO, alpha=0.2, s=10)
ax.set_xlabel('Disponibilidad (días/año)', fontsize=10, color='#2C2C2A'); ax.set_ylabel('Precio (USD)', fontsize=10, color='#2C2C2A')
ax.set_title('Precio vs Disponibilidad Anual', fontsize=11, fontweight='500', color='#2C2C2A')
corr2 = df['availability_365'].corr(df['price'])
ax.text(0.03, 0.97, f'r = {corr2:.3f}', transform=ax.transAxes, fontsize=10, color='#2C2C2A', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#D3D1C7', alpha=0.9))
plt.tight_layout(); plt.savefig('Visualizaciones/scatter_relaciones.png', dpi=180, bbox_inches='tight', facecolor=FONDO); plt.close()
print("  scatter_relaciones.png ✓")

# Gráfica 4 — Mapa de calor
fig, ax = plt.subplots(figsize=(9, 7)); fig.patch.set_facecolor(FONDO)
labels_es = ['Precio','Noches mín.','Núm. reseñas','Reseñas/mes','Listings host','Disponibilidad']
cm = df[cols_corr].corr(); cm.index = labels_es; cm.columns = labels_es
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(cm, annot=True, fmt='.2f', cmap=cmap, center=0, vmin=-1, vmax=1,
            square=True, linewidths=0.5, linecolor='#F1EFE8',
            annot_kws={'size':10,'weight':'500'}, ax=ax, cbar_kws={'shrink':0.8})
ax.set_title('Mapa de Calor de Correlaciones', fontsize=13, fontweight='bold', color='#2C2C2A', pad=14)
ax.tick_params(colors='#2C2C2A', labelsize=9.5)
plt.tight_layout(); plt.savefig('Visualizaciones/heatmap_correlaciones.png', dpi=180, bbox_inches='tight', facecolor=FONDO); plt.close()
print("  heatmap_correlaciones.png ✓")

# Gráfica 5 — Distribución por tipo y borough
fig, axes = plt.subplots(1, 2, figsize=(13, 5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Distribución por Tipo de Habitación y Borough', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; ax.set_facecolor(FONDO)
rt_c = df['room_type'].value_counts()
wedges, texts, autotexts = ax.pie(rt_c, labels=rt_c.index, autopct='%1.1f%%',
    colors=[AZUL,NARANJA,VERDE], startangle=90, pctdistance=0.75,
    wedgeprops=dict(edgecolor='white', linewidth=1.5))
for t in texts: t.set_fontsize(10); t.set_color('#2C2C2A')
for at in autotexts: at.set_fontsize(9.5); at.set_color('white'); at.set_fontweight('bold')
ax.set_title('Tipos de Habitación', fontsize=11, fontweight='500', color='#2C2C2A', pad=10)
ax = axes[1]; estilo(ax); ax.grid(axis='x', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
ng_c = df['neighbourhood_group'].value_counts()
bars = ax.barh(ng_c.index, ng_c.values, color=PALETA, alpha=0.85, edgecolor='white')
for bar, val in zip(bars, ng_c.values):
    ax.text(bar.get_width()+20, bar.get_y()+bar.get_height()/2, f'{val:,}', va='center', fontsize=9, color='#2C2C2A')
ax.set_title('Listings por Borough', fontsize=11, fontweight='500', color='#2C2C2A', pad=10)
ax.set_xlabel('Número de listings', fontsize=10, color='#2C2C2A')
plt.tight_layout(); plt.savefig('Visualizaciones/distribucion_tipos.png', dpi=180, bbox_inches='tight', facecolor=FONDO); plt.close()
print("  distribucion_tipos.png ✓")

print("\nAnálisis completo. Archivos generados en Visualizaciones/")
