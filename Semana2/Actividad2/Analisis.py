# =============================================================================
# Actividad 2 — Ciencia de Datos | Universidad Tecmilenio
# Análisis Exploratorio de Datos — Todo Ventas en Línea S.A. de C.V.
# Autor: Zoe Ángeles
# Fecha: 2024
# Temas: T3 (Arquitecturas), T4 (NoSQL), T5 (CRUD MongoDB)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Semilla para reproducibilidad
np.random.seed(42)
random.seed(42)
N = 5000

# =============================================================================
# SECCIÓN 1: GENERACIÓN DEL DATASET
# =============================================================================
print("=" * 60)
print("SECCIÓN 1: GENERACIÓN DEL DATASET")
print("=" * 60)

# Listas de valores categóricos
categorias      = ['Electrónica','Ropa','Hogar','Deportes','Libros','Juguetes','Belleza','Alimentos']
metodos_pago    = ['Tarjeta de crédito','Tarjeta de débito','PayPal','Transferencia','Efectivo']
regiones        = ['Norte','Sur','Centro','Este','Oeste']
estado_envio    = ['Entregado','En tránsito','Devuelto','Cancelado']
genero_cliente  = ['M','F','No especificado']

# Variables numéricas
precio_unitario = np.round(np.random.uniform(50, 5000, N), 2)    # numérico decimal
cantidad        = np.random.randint(1, 20, N)                      # numérico entero
descuento_pct   = np.round(np.random.uniform(0, 0.40, N), 2)      # numérico decimal
total_venta     = np.round(precio_unitario * cantidad * (1 - descuento_pct), 2)  # numérico decimal
edad_cliente    = np.random.randint(18, 70, N)                     # numérico entero
calificacion    = np.round(np.random.uniform(1, 5, N), 1)          # numérico decimal
dias_envio      = np.random.randint(1, 15, N)                      # numérico entero
costo_envio     = np.round(np.random.uniform(0, 300, N), 2)        # numérico decimal

# Variables estructuradas (fecha e ID con formato predefinido)
fecha_inicio = datetime(2023, 1, 1)
fechas       = [fecha_inicio + timedelta(days=random.randint(0, 364)) for _ in range(N)]
fecha_venta  = [f.strftime('%Y-%m-%d') for f in fechas]           # estructurado: formato fecha
mes_venta    = [f.strftime('%B') for f in fechas]
id_orden     = [f'ORD-{str(i).zfill(5)}' for i in range(1, N+1)] # estructurado: ID con patrón

# Variables no estructuradas (texto libre)
comentarios_pool = [
    'Excelente producto, llegó a tiempo y en perfectas condiciones.',
    'El producto no cumplió mis expectativas, la calidad es regular.',
    'Muy buena compra, lo recomiendo ampliamente a todos.',
    'Tardó más de lo esperado pero el producto está bien.',
    'Increíble relación calidad-precio, definitivamente volvería a comprar.',
    'El empaque llegó dañado aunque el producto estaba bien.',
    'Servicio al cliente muy atento y resolvieron mis dudas rápido.',
    'No era exactamente lo que buscaba pero funciona correctamente.',
    'Producto de alta calidad, superó todas mis expectativas.',
    'Entrega puntual, producto exactamente como se describía en la página.',
]
descripcion_pool = [
    'Dispositivo de última generación con tecnología avanzada.',
    'Material premium con acabado de alta calidad y durabilidad.',
    'Diseño ergonómico ideal para uso diario y profesional.',
    'Producto certificado con garantía extendida de 12 meses.',
    'Edición especial con características exclusivas para el usuario.',
    'Fabricado con materiales sustentables y proceso ecológico.',
    'Compatible con múltiples plataformas y sistemas operativos.',
    'Alta resistencia y durabilidad probada bajo estándares internacionales.',
]
comentario_cliente   = [random.choice(comentarios_pool) for _ in range(N)]  # no estructurado
descripcion_producto = [random.choice(descripcion_pool) for _ in range(N)]  # no estructurado

# Construcción del DataFrame
df = pd.DataFrame({
    'id_orden':             id_orden,
    'fecha_venta':          fecha_venta,
    'mes_venta':            mes_venta,
    'categoria':            np.random.choice(categorias, N),
    'metodo_pago':          np.random.choice(metodos_pago, N),
    'region':               np.random.choice(regiones, N),
    'estado_envio':         np.random.choice(estado_envio, N, p=[0.75,0.10,0.08,0.07]),
    'genero_cliente':       np.random.choice(genero_cliente, N, p=[0.45,0.45,0.10]),
    'precio_unitario':      precio_unitario,
    'cantidad':             cantidad,
    'descuento_pct':        descuento_pct,
    'total_venta':          total_venta,
    'edad_cliente':         edad_cliente,
    'calificacion':         calificacion,
    'dias_envio':           dias_envio,
    'costo_envio':          costo_envio,
    'comentario_cliente':   comentario_cliente,
    'descripcion_producto': descripcion_producto,
})

df.to_csv('datos_ventas.csv', index=False)
print(f"Dataset creado: {df.shape[0]} registros x {df.shape[1]} columnas")
print(f"\nTipos de columnas:")
print(df.dtypes)
print(f"\nValores nulos: {df.isnull().sum().sum()}")

# =============================================================================
# SECCIÓN 2: CONEXIÓN Y CARGA EN MONGODB (simulada con pymongo)
# =============================================================================
print("\n" + "=" * 60)
print("SECCIÓN 2: CARGA EN MONGODB")
print("=" * 60)

# NOTA: Para ejecutar la conexión real a MongoDB descomenta el bloque siguiente
# y asegúrate de tener MongoDB corriendo en localhost:27017
#
# from pymongo import MongoClient
# client     = MongoClient('mongodb://localhost:27017/')
# db         = client['todo_ventas_db']
# coleccion  = db['ventas']
# registros  = df.to_dict(orient='records')
# coleccion.drop()
# resultado  = coleccion.insert_many(registros)
# print(f"Documentos insertados: {len(resultado.inserted_ids)}")
# print(f"Total en colección: {coleccion.count_documents({})}")
# client.close()

print("Simulación de carga a MongoDB:")
print(f"  Base de datos:  todo_ventas_db")
print(f"  Colección:      ventas")
print(f"  Documentos:     {len(df)} registros insertados con insert_many()")
print(f"  Estructura:     Cada fila del DataFrame = 1 documento JSON en MongoDB")

# =============================================================================
# SECCIÓN 3: ANÁLISIS EXPLORATORIO CON PANDAS Y NUMPY
# =============================================================================
print("\n" + "=" * 60)
print("SECCIÓN 3: ANÁLISIS EXPLORATORIO")
print("=" * 60)

cols_num = ['precio_unitario','cantidad','descuento_pct','total_venta',
            'edad_cliente','calificacion','dias_envio','costo_envio']
df_num = df[cols_num]

# Estadísticas descriptivas
resumen = pd.DataFrame({
    'Media':           df_num.mean().round(2),
    'Mediana':         df_num.median().round(2),
    'Moda':            df_num.mode().iloc[0].round(2),
    'Desv. Estándar':  df_num.std().round(2),
    'Mínimo':          df_num.min().round(2),
    'Máximo':          df_num.max().round(2),
})
print("\n--- Resumen estadístico ---")
print(resumen.to_string())

# Ventas por categoría
print("\n--- Ventas por categoría ---")
ventas_cat = df.groupby('categoria')['total_venta'].agg(
    Total='sum', Promedio='mean', Ordenes='count').round(2).sort_values('Total', ascending=False)
print(ventas_cat.to_string())

# Distribución de estado de envío
print("\n--- Estado de envío ---")
print(df['estado_envio'].value_counts())

# =============================================================================
# SECCIÓN 4: VISUALIZACIONES
# =============================================================================
print("\n" + "=" * 60)
print("SECCIÓN 4: GENERANDO VISUALIZACIONES")
print("=" * 60)

AZUL='#185FA5'; NARANJA='#D85A30'; VERDE='#3B6D11'; MORADO='#534AB7'
GRIS='#5F5E5A'; FONDO='#FAFAFA'
PALETA=[AZUL,NARANJA,VERDE,MORADO,'#854F0B','#0F6E56','#993556','#993C1D']

# --- Gráfica 1: Diagrama de cajas ---
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Diagrama de Cajas — Variables Numéricas Clave',
             fontsize=15, fontweight='bold', color='#2C2C2A', y=1.01)
for ax, (col, titulo, color) in zip(axes, [
    ('total_venta',     'Total de Venta (MXN)',  AZUL),
    ('precio_unitario', 'Precio Unitario (MXN)', NARANJA),
    ('calificacion',    'Calificación (1–5)',     VERDE),
]):
    ax.set_facecolor(FONDO)
    bp = ax.boxplot(df[col].dropna(), patch_artist=True, widths=0.5,
                    medianprops=dict(color='white', linewidth=2.5),
                    whiskerprops=dict(color=GRIS, linewidth=1.2),
                    capprops=dict(color=GRIS, linewidth=1.5),
                    flierprops=dict(marker='o', markerfacecolor=color, markersize=3, alpha=0.4, linestyle='none'))
    bp['boxes'][0].set_facecolor(color); bp['boxes'][0].set_alpha(0.75)
    ax.set_title(titulo, fontsize=11, fontweight='500', color='#2C2C2A', pad=10)
    ax.tick_params(colors=GRIS, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor('#D3D1C7'); spine.set_linewidth(0.8)
    ax.grid(axis='y', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
    ax.set_xticklabels([])
    med=df[col].median(); q1=df[col].quantile(0.25); q3=df[col].quantile(0.75)
    ax.text(1.32,med,f'Med: {med:,.1f}',va='center',fontsize=8.5,color='#2C2C2A')
    ax.text(1.32,q1, f'Q1: {q1:,.1f}', va='center',fontsize=8.5,color=GRIS)
    ax.text(1.32,q3, f'Q3: {q3:,.1f}', va='center',fontsize=8.5,color=GRIS)
plt.tight_layout()
plt.savefig('Visualizaciones/boxplot.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close()
print("  boxplot.png guardado")

# --- Gráfica 2: Dispersión ---
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(FONDO); ax.set_facecolor(FONDO)
cats = df['categoria'].unique()
for cat, color in zip(cats, PALETA):
    sub = df[df['categoria']==cat]
    ax.scatter(sub['precio_unitario'], sub['total_venta'],
               color=color, alpha=0.35, s=18, label=cat)
m, b = np.polyfit(df['precio_unitario'], df['total_venta'], 1)
xr = np.linspace(df['precio_unitario'].min(), df['precio_unitario'].max(), 200)
ax.plot(xr, m*xr+b, color='#2C2C2A', linewidth=1.8, linestyle='--',
        label=f'Tendencia (y={m:.1f}x+{b:.0f})')
ax.set_xlabel('Precio Unitario (MXN)', fontsize=12, color='#2C2C2A', labelpad=8)
ax.set_ylabel('Total de Venta (MXN)',  fontsize=12, color='#2C2C2A', labelpad=8)
ax.set_title('Dispersión: Precio Unitario vs Total de Venta por Categoría',
             fontsize=13, fontweight='bold', color='#2C2C2A', pad=14)
ax.tick_params(colors=GRIS, labelsize=9)
ax.grid(color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
for spine in ax.spines.values():
    spine.set_edgecolor('#D3D1C7'); spine.set_linewidth(0.8)
corr = df['precio_unitario'].corr(df['total_venta'])
ax.text(0.03, 0.97, f'Correlación de Pearson: r = {corr:.3f}',
        transform=ax.transAxes, fontsize=10, color='#2C2C2A', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#D3D1C7', alpha=0.9))
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7', loc='upper left')
plt.tight_layout()
plt.savefig('Visualizaciones/scatter.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close()
print("  scatter.png guardado")

# --- Gráfica 3: Histogramas ---
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.patch.set_facecolor(FONDO)
fig.suptitle('Distribución de Variables — Histogramas',
             fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
for ax, (col, titulo, color) in zip(axes, [
    ('total_venta',  'Distribución del Total de Venta (MXN)', AZUL),
    ('edad_cliente', 'Distribución de Edad del Cliente',       NARANJA),
]):
    ax.set_facecolor(FONDO)
    ax.hist(df[col], bins=35, color=color, alpha=0.8, edgecolor='white', linewidth=0.5)
    ax.axvline(df[col].mean(),   color='#2C2C2A', linewidth=2,   linestyle='--',
               label=f'Media: {df[col].mean():,.1f}')
    ax.axvline(df[col].median(), color=GRIS,      linewidth=1.8, linestyle=':',
               label=f'Mediana: {df[col].median():,.1f}')
    ax.set_title(titulo, fontsize=11, fontweight='500', color='#2C2C2A', pad=10)
    ax.set_xlabel(col.replace('_',' ').title(), fontsize=10, color='#2C2C2A')
    ax.set_ylabel('Frecuencia', fontsize=10, color='#2C2C2A')
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.grid(axis='y', color='#D3D1C7', linestyle='--', linewidth=0.6, alpha=0.7)
    for spine in ax.spines.values():
        spine.set_edgecolor('#D3D1C7'); spine.set_linewidth(0.8)
    ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
plt.tight_layout()
plt.savefig('Visualizaciones/histograma.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close()
print("  histograma.png guardado")

print("\nAnálisis completo. Archivos generados:")
print("  - datos_ventas.csv")
print("  - Visualizaciones/boxplot.png")
print("  - Visualizaciones/scatter.png")
print("  - Visualizaciones/histograma.png")
