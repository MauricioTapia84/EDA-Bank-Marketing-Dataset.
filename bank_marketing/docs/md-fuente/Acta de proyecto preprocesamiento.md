Evaluación Parcial N°4 – Preprocesamiento de Datos para Machine Learning
Proyecto: Predicción de Suscripción a Depósitos a Plazo (Bank Marketing Dataset)
Campo	Detalle
Asignatura	ADY1100 – Preprocesamiento de Datos
Integrantes	Mauricio Tapia, Tomas Zapata, Gabriel Muñoz
Fecha	Junio 2026
Herramienta de desarrollo	Python (Visual Studio Code / Jupyter Notebook)

1. Antecedentes del Proyecto
El Banco Financiero Global busca mejorar la efectividad de sus campañas de marketing telefónico mediante la identificación de clientes con mayor probabilidad de contratar un depósito a plazo.
Actualmente, la tasa de conversión es cercana al 10%, lo que implica que una gran cantidad de recursos se destinan a contactar clientes que finalmente no contratan el producto. El objetivo del proyecto es preparar adecuadamente los datos para construir modelos predictivos que permitan optimizar futuras campañas.
2. Objetivo General
Preparar el conjunto de datos Bank Marketing mediante técnicas de preprocesamiento, transformación e ingeniería de características, generando un dataset optimizado para futuros modelos de Machine Learning capaces de predecir la contratación de depósitos a plazo.
3. Objetivos Específicos
    1. Separar el dataset en conjuntos de entrenamiento y prueba antes del EDA y las transformaciones.
    2. Identificar y tratar valores faltantes.
    3. Detectar y corregir inconsistencias en los datos.
    4. Escalar variables numéricas.
    5. Codificar variables categóricas.
    6. Crear nuevas variables relevantes mediante ingeniería de características.
    7. Evaluar el impacto de las transformaciones realizadas sin contaminar el conjunto de prueba.
    8. Documentar técnicamente todas las decisiones tomadas.
    9. Preparar una presentación de defensa oral.
4. Descripción del Dataset
El dataset contiene:
    • 41.188 registros.
    • 21 variables.
    • 10 variables numéricas.
    • 10 variables categóricas.
    • 1 variable objetivo (suscripción a depósito a plazo).
 Bank Marketing Dataset.pdf
La variable objetivo corresponde a:
    • yes: Cliente contrató un depósito a plazo.
    • no: Cliente no contrató un depósito a plazo.
Decisión metodológica obligatoria: separar Train/Test antes del EDA y las transformaciones
Antes de realizar el análisis exploratorio detallado, la imputación, el escalamiento, la codificación o la ingeniería de características, el equipo debe dividir el dataset en un conjunto de entrenamiento (Train) y un conjunto de prueba (Test).
La razón es evitar fuga de información (data leakage): cualquier estadística aprendida del conjunto completo (medias, medianas, categorías, límites de outliers, parámetros de escalamiento, etc.) puede transferir información del Test al Train y producir métricas optimistas e inválidas.
Reglas operativas:
    1. Realizar train_test_split(...) inmediatamente después de cargar el dataset y separar X e y.
    2. Usar estratificación por la variable objetivo (stratify=y) debido al desbalance (~90/10).
    3. El EDA descriptivo inicial puede usarse para comprender la estructura general del dataset, pero todas las decisiones que aprendan parámetros deben ajustarse únicamente con el conjunto de entrenamiento.
    4. Imputadores (SimpleImputer), escaladores (StandardScaler), codificadores (OneHotEncoder / OrdinalEncoder), detectores de outliers y transformaciones estadísticas deben hacer fit solo en Train y luego transform en Train y Test.
    5. Las nuevas variables basadas en estadísticas globales también deben derivarse usando únicamente información del Train.
    6. El conjunto Test debe permanecer intocable hasta la evaluación final del pipeline.
Flujo correcto (resumen):
Este criterio debe quedar explícito tanto en el notebook como en la defensa oral, ya que forma parte de las buenas prácticas de preparación de datos para Machine Learning.
5. Metodología del Proyecto (Paso a Paso)
Etapa 0: Separación Inicial del Dataset (obligatoria)
Actividades
    1. Cargar el dataset original.
    2. Separar variables predictoras (X) y variable objetivo (y).
    3. Aplicar train_test_split con estratificación.
    4. Guardar los subconjuntos: X_train, X_test, y_train, y_test.
    5. Declarar explícitamente que X_test/y_test quedan reservados para evaluación final.
Entregables
    • Tabla con tamaños de Train/Test.
    • Proporción de clases en ambos subconjuntos.
    • Celda del notebook con el split y random_state documentado.
Etapa 1: Comprensión de los Datos (sobre Train)
Actividades
    • Revisar dimensiones de Train y Test.
    • Identificar tipos de datos.
    • Analizar distribución de la variable objetivo en Train.
    • Detectar valores nulos y valores unknown en Train.
Entregables
    • Tabla descriptiva.
    • Resumen estadístico de Train.
    • Distribución inicial de la variable objetivo en Train.
Etapa 2: Tratamiento de Datos Faltantes (fit solo en Train)
Actividades
    • Detectar valores faltantes explícitos en Train.
    • Detectar valores unknown en Train.
    • Determinar porcentaje de faltantes por variable en Train.
    • Definir técnicas apropiadas: eliminación, imputación por moda, imputación por mediana o agrupaciones lógicas.
    • Ajustar (fit) los imputadores con Train y luego transform en Train y Test.
Justificación
Explicar por qué se seleccionó cada técnica y cómo mejora la calidad de los datos sin utilizar información del Test.
EVALUACIÓN PARCIAL 4_ESTUDIANTE.pdf
Gráficos sugeridos
    • Porcentaje de valores faltantes por variable (Train).
    • Comparación antes/después de la imputación en Train.
Etapa 3: Limpieza de Datos (decisiones aprendidas en Train)
Actividades
    • Eliminar registros duplicados del Train si corresponde.
    • Revisar variables con varianza cero en Train.
    • Detectar posibles data leak.
    • Definir reglas de tratamiento de outliers usando únicamente Train.
Caso especial
La variable duration deberá analizarse cuidadosamente, ya que suele considerarse una variable que introduce fuga de información (Data Leakage).
Bank Marketing Dataset.pdf
Gráficos sugeridos
    • Boxplots (Train).
    • Histogramas (Train).
Etapa 4: Análisis Exploratorio de Datos (EDA) – Train
Análisis Univariado
Analizar individualmente cada variable en X_train:
    • Edad.
    • Educación.
    • Ocupación.
    • Estado civil.
    • Contactos realizados.
    • Euribor.
    • Campaña.
Visualizaciones
    • Histogramas.
    • Countplots.
    • Boxplots.
Meta
Generar al menos 15 gráficos durante el proyecto.
EVALUACIÓN PARCIAL 4_ESTUDIANTE.pdf
Análisis Bivariado (Train)
Usar porcentajes para comparaciones relativas entre la variable objetivo y las demás variables, priorizando tasas de conversión y no frecuencias absolutas.
Bank Marketing Dataset.pdf
Etapa 5: Escalamiento de Variables Numéricas (fit solo en Train)
Variables candidatas
    • age
    • campaign
    • pdays
    • previous
    • emp.var.rate
    • cons.price.idx
    • cons.conf.idx
    • euribor3m
    • nr.employed
Técnica
Se utilizará principalmente StandardScaler porque centra los datos en media 0 y escala con desviación estándar 1, favoreciendo algoritmos de Machine Learning.
Regla crítica
El escalador debe hacer fit(X_train_num) y luego transform(X_train_num) y transform(X_test_num). Nunca hacer fit sobre el dataset completo.
Evidencia requerida
Mostrar distribuciones antes y después del escalamiento en Train.
EVALUACIÓN PARCIAL 4_ESTUDIANTE.pdf
Etapa 6: Codificación de Variables Categóricas (fit solo en Train)
Técnicas
    • One-Hot Encoding para variables nominales: job, marital, contact, month, poutcome.
    • Ordinal Encoding para variables con orden natural: education.
Regla crítica
Los codificadores deben aprender las categorías en Train (fit) y aplicarse después a Train y Test (transform). Configurar handle_unknown='ignore' en One-Hot cuando corresponda.
Evidencia
Mostrar ejemplos de variables originales y transformadas.
EVALUACIÓN PARCIAL 4_ESTUDIANTE.pdf
Etapa 7: Ingeniería de Características (derivada desde Train)
Objetivo
Crear variables que aporten nueva información al modelo.
Propuestas
    1. Grupo Etario: edad → Joven / Adulto / Adulto Mayor.
    2. Intensidad de Contacto: combinación de campaign y previous.
    3. Contacto Previo: variable binaria Sí/No.
    4. Riesgo Económico: combinación de euribor3m y emp.var.rate.
    5. Cliente Frecuentemente Contactado: variable binaria según número de campañas.
Regla crítica
Si una nueva variable depende de umbrales, cuantiles, medias u otras estadísticas, dichos parámetros deben calcularse solo con Train y luego aplicarse a Test.
Justificación
Estas variables pueden capturar patrones que las variables originales no reflejan directamente.
Etapa 8: Construcción del Pipeline
Se implementará un pipeline automatizado utilizando Pipeline, ColumnTransformer, SimpleImputer, StandardScaler y OneHotEncoder.
Beneficios
    • Reproducibilidad.
    • Menor riesgo de errores.
    • Garantiza que fit ocurra solo en Train.
    • Escalabilidad.
Etapa 9: Evaluación del Dataset Procesado
Verificar:
    • Ausencia de valores nulos en las matrices transformadas.
    • Correcto escalamiento.
    • Correcta codificación.
    • Nuevas variables generadas.
    • Consistencia dimensional entre Train y Test.
Entregable
Dataset final listo para Machine Learning, manteniendo el Test reservado para evaluación final.
Etapa 10: Elaboración de Informe Técnico
El notebook deberá contener:
    1. Introducción.
    2. Objetivo.
    3. Descripción del dataset.
    4. Separación Train/Test y justificación anti-leakage.
    5. Tratamiento de faltantes.
    6. Escalamiento.
    7. Codificación.
    8. Ingeniería de características.
    9. Pipeline y transformaciones aplicadas.
    10. Resultados.
    11. Conclusiones.
    12. Referencias.
 EVALUACIÓN PARCIAL 4_ESTUDIANTE.pdf
6. Distribución Equitativa de Tareas
Rol A – Split, Análisis y Limpieza Inicial
Responsable: Integrante 1
Funciones
    • Comprensión del negocio.
    • Carga del dataset.
    • Separación Train/Test con estratificación y documentación del split.
    • Revisión de tipos de datos.
    • Identificación de nulos en Train.
    • Tratamiento de unknown.
    • Eliminación de duplicados.
    • Estadísticas descriptivas de Train.
    • 5 gráficos EDA.
Entregables
    • Sección Introducción.
    • Sección Dataset.
    • Sección Separación Train/Test.
    • Sección Tratamiento de Datos Faltantes.
Rol B – Transformación y Preparación de Datos
Responsable: Integrante 2
Funciones
    • Escalamiento numérico.
    • One-Hot Encoding.
    • Ordinal Encoding.
    • Comparaciones antes/después.
    • Construcción del Pipeline.
    • Verificación de que todos los fit se realicen solo en Train.
    • 5 gráficos asociados.
Entregables
    • Sección Escalamiento.
    • Sección Codificación.
    • Sección Pipeline.
Rol C – Ingeniería de Características, Validación y Presentación
Responsable: Integrante 3
Funciones
    • Creación de nuevas variables.
    • Justificación de ingeniería de características.
    • Validación del dataset final (Train y Test transformados).
    • Elaboración de conclusiones.
    • Preparación de diapositivas.
    • 5 gráficos finales.
Entregables
    • Sección Feature Engineering.
    • Sección Validación del Dataset Procesado.
    • Conclusiones.
    • Presentación oral.
7. Distribución para la Defensa Oral
Integrante	Temas
Integrante 1 (33%)	Introducción, problema de negocio, dataset, separación Train/Test y prevención de leakage, valores faltantes y limpieza de datos.
Integrante 2 (33%)	Escalamiento, codificación, pipeline y justificación técnica de fit solo en Train.
Integrante 3 (34%)	Ingeniería de características, validación del dataset final, impacto en el proyecto y conclusiones.
8. Resultado Esperado
Al finalizar el proyecto, el equipo dispondrá de un dataset completamente preparado para la construcción de modelos predictivos, con datos limpios, escalados, codificados y enriquecidos mediante ingeniería de características, sin contaminación entre Train y Test, permitiendo una evaluación válida y realista del desempeño futuro de los modelos y una mejor identificación de clientes con alta probabilidad de contratar depósitos a plazo.
Bank Marketing Dataset.pdf+1
Criterio obligatorio de aceptación
El notebook y la presentación deberán demostrar explícitamente que el train_test_split se ejecutó antes del EDA detallado y de cualquier transformación aprendida, y que imputadores, escaladores, codificadores e ingeniería de características hicieron fit únicamente sobre Train y transform sobre Train y Test. La ausencia de esta evidencia se considerará una desviación metodológica relevante.

