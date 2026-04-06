# Semana 2: Arquitecturas de Datos y MongoDB

**Fecha:** 27/03/2025
**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Temas cubiertos:** T3 (Arquitecturas de almacenamiento), T4 (Bases de datos NoSQL), T5 (Operaciones CRUD con MongoDB)

---

## 1. Ejercicios Complementarios

### Ejercicio 1: Consultas Básicas SQL

Dada la tabla `empleados`:

**1. Seleccionar todos los empleados:**
```sql
SELECT * FROM empleados;
```

**2. Nombres y salarios de empleados de IT:**
```sql
SELECT nombre, salario
FROM empleados
WHERE departamento = 'IT';
```

**3. Empleado con mayor salario:**
```sql
SELECT nombre, salario
FROM empleados
ORDER BY salario DESC
LIMIT 1;
```

**4. Contar empleados por departamento:**
```sql
SELECT departamento, COUNT(*) AS total_empleados
FROM empleados
GROUP BY departamento;
```

**5. Actualizar el salario de María a 50000:**
```sql
UPDATE empleados
SET salario = 50000
WHERE nombre = 'María';
```

---

### Ejercicio 2: Joins SQL

**1. INNER JOIN entre empleados y departamentos:**
```sql
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.id_departamento = d.id;
```
*Resultado: muestra solo empleados que tienen un departamento asignado que existe en la tabla departamentos.*

**2. LEFT JOIN mostrando todos los empleados:**
```sql
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.id_departamento = d.id;
```
*Resultado: muestra todos los empleados, aunque no tengan departamento asignado (aparece NULL en ese caso).*

**3. Contar empleados por departamento:**
```sql
SELECT d.nombre AS departamento, COUNT(e.id) AS total_empleados
FROM departamentos d
LEFT JOIN empleados e ON d.id = e.id_departamento
GROUP BY d.nombre;
```

---

### Ejercicio 3: Manipulación de JSON

Dado el JSON de empleados:

**1. Extraer los nombres de todos los empleados:**
```python
import json

data = {
    "empleados": [
        {"id": 1, "nombre": "Juan",   "habilidades": ["Python", "SQL"]},
        {"id": 2, "nombre": "María",  "habilidades": ["Java", "MongoDB"]},
        {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
    ]
}

nombres = [emp["nombre"] for emp in data["empleados"]]
print(nombres)  # ['Juan', 'María', 'Carlos']
```

**2. Agregar una nueva habilidad a Juan:**
```python
data["empleados"][0]["habilidades"].append("Pandas")
print(data["empleados"][0]["habilidades"])  # ['Python', 'SQL', 'Pandas']
```

**3. Crear un nuevo empleado con id: 4:**
```python
nuevo_empleado = {"id": 4, "nombre": "Sofía", "habilidades": ["TensorFlow", "Keras"]}
data["empleados"].append(nuevo_empleado)
```

**4. Eliminar las habilidades de María:**
```python
data["empleados"][1]["habilidades"] = []
```

---

### Ejercicio 4: Estructuras de Datos en Python

```python
empleados = [
    {"id": 1, "nombre": "Juan",   "salario": 50000},
    {"id": 2, "nombre": "María",  "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

# 1. Agregar un nuevo empleado
empleados.append({"id": 4, "nombre": "Ana", "salario": 60000})

# 2. Buscar empleado por id
def buscar_por_id(lista, id_buscado):
    return next((e for e in lista if e["id"] == id_buscado), None)

print(buscar_por_id(empleados, 2))  # {'id': 2, 'nombre': 'María', 'salario': 45000}

# 3. Calcular promedio de salarios
promedio = sum(e["salario"] for e in empleados) / len(empleados)
print(f"Promedio: ${promedio:,.2f}")  # Promedio: $52,500.00

# 4. Filtrar empleados con salario > 50000
altos_salarios = [e for e in empleados if e["salario"] > 50000]
print(altos_salarios)  # Carlos y Ana

# 5. Actualizar el nombre del empleado con id=2
for e in empleados:
    if e["id"] == 2:
        e["nombre"] = "María González"
        break
```

---

### Ejercicio 5: Operaciones CRUD en MongoDB

```javascript
// Insertar documentos
db.productos.insertMany([
    {"nombre": "Laptop",     "precio": 999,  "categoria": "Electrónica"},
    {"nombre": "Mouse",      "precio": 29,   "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299,  "categoria": "Muebles"}
])

// 1. READ: Todos los productos de Electrónica
db.productos.find({ "categoria": "Electrónica" })

// 2. READ: Productos con precio menor a 100
db.productos.find({ "precio": { $lt: 100 } })

// 3. UPDATE: Aumentar precio de Laptop en 10%
db.productos.updateOne(
    { "nombre": "Laptop" },
    { $mul: { "precio": 1.10 } }
)

// 4. DELETE: Eliminar productos con precio menor a 50
db.productos.deleteMany({ "precio": { $lt: 50 } })

// 5. CREATE: Agregar un nuevo producto
db.productos.insertOne({
    "nombre": "Teclado Mecánico",
    "precio": 149,
    "categoria": "Electrónica"
})
```

---

### Ejercicio 6: Consultas Avanzadas en MongoDB

```javascript
// Colección: estudiantes
// {"nombre": "Ana",   "materias": ["Math", "Physics"],   "edad": 20}
// {"nombre": "Luis",  "materias": ["Math", "Chemistry"],  "edad": 22}
// {"nombre": "Sofia", "materias": ["Biology"],             "edad": 19}

// 1. Encontrar estudiantes que cursan Math
db.estudiantes.find({ "materias": "Math" })

// 2. Encontrar estudiantes mayores de 20
db.estudiantes.find({ "edad": { $gt: 20 } })

// 3. Contar estudiantes por edad
db.estudiantes.aggregate([
    { $group: { _id: "$edad", total: { $sum: 1 } } },
    { $sort: { _id: 1 } }
])

// 4. Proyectar solo nombres
db.estudiantes.find({}, { "nombre": 1, "_id": 0 })
```

---

### Ejercicio 7: Tipos de Bases de Datos NoSQL

**1. Documentales (MongoDB, CouchDB)**
Almacenan datos como documentos JSON/BSON con esquema flexible. Ideales cuando cada registro puede tener atributos distintos.
- *Cuándo usar:* catálogos de productos, perfiles de usuario, e-commerce.
- *Ventajas:* esquema flexible, consultas ricas, fácil escalado horizontal.
- *Desventajas:* no garantizan transacciones ACID complejas entre documentos, pueden generar duplicación de datos.

**2. Key-Value (Redis, DynamoDB)**
Almacenan pares clave-valor, como un diccionario gigante. Son las más rápidas.
- *Cuándo usar:* caché de sesiones, contadores en tiempo real, carritos de compra temporales.
- *Ventajas:* altísimo rendimiento en lectura/escritura, muy simples.
- *Desventajas:* no permiten consultas complejas por valor, difícil buscar sin la clave exacta.

**3. Columnar (Cassandra, HBase)**
Organizan los datos por columnas en lugar de filas. Optimizadas para analítica a gran escala.
- *Cuándo usar:* análisis de series de tiempo, logs de eventos, Big Data analytics.
- *Ventajas:* altísimo rendimiento en lecturas de columnas específicas, excelente compresión.
- *Desventajas:* complejas de modelar, no son flexibles para cambios frecuentes de esquema.

**4. Grafos (Neo4j)**
Almacenan datos como nodos y relaciones. Óptimas para datos altamente conectados.
- *Cuándo usar:* redes sociales, sistemas de recomendación, detección de fraude, mapas de rutas.
- *Ventajas:* consultas de relaciones complejas son muy rápidas y naturales.
- *Desventajas:* no escalan tan bien horizontalmente como otras NoSQL, curva de aprendizaje alta.

---

### Ejercicio 8: Arquitecturas de Almacenamiento

**1. ¿Qué es un Data Lake?**
Un Data Lake es un repositorio centralizado que almacena datos en su formato original (crudo), sin transformarlos previamente. Puede contener datos estructurados, semi-estructurados y no estructurados. Herramientas comunes: Amazon S3, Azure Data Lake, Hadoop HDFS.

**2. ¿Qué es un Data Warehouse?**
Un Data Warehouse es un sistema de almacenamiento optimizado para análisis y reportes. Los datos llegan ya transformados, limpios y estructurados en esquemas predefinidos. Herramientas comunes: Snowflake, Google BigQuery, Amazon Redshift.

**3. Diferencias entre OLAP y OLTP:**

| Característica | OLTP | OLAP |
|----------------|------|------|
| Propósito | Transacciones operativas del día a día | Análisis y reportes históricos |
| Operaciones | INSERT, UPDATE, DELETE frecuentes | SELECT con agregaciones complejas |
| Volumen de datos | Miles de registros por transacción | Millones o billones de registros |
| Velocidad | Muy rápido en escritura | Optimizado para lectura masiva |
| Ejemplo | Sistema de punto de venta | Dashboard de ventas anuales |

**4. ¿Qué es ETL?**
ETL significa Extract, Transform, Load (Extraer, Transformar, Cargar). Es el proceso de:
- **Extract:** obtener datos de diversas fuentes (bases de datos, APIs, archivos).
- **Transform:** limpiar, normalizar, enriquecer y aplicar reglas de negocio a los datos.
- **Load:** cargar los datos transformados al destino final (Data Warehouse o Data Lake).

---

## 2. Actividades Prácticas

### Actividad 2.1: Investigación de Arquitecturas de Datos

**Data Warehouse vs Data Lake vs Data Mart:**

| Característica | Data Lake | Data Warehouse | Data Mart |
|----------------|-----------|----------------|-----------|
| Datos | Crudos, sin procesar | Procesados y estructurados | Subconjunto del DW |
| Esquema | Schema-on-read | Schema-on-write | Schema-on-write |
| Usuarios | Data Scientists | Analistas de negocio | Áreas específicas |
| Costo | Bajo almacenamiento | Alto (procesamiento) | Medio |
| Flexibilidad | Alta | Baja | Media |

Un **Data Mart** es un subconjunto de un Data Warehouse orientado a un área específica del negocio (por ejemplo, el Data Mart de Ventas solo contiene datos del área comercial).

**Diagrama conceptual:**
```
Fuentes de datos → [ETL] → Data Lake (datos crudos)
                              ↓ [Transformación]
                         Data Warehouse (datos limpios)
                              ↓ [Especialización]
              Data Mart Ventas | Data Mart Finanzas | Data Mart RRHH
```

---

### Actividad 2.2: Introducción a MongoDB

**Pasos de instalación en Fedora Linux:**
```bash
# Agregar repositorio de MongoDB
sudo dnf install -y mongodb-org

# Iniciar el servicio
sudo systemctl start mongod
sudo systemctl enable mongod

# Verificar estado
sudo systemctl status mongod
```

**Creación de base de datos y colección de prueba:**
```javascript
// En MongoDB Shell (mongosh)
use prueba_db

db.productos_prueba.insertMany([
    { "nombre": "Laptop",    "precio": 15000, "categoria": "Electrónica" },
    { "nombre": "Mochila",   "precio": 450,   "categoria": "Accesorios"  },
    { "nombre": "Audífonos", "precio": 800,   "categoria": "Electrónica" },
    { "nombre": "Cuaderno",  "precio": 45,    "categoria": "Papelería"   },
    { "nombre": "Silla",     "precio": 2200,  "categoria": "Muebles"     }
])

db.productos_prueba.find().pretty()
```

---

### Actividad 2.3: Operaciones CRUD en MongoDB con Python

```python
from pymongo import MongoClient
import random

# Conexión a MongoDB
client    = MongoClient('mongodb://localhost:27017/')
db        = client['empresa_db']
coleccion = db['empleados']

# CREATE: Insertar 10 empleados
empleados = [
    {"nombre": "Laura Méndez",    "departamento": "IT",        "salario": 52000},
    {"nombre": "Roberto Sánchez", "departamento": "Ventas",    "salario": 38000},
    {"nombre": "Gabriela Torres", "departamento": "IT",        "salario": 60000},
    {"nombre": "Miguel Ángel",    "departamento": "RRHH",      "salario": 42000},
    {"nombre": "Patricia Ruiz",   "departamento": "Finanzas",  "salario": 55000},
    {"nombre": "Eduardo Vargas",  "departamento": "Ventas",    "salario": 35000},
    {"nombre": "Sofía Morales",   "departamento": "IT",        "salario": 65000},
    {"nombre": "Fernando López",  "departamento": "Marketing", "salario": 41000},
    {"nombre": "Daniela Castro",  "departamento": "Finanzas",  "salario": 58000},
    {"nombre": "Andrés Gutiérrez","departamento": "IT",        "salario": 70000},
]
coleccion.insert_many(empleados)
print(f"Insertados: {coleccion.count_documents({})} empleados")

# READ: Empleados del departamento IT
print("\nEmpleados de IT:")
for emp in coleccion.find({"departamento": "IT"}):
    print(f"  - {emp['nombre']}: ${emp['salario']:,}")

# UPDATE: Aumentar salario de Gabriela Torres
coleccion.update_one(
    {"nombre": "Gabriela Torres"},
    {"$set": {"salario": 67000}}
)
print("\nSalario de Gabriela Torres actualizado a $67,000")

# DELETE: Eliminar empleado
coleccion.delete_one({"nombre": "Eduardo Vargas"})
print("Eduardo Vargas eliminado de la colección")

client.close()
```

---

### Actividad 2.4: Modelado de Datos NoSQL — Sistema de Biblioteca Digital

**Justificación del diseño:**
Se eligió un modelo de documentos embebidos para datos que se consultan juntos frecuentemente, y referencias para evitar duplicación excesiva. MongoDB permite este enfoque híbrido.

**5 Colecciones:**

```json
// Colección 1: libros
{
  "_id": "ObjectId('...')",
  "isbn": "978-607-99999-1-1",
  "titulo": "Fundamentos de Ciencia de Datos",
  "autores": ["Ana García", "Luis Martínez"],
  "genero": "Tecnología",
  "año_publicacion": 2022,
  "disponible": true,
  "total_copias": 3,
  "copias_disponibles": 2,
  "calificacion_promedio": 4.5
}

// Colección 2: usuarios
{
  "_id": "ObjectId('...')",
  "num_socio": "SOC-00142",
  "nombre": "María López",
  "email": "maria@email.com",
  "fecha_registro": "2023-05-10",
  "prestamos_activos": 1,
  "historial_ids": ["ObjectId('...')"]
}

// Colección 3: prestamos
{
  "_id": "ObjectId('...')",
  "libro_id": "ObjectId('...')",
  "usuario_id": "ObjectId('...')",
  "fecha_prestamo": "2024-03-01",
  "fecha_devolucion_esperada": "2024-03-15",
  "fecha_devolucion_real": null,
  "estado": "activo",
  "multa_acumulada": 0.00
}

// Colección 4: reseñas
{
  "_id": "ObjectId('...')",
  "libro_id": "ObjectId('...')",
  "usuario_id": "ObjectId('...')",
  "calificacion": 5,
  "comentario": "Libro muy completo y bien explicado.",
  "fecha": "2024-02-20",
  "verificado": true
}

// Colección 5: autores
{
  "_id": "ObjectId('...')",
  "nombre": "Ana García",
  "nacionalidad": "México",
  "biografia": "Doctora en Ciencias Computacionales con 15 años de experiencia.",
  "libros_ids": ["ObjectId('...')"],
  "sitio_web": "https://anagarcia.dev"
}
```

---

## 3. Actividad Evaluable — Análisis Exploratorio de Datos (Todo Ventas en Línea S.A. de C.V.)

### 3.1 Definición del Problema

**Objetivo del proyecto:**
Realizar un análisis exploratorio de datos sobre el historial de ventas del año 2023 de "Todo Ventas en Línea S.A. de C.V." con el fin de comprender el rendimiento comercial, identificar patrones de comportamiento del cliente y extraer insights que orienten las estrategias comerciales del año en curso.

**Preguntas clave de investigación:**
1. ¿Qué categoría de producto genera mayor volumen de ventas en términos monetarios?
2. ¿Existe una correlación entre el precio unitario del producto y el total de la venta?
3. ¿Cómo se distribuyen las edades de los clientes que realizan compras?
4. ¿Cuál es la distribución del total de ventas y qué tan sesgada es?
5. ¿Qué tan satisfechos están los clientes en general (calificación promedio)?

---

### 3.2 Generación y Descripción del Dataset

El dataset fue generado programáticamente con Python usando `NumPy` y `random` con semilla fija (seed=42) para garantizar reproducibilidad. Contiene **5,000 registros** y **18 columnas**.

**Descripción de columnas:**

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `id_orden` | Estructurado | Identificador único con formato ORD-XXXXX |
| `fecha_venta` | Estructurado | Fecha con formato YYYY-MM-DD |
| `mes_venta` | Categórico | Nombre del mes en inglés |
| `categoria` | Categórico | Categoría del producto (8 posibles) |
| `metodo_pago` | Categórico | Método de pago usado |
| `region` | Categórico | Región geográfica del cliente |
| `estado_envio` | Categórico | Estado actual del envío |
| `genero_cliente` | Categórico | Género reportado por el cliente |
| `precio_unitario` | Numérico decimal | Precio por unidad en MXN |
| `cantidad` | Numérico entero | Unidades compradas |
| `descuento_pct` | Numérico decimal | Porcentaje de descuento aplicado (0–40%) |
| `total_venta` | Numérico decimal | Monto final de la venta en MXN |
| `edad_cliente` | Numérico entero | Edad del comprador en años |
| `calificacion` | Numérico decimal | Calificación del producto (1–5) |
| `dias_envio` | Numérico entero | Días que tardó el envío |
| `costo_envio` | Numérico decimal | Costo del envío en MXN |
| `comentario_cliente` | No estructurado | Opinión libre del cliente |
| `descripcion_producto` | No estructurado | Descripción narrativa del artículo |

---

### 3.3 Carga en MongoDB

```python
from pymongo import MongoClient
import pandas as pd

df = pd.read_csv('datos_ventas.csv')

client    = MongoClient('mongodb://localhost:27017/')
db        = client['todo_ventas_db']
coleccion = db['ventas']

coleccion.drop()  # Limpiar colección si ya existe
registros = df.to_dict(orient='records')
resultado = coleccion.insert_many(registros)

print(f"Documentos insertados: {len(resultado.inserted_ids)}")
# Output: Documentos insertados: 5000
client.close()
```

Cada fila del DataFrame se convierte en un documento JSON en MongoDB. La colección `ventas` dentro de la base de datos `todo_ventas_db` almacena los 5,000 documentos con sus 18 campos.

---

### 3.4 Análisis Exploratorio con Pandas y NumPy

**Resumen estadístico de variables numéricas:**

| Variable | Media | Mediana | Moda | Desv. Estándar | Mínimo | Máximo |
|----------|-------|---------|------|----------------|--------|--------|
| precio_unitario | 2,509.32 | 2,525.04 | 431.05 | 1,433.69 | 50.06 | 4,998.60 |
| cantidad | 10.07 | 10.00 | 10.00 | 5.48 | 1 | 19 |
| descuento_pct | 0.20 | 0.20 | 0.10 | 0.12 | 0.00 | 0.40 |
| total_venta | 20,151.85 | 15,339.88 | 1,397.59 | 17,386.45 | 38.27 | 87,582.05 |
| edad_cliente | 43.57 | 44.00 | 27.00 | 15.10 | 18 | 69 |
| calificacion | 3.04 | 3.00 | 3.90 | 1.16 | 1.00 | 5.00 |
| dias_envio | 7.60 | 8.00 | 10.00 | 3.98 | 1 | 14 |
| costo_envio | 147.30 | 146.27 | 154.02 | 85.43 | 0.03 | 299.92 |

**Ventas totales por categoría:**

| Categoría | Total Ventas (MXN) | Promedio por Orden | Órdenes |
|-----------|--------------------|--------------------|---------|
| Deportes | $14,075,410.43 | $20,340.19 | 692 |
| Juguetes | $13,834,026.45 | $20,678.66 | 669 |
| Belleza | $12,680,665.75 | $20,419.75 | 621 |
| Alimentos | $12,666,604.56 | $21,075.88 | 601 |
| Ropa | $12,415,288.61 | $19,928.23 | 623 |
| Electrónica | $12,032,397.72 | $19,344.69 | 622 |
| Libros | $11,798,810.95 | $20,663.42 | 571 |
| Hogar | $11,256,033.71 | $18,728.84 | 601 |

**Estado de envíos:**
- Entregado: 3,732 órdenes (74.6%)
- En tránsito: 502 (10.0%)
- Devuelto: 408 (8.2%)
- Cancelado: 358 (7.2%)

**Interpretación del análisis exploratorio:**
La media del total de venta ($20,151.85 MXN) es significativamente mayor que la mediana ($15,339.88 MXN), lo que indica que la distribución está sesgada hacia la derecha: existen ventas de alto valor que elevan el promedio. La categoría Deportes lidera en ventas totales, pero Alimentos tiene el ticket promedio más alto. La calificación promedio de 3.04 sobre 5 sugiere oportunidades de mejora en satisfacción del cliente. El 74.6% de las órdenes se entregaron exitosamente, mientras que el 8.2% fue devuelto, una tasa que merece atención para reducirla.

---

### 3.5 Visualizaciones

#### Gráfica 1: Diagrama de Cajas

![Diagrama de Cajas](Visualizaciones/boxplot.png)

**Interpretación:**
- **Total de Venta:** La caja se concentra entre Q1=$7,005 y Q3=$27,948, con una mediana de $15,340. Existe una cantidad considerable de valores atípicos superiores (ventas de alto valor), lo que explica que la media supere a la mediana.
- **Precio Unitario:** Distribución bastante uniforme entre $50 y $5,000, con la mediana ($2,525) casi centrada, lo que indica que no hay sesgo pronunciado en los precios del catálogo.
- **Calificación:** La caja está comprimida entre 2.0 y 4.1, con mediana en 3.0. La distribución es relativamente simétrica, indicando que los clientes califican de forma dispersa sin una tendencia clara hacia arriba o abajo.

---

#### Gráfica 2: Diagrama de Dispersión

![Dispersión Precio vs Total de Venta](Visualizaciones/scatter.png)

**Interpretación:**
La gráfica muestra la relación entre el precio unitario y el total de la venta para las 5,000 órdenes, diferenciadas por categoría. La correlación de Pearson de **r = 0.655** indica una correlación positiva moderada-alta: en general, productos más caros generan ventas totales mayores. Sin embargo, la nube de puntos tiene dispersión vertical considerable, lo que refleja que la cantidad comprada y el descuento aplicado también influyen de forma importante en el total final. Todas las categorías presentan un comportamiento similar, sin que ninguna se separe significativamente del patrón general.

---

#### Gráfica 3: Histogramas de Distribución

![Histogramas](Visualizaciones/histograma.png)

**Interpretación:**
- **Total de Venta:** La distribución está sesgada a la derecha (sesgo positivo). La mayoría de las ventas se concentran entre $0 y $30,000 MXN, pero existe una cola larga hacia valores altos, lo que eleva la media ($20,152) por encima de la mediana ($15,340). Esto es típico en e-commerce: la mayoría de órdenes son de valor moderado, pero unas pocas órdenes de alto valor aportan mucho al total.
- **Edad del Cliente:** La distribución es aproximadamente uniforme entre los 18 y 69 años, lo que indica que la tienda atiende a un público muy diverso en edad. No hay una concentración marcada en ningún rango etario, lo cual es una oportunidad para segmentar campañas por grupo de edad.

---

## 4. Resumen de Aprendizaje

- Las bases de datos NoSQL como MongoDB son fundamentales para manejar datos con esquemas variables y volúmenes grandes, a diferencia del SQL tradicional que requiere esquemas rígidos.
- La Arquitectura Lambda permite combinar procesamiento en tiempo real y por lotes, siendo ideal para empresas con necesidades de análisis tanto operativas como históricas.
- El análisis exploratorio de datos (EDA) es el paso más crítico antes de cualquier modelado: permite entender la distribución, detectar valores atípicos y definir las preguntas correctas.
- La diferencia entre media y mediana en el total de ventas revela el sesgo de la distribución, un dato esencial para no tomar decisiones basadas solo en el promedio.
- Python con Pandas y NumPy es suficiente para realizar un EDA completo y riguroso sobre datasets de miles de registros.
- Las visualizaciones (boxplot, scatter, histograma) no son decorativas: cada una responde una pregunta específica sobre los datos.

---

## 5. Dudas o Preguntas

- ¿Cómo se maneja el versionado de esquemas en MongoDB cuando los documentos evolucionan con el tiempo?
- ¿En qué escenarios es preferible usar un Data Lakehouse en lugar de separar Data Lake y Data Warehouse?

---

## 6. Commits Realizados

```
Semana2: Ejercicios complementarios SQL, JSON y MongoDB
Semana2: Actividades prácticas 2.1 a 2.4
Semana2: Actividad evaluable - Dataset generado y análisis EDA
Semana2: Visualizaciones - boxplot, scatter, histograma
Semana2: Consolidado completo
```

---

## 7. Referencias

- MongoDB Inc. (2024). *MongoDB CRUD Operations.* https://www.mongodb.com/docs/manual/crud/
- McKinney, W. (2022). *Python for Data Analysis, 3rd ed.* O'Reilly Media.
- Pandas Development Team. (2024). *Pandas Documentation.* https://pandas.pydata.org/docs/
- Hunter, J.D. (2007). *Matplotlib: A 2D Graphics Environment.* Computing in Science & Engineering.
- Waskom, M. (2021). *Seaborn: Statistical Data Visualization.* JOSS.
- W3Schools. (2024). *SQL Tutorial.* https://www.w3schools.com/sql/
- IBM Cloud. (2024). *Data Lake vs Data Warehouse.* https://www.ibm.com/cloud/learn/data-lake
