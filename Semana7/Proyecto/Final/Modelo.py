# ============================================================================
# PROYECTO FINAL — MODELO DE REGRESIÓN LINEAL MÚLTIPLE
# Predicción de precios Airbnb NYC
# Curso: QR.LSTI2309TEO — Universidad Tecmilenio
# Autor: Zoe Ángeles | Fecha: 08/05/2026
# ============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
from matplotlib.patches import Patch
import os, warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

FONDO='#FAFAFA'; AZUL='#185FA5'; NARANJA='#D85A30'; VERDE='#3B6D11'
MORADO='#534AB7'; GRIS='#5F5E5A'
PALETA=['#185FA5','#D85A30','#3B6D11','#534AB7','#854F0B']
os.makedirs('Visualizaciones', exist_ok=True)

def estilo(ax):
    ax.set_facecolor(FONDO); ax.tick_params(colors=GRIS,labelsize=9)
    ax.grid(color='#D3D1C7',linestyle='--',linewidth=0.6,alpha=0.7)
    for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)

# ── 1. CARGA Y PREPARACIÓN ────────────────────────────────────────────────────
df = pd.read_csv('Datos/airbnb_limpio.csv')
print(f"Dataset cargado: {len(df):,} registros")

# Encoding de variables categóricas
le_ng = LabelEncoder(); le_rt = LabelEncoder()
df['ng_enc'] = le_ng.fit_transform(df['neighbourhood_group'])
df['rt_enc'] = le_rt.fit_transform(df['room_type'])
print(f"Borough encoding: {dict(zip(le_ng.classes_, le_ng.transform(le_ng.classes_)))}")
print(f"Room type encoding: {dict(zip(le_rt.classes_, le_rt.transform(le_rt.classes_)))}")

# ── 2. IDENTIFICACIÓN DE VARIABLES ───────────────────────────────────────────
# Variable dependiente (y):    price — precio por noche en USD
# Variables independientes (X): borough, room_type, minimum_nights,
#                                number_of_reviews, reviews_per_month,
#                                host_listings_count, availability_365
features = ['ng_enc','rt_enc','minimum_nights','number_of_reviews',
            'reviews_per_month','calculated_host_listings_count','availability_365']
X = df[features]; y = df['price']

# ── 3. ANÁLISIS DE MULTICOLINEALIDAD — VIF ────────────────────────────────────
vif_df = pd.DataFrame({'Variable': features,
    'VIF': [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]})
print(f"\nVIF (>10 indica multicolinealidad severa):\n{vif_df.to_string(index=False)}")
# Todos los VIF < 5: no hay multicolinealidad problemática

# ── 4. PAIRPLOT — ANÁLISIS DE CORRELACIÓN ─────────────────────────────────────
pairplot_df = df[['price','minimum_nights','number_of_reviews','availability_365']].sample(800,random_state=42)
g = sns.pairplot(pairplot_df, plot_kws={'alpha':0.3,'s':10,'color':AZUL},
                 diag_kws={'color':AZUL,'alpha':0.7})
g.figure.suptitle('Pairplot — Variables del Modelo Airbnb NYC', y=1.02,
                   fontsize=13, fontweight='bold', color='#2C2C2A')
g.figure.patch.set_facecolor(FONDO)
plt.savefig('Visualizaciones/pairplot_final.png',dpi=150,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("\npairplot_final.png ✓")

print(f"\nCorrelaciones con precio:\n{df[features+['price']].corr()['price'].drop('price').sort_values().round(4)}")

# ── 5. DIVISIÓN DE DATOS ──────────────────────────────────────────────────────
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(f"\nEntrenamiento: {len(X_train):,} | Prueba: {len(X_test):,}")

# ── 6. CONSTRUCCIÓN Y ENTRENAMIENTO ───────────────────────────────────────────
modelo = LinearRegression()
modelo.fit(X_train, y_train)
print(f"\nModelo entrenado.")
print(f"Intercepto: {modelo.intercept_:.2f}")
for f,c in zip(features,modelo.coef_):
    print(f"  {f}: {c:.4f}")

# ── 7. EVALUACIÓN ─────────────────────────────────────────────────────────────
y_pred = modelo.predict(X_test)
r2     = r2_score(y_test, y_pred)
n,k    = len(X_test), len(features)
r2_adj = 1 - (1-r2)*(n-1)/(n-k-1)
mae    = mean_absolute_error(y_test, y_pred)
mse    = mean_squared_error(y_test, y_pred)
rmse   = np.sqrt(mse)

print(f"\n=== MÉTRICAS DE EVALUACIÓN ===")
print(f"R²         = {r2:.4f}  → explica el {r2*100:.1f}% de la varianza en precio")
print(f"R² ajustado= {r2_adj:.4f}")
print(f"MAE        = ${mae:.2f}")
print(f"MSE        = {mse:.2f}")
print(f"RMSE       = ${rmse:.2f}")

# ── 8. PREDICCIONES ───────────────────────────────────────────────────────────
print(f"\n=== PREDICCIONES DE EJEMPLO ===")
ej = pd.DataFrame({'ng_enc':[4,0,2,1],'rt_enc':[0,1,0,2],
    'minimum_nights':[2,1,3,7],'number_of_reviews':[10,50,5,100],
    'reviews_per_month':[0.5,2.0,0.2,3.0],
    'calculated_host_listings_count':[1,2,1,5],'availability_365':[120,200,50,300]})
preds_ej = modelo.predict(ej)
for desc,p in zip(['Manhattan/Entire home','Brooklyn/Private room',
                    'Queens/Entire home','Bronx/Shared room'], preds_ej):
    print(f"  {desc}: ${p:.0f}/noche")

# ── 9. VISUALIZACIONES ────────────────────────────────────────────────────────
# G1: Distribución precio + por borough
fig,axes=plt.subplots(1,2,figsize=(14,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Distribución de Precios — Airbnb NYC',fontsize=14,fontweight='bold',color='#2C2C2A',y=1.02)
ax=axes[0]; estilo(ax)
ax.hist(df['price'],bins=40,color=AZUL,alpha=0.82,edgecolor='white',lw=0.4)
ax.axvline(df['price'].mean(),  color=NARANJA,lw=2,ls='--',label=f'Media: ${df["price"].mean():.0f}')
ax.axvline(df['price'].median(),color=VERDE,  lw=2,ls=':' ,label=f'Mediana: ${df["price"].median():.0f}')
ax.set_xlabel('Precio por noche (USD)',fontsize=11,color='#2C2C2A')
ax.set_ylabel('Frecuencia',fontsize=11,color='#2C2C2A')
ax.set_title('Histograma de Precio',fontsize=11,fontweight='500',color='#2C2C2A')
ax.legend(fontsize=9,framealpha=0.9,edgecolor='#D3D1C7')
ax=axes[1]; estilo(ax)
order_b=df.groupby('neighbourhood_group')['price'].median().sort_values(ascending=False)
bars=ax.bar(order_b.index,order_b.values,color=PALETA,alpha=0.85,edgecolor='white')
for bar,val in zip(bars,order_b.values):
    ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+1.5,f'${val:.0f}',
            ha='center',va='bottom',fontsize=9,fontweight='bold',color='#2C2C2A')
ax.set_xlabel('Borough',fontsize=11,color='#2C2C2A')
ax.set_ylabel('Precio mediano (USD)',fontsize=11,color='#2C2C2A')
ax.set_title('Precio Mediano por Borough',fontsize=11,fontweight='500',color='#2C2C2A')
ax.tick_params(axis='x',rotation=10)
plt.tight_layout()
plt.savefig('Visualizaciones/distribucion_precio.png',dpi=180,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("distribucion_precio.png ✓")

# G2: Real vs Predicho + Residuos
fig,axes=plt.subplots(1,2,figsize=(14,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Evaluación del Modelo — Predicciones vs Reales',fontsize=14,fontweight='bold',color='#2C2C2A',y=1.02)
ax=axes[0]; estilo(ax)
ax.scatter(y_test,y_pred,color=MORADO,alpha=0.35,s=12,edgecolors='none')
lims=[min(y_test.min(),y_pred.min())-10,max(y_test.max(),y_pred.max())+10]
ax.plot(lims,lims,color=NARANJA,lw=2,ls='--',label='Predicción perfecta')
ax.set_xlabel('Precio real (USD)',fontsize=11,color='#2C2C2A')
ax.set_ylabel('Precio predicho (USD)',fontsize=11,color='#2C2C2A')
ax.set_title('Real vs Predicho',fontsize=11,fontweight='500',color='#2C2C2A')
ax.legend(fontsize=9,framealpha=0.9,edgecolor='#D3D1C7')
ax.text(0.03,0.97,f'R² = {r2:.4f}\nRMSE = ${rmse:.1f}',
        transform=ax.transAxes,fontsize=10,color='#2C2C2A',va='top',
        bbox=dict(boxstyle='round,pad=0.4',facecolor='white',edgecolor='#D3D1C7',alpha=0.9))
ax=axes[1]; estilo(ax)
res=y_test.values-y_pred
ax.hist(res,bins=35,color=VERDE,alpha=0.82,edgecolor='white',lw=0.4)
ax.axvline(res.mean(),color=NARANJA,lw=2,ls='--',label=f'Media: {res.mean():.1f}')
ax.set_xlabel('Residuos (USD)',fontsize=11,color='#2C2C2A')
ax.set_ylabel('Frecuencia',fontsize=11,color='#2C2C2A')
ax.set_title('Distribución de Residuos',fontsize=11,fontweight='500',color='#2C2C2A')
ax.legend(fontsize=9,framealpha=0.9,edgecolor='#D3D1C7')
plt.tight_layout()
plt.savefig('Visualizaciones/predicciones_residuos.png',dpi=180,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("predicciones_residuos.png ✓")

# G3: Importancia de características
fig,ax=plt.subplots(figsize=(10,5)); fig.patch.set_facecolor(FONDO); ax.set_facecolor(FONDO)
labels_es=['Borough','Tipo habitación','Noches mín.','Núm. reseñas','Reseñas/mes','Listings host','Disponibilidad']
colors_c=[AZUL if c>0 else NARANJA for c in modelo.coef_]
bars_c=ax.barh(labels_es,modelo.coef_,color=colors_c,alpha=0.85,edgecolor='white',lw=0.5)
ax.axvline(0,color='#2C2C2A',lw=1.5,ls='--')
for bar,val in zip(bars_c,modelo.coef_):
    ax.text(val+(0.5 if val>=0 else -0.5),bar.get_y()+bar.get_height()/2,
            f'{val:.2f}',va='center',ha='left' if val>=0 else 'right',fontsize=9,color='#2C2C2A')
ax.set_xlabel('Coeficiente (impacto en precio USD)',fontsize=11,color='#2C2C2A')
ax.set_title('Importancia de Características — Coeficientes del Modelo',fontsize=12,fontweight='bold',color='#2C2C2A',pad=12)
ax.tick_params(colors=GRIS,labelsize=10)
ax.grid(axis='x',color='#D3D1C7',linestyle='--',linewidth=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
leg=[Patch(facecolor=AZUL,label='Efecto positivo en precio'),
     Patch(facecolor=NARANJA,label='Efecto negativo en precio')]
ax.legend(handles=leg,fontsize=9,framealpha=0.9,edgecolor='#D3D1C7')
plt.tight_layout()
plt.savefig('Visualizaciones/importancia_features.png',dpi=180,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("importancia_features.png ✓")

# G4: Boxplots
fig,axes=plt.subplots(1,2,figsize=(14,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Precio por Tipo de Habitación y Borough',fontsize=14,fontweight='bold',color='#2C2C2A',y=1.02)
ax=axes[0]; estilo(ax)
order_rt=df.groupby('room_type')['price'].median().sort_values(ascending=False).index
data_rt=[df[df['room_type']==rt]['price'].values for rt in order_rt]
bp=ax.boxplot(data_rt,patch_artist=True,widths=0.5,
              medianprops=dict(color='white',linewidth=2.5),
              whiskerprops=dict(color=GRIS,linewidth=1.2),
              capprops=dict(color=GRIS,linewidth=1.5),
              flierprops=dict(marker='o',markersize=2,alpha=0.3,linestyle='none'))
for patch,c in zip(bp['boxes'],[AZUL,NARANJA,VERDE]): patch.set_facecolor(c); patch.set_alpha(0.75)
ax.set_xticklabels(order_rt,fontsize=9); ax.set_ylabel('Precio/noche (USD)',fontsize=11,color='#2C2C2A')
ax.set_title('Por Tipo de Habitación',fontsize=11,fontweight='500',color='#2C2C2A')
ax=axes[1]; estilo(ax)
order_ng=df.groupby('neighbourhood_group')['price'].median().sort_values(ascending=False).index
data_ng=[df[df['neighbourhood_group']==ng]['price'].values for ng in order_ng]
bp2=ax.boxplot(data_ng,patch_artist=True,widths=0.5,
               medianprops=dict(color='white',linewidth=2.5),
               whiskerprops=dict(color=GRIS,linewidth=1.2),
               capprops=dict(color=GRIS,linewidth=1.5),
               flierprops=dict(marker='o',markersize=2,alpha=0.3,linestyle='none'))
for patch,c in zip(bp2['boxes'],PALETA): patch.set_facecolor(c); patch.set_alpha(0.75)
ax.set_xticklabels(order_ng,fontsize=8.5,rotation=12); ax.set_ylabel('Precio/noche (USD)',fontsize=11,color='#2C2C2A')
ax.set_title('Por Borough',fontsize=11,fontweight='500',color='#2C2C2A')
plt.tight_layout()
plt.savefig('Visualizaciones/boxplot_final.png',dpi=180,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("boxplot_final.png ✓")

# G5: Heatmap correlaciones
fig,ax=plt.subplots(figsize=(9,7)); fig.patch.set_facecolor(FONDO)
cols_hm=['price','minimum_nights','number_of_reviews','reviews_per_month',
         'calculated_host_listings_count','availability_365']
labels_hm=['Precio','Noches mín.','Núm. reseñas','Reseñas/mes','Listings host','Disponibilidad']
cm_hm=df[cols_hm].corr(); cm_hm.index=labels_hm; cm_hm.columns=labels_hm
cmap=sns.diverging_palette(230,20,as_cmap=True)
sns.heatmap(cm_hm,annot=True,fmt='.2f',cmap=cmap,center=0,vmin=-1,vmax=1,
            square=True,linewidths=0.5,linecolor='#F1EFE8',
            annot_kws={'size':10,'weight':'500'},ax=ax,cbar_kws={'shrink':0.8})
ax.set_title('Mapa de Calor de Correlaciones',fontsize=13,fontweight='bold',color='#2C2C2A',pad=14)
ax.tick_params(colors='#2C2C2A',labelsize=9.5)
plt.tight_layout()
plt.savefig('Visualizaciones/heatmap_final.png',dpi=180,bbox_inches='tight',facecolor=FONDO)
plt.close(); print("heatmap_final.png ✓")

print(f"\nAnálisis completo.")
print(f"R²={r2:.4f} | R²adj={r2_adj:.4f} | MAE=${mae:.2f} | RMSE=${rmse:.2f} | MSE={mse:.2f}")
