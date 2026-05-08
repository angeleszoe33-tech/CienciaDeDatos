# ============================================================================
# PROYECTO FINAL — LIMPIEZA DE DATOS
# Mercado Inmobiliario Airbnb NYC
# Curso: QR.LSTI2309TEO — Universidad Tecmilenio
# Autor: Zoe Ángeles | Fecha: 08/05/2026
# ============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ── CARGA ─────────────────────────────────────────────────────────────────────
df_raw = pd.read_csv('Datos/airbnb_nyc.csv')
print(f"Registros originales: {len(df_raw):,}")
print(f"\nValores nulos:\n{df_raw.isnull().sum()}")
print(f"\nEstadísticas precio:\n{df_raw['price'].describe().round(2)}")

# ── IMPUTACIÓN DE NULOS ───────────────────────────────────────────────────────
df = df_raw.copy()
# reviews_per_month: nulos = listings sin reseñas → 0 tiene sentido de negocio
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
# number_of_reviews: nulos → 0
df['number_of_reviews'] = df['number_of_reviews'].fillna(0)
print(f"\nNulos tras imputación: {df.isnull().sum().sum()}")

# ── DETECCIÓN Y REMOCIÓN DE OUTLIERS — MÉTODO IQR ────────────────────────────
Q1_p, Q3_p = df['price'].quantile([0.25, 0.75])
IQR_p = Q3_p - Q1_p
lim_inf_p = Q1_p - 1.5 * IQR_p
lim_sup_p = Q3_p + 1.5 * IQR_p
print(f"\nPrecio — Límite inferior: ${lim_inf_p:.0f} | Límite superior: ${lim_sup_p:.0f}")
outliers_precio = df[(df['price'] < lim_inf_p) | (df['price'] > lim_sup_p)]
print(f"Outliers de precio detectados: {len(outliers_precio)}")

# Minimum nights: más de 30 noches mínimas es extremo para análisis de mercado
outliers_nights = df[df['minimum_nights'] > 30]
print(f"Outliers de minimum_nights (>30): {len(outliers_nights)}")

df_limpio = df[(df['price'] >= lim_inf_p) & (df['price'] <= lim_sup_p)]
df_limpio = df_limpio[df_limpio['minimum_nights'] <= 30]
print(f"\nRegistros finales: {len(df_limpio):,}")
print(f"\nEstadísticas precio post-limpieza:\n{df_limpio['price'].describe().round(2)}")

# ── GUARDAR ───────────────────────────────────────────────────────────────────
df_limpio.to_csv('Datos/airbnb_limpio.csv', index=False)
print("\nDataset limpio guardado en Datos/airbnb_limpio.csv")
