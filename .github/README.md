# Bank Marketing Dataset

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

## Dataset

- Archivo fuente: `data/raw/bank-additional-full.csv`
- Registros: `41.188`
- Variables: `21`
- Problema: clasificación binaria
- Distribución aproximada de la clase objetivo:
  - `no`: `36.548`
  - `yes`: `4.640`

## Criterio metodológico

La regla central del proyecto es:

1. cargar el dataset,
2. separar `X` e `y`,
3. ejecutar `train_test_split(..., stratify=y, random_state=42)`,
4. hacer EDA y transformaciones aprendidas solo sobre `Train`,
5. aplicar `transform` a `Train` y `Test`,
6. reservar `Test` para la validación final.

Esto evita `data leakage` y mantiene válida la evaluación posterior.

## Estructura del proyecto

- `data/raw/`: dataset original.
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
- Mantener consistencia entre `Train` y `Test`.

### 5. Pipeline

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
cd /home/tomy/Downloads/Instituto/Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 2. Crear entorno virtual

```bash
cd /home/tomy/Downloads/Instituto/Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 3. Instalar dependencias

```bash
cd /home/tomy/Downloads/Instituto/Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 4. Registrar kernel

```bash
cd /home/tomy/Downloads/Instituto/Bank/EDA-Bank-Marketing-Dataset./bank_marketing
```

### 5. Abrir Jupyter

Se recomienda ejecutar Jupyter desde `notebooks/` para que los imports locales funcionen sin ajustes extra.

```bash
cd /home/tomy/Downloads/Instituto/Bank/EDA-Bank-Marketing-Dataset./bank_marketing
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
