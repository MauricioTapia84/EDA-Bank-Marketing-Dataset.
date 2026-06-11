# 📋 Plan de Trabajo - Rol B: Transformación y Preparación de Datos

**Responsable**: Mauricio Tapia  
**Proyecto**: Bank Marketing - Predicción de Suscripción a Depósitos a Plazo  
**Fecha**: Junio 2026

---

## 📌 Resumen ejecutivo

Tu rol B consiste en preparar el dataset limpio (entregado por Rol A) para Machine Learning mediante:
1. **Escalamiento** de variables numéricas
2. **Codificación** de variables categóricas
3. **Construcción** de un pipeline reproducible
4. **Documentación** con 5 gráficos comparativos

---

## 🎯 Tareas principales

### ✅ Tarea 1: Preparación del ambiente (30 min)

```bash
# En terminal
cd /home/mauricio/Documentos/GitHub/EDA-Bank-Marketing-Dataset./bank_marketing

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
pip freeze > requirements.txt
```

**Deliverable**: `requirements.txt` actualizado.

---

### ✅ Tarea 2: Cargar datos y realizar Train/Test Split (1 hora)

**Archivo**: `notebooks/role_b_structure.ipynb` (celdas 1-4)

**Acciones**:
- [ ] Cargar `bank_marketing.csv` desde `data/`
- [ ] Definir columnas numéricas, nominales y ordinales
- [ ] Ejecutar `train_test_split()` con `stratify=y` y `random_state=42`
- [ ] Guardar `X_train_original.csv`, `X_test_original.csv`

**Criterio de validación**:
- Train/Test tienen proporción similar de clases (stratificación correcta)
- Tamaños: Train ~80%, Test ~20%

---

### ✅ Tarea 3: Escalamiento numérico (1 hora)

**Archivo**: `notebooks/role_b_structure.ipynb` (celdas 5-6)

**Acciones**:
- [ ] Crear `StandardScaler()`
- [ ] **Hacer fit SOLO en X_train**
- [ ] Aplicar transform en X_train y X_test
- [ ] Generar **Gráfico 1**: Comparación antes/después (histogramas + boxplots)

**Criterio de validación**:
- Media de variables escaladas ≈ 0
- Desviación estándar ≈ 1
- X_test tiene misma transformación que X_train

---

### ✅ Tarea 4: Codificación categórica (1.5 horas)

**Archivo**: `notebooks/role_b_structure.ipynb` (celdas 7-9)

**Acciones**:
- [ ] Crear `OneHotEncoder(handle_unknown='ignore', drop='first')` para nominales
- [ ] Crear `OrdinalEncoder(handle_unknown='use_encoded_value')` para ordinales
- [ ] **Hacer fit SOLO en X_train**
- [ ] Aplicar transform en X_train y X_test
- [ ] Generar **Gráfico 2**: Distribución antes de codificación

**Criterio de validación**:
- OneHot: Cada categoría original se convierte en columnas binarias
- Ordinal: Educación se convierte en números ordenados
- X_test maneja categorías desconocidas sin errores

---

### ✅ Tarea 5: Construcción del Pipeline (1.5 horas)

**Archivo**: `notebooks/role_b_structure.ipynb` (celdas 10-11)

**Acciones**:
- [ ] Crear `Pipeline` para cada tipo de variable (numeric, nominal, ordinal)
- [ ] Encapsular en `ColumnTransformer`
- [ ] **Hacer fit SOLO en X_train**
- [ ] Aplicar transform en X_train y X_test
- [ ] Guardar `X_train_transformed.csv`, `X_test_transformed.csv`
- [ ] Generar **Gráfico 3**: Dimensionalidad antes/después

**Criterio de validación**:
- Pipeline ejecuta sin errores
- X_train_transformed y X_test_transformed tienen misma dimensión
- No hay valores NaN en datasets transformados

---

### ✅ Tarea 6: Validación y gráficos finales (1 hora)

**Archivo**: `notebooks/role_b_structure.ipynb` (celdas 12-14)

**Acciones**:
- [ ] Ejecutar validaciones (ausencia de NaN, escalamiento correcto, consistencia)
- [ ] Generar **Gráfico 4**: Matriz de correlación antes/después
- [ ] Generar **Gráfico 5**: Varianza antes/después
- [ ] Guardar todos los gráficos en `reports/`

**Criterio de validación**:
- Todos los gráficos están en alta resolución (300 dpi)
- Cada gráfico tiene título, ejes etiquetados y leyenda clara

---

### ✅ Tarea 7: Documentación y guión oral (1.5 horas)

**Archivo**: `notebooks/role_b_structure.ipynb` (sección 7)

**Acciones**:
- [ ] Estudiar el guión de defensa oral
- [ ] Preparar explicación de cada sección (5-7 min por sección)
- [ ] Anticipar preguntas comunes
- [ ] Practicar presentación con ejemplos concretos

**Criterio de validación**:
- Puedes explicar cada decisión técnica justificadamente
- Puedes responder preguntas sobre leakage, escalamiento, codificación

---

## 📊 5 Gráficos requeridos

| # | Nombre | Archivo | Descripción |
|---|--------|---------|-------------|
| 1 | Escalamiento antes/después | `01_escalamiento_comparacion.png` | Histogramas + Boxplots de variable numérica |
| 2 | Categorías nominales/ordinales | `02_categoricas_antes.png` | Barras de distribución de job, marital, education |
| 3 | Dimensionalidad | `03_dimensionalidad_pipeline.png` | Barras: columnas antes/después |
| 4 | Correlación antes/después | `04_correlacion_transformacion.png` | Heatmaps de correlación |
| 5 | Varianza escalamiento | `05_varianza_escalamiento.png` | Barras: varianza de 9 numéricas |

---

## 📂 Estructura esperada al finalizar

```
bank_marketing/
├── data/
│   ├── bank_marketing.csv                 (original)
│   ├── X_train_original.csv              (antes de transformar)
│   ├── X_test_original.csv               (antes de transformar)
│   ├── X_train_transformed.csv           (después de transformar)
│   └── X_test_transformed.csv            (después de transformar)
├── notebooks/
│   ├── role_b_structure.ipynb            (este cuaderno, completo)
│   └── role_b_preprocessing.py           (script auxiliar)
├── reports/
│   ├── 01_escalamiento_comparacion.png
│   ├── 02_categoricas_antes.png
│   ├── 03_dimensionalidad_pipeline.png
│   ├── 04_correlacion_transformacion.png
│   └── 05_varianza_escalamiento.png
└── README.md
```

---

## ⏱️ Cronograma estimado

| Tarea | Tiempo | Total |
|-------|--------|-------|
| 1. Setup entorno | 30 min | 30 min |
| 2. Carga y split | 1 h | 1.5 h |
| 3. Escalamiento | 1 h | 2.5 h |
| 4. Codificación | 1.5 h | 4 h |
| 5. Pipeline | 1.5 h | 5.5 h |
| 6. Validación | 1 h | 6.5 h |
| 7. Documentación | 1.5 h | **8 h (total)** |

**Recomendación**: Distribuir en 2-3 sesiones de 2.5-3 horas cada una.

---

## 🔗 Referencias

- [sklearn.preprocessing.StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [sklearn.preprocessing.OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
- [sklearn.compose.ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)
- [Prevención de Data Leakage](https://machinelearningmastery.com/data-leakage-machine-learning/)

---

## 💡 Tips importantes

1. **Siempre hacer fit en Train**: Si olvidas hacer fit en Test, hay data leakage.
2. **Usar `random_state=42`**: Asegura reproducibilidad.
3. **`handle_unknown='ignore'`**: Previene errores si Test tiene categorías nuevas.
4. **Documentar cada paso**: Comentarios claros en el notebook ayudan en la defensa oral.
5. **Validar dimensiones**: Train y Test deben tener la misma cantidad de columnas.

---

## ❓ Preguntas frecuentes

**P: ¿Qué es data leakage?**  
R: Cuando información del Test filtra hacia el Train, causando que el modelo aparente ser mejor de lo que realmente es.

**P: ¿Por qué `StandardScaler` y no otro?**  
R: StandardScaler es robusto, centra los datos y es el estándar en ML. MinMaxScaler es más sensible a outliers.

**P: ¿Qué pasa si una categoría en Test no estaba en Train?**  
R: Con `handle_unknown='ignore'`, se trata como valor faltante. Con `handle_unknown='error'`, lanza excepción.

---

**Última actualización**: 11 de junio de 2026  
**Estado**: 🟢 Listo para comenzar
