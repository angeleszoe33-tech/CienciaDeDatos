# ============================================================================
# ACTIVIDAD 4 — PARTE 2: Regresión Logística Binaria
# Análisis de supervivencia — Titanic
# Curso: QR.LSTI2309TEO — Universidad Tecmilenio
# Autor: Zoe Ángeles | Fecha: 26/04/2026
# Temas: T11 (Análisis preliminar), T12 (Regresión logística)
# ============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,
                              classification_report, roc_auc_score, roc_curve)
from scipy import stats
import os, warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

FONDO='#FAFAFA'; AZUL='#185FA5'; NARANJA='#D85A30'; VERDE='#3B6D11'; GRIS='#5F5E5A'

# ── 1. CARGA DE DATOS ─────────────────────────────────────────────────────────
# Fuente: OpenML Titanic — https://www.openml.org/data/get_csv/16826755/phpMYEkMl
df = pd.read_csv('Datos/titanic.csv')
print(f"Dataset cargado: {df.shape}")
print(f"\nNulos:\n{df.isnull().sum()}")

# ── 2. LIMPIEZA ───────────────────────────────────────────────────────────────
# Eliminar columnas no necesarias para el análisis
df = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
# Imputar nulos
df['Age']      = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(f"\nNulos post-limpieza: {df.isnull().sum().sum()}")

# ── 3. CONVERSIÓN DE TIPOS ────────────────────────────────────────────────────
df['Pclass']   = df['Pclass'].astype('category')
df['Sex']      = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
print(f"\nTipos de datos:\n{df.dtypes}")

# Encoding para el modelo
df['Sex_enc']    = (df['Sex'] == 'female').astype(int)  # female=1, male=0
df['Pclass_enc'] = df['Pclass'].astype(int)
print(f"\nDistribución Survived: {df['Survived'].value_counts().to_dict()}")

# ── 4. VISUALIZACIÓN DE DATOS ─────────────────────────────────────────────────
os.makedirs('Visualizaciones', exist_ok=True)

fig, axes = plt.subplots(1,2, figsize=(13,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Análisis de Supervivencia — Titanic', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; ax.set_facecolor(FONDO)
surv_sex = df.groupby('Sex')['Survived'].mean()
bars = ax.bar(surv_sex.index, surv_sex.values*100, color=[AZUL,NARANJA], alpha=0.85, edgecolor='white')
for bar, val in zip(bars, surv_sex.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f'{val*100:.1f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_ylabel('Tasa de supervivencia (%)'); ax.set_title('Supervivencia por Sexo', fontweight='500')
ax.set_ylim(0,100); ax.tick_params(colors=GRIS, labelsize=9)
ax.grid(axis='y',color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
ax = axes[1]; ax.set_facecolor(FONDO)
surv_cl = df.groupby('Pclass')['Survived'].mean()
bars2 = ax.bar(['1ª Clase','2ª Clase','3ª Clase'], surv_cl.values*100,
               color=[AZUL,VERDE,NARANJA], alpha=0.85, edgecolor='white')
for bar, val in zip(bars2, surv_cl.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1, f'{val*100:.1f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_ylabel('Tasa de supervivencia (%)'); ax.set_title('Supervivencia por Clase', fontweight='500')
ax.set_ylim(0,100); ax.tick_params(colors=GRIS, labelsize=9)
ax.grid(axis='y',color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
plt.tight_layout()
plt.savefig('Visualizaciones/titanic_barras.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("titanic_barras.png ✓")

# ── 5. PRUEBA T-TEST ──────────────────────────────────────────────────────────
age_surv   = df[df['Survived']==1]['Age']
age_nosurv = df[df['Survived']==0]['Age']
t_stat, p_val = stats.ttest_ind(age_surv, age_nosurv)
print(f"\n=== T-TEST: Edad por supervivencia ===")
print(f"Media sobrevivientes:    {age_surv.mean():.2f} años")
print(f"Media no sobrevivientes: {age_nosurv.mean():.2f} años")
print(f"t = {t_stat:.4f} | p = {p_val:.6f}")
print(f"Conclusión: {'Diferencia significativa' if p_val<0.05 else 'Sin diferencia significativa'} (α=0.05)")

# ── 6. DIVISIÓN DE DATOS ──────────────────────────────────────────────────────
features = ['Pclass_enc','Sex_enc','Age','SibSp','Parch','Fare']
X = df[features]; y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nEntrenamiento: {len(X_train)} | Prueba: {len(X_test)}")

# ── 7. CREACIÓN DEL MODELO ────────────────────────────────────────────────────
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# ── 8. COEFICIENTES Y ODDS RATIO ─────────────────────────────────────────────
y_pred      = modelo.predict(X_test)
y_pred_prob = modelo.predict_proba(X_test)[:,1]
acc  = accuracy_score(y_test, y_pred)
auc  = roc_auc_score(y_test, y_pred_prob)
cm   = confusion_matrix(y_test, y_pred)

coefs_df = pd.DataFrame({
    'Variable':    features,
    'Coeficiente': modelo.coef_[0].round(4),
    'Odds Ratio':  np.exp(modelo.coef_[0]).round(4)
})
print(f"\nAccuracy: {acc:.4f} | AUC-ROC: {auc:.4f}")
print(f"\nCoeficientes y Odds Ratio:\n{coefs_df.to_string(index=False)}")
print(f"\nMatriz de confusión:\n{cm}")
print(f"\n{classification_report(y_test, y_pred)}")

# Gráfica ROC + Odds Ratio
fig, axes = plt.subplots(1,2, figsize=(13,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Regresión Logística — Titanic', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
MORADO='#534AB7'
ax = axes[0]; ax.set_facecolor(FONDO)
vars_lbl = ['Clase','Sexo (fem.)','Edad','Hermanos/\nCónyuge','Padres/\nHijos','Tarifa']
OR_vals  = np.exp(modelo.coef_[0])
colors_or = [VERDE if v > 1 else NARANJA for v in OR_vals]
bars3 = ax.barh(vars_lbl, OR_vals, color=colors_or, alpha=0.85, edgecolor='white')
ax.axvline(1, color='#2C2C2A', lw=1.5, ls='--', label='OR=1 (sin efecto)')
for bar, val in zip(bars3, OR_vals):
    ax.text(val+0.05, bar.get_y()+bar.get_height()/2, f'{val:.3f}', va='center', fontsize=9)
ax.set_xlabel('Odds Ratio'); ax.set_title('Odds Ratio por Variable', fontweight='500')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.tick_params(colors=GRIS, labelsize=9); ax.grid(color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
ax = axes[1]; ax.set_facecolor(FONDO)
fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
ax.plot(fpr, tpr, color=AZUL, lw=2.5, label=f'AUC = {auc:.3f}')
ax.plot([0,1],[0,1], color=GRIS, lw=1.5, ls='--', label='Azar (AUC=0.5)')
ax.fill_between(fpr, tpr, alpha=0.12, color=AZUL)
ax.set_xlabel('Tasa de Falsos Positivos'); ax.set_ylabel('Tasa de Verdaderos Positivos')
ax.set_title('Curva ROC', fontweight='500')
ax.legend(fontsize=9.5, framealpha=0.9, edgecolor='#D3D1C7')
ax.tick_params(colors=GRIS, labelsize=9); ax.grid(color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
plt.tight_layout()
plt.savefig('Visualizaciones/logistica_roc.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("logistica_roc.png ✓")

# Distribución de edad + matriz de confusión
fig, axes = plt.subplots(1,2, figsize=(13,5)); fig.patch.set_facecolor(FONDO)
fig.suptitle('Edad y Matriz de Confusión', fontsize=14, fontweight='bold', color='#2C2C2A', y=1.02)
ax = axes[0]; ax.set_facecolor(FONDO)
ax.hist(age_nosurv, bins=25, color=NARANJA, alpha=0.7, label=f'No sobrevivió (μ={age_nosurv.mean():.1f})', edgecolor='white')
ax.hist(age_surv,   bins=25, color=AZUL,   alpha=0.7, label=f'Sobrevivió (μ={age_surv.mean():.1f})',    edgecolor='white')
ax.set_xlabel('Edad'); ax.set_ylabel('Frecuencia')
ax.set_title(f'Distribución de Edad\nt={t_stat:.3f}, p={p_val:.4f}', fontweight='500')
ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D3D1C7')
ax.tick_params(colors=GRIS, labelsize=9); ax.grid(axis='y',color='#D3D1C7',ls='--',lw=0.6,alpha=0.7)
for sp in ax.spines.values(): sp.set_edgecolor('#D3D1C7'); sp.set_linewidth(0.8)
ax = axes[1]; ax.set_facecolor(FONDO)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
            xticklabels=['No sobrevivió','Sobrevivió'],
            yticklabels=['No sobrevivió','Sobrevivió'],
            cbar_kws={'shrink':0.8}, linewidths=0.5, linecolor='white',
            annot_kws={'size':13,'weight':'bold'})
ax.set_xlabel('Predicho'); ax.set_ylabel('Real')
ax.set_title(f'Matriz de Confusión (Acc={acc:.3f})', fontweight='500')
ax.tick_params(colors='#2C2C2A', labelsize=9)
plt.tight_layout()
plt.savefig('Visualizaciones/titanic_confusion.png', dpi=180, bbox_inches='tight', facecolor=FONDO)
plt.close(); print("titanic_confusion.png ✓")
print("\nAnálisis completo.")
