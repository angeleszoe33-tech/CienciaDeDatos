### Actividad 1.3: Configuración del Entorno de Trabajo

**Instalación de Python y librerías:**

```bash
# Verificar instalación de Python
python --version  # Python 3.11.x

# Instalar librerías con pip
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

**Script de verificación:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", plt.matplotlib.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Todas las librerías instaladas correctamente.")
```

**Ejemplo básico de carga de datos en Jupyter:**
```python
import pandas as pd

# Carga de un dataset de ejemplo
df = pd.read_csv('datos_ejemplo.csv')
print(df.head())
print(df.info())
print(df.describe())
```

**Entregable:** Entorno configurado, librerías verificadas.
