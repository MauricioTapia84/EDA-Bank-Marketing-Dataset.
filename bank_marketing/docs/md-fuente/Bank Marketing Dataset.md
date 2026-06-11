                         Bank Marketing Dataset
                                  Exploratory Data Analysis


Introduction
Banco Financiero Global busca anticipar qué clientes se suscriben a depósito a plazo, para
ello recolectaron datos entre mayo 2008 y noviembre 2010 con el objetivo de encontrar
patrones en los comportamientos de sus clientes y así optimizar sus campañas de
marketing.


Problema
Baja tasa de conversión (10% app) pese a la alta inversión publicitaria en call center.


Objetivo
   ●​ Reconocer las características (features) de los clientes que contratan un depósito a
      plazo.
   ●​ Construir un modelo predictivo para identificar clientes con mayor propensión a
      suscribir un depósito a plazo.


Dataset
41.188 filas y 21 columnas; 10 columnas numéricas y 10 columnas categóricas además de
la variable objetivo que distingue a quienes se suscriben a un depósito a plazo.


Preprocesamiento
Datos faltantes escondidos como Unknown (desconocidos o no?), eliminar data leaker,
transformación, agrupamiento, capear outliers, imputación de valores faltantes, eliminar
duplicados


Análisis Univariado
   ●​ Variable objetivo; desbalanceo de clases 90% vs 10%
   ●​ Variables desechables; duración de la llamada Data Leaker
   ●​ Graficar cada variable (20) mostrando alguna q nos llame la atención: Edad
      (jubilados), número de contactos (valores extremos), nivel de educación (alta)
   ●​ Nombre de los ejes, títulos y categorías
   ●​ Unidad de medida Tasa de Eur… , conteo, porcentajes, segundos, años
   ●​ Varianza cero
Análisis Bivariado
Usar porcentajes para comparaciones relativas
   ●​ Variable objetivo contra todas las demás variables (20), incluyendo coeficiente de
       correlación: Edad o grupo etario, cantidad de contactos, existencia de contacto
       previo, tipo de trabajo, nivel educativo,canal de contacto, resultado de campaña
       anterior, mes de contacto (mayo), tasa de Euribor
   ●​ Usar gráficos comparaciones relativas (Tasa de conversión); frecuencia relativa vs
       frecuencia absoluta


Análisis Multivariado
   ●​ Matriz de correlación; v. objetivo contra todas las demás (Spearman y Cramer)
   ●​ multicolinealidad entre predictores; variables macroeconómicas


Pipeline
   ●​ Limpieza, Na, duplicados
   ●​ Transformacion One Hot Encoding, Standard Scaler


Machine Learning
   ●​   Problema: clasificación
   ●​   Modelo: RL RF XGboost
   ●​   Métricas de desempeño:
   ●​   Metodología de Validación:


Conclusiones
   ●​ ¿Es posible crear un modelo predictivo?
   ●​ Cuales son los principales predictores; ¿que caracteriza a un cliente que contrata un
      depósito a plazo?
   ●​ Variables descartadas
   ●​ Contexto económico
