# Clasificacion de Incidentes segun ISO/IEC 25022 (Escenario 2)

Fuente de datos: `incidentes_2025_iso_25022.csv` (3000 incidentes). Clasificacion generada por
`scripts/clasificar_incidentes.py` mediante un motor de reglas (patrones exactos
y expresiones regulares) sobre las 244 descripciones unicas del dataset, y
aplicada a las 3000 filas. Dataset completo clasificado en `data/incidentes_2025_clasificados.csv`.

## Tabla 2.2: Clasificacion de incidentes (una fila por tipo de incidente real)

### Efectividad (1197 incidentes, 39.9% del total)

| ID | Descripcion | Modulo | Justificacion tecnica |
|---|---|---|---|
| 3347 | Version desactualizada del app impide iniciar sesion | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2368 | La app no permite actualizar el numero de contacto del paciente | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3522 | La aplicacion se cierra inesperadamente al abrir resultados de laboratorio | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1737 | El boton de teleconsulta no redirige correctamente a la videollamada | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2445 | El inicio de sesion con biometria falla de forma intermitente | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1632 | Resultados de examenes no se visualizan en formato PDF | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2415 | Notificaciones push no llegan pese a estar activadas | App Movil | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2020 | El sistema no reconoce el convenio con la aseguradora | Facturacion | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2209 | El sistema no permite anular una factura emitida por error | Facturacion | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2008 | El modulo de facturacion se cae durante el cierre de caja | Facturacion | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3173 | Factura electronica no llega al correo registrado del paciente | Facturacion | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3832 | El sistema bloquea la dispensacion sin mostrar el motivo | Farmacia | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3291 | Perdida de la nota de evolucion tras un cierre inesperado de sesion | HCE | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3900 | El campo de diagnostico CIE-10 no permite busqueda por texto | HCE | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1369 | El sistema se congela al adjuntar resultados de laboratorio a la HCE | HCE | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1280 | Las imagenes de rayos X no cargan en el visor DICOM | Imagenologia | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1246 | El sistema no permite adjuntar el reporte en PDF del laboratorio externo | Laboratorio | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1509 | El sistema no envia la confirmacion por correo electronico | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3934 | Filtro de especialidad medica no devuelve resultados | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1340 | Error al reagendar una cita previamente confirmada | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3011 | Notificacion de recordatorio de cita llega con la fecha incorrecta | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3978 | Usuario no logra agendar tras 3 intentos | Portal Citas | El usuario no logra completar su objetivo (agendar la cita) pese a reintentar: fallo de Efectividad. |
| 1073 | Sesion expira antes de finalizar el proceso de agendamiento | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3852 | Cita agendada no aparece reflejada en el calendario del especialista | Portal Citas | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1986 | El reporte de ocupacion hospitalaria no se actualiza automaticamente | Reportes Gerenciales | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2863 | Exportacion a Excel del reporte gerencial falla de forma intermitente | Reportes Gerenciales | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2154 | El dashboard de indicadores no refleja los datos del ultimo cierre | Reportes Gerenciales | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3137 | El chat de la consulta no permite enviar imagenes | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 3147 | Grabacion de la consulta no se almacena correctamente | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2294 | El medico no puede compartir pantalla con resultados de examenes | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1473 | La sesion se cierra automaticamente antes de terminar la consulta | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 2349 | Receta electronica no se genera al finalizar la teleconsulta | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |
| 1066 | Videollamada se corta a los 4 minutos | Telemedicina | La teleconsulta (tarea) no se completa: el objetivo del usuario queda inconcluso, por lo tanto es Efectividad. |
| 2488 | Paciente no puede unirse a la sala virtual a la hora agendada | Telemedicina | El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo. |

### Eficiencia (360 incidentes, 12.0% del total)

| ID | Descripcion | Modulo | Justificacion tecnica |
|---|---|---|---|
| 3155 | Consumo elevado de datos moviles al abrir el modulo de citas | App Movil | Mide el consumo de un recurso (datos moviles) necesario para lograr una tarea que si se completa, encajando en la relacion recursos/resultado de Eficiencia. |
| 1321 | Retraso de 11s al procesar el pago con tarjeta de credito | Facturacion | El pago se procesa (objetivo logrado); el problema es el tiempo invertido, metrica de Eficiencia. |
| 1056 | Tiempo de respuesta del modulo de farmacia supera los 31s | Farmacia | Es un umbral de tiempo de carga/respuesta frente a una tarea que si se completa; corresponde a Eficiencia, no a Efectividad. |
| 1062 | Tiempo de carga de la ficha clinica supera los 23s en horas pico | HCE | Es un umbral de tiempo de carga/respuesta frente a una tarea que si se completa; corresponde a Eficiencia, no a Efectividad. |
| 1441 | Nota de evolucion tarda 10s en guardarse | HCE | Mide el tiempo que toma completar una tarea ya lograda (guardar la nota); es una razon tiempo/tarea, propia de Eficiencia. |
| 1134 | Tiempo de carga de estudios de imagen supera los 18s | Imagenologia | Es un umbral de tiempo de carga/respuesta frente a una tarea que si se completa; corresponde a Eficiencia, no a Efectividad. |
| 1110 | Retraso de 18s en la disponibilidad de resultados criticos | Laboratorio | Mide el tiempo hasta disponibilidad del resultado; es una metrica temporal (Eficiencia), aunque un retraso extremo deberia escalarse tambien como alerta de riesgo clinico. |
| 2057 | Tiempo de espera en el portal supera los 11s en horas pico | Portal Citas | Es un umbral de tiempo de carga/respuesta frente a una tarea que si se completa; corresponde a Eficiencia, no a Efectividad. |
| 2467 | Tiempo de generacion del reporte mensual supera los 25 minutos | Reportes Gerenciales | Mide duracion de un proceso que se completa (generacion de reporte); recursos (tiempo) usados para lograr el objetivo. |
| 1548 | Notificacion de inicio de teleconsulta llega con retraso de 13s | Telemedicina | Metrica de tiempo sobre una notificacion que si llega; corresponde a Eficiencia. |

### Satisfaccion (138 incidentes, 4.6% del total)

| ID | Descripcion | Modulo | Justificacion tecnica |
|---|---|---|---|
| 3266 | Perdida de calidad en las imagenes al ser visualizadas desde la app | Imagenologia | El sistema puede seguir siendo usable, pero degrada la percepcion de comodidad/confianza del usuario (calidad de experiencia), sin impedir totalmente la tarea ni exponer un riesgo concreto. |
| 2017 | Formulario confuso, abandono de registro antes de completar la cita | Portal Citas | El sistema puede seguir siendo usable, pero degrada la percepcion de comodidad/confianza del usuario (calidad de experiencia), sin impedir totalmente la tarea ni exponer un riesgo concreto. |
| 3262 | Audio desincronizado durante la teleconsulta | Telemedicina | El sistema puede seguir siendo usable, pero degrada la percepcion de comodidad/confianza del usuario (calidad de experiencia), sin impedir totalmente la tarea ni exponer un riesgo concreto. |
| 3430 | Calidad de video muy baja pese a tener buena conexion a internet | Telemedicina | El sistema puede seguir siendo usable, pero degrada la percepcion de comodidad/confianza del usuario (calidad de experiencia), sin impedir totalmente la tarea ni exponer un riesgo concreto. |

### Libertad de Riesgo (1221 incidentes, 40.7% del total)

| ID | Descripcion | Modulo | Justificacion tecnica |
|---|---|---|---|
| 1120 | Nota de credito no se aplica al saldo pendiente del paciente | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3543 | Reintento de transaccion genera doble cobro en la tarjeta | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1610 | Error de calculo en el copago del seguro medico | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1567 | Reembolso aprobado no se refleja en el estado de cuenta | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3348 | Factura generada con el nombre del paciente incorrecto | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3411 | Factura duplicada al reintentar pago | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1123 | Discrepancia entre el monto facturado y el detalle de servicios | Facturacion | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1786 | Duplicidad de codigos entre dos presentaciones distintas de un mismo farmaco | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1072 | Alerta de vencimiento de lote no se muestra en el modulo | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1904 | El sistema no descuenta automaticamente el medicamento dispensado | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 2371 | Error al registrar la dispensacion de un medicamento controlado | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1670 | Receta electronica llega incompleta desde el modulo de HCE | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1814 | Inventario del sistema no coincide con el stock fisico del insumo | Farmacia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1210 | Historial de alergias no carga al abrir la ficha del paciente | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 2416 | Signos vitales registrados por enfermeria no aparecen en la HCE del medico | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3846 | Datos de otro paciente visibles brevemente al abrir un expediente | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3980 | Receta electronica se genera con la dosis incorrecta tras guardar | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1075 | Orden medica no se sincroniza con el modulo de farmacia | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1377 | Alerta de interaccion medicamentosa no se despliega correctamente | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1530 | Duplicado de historia clinica al registrar un paciente ya existente | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3617 | Consulta anterior no se muestra en el resumen de antecedentes | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 2334 | Firma electronica del medico no se valida al cerrar la consulta | HCE | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 2857 | El informe radiologico no se adjunta automaticamente a la HCE | Imagenologia | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3640 | Orden de laboratorio duplicada tras reintentar el envio | Laboratorio | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1306 | Resultado de examen de laboratorio no se sincroniza con la HCE | Laboratorio | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3506 | Codigo de barras de la muestra no es reconocido por el lector | Laboratorio | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 2235 | Doble reserva de un mismo cupo por dos pacientes distintos | Portal Citas | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3791 | El pago del bono de consulta no se refleja tras completarlo | Portal Citas | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3177 | El portal muestra disponibilidad para un horario ya ocupado | Portal Citas | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 3959 | Cancelacion de cita no libera el cupo en el calendario | Portal Citas | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |
| 1196 | Discrepancia entre el reporte financiero y el modulo de facturacion | Reportes Gerenciales | Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad). |

### Cobertura de Contexto (84 incidentes, 2.8% del total)

| ID | Descripcion | Modulo | Justificacion tecnica |
|---|---|---|---|
| 1151 | El sistema no permite adjuntar imagenes de heridas desde la tablet | HCE | El fallo solo se manifiesta en un contexto de uso especifico (tipo de dispositivo/canal), lo que evidencia que el sistema no mantiene su calidad fuera del contexto principal de diseno. |
| 2196 | Boton de confirmar cita no responde en dispositivos moviles | Portal Citas | El fallo solo se manifiesta en un contexto de uso especifico (tipo de dispositivo/canal), lo que evidencia que el sistema no mantiene su calidad fuera del contexto principal de diseno. |

## Resumen cuantitativo por caracteristica

| Caracteristica ISO/IEC 25022 | Incidentes | % del total |
|---|---|---|
| Efectividad | 1197 | 39.9% |
| Eficiencia | 360 | 12.0% |
| Satisfaccion | 138 | 4.6% |
| Libertad de Riesgo | 1221 | 40.7% |
| Cobertura de Contexto | 84 | 2.8% |

## Incidentes por modulo y caracteristica

| Modulo | Efectividad | Eficiencia | Satisfaccion | Libertad de Riesgo | Cobertura de Contexto |
|---|---|---|---|---|---|
| App Movil | 241 | 37 | 0 | 0 | 0 |
| Facturacion | 129 | 35 | 0 | 261 | 0 |
| Farmacia | 32 | 34 | 0 | 192 | 0 |
| HCE | 155 | 111 | 0 | 456 | 47 |
| Imagenologia | 52 | 28 | 37 | 34 | 0 |
| Laboratorio | 41 | 30 | 0 | 95 | 0 |
| Portal Citas | 271 | 38 | 35 | 164 | 37 |
| Reportes Gerenciales | 53 | 16 | 0 | 19 | 0 |
| Telemedicina | 223 | 31 | 66 | 0 | 0 |


## Actividad para el Estudiante: incidente "datos de otro paciente visibles"

Caso real del dataset (id `3846`, modulo `HCE`):
*"Datos de otro paciente visibles brevemente al abrir un expediente"*.

**¿Por que corresponde a Libertad de Riesgo y no a Efectividad, a pesar de tratarse
tambien de un error del sistema?** Porque la pregunta que define Efectividad es
"¿el usuario logro su objetivo?" -- en este caso el medico si pudo completar su
tarea (abrir el expediente). El problema no es la tarea del usuario que la reporta,
sino que el sistema **expuso datos clinicos de un tercero**, lo cual es un riesgo de
privacidad y cumplimiento normativo (proteccion de datos en salud) independiente
de si la tarea original se completo o no. La misma logica aplica al incidente
id `1210` (*"Historial de alergias no carga al abrir la ficha del paciente"*): que no cargue el
historial de alergias no es solo una falla funcional, es una condicion que puede
llevar a que el medico prescriba un medicamento contraindicado -- un riesgo clinico,
no solo una tarea incompleta.

## Preguntas de Discusion

**1. ¿Puede un sistema ser efectivo pero no eficiente? De un ejemplo del caso MediSalud.**

Si. Por ejemplo, "Nota de evolucion tarda 28s en guardarse": el medico logra
guardar la nota (Efectividad cumplida, la tarea se completa), pero el tiempo
invertido excede por mucho el umbral RNF-01 (8s en el 90% de los casos), por lo
que el sistema es efectivo pero deficiente en Eficiencia.

**2. ¿Por que la Cobertura de Contexto es especialmente relevante para una red
hospitalaria con sedes en cinco ciudades distintas?**

Porque MediSalud no opera en un unico contexto: cada sede (Quito, Guayaquil,
Cuenca, Ambato, Manta) puede tener conectividad, dispositivos y volumen de
usuarios distintos. Un modulo que funciona bien en Quito (mejor infraestructura)
podria fallar en Manta; y canales como el portal movil introducen contextos de
uso (dispositivos, redes moviles) no siempre contemplados en el diseno original.
Los incidentes de tipo "Cobertura de Contexto" (p. ej. boton de confirmar cita que no
responde en moviles, adjuntar imagenes desde tablet) muestran que la calidad
del sistema no es uniforme entre contextos, lo cual justifica medir
explicitamente esta caracteristica y no asumir que un resultado positivo en
un contexto se replica en todos.

## Conclusiones Parciales

La clasificacion basada en reglas sobre las 78
patrones de incidente identificados en los datos reales confirma el patron de
confusion mencionado en el taller: una lectura superficial tenderia a marcar la
mayoria de estos incidentes como "Efectividad", pero al aplicar la pregunta guia
("¿logro su objetivo?" vs "¿a que costo o riesgo lo logro?") una parte importante
se reclasifica como Eficiencia (temporizaciones) o Libertad de Riesgo (seguridad
clinica, financiera y de privacidad). Esto valida que ISO/IEC 25022 aporta un
vocabulario comun que evita reportar todos los problemas de forma ambigua como
"el sistema falla".
