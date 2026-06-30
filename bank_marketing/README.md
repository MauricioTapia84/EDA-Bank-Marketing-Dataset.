# Bank Marketing Dataset

<<<<<<< HEAD
Proyecto de preprocesamiento y preparación de datos para un caso de predicción de suscripción a depósitos a plazo.

Este repositorio organiza el trabajo del dataset `Bank Marketing` con foco en:

- separación correcta de `Train` y `Test`,
- limpieza de datos,
- análisis exploratorio,
- escalamiento y codificación,
- construcción de un pipeline reproducible,
- validación del dataset procesado para modelado posterior.

## Objetivo

Preparar el conjunto de datos `bank-additional-full.csv` para que pueda usarse en Machine Learning sin fuga de información y con transformaciones bien documentadas.

La variable objetivo es `y`, que indica si el cliente contrató o no un depósito a plazo:

- `yes`: contrató
- `no`: no contrató
=======
Proyecto de preprocesamiento, analisis exploratorio y modelado para predecir la suscripcion a depositos a plazo.

El objetivo del repositorio es presentar un flujo reproducible y entendible para la revision del profesor:

- carga del dataset original,
- separacion estratificada de `Train` y `Test`,
- limpieza y tratamiento de faltantes,
- escalamiento de variables numericas,
- codificacion de variables categoricas,
- construccion de un pipeline reproducible,
- comparacion entre modelos,
- evaluacion final sobre `Test`.

## Objetivo del proyecto

Preparar el conjunto `bank-additional-full.csv` para que quede listo para modelado y evaluacion final, evitando fuga de informacion y dejando evidencia clara de cada decision metodologica.

La variable objetivo es `y`:

- `yes`: el cliente contrato un deposito a plazo
- `no`: el cliente no contrato un deposito a plazo
>>>>>>> a31803a (2.2.0)

## Dataset

- Archivo fuente: `data/raw/bank-additional-full.csv`
- Registros: `41.188`
<<<<<<< HEAD
- Variables: `21`
- Problema: clasificación binaria
- Distribución aproximada de la clase objetivo:
  - `no`: `36.548`
  - `yes`: `4.640`

## Criterio metodológico

La regla central del proyecto es:
=======
- Variables originales: `21`
- Tipo de problema: clasificacion binaria
- Distribucion aproximada de la clase objetivo:
  - `no`: `36.548`
  - `yes`: `4.640`

## Metodologia

La secuencia aplicada en el proyecto es esta:
>>>>>>> a31803a (2.2.0)

1. cargar el dataset,
2. separar `X` e `y`,
3. ejecutar `train_test_split(..., stratify=y, random_state=42)`,
<<<<<<< HEAD
4. hacer EDA y transformaciones aprendidas solo sobre `Train`,
5. aplicar `transform` a `Train` y `Test`,
6. reservar `Test` para la validación final.

Esto evita `data leakage` y mantiene válida la evaluación posterior.
=======
4. reservar `Test` desde el inicio,
5. aprender imputacion, escalado y codificacion solo con `Train`,
6. aplicar `transform` sobre `Train` y `Test`,
7. validar modelos con una particion interna derivada de `Train`,
8. usar `Test` una sola vez para la evaluacion final.

Este criterio evita que estadisticas del conjunto de prueba influyan en el entrenamiento.

## Resultados principales

El mejor modelo del flujo actual es `Random Forest`.

- Mejor F1 en validacion interna
- Umbral seleccionado: `0.603`
- Evaluacion final sobre `Test` para la clase `yes`:
  - precision: `0.48`
  - recall: `0.59`
  - F1: `0.53`
  - accuracy global: `0.88`
>>>>>>> a31803a (2.2.0)

## Estructura del proyecto

- `data/raw/`: dataset original.
<<<<<<< HEAD
- `data/splits/`: particiones `X_train`, `X_test`, `y_train`, `y_test`.
- `data/processed/`: versiones limpiadas y listas para modelado.
- `docs/`: documentación del proyecto.
- `notebooks/`: notebooks y scripts de trabajo.
- `reports/`: gráficos, resultados y material de presentación.

## Flujo de trabajo

### 1. Separación inicial

- Cargar `bank-additional-full.csv`.
- Separar variables predictoras y objetivo.
- Ejecutar `train_test_split` con estratificación.
- Guardar los subconjuntos para trazabilidad.

### 2. Comprensión y limpieza

- Revisar tipos de datos.
- Detectar `unknown`, nulos y duplicados.
- Definir reglas de tratamiento para el conjunto de entrenamiento.
- Eliminar variables o registros que introduzcan fuga de información si corresponde.

### 3. EDA sobre `Train`

- Analizar distribuciones univariadas.
- Explorar relaciones bivariadas con `y`.
- Priorizar tasas de conversión sobre frecuencias absolutas.
- Generar gráficos útiles para la defensa y el informe.

### 4. Transformaciones

- Escalar variables numéricas con `StandardScaler`.
- Codificar variables categóricas con `OneHotEncoder` y `OrdinalEncoder`.
- Aplicar imputación si corresponde.
=======
- `data/splits/`: particiones iniciales `X_train`, `X_test`, `y_train`, `y_test`.
- `data/processed/`: versiones procesadas y listas para modelado.
- `docs/md-fuente/`: documentacion tecnica y teorica del proyecto.
- `notebooks/`: notebooks de preprocesamiento y modelado.
- `reports/`: material de apoyo, graficos y presentacion.

## Flujo de trabajo

### 1. Preparacion inicial

- Cargar el dataset original.
- Separar variables explicativas y variable objetivo.
- Reservar `Test` mediante `train_test_split` con estratificacion.
- Guardar los subconjuntos para trazabilidad.

### 2. Limpieza y comprension

- Revisar tipos de datos.
- Detectar `unknown`, nulos y duplicados.
- Tratar `unknown` como valor faltante cuando corresponde.
- Excluir `duration` por su riesgo de fuga de informacion.

### 3. Analisis exploratorio

- Describir distribuciones univariadas.
- Explorar relaciones entre variables y la variable objetivo.
- Priorizar tasas de conversion sobre frecuencias absolutas.
- Generar graficos utiles para la defensa.

### 4. Transformaciones

- Imputar valores faltantes.
- Escalar variables numericas con `StandardScaler`.
- Codificar variables categoricas con `OneHotEncoder` y `OrdinalEncoder`.
>>>>>>> a31803a (2.2.0)
- Mantener consistencia entre `Train` y `Test`.

### 5. Pipeline

<<<<<<< HEAD
- Consolidar las transformaciones en `Pipeline` y `ColumnTransformer`.
- Ajustar `fit` solo con `Train`.
- Usar `transform` para `Train` y `Test`.

### 6. Validación

- Verificar ausencia de nulos en las matrices procesadas.
- Confirmar consistencia dimensional.
- Revisar resultados antes de modelar.

## Archivos relevantes

- `notebooks/01_preprocesamiento_proyecto.ipynb`: notebook principal del flujo.
- `notebooks/02_modelado_basico.ipynb`: modelado base posterior al preprocesamiento.
- `notebooks/preprocessing.py`: funciones de apoyo reutilizables.
- `data/raw/bank-additional-full.csv`: dataset original.

## Ejecución local

### 1. Entrar al proyecto

```bash
cd /Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 2. Crear entorno virtual

```bash
cd /Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 3. Instalar dependencias

```bash
cd /Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 4. Registrar kernel

```bash
cd /Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 5. Abrir Jupyter

Se recomienda ejecutar Jupyter desde `notebooks/` para que los imports locales funcionen sin ajustes extra.

```bash
cd /Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

## Orden sugerido de ejecución

1. `01_preprocesamiento_proyecto.ipynb`
2. `02_modelado_basico.ipynb`

## Entregables esperados

- Separación formal de `Train` y `Test`.
- Limpieza documentada de los datos.
- EDA con al menos 15 gráficos útiles.
- Escalamiento y codificación justificadas.
- Pipeline reproducible.
- Dataset final preparado para modelado.
- Informe técnico y defensa oral.

## Nota metodológica

`duration` debe tratarse con cuidado porque puede introducir fuga de información. El proyecto la analiza como variable delicada y, si corresponde, la excluye del flujo de modelado.
=======
- Consolidar transformaciones con `Pipeline` y `ColumnTransformer`.
- Ajustar `fit` solo en `Train`.
- Aplicar `transform` a `Train` y `Test`.

### 6. Modelado

- Entrenar modelos base y supervisados sobre el flujo ya preprocesado.
- Comparar desempeno con una validacion interna derivada de `Train`.
- Seleccionar el mejor modelo segun F1 en validacion.

### 7. Validacion

- Confirmar ausencia de `duration` en los CSV procesados.
- Verificar que el split conserve la proporcion de clases.
- Revisar que el pipeline produzca matrices consistentes.
- Confirmar que el modelo final se evalua una sola vez sobre `Test`.

## Archivos relevantes

- `notebooks/01_preprocesamiento_proyecto.ipynb`: flujo principal de limpieza, EDA, transformacion y validacion de variables.
- `notebooks/02_modelado_basico.ipynb`: comparacion de modelos y evaluacion final.
- `notebooks/preprocessing.py`: funciones reutilizables para carga, split y pipeline.
- `docs/md-fuente/MARCO_TEORICO_Y_EXPLICATIVO.md`: marco teorico del proyecto.
- `docs/md-fuente/EVALUACIÓN PARCIAL 4_ESTUDIANTE.md`: pauta y rubrica.

## Ejecucion local

### Desde la raiz del repositorio

```bash
cd bank_marketing
source ../.venv/bin/activate
```

### Ejecutar preprocesamiento

```bash
cd bank_marketing/notebooks
../../.venv/bin/python preprocessing.py
```

### Abrir Jupyter

```bash
cd bank_marketing/notebooks
../../.venv/bin/jupyter lab
```

### Ejecutar notebooks con nbconvert

```bash
cd bank_marketing/notebooks
../../.venv/bin/jupyter nbconvert --to notebook --execute 01_preprocesamiento_proyecto.ipynb --output /tmp/01_preprocesamiento_proyecto_ejecutado.ipynb
../../.venv/bin/jupyter nbconvert --to notebook --execute 02_modelado_basico.ipynb --output /tmp/02_modelado_basico_ejecutado.ipynb
```

## Entregables esperados

- dataset original documentado,
- split estratificado y trazable,
- limpieza y transformaciones justificadas,
- pipeline reproducible,
- comparacion antes/despues de las transformaciones,
- modelo base y modelo final evaluados,
- informe tecnico y presentacion oral.

## Cierre

El proyecto queda orientado a defensa final: datos preparados, modelado reproducible y resultados resumidos para explicar al profesor sin notas internas innecesarias.
>>>>>>> a31803a (2.2.0)
