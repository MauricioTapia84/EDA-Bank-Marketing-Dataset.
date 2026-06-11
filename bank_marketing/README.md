# Bank Marketing Dataset - Rol B: Transformación de Datos

Este proyecto se centra en la preparación del dataset `Bank Marketing` para su uso en Machine Learning, con énfasis en las tareas del Rol B: transformación y preparación de datos.

## Estructura propuesta

- `data/`
  - Dataset original (`bank_marketing.csv` o equivalente).
- `docs/`
  - Documentos de soporte y fuentes (`md-fuente/`).
- `notebooks/`
  - Notebooks y scripts de trabajo.
- `reports/`
  - Resultados finales, resúmenes y presentaciones.

## Objetivo principal del Rol B

- Realizar escalamiento de variables numéricas.
- Codificar variables categóricas correctamente.
- Construir un pipeline reproducible con transformaciones solo ajustadas en `Train`.
- Comparar `antes` y `después` de las transformaciones.
- Producir las secciones de `Escalamiento`, `Codificación` y `Pipeline` en el informe.

## Flujo de trabajo recomendado

1. Colocar el dataset en `data/` con un nombre claro, por ejemplo `bank_marketing.csv`.
2. Cargar los datos y separar `X` / `y`.
3. Ejecutar `train_test_split(..., stratify=y, random_state=...)` antes de cualquier tratamiento.
4. Definir columnas numéricas y categóricas.
5. Crear un pipeline de preprocesamiento con `ColumnTransformer`.
6. Ajustar el fit solo en `X_train` y usar `transform` en ambos conjuntos.
7. Generar visualizaciones de antes y después.
8. Documentar cada paso en el notebook.

## Checklist del rol B

- [ ] Definir columnas numéricas y categóricas.
- [ ] Crear transformador numérico (`SimpleImputer + StandardScaler`).
- [ ] Crear transformador categórico (`SimpleImputer + OneHotEncoder | OrdinalEncoder`).
- [ ] Encapsular todo en `Pipeline` y `ColumnTransformer`.
- [ ] Probar que el fit no ve `X_test`.
- [ ] Guardar los resultados transformados para validación.
- [ ] Incluir gráficos de comparación antes/después.

## Notas importantes

- `StandardScaler` solo debe hacer `fit` en `X_train`.
- `OneHotEncoder(handle_unknown='ignore')` es ideal para evitar errores con categorías nuevas en `X_test`.
- Si algún valor faltante existe, el imputador debe ser ajustado solo en `Train`.
- No usar estadísticas del dataset completo para el escalado ni la codificación.

## Siguientes pasos

1. Revisar `docs/md-fuente/Acta de proyecto preprocesamiento.md` para confirmar responsabilidades.
2. Crear un notebook en `notebooks/` que implemente el pipeline.
3. Agregar visualizaciones en el informe para demostrar la transformación.
