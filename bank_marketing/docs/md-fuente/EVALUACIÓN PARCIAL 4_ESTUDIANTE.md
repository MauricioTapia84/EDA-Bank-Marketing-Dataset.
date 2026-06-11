Evaluación Parcial N°4
Preprocesamiento de datos para un proyecto de machine learning
Estudiante

         Sigla                                 Nombre Asignatura                                   Tiempo Asignado              % Ponderación

      ADY1100                            PREPROCESAMIENTO DE DATOS                                      5 horas                       25%


1. Situación evaluativa
         Ejecución                              Entrega de
                                           X                                       X    Presentación
         práctica                               encargo




2. Instrucciones generales para el/la estudiante
 Descripción general de la evaluación:

 En equipos, trabajarás en equipos de 2-3 integrantes, con un conjunto de datos asociado al caso semestral, donde deberán realizar el tratamiento
 de datos faltantes, aplicando técnicas como imputación o eliminación, dependiendo del caso. Luego, deberán escalar las variables numéricas y
 codificar las variables categóricas utilizando métodos apropiados (por ejemplo, LabelEncoder o OneHotEncoder). Además, se solicitará que
 apliquen ingeniería de características, creando nuevas variables que puedan mejorar el rendimiento de un modelo de machine le arning. La
 evaluación consistirá en un informe técnico y una presentación explicativa de los procesos realizados, justificando cada decisión en función de los
 requerimientos del proyecto.

 La presentación será del tipo defensa oral, donde deben explicar y justificar las decisiones tomadas en el tratamiento de datos faltantes,
 escalamiento, codificación y generación de variables, destacando su impacto en el desempeño del modelo y los resultados del proyecto. Además,

Subdirección de Diseño Instruccional
 los equipos deben reflejar el aprendizaje obtenido mediante ejemplos concretos y gráficos generados con Python, integrando de forma clara y
 visual los avances logrados en el preprocesamiento de datos. La presentación debe contar con la participación equitativa y activa de todos/as sus
 integrantes, ya que será calificada de manera individual.

 La distribución de los porcentajes en esta evaluación es la siguiente:

                       Evaluación                             Tipo de situación evaluativa                Distribución de porcentajes en la Parcial
                                                    Informe técnico                                                         30%
  Parcial N°4
                                                    Presentación                                                            70%
  Total                                                                                                                    100%



 2.1. Instrucciones informe grupal:

 Formato e instrucciones generales del Informe técnico:

                •   Documento en formato .ipynb
                •   Cada bloque de código debe estar acompañado de comentarios que expliquen su propósito.
                •   El informe debe estar dividido en secciones claras, utilizar encabezados (##) y descripciones para separar cada parte del análisis.
                •   Debe tener al menos 15 gráficos que expliquen la data.
                •   Las citas y referencias deben incluirse en una sección especial para referencias.

 A través de un informe técnico grupal de tipo jupyter notebook, los equipos deberán abordar los siguientes aspectos:

      1. Identificación y justificación de técnicas de tratamiento:
                •   Expliquen cómo el tratamiento de datos faltantes asegura la integridad de los datos para su posterior uso en algoritmos de
                    machine learning.
                •   Presenten ejemplos de cómo la técnica seleccionada afectó positivamente el conjunto de datos procesado.

      2. Técnicas empleadas para la normalización y estandarización con su justificación:
             • Proporcionen ejemplos de cómo el escalamiento estandarizó las variables y permitió un desempeño sin errores de los
                 algoritmos.
             • Presenten visualizaciones (antes y después del escalamiento) que demuestren la transformación de los datos.


Subdirección de Diseño Instruccional
      3. Técnicas de codificación:
             • Detallen las técnicas empleadas (Label Encoding, One-Hot Encoding, Ordinal Encoding y categorical encoding).
             • Justifiquen por qué se seleccionó una técnica específica según las características de las variables categóricas y el modelo.

      4. Proceso de creación de nuevas variables:
             • Expliquen las técnicas aplicadas (agregaciones, transformaciones matemáticas, interacciones entre variables, etc.).
             • Justifiquen cómo estas nuevas variables aportan valor al análisis y mejoran el rendimiento del modelo.


 2.2. Instrucciones para la elaboración de la presentación:

 A través de una presentación grupal, los equipos deberán abordar los siguientes aspectos:

      1. Explicar las decisiones tomadas al tratar los datos faltantes.
             • Identificar los valores faltantes en el conjunto de datos y mostrar ejemplos concretos.
             • Justificar la técnica seleccionada (eliminación, imputación, etc.) con base en las características del dataset.
             • Explicar el impacto del tratamiento en la calidad y consistencia de los datos para el proyecto.


      2. Demostrar cómo el escalamiento de las variables numéricas mejora el desempeño de los algoritmos.
            • Explicar por qué es necesario escalar las variables numéricas en proyectos de machine learning.
            • Mostrar la técnica empleada (MinMaxScaler, StandardScaler, etc.) y justificar su elección.

      3. Justificar la selección de las técnicas de codificación y su impacto en el modelo.
             • Detallar la técnica utilizada (Label Encoding, One-Hot Encoding, etc.) y por qué fue adecuada para este caso.
             • Mostrar ejemplos de cómo los datos categóricos fueron transformados.

      4. Explicar las técnicas de ingeniería de características aplicadas.
             • Describir el proceso de creación de nuevas variables y su conexión con los objetivos del proyecto.
             • Mostrar ejemplos concretos de las nuevas variables generadas y cómo enriquecieron el dataset.




Subdirección de Diseño Instruccional
3. Pauta de Evaluación
         Categoría               % logro                                                Descripción niveles de logro

 Muy buen desempeño               100%        Demuestra un desempeño destacado, evidenciando el logro de todos los aspectos evaluados en el indicador.


 Buen desempeño                    80%        Demuestra un alto desempeño del indicador, presentando pequeñas omisiones, dificultades y/o errores.

                                              Demuestra un desempeño competente, evidenciando el logro de los elementos básicos del indicador, pero con
 Desempeño aceptable               60%
                                              omisiones, dificultades o errores.
                                              Presenta importantes omisiones, dificultades o errores en el desempeño, que no permiten evidenciar los
 Desempeño incipiente              30%
                                              elementos básicos del logro del indicador, por lo que no puede ser considerado competente.

 Desempeño no logrado                  0%     Presenta ausencia o incorrecto desempeño.




3.1. Rúbrica de Evaluación
                                                                             Categorías de Respuesta
                                                                                                                                                       Ponderación
  Indicador de Evaluación                Muy buen                                    Desempeño                  Desempeño            Desempeño no      Indicador de
                                                          Buen desempeño
                                        desempeño                                     aceptable                  incipiente             logrado         Evaluación
                                                                80%
                                           100%                                         60%                         30%                   0%

 Dimensión: Informe técnico
                                Justifica               Justifica las técnicas   Justifica de forma
 1. Justifica las técnicas                                                                                 Justifica las técnicas
                                detalladamente    las   de tratamiento de        básica las técnicas de                             No justifica las
 empleadas para tratar los                                                                                 de manera limitada o
                                técnicas          de    datos faltantes de       tratamiento de datos                               técnicas
 datos           faltantes,                                                                                incorrecta,       con
                                tratamiento de datos    manera adecuada,         faltantes,         con                             empleadas para         5%
 asegurando claridad y                                                                                     explicaciones
                                faltantes,       con    con      explicaciones   algunas omisiones o                                tratar los datos
 precisión      en       la                                                                                insuficientes        o
                                explicaciones claras,   claras y mínimas         falta de claridad en la                            faltantes.
 documentación.                                                                                            confusas y varias
                                precisas            y   omisiones.               documentación.

Subdirección de Diseño Instruccional
                                relacionadas con los                                                          omisiones   en        la
                                requerimientos   del                                                          documentación.
                                proyecto.
                                                                                     Detalla las técnicas     Detalla de manera
                                Detalla las técnicas de
                                                                                     de escalamiento de       limitada o incorrecta
                                escalamiento               Detalla las técnicas
 2. Detalla las técnicas de                                                          forma básica, con        las      técnicas    de
                                utilizadas,         con    de escalamiento, con
 escalamiento aplicadas,                                                             justificaciones          escalamiento,       sin    No detalla las
                                explicaciones claras y     mínimas omisiones o
 justificando su elección                                                            limitadas          o     justificar                 técnicas     de
                                precisas,                  errores en la relación                                                                            10%
 en función de los                                                                   explicaciones            adecuadamente        su    escalamiento
                                vinculándolas con los      con                 los
 requerimientos         del                                                          incompletas sobre su     elección ni vincularlas    utilizadas.
                                requerimientos       del   requerimientos del
 proyecto.                                                                           relación con los         con                 los
                                proyecto y destacando      proyecto.
                                                                                     requerimientos del       requerimientos      del
                                su impacto positivo.
                                                                                     proyecto.                proyecto.
                                Describe
                                detalladamente       las   Describe
                                                                                                              Describe de manera
                                técnicas             de    adecuadamente las         Describe las técnicas
 3. Describe las técnicas                                                                                     limitada o incorrecta
                                codificación utilizadas    técnicas            de    de codificación de
 de codificación utilizadas                                                                                   las     técnicas     de    No describe las
                                y analiza con precisión    codificación              forma básica, con
 y analiza cómo estas                                                                                         codificación utilizadas,   técnicas     de
                                cómo estas integran        utilizadas,       con     análisis limitado o                                                     5%
 integran las variables                                                                                       con             análisis   codificación
                                las           variables    mínimas omisiones o       incompleto sobre su
 categóricas     en     los                                                                                   insuficiente o confuso     utilizadas
                                categóricas en los         errores al explicar su    integración en los
 algoritmos.                                                                                                  sobre su integración
                                algoritmos,                integración en los        algoritmos.
                                                                                                              en los algoritmos.
                                destacando            su   algoritmos.
                                relevancia.
                                                           Detalla                   Detalla de forma
                                Detalla
                                                           adecuadamente el          aceptable el proceso     Detalla de manera
                                exhaustivamente el
 4. Detalla el proceso de                                  proceso de creación       de      creación   de    limitada o incorrecta
                                proceso de creación
 creación de nuevas                                        de nuevas variables,      nuevas variables, con    el proceso de creación     No detalla el
                                de nuevas variables,
 variables, justificando su                                destacando        su      justificaciones          de nuevas variables,       proceso        de
                                vinculándolas con los                                                                                                        10%
 relevancia      para     el                               relevancia para el        limitadas           o    sin           justificar   creación       de
                                objetivos del proyecto
 proyecto y el impacto                                     proyecto     y    su      explicaciones            adecuadamente         su   nuevas variables.
                                y    explicando     su
 esperado en el modelo                                     impacto     en     el     incompletas sobre su     relevancia     ni     su
                                impacto positivo en el
                                                           modelo, con mínimas       impacto       en    el   impacto en el modelo.
                                modelo.
                                                           omisiones o errores.      modelo.

 Dimensión: Presentación - Defensa Oral



Subdirección de Diseño Instruccional
                                Explica con claridad y
                                detalle las decisiones      Explica las decisiones
                                                                                       Explica de forma
                                tomadas al tratar los       tomadas al tratar los                                Explica de manera
 1. Explica las decisiones                                                             adecuada         las
                                datos          faltantes,   datos        faltantes,                              limitada o incorrecta
 tomadas al tratar los                                                                 decisiones tomadas                                  No explica las
                                demostrando dominio         demostrando                                          las        decisiones
 datos faltantes y cómo                                                                al tratar los datos                                 decisiones
                                técnico y relacionando      conocimiento                                         tomadas,
 estas          decisiones                                                             faltantes,      con                                 tomadas       ni
                                su impacto con los          técnico, con mínimas                                 demostrando dominio                          15%
 impactan en el proyecto,                                                              algunas omisiones o                                 responde a las
                                objetivos             del   omisiones o errores,                                 técnico básico al
 respondiendo          con                                                             respuestas                                          preguntas del/la
                                proyecto,                   respondiendo         la                              responder          las
 precisión las preguntas                                                               incompletas a las                                   docente.
                                respondiendo         con    mayoría      de     las                              preguntas       del/la
 del docente.                                                                          preguntas     del/la
                                precisión todas las         preguntas        del/la                              docente.
                                                                                       docente.
                                preguntas          del/la   docente con claridad.
                                docente.
                                Demuestra de forma                                     Demuestra         el
                                                            Demuestra cómo el                                    Demuestra          un
                                destacada cómo el                                      impacto          del                                No     demuestra
 2. Demuestra cómo el                                       escalamiento mejora                                  conocimiento limitado
                                escalamiento mejora                                    escalamiento en los                                 cómo          el
 escalamiento de las                                        el desempeño de los                                  sobre el impacto del
                                el desempeño de los                                    algoritmos,     con                                 escalamiento
 variables      numéricas                                   algoritmos,        con                               escalamiento,     con
                                algoritmos,          con                               explicaciones                                       mejora        el
 mejora el desempeño de                                     mínimas omisiones,                                   explicaciones
                                explicaciones                                          adecuadas, pero con                                 desempeño de los   15%
 los           algoritmos,                                  respondiendo         la                              insuficientes        y
                                detalladas y técnicas,                                 algunas respuestas                                  algoritmos    ni
 respondiendo          con                                  mayoría     de      las                              respuestas       poco
                                respondiendo         con                               incompletas        o                                responde a las
 precisión técnica las                                      preguntas       del/la                               precisas      a    las
                                precisión y dominio                                    incorrectas a las                                   preguntas    del
 preguntas del docente.                                     docente            con                               preguntas       del/la
                                todas las preguntas                                    preguntas     del/la                                docente.
                                                            precisión técnica.                                   docente.
                                del/la docente.                                        docente.
                                Justifica de forma          Justifica la selección                               Justifica de manera
                                destacada la selección      de las técnicas de         Justifica la selección    limitada o incorrecta
                                                                                                                                           No justifica ni
 3. Justifica la selección de   de las técnicas de          codificación,              de las técnicas de        la selección de las
                                                                                                                                           explica       la
 las        técnicas       de   codificación,               destacando           su    codificación,      con    técnicas            de
                                                                                                                                           selección de las
 codificación y su impacto      destacando             su   impacto       en      el   explicaciones             codificación,      con
                                                                                                                                           técnicas     de
 en         el       modelo,    impacto positivo en el      modelo,                    limitadas             o   explicaciones                                20%
                                                                                                                                           codificación  ni
 respondiendo preguntas         modelo,                     respondiendo          la   respuestas                insuficientes         y
                                                                                                                                           responde a las
 del docente con precisión      respondiendo         con    mayoría      de     las    incompletas a las         respuestas        poco
                                                                                                                                           preguntas del/la
 técnica.                       precisión y dominio         preguntas        del/la    preguntas        del/la   precisas      a     las
                                                                                                                                           docente.
                                todas las preguntas         docente con claridad       docente.                  preguntas        del/la
                                del/la docente.             y precisión técnica.                                 docente.
 4. Explica las técnicas de     Explica de forma            Explica las técnicas       Explica las técnicas       Explica de manera        No explica   las
 ingeniería              de     destacada las técnicas      de ingeniería de           de ingeniería de           limitada o incorrecta    técnicas     de    20%
 características aplicadas,     de      ingeniería    de    características            características, con       las    técnicas    de    ingeniería   de


Subdirección de Diseño Instruccional
 destacando cómo estas          características           aplicadas,               explicaciones          ingeniería          de    características
 contribuyen al objetivo        aplicadas, destacando     destacando         su    adecuadas,     pero    características,          aplicadas.
 del             proyecto,      su contribución al        contribución        al   respuestas             demostrando
 respondiendo         con       proyecto              y   proyecto             y   incompletas        o   conocimiento
 precisión técnica.             respondiendo       con    respondiendo        la   incorrectas a las      técnico básico al
                                precisión       técnica   mayoría     de    las    preguntas     del/la   responder           las
                                todas las preguntas       preguntas      del/la    docente.               preguntas        del/la
                                del/la        docente,    docente con claridad,                           docente.
                                reflexionando sobre       con          mínimas
                                los       aprendizajes    omisiones o errores.
                                obtenidos.
                                                                          Total                                                                       100%




Subdirección de Diseño Instruccional
