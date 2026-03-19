# Semana 1: Fundamentos de Ciencia de Datos y Big Data

**Fecha:** 19/03/2025
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Temas cubiertos:** T1 (Fundamentos de Ciencia de Datos), T2 (Big Data)

---

## 1. Ejercicios Complementarios

### Ejercicio 1: Operaciones Algebraicas Básicas

**Solución:**

**a) 3x + 5 = 17**
```
3x = 17 - 5
3x = 12
x = 12 / 3
x = 4
```
**Resultado:** x = 4

**b) 2y - 8 = 22**
```
2y = 22 + 8
2y = 30
y = 30 / 2
y = 15
```
**Resultado:** y = 15

**c) 4z + 3 = 3z + 10**
```
4z - 3z = 10 - 3
z = 7
```
**Resultado:** z = 7

**d) 5(x + 2) = 35**
```
5x + 10 = 35
5x = 35 - 10
5x = 25
x = 25 / 5
x = 5
```
**Resultado:** x = 5

---

### Ejercicio 2: Funciones Lineales

Dada la función **f(x) = 2x + 3**:

| x    | f(x) = 2x + 3 | Resultado |
|------|----------------|-----------|
| f(0) | 2(0) + 3       | **3**     |
| f(1) | 2(1) + 3       | **5**     |
| f(5) | 2(5) + 3       | **13**    |
| f(10)| 2(10) + 3      | **23**    |

**Análisis de la función:**
- **Pendiente (m):** 2 → por cada unidad que aumenta x, f(x) sube 2 unidades.
- **Ordenada al origen (b):** 3 → la función corta el eje Y en el punto (0, 3).
- La función es **creciente** (pendiente positiva).

---

### Ejercicio 3: Escalas y Volúmenes (Big Data)

| Cantidad                        | Valor numérico      | Notación Científica | Equivalencia  |
|---------------------------------|---------------------|----------------------|---------------|
| 1,000,000 bytes                 | 1,000,000           | **1 × 10⁶**         | 1 Megabyte    |
| 1,000,000,000 registros         | 1,000,000,000       | **1 × 10⁹**         | 1 Gigaregistro|
| 1,000,000,000,000 bytes         | 1,000,000,000,000   | **1 × 10¹²**        | 1 Terabyte    |

**Referencias de escala:**
- 10³ = Kilo (KB)
- 10⁶ = Mega (MB)
- 10⁹ = Giga (GB)
- 10¹² = Tera (TB)
- 10¹⁵ = Peta (PB)
- 10¹⁸ = Exa (EB)

---

### Ejercicio 4: Diagramas de Flujo (Pseudocódigo)

**a) Determinar si un número es par o impar:**
```
INICIO
  LEER numero
  SI (numero MOD 2 == 0) ENTONCES
    IMPRIMIR "El número es par"
  SINO
    IMPRIMIR "El número es impar"
  FIN SI
FIN
```

**b) Calcular el promedio de 3 números:**
```
INICIO
  LEER a, b, c
  promedio = (a + b + c) / 3
  IMPRIMIR "El promedio es: " + promedio
FIN
```

**c) Encontrar el mayor de 4 números:**
```
INICIO
  LEER a, b, c, d
  mayor = a
  SI (b > mayor) ENTONCES mayor = b
  SI (c > mayor) ENTONCES mayor = c
  SI (d > mayor) ENTONCES mayor = d
  IMPRIMIR "El mayor es: " + mayor
FIN
```

---

### Ejercicio 5: Pseudocódigo

**a) Calcular el factorial de un número:**
```
INICIO
  LEER n
  factorial = 1
  PARA i = 1 HASTA n HACER
    factorial = factorial * i
  FIN PARA
  IMPRIMIR "Factorial de " + n + " = " + factorial
FIN
```

**b) Buscar un elemento en una lista:**
```
INICIO
  LEER lista[], elemento_buscado
  encontrado = FALSO
  PARA i = 0 HASTA longitud(lista)-1 HACER
    SI lista[i] == elemento_buscado ENTONCES
      encontrado = VERDADERO
      IMPRIMIR "Encontrado en posición " + i
    FIN SI
  FIN PARA
  SI NO encontrado ENTONCES
    IMPRIMIR "Elemento no encontrado"
FIN
```

**c) Ordenar una lista de números (Burbuja):**
```
INICIO
  LEER lista[]
  n = longitud(lista)
  PARA i = 0 HASTA n-2 HACER
    PARA j = 0 HASTA n-i-2 HACER
      SI lista[j] > lista[j+1] ENTONCES
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
      FIN SI
    FIN PARA
  FIN PARA
  IMPRIMIR lista
FIN
```

---

### Ejercicio 6: Operaciones Booleanas

```python
a = True
b = False
c = True

print(a and b)       # False  → True AND False = False
print(a or b)        # True   → True OR False  = True
print(not b)         # True   → NOT False      = True
print(a and c)       # True   → True AND True  = True
print((a or b) and c) # True  → (True OR False) AND True = True AND True = True
```

| Expresión         | Resultado |
|-------------------|-----------|
| `a and b`         | **False** |
| `a or b`          | **True**  |
| `not b`           | **True**  |
| `a and c`         | **True**  |
| `(a or b) and c`  | **True**  |

---

### Ejercicio 7: Historia de la Ciencia de Datos

**1. ¿Quién es considerada la primera científica de datos?**

Florence Nightingale (1820-1910) es considerada por muchos la primera científica de datos. Fue pionera en el uso de estadísticas y visualizaciones de datos para mejorar la atención médica durante la Guerra de Crimea. Su famoso "diagrama de área polar" demostró que la mayoría de las muertes soldados no eran por combate sino por enfermedades prevenibles, usando datos para impulsar decisiones y cambios en políticas sanitarias.

**2. ¿Qué es el "Data Science Venn Diagram" de Drew Conway?**

El Diagrama de Venn de Drew Conway (2010) representa la intersección de tres áreas del conocimiento necesarias para la ciencia de datos:
- **Habilidades matemáticas y estadísticas:** capacidad de modelar y analizar datos.
- **Conocimiento de dominio (expertise):** entendimiento profundo del área de negocio o campo de aplicación.
- **Habilidades de programación (hacking skills):** capacidad de recolectar, procesar y manipular datos con código.

La intersección de las tres áreas define al Científico de Datos. Conway argumentó que sin las tres, solo se tienen capacidades parciales (por ejemplo, estadística + dominio sin programación = "investigación tradicional"; programación + estadística sin dominio = "zona de peligro").

**3. Tres herramientas modernas de Big Data:**
- **Apache Spark:** motor de procesamiento distribuido para análisis de grandes volúmenes de datos en tiempo real y por lotes.
- **Apache Kafka:** plataforma de streaming de datos en tiempo real, muy usada para pipelines de datos.
- **Hadoop (HDFS + MapReduce):** framework para almacenamiento distribuido y procesamiento paralelo de grandes datasets.

---

### Ejercicio 8: Aplicaciones de Big Data

**Salud — Detección temprana de enfermedades:**
IBM Watson Health analiza millones de registros médicos, imágenes clínicas y literatura científica para ayudar a diagnosticar enfermedades como el cáncer con mayor precisión. Los hospitales utilizan Big Data para predecir readmisiones de pacientes y optimizar recursos.

**Finanzas — Detección de fraude:**
Visa y Mastercard procesan miles de transacciones por segundo usando algoritmos de Machine Learning entrenados con Big Data para detectar patrones de fraude en tiempo real, bloqueando transacciones sospechosas antes de que se completen.

**Redes sociales — Personalización de contenido:**
Meta (Facebook/Instagram) recopila y analiza petabytes de datos de interacción de sus usuarios (likes, tiempo de visualización, clics) para personalizar el feed de noticias y la publicidad, usando modelos predictivos entrenados con Big Data.

**Deportes — Análisis de rendimiento:**
La NBA y equipos como los Golden State Warriors utilizan sistemas de tracking con cámaras en los estadios que capturan millones de puntos de datos por partido (posición de jugadores, velocidad, trayectoria del balón). Estos datos se analizan para optimizar estrategias de juego, prevenir lesiones y evaluar jugadores.

---

## 2. Actividades Prácticas

### Actividad 1.0: Configuración de Git y Repositorio

**Descripción:** Configuración del entorno de trabajo con Git y GitHub.

**Pasos realizados:**

1. Cuenta creada en GitHub: `https://github.com/[mi_usuario]`
2. Repositorio creado: `CienciaDeDatos` (público)
3. Estructura de carpetas creada localmente según la plantilla del curso.
4. Repositorio inicializado con `git init`.
5. README.md inicial creado con el progreso del curso.
6. Repositorio conectado a GitHub con `git remote add origin`.
7. Primer commit realizado: "Initial commit: Estructura inicial del repositorio".

**Comandos utilizados:**
```bash
git init
git config --global user.name "Mi Nombre"
git config --global user.email "mi@email.com"
git remote add origin https://github.com/mi_usuario/CienciaDeDatos.git
git add .
git commit -m "Initial commit: Estructura inicial del repositorio"
git push -u origin main
```

**Entregable:** Repositorio creado, estructura local lista, primer commit documentado.

---

### Actividad 1.1: Investigación de Conceptos Fundamentales

**1. ¿Qué es la Ciencia de Datos y sus componentes principales?**

La ciencia de datos es una disciplina interdisciplinaria que combina matemáticas, estadística, programación y conocimiento del dominio para extraer conocimiento y valor a partir de datos estructurados y no estructurados. Sus componentes principales son:

- **Recolección de datos:** obtención de datos desde diversas fuentes (bases de datos, APIs, sensores, web scraping).
- **Limpieza y preparación de datos:** identificación y corrección de datos erróneos, faltantes o duplicados.
- **Análisis exploratorio (EDA):** comprensión inicial de los datos mediante estadísticas y visualizaciones.
- **Modelado predictivo:** aplicación de algoritmos de Machine Learning para predicción y clasificación.
- **Visualización e interpretación:** comunicación de los hallazgos de forma comprensible.
- **Toma de decisiones basada en datos:** uso de los insights para resolver problemas reales.

**2. Diferencia entre datos estructurados y no estructurados:**

| Tipo | Definición | Ejemplos |
|------|------------|---------|
| **Estructurados** | Datos organizados en un formato fijo, con filas y columnas. Fáciles de almacenar en bases de datos relacionales. | Tablas de Excel, bases de datos SQL, registros de ventas. |
| **No estructurados** | Datos sin un formato predefinido. Representan ~80% de los datos generados hoy. Requieren técnicas especiales para su análisis. | Textos, imágenes, videos, correos electrónicos, publicaciones en redes sociales. |
| **Semi-estructurados** | Tienen alguna organización pero no siguen un esquema rígido. | JSON, XML, HTML, correos con metadatos. |

**3. Las 5 V del Big Data (con ejemplos):**

| V | Definición | Ejemplo |
|---|------------|---------|
| **Volumen** | Cantidad masiva de datos generados y almacenados. | Facebook genera ~4 petabytes de datos por día. |
| **Velocidad** | Rapidez con la que se generan y procesan los datos. | Las transacciones de bolsa de valores ocurren en microsegundos. |
| **Variedad** | Diversidad de tipos y formatos de datos. | Una empresa recopila datos de formularios (estructurado), chats (texto), fotos (imágenes) y GPS (señales). |
| **Veracidad** | Confiabilidad, calidad y exactitud de los datos. | Datos de redes sociales con errores ortográficos, duplicados o información falsa. |
| **Valor** | Utilidad real que se puede extraer de los datos. | Amazon analiza el historial de compras para recomendar productos y aumentar ventas. |

**4. Perfiles profesionales en Ciencia de Datos:**

- **Científico de Datos (Data Scientist):** diseña modelos predictivos y algoritmos de ML.
- **Ingeniero de Datos (Data Engineer):** construye y mantiene pipelines de datos e infraestructura.
- **Analista de Datos (Data Analyst):** analiza datos y genera reportes para toma de decisiones.
- **Arquitecto de Datos (Data Architect):** diseña la estructura y arquitectura de los sistemas de datos.
- **Ingeniero de ML (ML Engineer):** pone en producción los modelos desarrollados por el Data Scientist.
- **Especialista en BI (Business Intelligence):** crea dashboards y reportes para el negocio.

---

### Actividad 1.2: Análisis de Casos de Uso

**Netflix:**
- **Datos recopilados:** historial de visualización, tiempo de pausa, calificaciones, búsquedas, dispositivo usado, hora de visualización.
- **Técnicas utilizadas:** filtrado colaborativo, algoritmos de recomendación, A/B testing, análisis de retención.
- **Problema resuelto:** personalización del catálogo para cada usuario, reduciendo el tiempo de búsqueda y aumentando el tiempo de visualización. Se estima que su motor de recomendación ahorra ~1 billón de dólares al año en retención de clientes.

**Amazon:**
- **Datos recopilados:** historial de compras, búsquedas, listas de deseos, tiempo en página, reseñas, datos de envío.
- **Técnicas utilizadas:** filtrado colaborativo y basado en contenido, análisis de precios dinámicos, predicción de demanda.
- **Problema resuelto:** sistema de recomendación "los clientes también compraron", optimización de inventario y precios en tiempo real, predicción de qué productos almacenar en qué bodega.

**Spotify:**
- **Datos recopilados:** canciones escuchadas, listas creadas, tiempo de escucha, géneros favoritos, hora del día, ubicación geográfica.
- **Técnicas utilizadas:** procesamiento de audio con ML, NLP para análisis de letras, grafos de usuarios.
- **Problema resuelto:** playlists personalizadas como "Discover Weekly", predicción de canciones que el usuario querrá escuchar, identificación de nuevos artistas con potencial de éxito.

---

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

---

### Actividad 1.4: Exploración de Fuentes de Datos

**¿Qué es Kaggle?**

Kaggle es la plataforma de ciencia de datos más grande del mundo, propiedad de Google. Ofrece miles de datasets públicos y gratuitos, competencias de ML con premios en efectivo, notebooks Jupyter gratuitos en la nube (con GPU), y una comunidad activa de más de 10 millones de usuarios.

**3 Datasets explorados:**

1. **Titanic - Machine Learning from Disaster**
   - Contiene datos de 891 pasajeros: nombre, edad, género, clase, tarifa, si sobrevivió.
   - Tipo de datos: estructurado (CSV).
   - Preguntas posibles: ¿Qué características predijeron mejor la supervivencia? ¿Hubo sesgo de género/clase?

2. **House Prices: Advanced Regression Techniques**
   - Contiene 79 variables de casas en Iowa: tamaño, año de construcción, número de habitaciones, calidad, precio de venta.
   - Tipo de datos: estructurado (CSV).
   - Preguntas posibles: ¿Qué variables influyen más en el precio? ¿Se puede predecir el precio de una casa nueva?

3. **COVID-19 World Vaccination Progress**
   - Datos de vacunación por país: dosis administradas, población vacunada, tipo de vacuna, fechas.
   - Tipo de datos: estructurado (CSV), actualizado regularmente.
   - Preguntas posibles: ¿Qué países tuvieron mayor ritmo de vacunación? ¿Existe correlación entre vacunación y mortalidad?

**Dataset elegido para el curso:** House Prices
- Contiene 1,460 registros de casas con 79 variables descriptivas.
- Podría responder preguntas como: predecir el precio de venta, identificar qué renovaciones agregan más valor, analizar tendencias del mercado inmobiliario.

---

## 3. Actividad Evaluable — Caso DeportivaMX

### Punto 1: Perfiles de Ciencia de Datos

Para resolver los desafíos de DeportivaMX, se recomienda contratar los siguientes perfiles:

**a) Ingeniero de Datos (Data Engineer)**
*Justificación:* Es el perfil más urgente. DeportivaMX tiene un crecimiento acelerado de registros de ventas y actualmente no cuenta con infraestructura adecuada. El Ingeniero de Datos será responsable de diseñar, construir y mantener los pipelines que integren los datos de ventas, clientes y productos desde múltiples fuentes hacia un almacén centralizado. Sin este perfil, los datos no llegarán limpios ni a tiempo al resto del equipo.

**b) Científico de Datos (Data Scientist)**
*Justificación:* Una vez que los datos estén disponibles y estructurados, se necesita un profesional que construya modelos predictivos para anticipar el comportamiento de los clientes: qué productos comprarán, cuándo volverán a comprar, qué promociones serán más efectivas. El Científico de Datos también diseñará sistemas de recomendación personalizados que mejoren directamente la experiencia del cliente, que es el objetivo principal de DeportivaMX.

**c) Analista de Datos (Data Analyst)**
*Justificación:* Este perfil traducirá los datos en insights comprensibles para la dirección y los equipos de negocio. Se encargará de generar dashboards y reportes sobre tendencias de ventas, desempeño por categoría de producto, comportamiento geográfico de clientes y KPIs de la tienda en línea. Es el puente entre el mundo técnico y las decisiones del negocio.

**d) Arquitecto de Datos (Data Architect)**
*Justificación:* Con el objetivo de implementar arquitecturas escalables y seguras, se necesita un arquitecto que diseñe la estructura general del ecosistema de datos: cómo se almacenarán los datos, qué herramientas usarán, cómo se garantizará la seguridad y la escalabilidad a medida que la empresa crezca. Este perfil tomará decisiones estratégicas como la selección del tipo de base de datos NoSQL más adecuado para cada caso.

---

### Punto 2: Las 5 V del Big Data aplicadas a DeportivaMX

**1. Volumen**
DeportivaMX, al ser una tienda en línea en crecimiento acelerado, genera constantemente grandes cantidades de datos: registros de ventas, clics de usuarios, historial de navegación, datos de clientes, inventarios y características de productos. A medida que escale, estos volúmenes podrían alcanzar millones de registros diarios, superando la capacidad de bases de datos relacionales tradicionales.

**2. Velocidad**
Las ventas en línea se generan en tiempo real, las 24 horas del día. Cada transacción completada, cada producto visto, cada carrito abandonado genera un evento de dato inmediato. DeportivaMX necesita procesar estos datos casi en tiempo real para tomar decisiones oportunas: ajustar precios, detectar problemas en el proceso de compra o activar notificaciones de stock bajo.

**3. Variedad**
Los datos de DeportivaMX provienen de múltiples fuentes y formatos:
- **Estructurados:** registros de ventas, tablas de inventario, datos de clientes.
- **No estructurados:** reseñas y comentarios de productos (texto), fotos de productos (imágenes), videos de unboxing.
- **Semi-estructurados:** logs del servidor web, datos de APIs de pago (JSON), datos de rastreo de envíos.

**4. Veracidad**
La calidad de los datos es un desafío crítico para DeportivaMX. Los clientes pueden registrar datos incorrectos (direcciones erróneas, correos duplicados), pueden existir duplicados de productos en el catálogo, o registros de ventas con errores. Si la empresa toma decisiones basadas en datos de baja calidad, las conclusiones serán incorrectas. Por eso, los procesos de limpieza y validación de datos son fundamentales.

**5. Valor**
El objetivo final no es acumular datos, sino extraer valor de ellos. Para DeportivaMX, el valor se traduce en: identificar qué productos tienen mayor demanda por temporada, qué clientes tienen mayor probabilidad de recompra, qué regiones del país muestran mayor crecimiento, y cómo personalizar las recomendaciones para incrementar el ticket promedio. Los datos, correctamente analizados, se convierten en ventaja competitiva directa.

---

### Punto 3: Arquitectura de Almacenamiento

**Arquitectura recomendada: Arquitectura Lambda**

Se recomienda implementar una **Arquitectura Lambda** combinada con un **Data Lake** como capa base. Esta arquitectura fue diseñada precisamente para empresas que necesitan procesar tanto datos históricos en lote como eventos en tiempo real.

**Justificación:**
- **Capa de velocidad (Speed Layer):** procesará los eventos de venta y comportamiento del usuario en tiempo real usando herramientas como Apache Kafka y Apache Spark Streaming. Esto permitirá a DeportivaMX reaccionar de forma inmediata a eventos (stock agotado, promociones activas, fraudes).
- **Capa de lote (Batch Layer):** procesará el historial completo de datos periódicamente para entrenar modelos predictivos, generar reportes consolidados y análisis de tendencias de largo plazo.
- **Capa de servicio (Serving Layer):** expone los resultados de ambas capas a las aplicaciones y dashboards de la empresa.

**Base de datos NoSQL recomendada: MongoDB**

Para el almacenamiento de datos no estructurados y semi-estructurados de DeportivaMX, MongoDB es la solución más adecuada por las siguientes razones:

- **Esquema flexible:** los productos deportivos de DeportivaMX tienen atributos muy distintos entre categorías. Una bicicleta tiene atributos completamente diferentes a una raqueta de tenis. MongoDB permite almacenar cada documento con su propio esquema, sin necesidad de alterar una tabla entera cuando se agrega un nuevo atributo.
- **Escalabilidad horizontal:** MongoDB escala fácilmente distribuyendo datos en múltiples servidores (sharding), lo que es fundamental para soportar el crecimiento acelerado de la empresa.
- **Alto rendimiento en lecturas:** el modelo de documentos JSON permite recuperar toda la información de un pedido o un cliente en una sola consulta, sin necesidad de JOINs complejos.
- **Soporte nativo para datos geoespaciales:** útil para analizar la distribución geográfica de clientes y optimizar logística de envíos.

---

### Punto 4: Diseño de Colecciones en JSON para MongoDB

```json
[
  {
    "coleccion": "clientes",
    "descripcion": "Información personal y de contacto de los clientes registrados",
    "ejemplo_documento": {
      "_id": "ObjectId('64a1b2c3d4e5f6789012abcd')",
      "nombre": "Carlos Ramírez",
      "email": "carlos.ramirez@email.com",
      "telefono": "+52 442 123 4567",
      "fecha_registro": "2024-03-15T10:30:00Z",
      "direcciones": [
        {
          "tipo": "envio",
          "calle": "Av. Constituyentes 500",
          "colonia": "Constituyentes",
          "ciudad": "Querétaro",
          "estado": "Querétaro",
          "cp": "76150",
          "es_predeterminada": true
        }
      ],
      "preferencias": {
        "categorias_favoritas": ["running", "ciclismo"],
        "talla_ropa": "M",
        "talla_calzado": 27
      },
      "historial_compras": ["ObjectId('...orden1')", "ObjectId('...orden2')"],
      "activo": true
    }
  },
  {
    "coleccion": "productos",
    "descripcion": "Catálogo de artículos deportivos con atributos variables por categoría",
    "ejemplo_documento": {
      "_id": "ObjectId('64a1b2c3d4e5f6789012efgh')",
      "nombre": "Tenis Running Pro X3",
      "sku": "TEN-RUN-PRO-X3-42",
      "categoria": "calzado",
      "subcategoria": "running",
      "marca": "SportMax",
      "precio": 1899.00,
      "precio_descuento": 1599.00,
      "moneda": "MXN",
      "stock": 45,
      "descripcion": "Tenis de alto rendimiento para corredores de largas distancias.",
      "atributos_especificos": {
        "talla": 42,
        "color": "azul/blanco",
        "material_suela": "goma de alto rendimiento",
        "drop_mm": 8,
        "peso_gr": 280,
        "tipo_pisada": "neutra"
      },
      "imagenes": [
        "https://cdn.deportivamx.mx/prod/ten-run-pro-x3-1.jpg",
        "https://cdn.deportivamx.mx/prod/ten-run-pro-x3-2.jpg"
      ],
      "calificacion_promedio": 4.7,
      "total_resenas": 128,
      "fecha_alta": "2024-01-10T00:00:00Z",
      "activo": true
    }
  },
  {
    "coleccion": "ordenes",
    "descripcion": "Registro de todas las ventas realizadas en la plataforma",
    "ejemplo_documento": {
      "_id": "ObjectId('64a1b2c3d4e5f6789012ijkl')",
      "numero_orden": "ORD-2024-00842",
      "cliente_id": "ObjectId('64a1b2c3d4e5f6789012abcd')",
      "fecha_orden": "2024-03-19T14:22:00Z",
      "estado": "enviado",
      "productos": [
        {
          "producto_id": "ObjectId('64a1b2c3d4e5f6789012efgh')",
          "nombre": "Tenis Running Pro X3",
          "sku": "TEN-RUN-PRO-X3-42",
          "cantidad": 1,
          "precio_unitario": 1599.00,
          "subtotal": 1599.00
        },
        {
          "producto_id": "ObjectId('...')",
          "nombre": "Calcetines Técnicos Running (par)",
          "sku": "CAL-TEC-RUN-M",
          "cantidad": 2,
          "precio_unitario": 149.00,
          "subtotal": 298.00
        }
      ],
      "resumen_precio": {
        "subtotal": 1897.00,
        "descuento_aplicado": 0.00,
        "costo_envio": 99.00,
        "impuestos": 318.72,
        "total": 2314.72,
        "moneda": "MXN"
      },
      "metodo_pago": {
        "tipo": "tarjeta_credito",
        "ultimos_digitos": "4521",
        "banco": "BBVA"
      },
      "direccion_envio": {
        "calle": "Av. Constituyentes 500",
        "colonia": "Constituyentes",
        "ciudad": "Querétaro",
        "estado": "Querétaro",
        "cp": "76150"
      },
      "seguimiento": {
        "numero_guia": "ESTAFETA-98765432",
        "paqueteria": "Estafeta",
        "fecha_estimada_entrega": "2024-03-22",
        "historial_estatus": [
          { "estatus": "confirmado", "fecha": "2024-03-19T14:25:00Z" },
          { "estatus": "preparando", "fecha": "2024-03-19T16:00:00Z" },
          { "estatus": "enviado", "fecha": "2024-03-20T09:15:00Z" }
        ]
      }
    }
  },
  {
    "coleccion": "resenas",
    "descripcion": "Opiniones y calificaciones de clientes sobre productos comprados",
    "ejemplo_documento": {
      "_id": "ObjectId('64a1b2c3d4e5f6789012mnop')",
      "producto_id": "ObjectId('64a1b2c3d4e5f6789012efgh')",
      "cliente_id": "ObjectId('64a1b2c3d4e5f6789012abcd')",
      "orden_id": "ObjectId('64a1b2c3d4e5f6789012ijkl')",
      "calificacion": 5,
      "titulo": "Excelentes para correr largas distancias",
      "comentario": "Los usé en mi primer medio maratón y el soporte fue increíble. La suela agarra perfecto en asfalto. Totalmente recomendados.",
      "ventajas": ["comodidad", "durabilidad", "soporte"],
      "desventajas": [],
      "verificado_compra": true,
      "fecha_resena": "2024-03-25T18:45:00Z",
      "votos_utiles": 23,
      "imagenes_adjuntas": []
    }
  }
]
```

---

## 4. Resumen de Aprendizaje

- La ciencia de datos es una disciplina interdisciplinaria que requiere combinar estadística, programación y conocimiento del negocio para generar valor real.
- El Big Data no se define solo por el volumen de datos, sino por las 5 V: Volumen, Velocidad, Variedad, Veracidad y Valor.
- Las bases de datos NoSQL como MongoDB ofrecen flexibilidad de esquema y escalabilidad horizontal, lo que las hace ideales para escenarios de crecimiento acelerado como el de DeportivaMX.
- La arquitectura Lambda permite combinar procesamiento en tiempo real (streaming) con procesamiento histórico (batch), cubriendo las necesidades tanto operativas como analíticas.
- Git es una herramienta fundamental para el trabajo colaborativo y el versionado de código y documentos en ciencia de datos.
- Plataformas como Kaggle democratizan el acceso a datasets reales, permitiendo practicar con datos del mundo real desde el inicio del aprendizaje.

---

## 5. Dudas o Preguntas

- ¿En qué casos es preferible usar una arquitectura Kappa en lugar de Lambda para el procesamiento de datos?
- ¿Cómo se manejan las transacciones ACID en MongoDB cuando se necesita consistencia fuerte entre colecciones?

---

## 6. Commits Realizados

```
Initial commit: Estructura inicial del repositorio
Semana1: Actividad 1.1 - Conceptos fundamentales
Semana1: Actividad 1.2 - Casos de uso
Semana1: Actividad 1.3 - Entorno de trabajo
Semana1: Actividad 1.4 - Fuentes de datos
Semana1: Actividad evaluable - Caso DeportivaMX
Semana1: Consolidado completo
```

---

## 7. Referencias

- Conway, D. (2010). *The Data Science Venn Diagram.* drewconway.com
- Marz, N. & Warren, J. (2015). *Big Data: Principles and best practices of scalable realtime data systems.* Manning Publications.
- MongoDB Inc. (2024). *MongoDB Documentation.* https://www.mongodb.com/docs/
- Apache Software Foundation. (2024). *Apache Spark Documentation.* https://spark.apache.org/docs/
- Kaggle. (2024). *Datasets.* https://www.kaggle.com/datasets
- IBM Cloud Education. (2024). *What is Big Data?* https://www.ibm.com/cloud/learn/big-data
- Pandas Development Team. (2024). *Pandas Documentation.* https://pandas.pydata.org/docs/
