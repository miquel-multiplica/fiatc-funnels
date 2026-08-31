# FIATC Salud · Backlog de quick wins

> Base de diseño: el **prototipo de la propuesta** (`propuesta/wireframe_propuesta.html`).
> Estos quick wins se materializan evolucionando ese prototipo hasta la versión final acordada.
> Presupuesto de diseño: **40h** para diseñar el funnel con quick wins.
> Todos validados con IT (28 jul) salvo indicación. Ordenados por fuga que atacan.
> Evidencia: ATC = respuestas Atención al Cliente · WT = walkthrough negocio · IT = sesión técnica · GA4 = tabla funnel 2025 · Diana/Anabel = datos negocio.

## Fuga 3 · Página de resultados (prioridad 1 — muro del 63-72%)

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 1 | **Efecto calculadora**: editar asegurados y modalidad desde resultados sin re-cotizar | WT (leads duplicados confirmados) + ATC (simulaciones que piden: recién nacido, quitar hijo, cambiar a copago) | "No habría problema" | Reduce además duplicidad de oportunidades |
| 2 | **Mensaje dual por audiencia**: portabilidad ("sin carencias desde el día uno") condicional para el ~40% que viene de cía + argumentario primer-seguro (rapidez, listas de espera, desde cuándo) para el ~59% | Anabel (40/59 split) + ATC (disparadores) | Estaban mirando datos → recibidos | Reformulado: condicional/dual, NO mensaje universal |
| 3 | **Cards de producto más completas + modal de detalles** | ATC (comparan sesiones psicología, pediatras, ginecólogos, garantías) | Sí — web y área privada ya tienen contenido que sirve | Pedir ese contenido a FIATC |
| 4 | **Claridad del precio**: tramos y cuándo aplican, total vs. persona, renovación, vencimiento, si el CP afecta | ATC (lista de malentendidos) | Copys sin problema | |
| 5 | **Guardar/compartir presupuesto visible** | ATC (decisión consultada en pareja, multi-sesión) + WT (casi nadie recupera) | El email ya existe | El gap es visibilidad y momento, no infraestructura |
| 6 | **Anticipación del proceso**: "100% online, X min, necesitarás DNI, incluye breve cuestionario de salud" | Fuga 4 (8% cae tras el clic) + ATC (abandonos al descubrir el cuestionario) | Copys sin problema | Ablanda también la fuga 4 |
| 7 | **Badges de orientación** (el más popular, etc.) | Lista quick wins específicos | Sí — contenido existente sirve | Validar etiquetas con negocio/legal (riesgo de rozar asesoramiento) |
| 8 | **Limpieza legacy**: quitar pestañas "Información/Calcula tu seguro", corregir Diagonal (no mostrar fuera de regla, o nombre sin botón) | WT (confirmado por negocio) | Trivial | |
| 9 | **Píldoras de social proof** | Lista transversal | "Podría ser genérico" ⚠ | Conflicto con principio de fidelidad: decidir con negocio claim real |
| 10 | **Mostrar ahorro en periodicidad de pago** | WT (anual "muy raro" pese a 4% dto.) | Sin problema | Apuesta de bajo coste; el incentivo puede ser irrelevante para este comprador |

## Fuga 2 · Consentimiento (-22/30%)

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 11 | Sugerencias de dominio al introducir email | Lista específicos | "Podríamos hacerlo" | Micro-mejora sin riesgo |
| 12 | **Diagnóstico Clarity antes de más recetas** (¿abandonan sin interactuar? ¿campo concreto? ¿checkbox?) | Causas desconocidas; anomalía marzo 70,1% | N/A (nuestro) | Prerequisito para intervenir este paso |

## Fuga 4 · Arranque de contratación (8% de leads cae entre clic y firma)

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 13 | Progreso visible + resumen sticky | Lista transversal | "Podríamos hacerlo" (sticky viable; iframe removible) | |
| 14 | Microcopy contextual en campos críticos | ATC (material listo: malentendidos, conceptos) | "Podríamos añadirlo" | Contenido de ATC, no inventado |
| 15 | Modal "Hablemos": teléfono / agendar llamada / WhatsApp (cuando esté) | WT (negocio quiere agendación como modal) | Call-me-back: "se podría proponer" | |
| 16 | Modal exit-intent con canales de ayuda | Lista transversal | "Podríamos hacerlo" | Combinar con pausa servida (guardar/compartir), no solo cerrar salidas |
| 17 | Mejorar patrón "copiar datos del titular" y selección asegurados/edades | Lista específicos | Front, sin problema | |

## Cuestionario de salud + pantalla KO

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 18 | Progreso por asegurado, preguntas una a una ("como Lemonade") | WT (petición espontánea de negocio) | "A nivel front, podría hacerse" | |
| 19 | Copy de tranquilización: "no es vinculante, puedes aportar informes, puedes rehusar" | ATC (guion verbal actual) | "Podemos aplicarlo" | Confirmar circuito de aprobación (legal/médico) — repregunta enviada a ATC |
| 20 | Lista de lo que NO hay que declarar (apendicitis, amigdalitis, parto, cesárea) | ATC | "Podemos aplicarlo" | Confirmar si la lista es oficial/completa — repregunta enviada |
| 21 | Máscara/placeholder peso y altura (sin comas ni puntos) | ATC (error nº1 del cuestionario) | "Podemos aplicar el formato" | El más barato de toda la lista |
| 22 | **Pantalla KO pedagógica**: qué pasará, cuándo llama Teladoc (1-2 días valle, más en campaña), quién es Teladoc, que es una ampliación normal | WT (112 KOs = mayor estado interno; "podríamos ser más pedagógicos") | "Podemos hacerlo" | |

## Post-venta / comunicación

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 23 | **Recordatorio post-emisión con checklist de documentación de derogación** (email; WhatsApp cuando esté) | WT (emiten sin doc; el usuario descubre carencias al denegársele una prueba) + ATC (reciben doc "que no tiene nada que ver") | Marketing Cloud (por confirmar detalle) | Aplica al ~40% de portabilidad — urgente |
| 24 | **Módulo opcional de subida de documentación de derogación**, en la pantalla que aparece tras declarar que viene de otra entidad: para quien la tenga a mano, indicando que tendrá que ser validada. Sin bloqueo para quien no la tenga | WT + IT | **"Podríamos añadir la documentación en el funnel"** | Complementa (no sustituye) el recordatorio 23, que cubre a quien no sube nada en el momento |
| 25 | Email de presupuesto como vehículo de retorno | WT/IT (existe, enlace aterriza en precio, casi nadie lo usa) | Confirmar editabilidad en Marketing Cloud | Auditar contenido actual con cotización de prueba |

## Modelo de contacto

| # | Quick win | Evidencia | Viabilidad IT | Notas |
|---|---|---|---|---|
| 26 | Agendación de llamada en el funnel (modal, elección de momento por el usuario) | WT (requisito negocio) + Ley ATC | "Se podría proponer" | Fase 1 de canales; WhatsApp = fase 2 |

## Caídos / aplazados

| Qué | Motivo | Destino |
|---|---|---|
| NIE/pasaporte en el formulario | Decisión de negocio, no técnica | Pregunta estratégica a negocio (ATC: ese perfil hoy llama; ¿cuánta venta se pierde/deriva?) |
| **Todo el flujo "ya cliente"** (pre-rellenado, ruta diferenciada) | De momento no se puede hacer nada en esta fase | Backlog |
| Descuento cliente visible junto al precio | Depende de legal + scoring | Carril B (con sponsor interno) |
| WhatsApp en el funnel | Herramienta no lista, datos no viajan bien | Fase 2, tras agendación |
| Cambio del proceso de firma (unificar/mover) | "Medio plazo, probar tiempos" | Carril B |

## Pendientes de información

| Qué | Quién |
|---|---|
| Confirmar tabla portabilidad: ¿sobre emisiones? ¿mismo split sobre cotizaciones? | Anabel/Diana |
| Diagnóstico Clarity: fugas 1 (arranque), 2 (consentimiento) y tramo clic→firma | Nosotros |
| Cuadro funnel temporada alta (oct-dic) | Analítica FIATC |
| Instrumentación paso a paso de la contratación (hoy no existe) | Propuesta nuestra — plan de medición |
| Claim de social proof real vs. genérico | Negocio |
| Contenido del área privada reutilizable para cards/modales | Pedir a FIATC |
| Respuestas a las 18 repreguntas de ATC (Start, firma, WhatsApp ATC, validez cotización...) | ATC |
| Tema legal del cliente identificado | FIATC (en curso) |
| ¿Estados W = foto o acumulado? | Diana |

## Ajustes y nuevos (revisión de prototipo con cliente, 31 jul 2026)

- **NUEVO · Banner de campaña "2 meses gratis" ("quita y pon")** — mostrar de **septiembre a febrero** en **inicio, resultados y periodicidad de pago**.
  - **Cómo funciona la campaña** (contexto FIATC): el requisito aplica a la **fecha de contratación** (efecto de póliza dentro del periodo de campaña), NO a la fecha de inicio. El **inicio de cobertura puede diferirse ~2-3 meses** desde la firma (p. ej. para esperar al vencimiento de la póliza anterior); si se pasa de ese margen, se pierde la promo. Gama Medifiatc (excepto dental, colectivos, grupos con tarifa especial, federaciones). Abono en 2 pagos en cuenta.
  - **Copy del banner** → sobre la contratación: *"Si contratas antes del [fecha]"* (no "como fecha de inicio").
  - **Tags en las fechas de inicio** (decisión: *badge en todas las que aplican*): si ambas fechas caen dentro del margen → badge en las dos; si una sí y otra no → badge solo en la que entra; si ninguna (fuera de temporada) → sin banner ni badge.
- **Fecha de inicio** — se mantiene (determina cobertura). Valorar badge tipo "En promoción".
- **DOB en contratación** — campos de fecha de nacimiento **deshabilitados** (vienen de la tarificación); mensaje "para cambiarla, vuelve a tarificar".
- **QW#18 cuestionario** — al marcar "Sí" → **textarea**; presentación **progresiva** (aparece la siguiente pregunta + scroll de foco; se puede revisar hacia arriba).
- **QW#24 derogación** — añadir la **pantalla del PPT** (solo si "Sí") con el copy oficial + **subida opcional de documentos** (póliza anterior o tarjeta con fecha de alta + último recibo; email web@fiatc.es).
- **Pago (Sabadell iframe)** — **unificar** el "ir a pagar" con los datos legales del precio del paso anterior; dejar el **TPV en un paso limpio** aparte.
- **Confirmación** — docs no descargables aún; si pagó → "ya eres de FIATC"; **priorizar descarga de la app** vs. alta de cliente; **aligerar** la pantalla + avisar de **correo para firmar**.
- **Descuentos ya cliente** — fase 2 (login/recuperar datos). En quick wins, **copy genérico sin mencionar descuentos** (paso "Identifícate como cliente").
- **WhatsApp** — sin canal a corto plazo en capas de contacto (**ocultar pero mantener código documentado**); **mantener la captación de consentimiento** de WhatsApp. Futuro: agente en vivo / agente de salud.

## Mapeo doc ATC v2 (23 jul 2026) → pills/FAQs y pendiente de flujo

> Repaso del doc v2 contra lo construido. Detalle de fuentes en `02-hallazgos-clave.md` (sección "Actualización doc ATC v2").

**A resolver como PILLS / FAQs contextuales** (las 5+ dudas más repetidas tras cotizar — pág. 4 del doc)
- **En resultados** (antes de decidir): ¿desde cuándo estoy cubierto? (carencias) · ¿tengo acceso a todo desde el principio? · ¿el precio es por persona o total? ✅ (ya) · ¿sube en la renovación? · ¿cuándo vence (mes de contratación vs. año natural)? · ¿el CP afecta al precio? · validez del presupuesto (15 días).
- **En/junto al cuestionario**: ¿qué pasa si declaro una patología? (¿afecta al precio?, ¿me obliga a contratar?, ¿cómo sigue?, ¿cómo recibo el resultado?) · ¿qué NO declarar? (apendicitis…) ✅ (ya en el modal, pendiente confirmar publicación).
- **En confirmación / post-venta**: ¿cuándo recibo la tarjeta? · ¿cómo uso el seguro sin tarjeta física? · ¿cuándo es el primer cargo? · ¿cómo consulto el cuadro médico? · ¿cómo pido cita (online/tel/presencial)?
- Revisar solape con el set actual `FAQS = { resultados, asegurados }` antes de añadir; priorizar las de resultados y las del cuestionario.

**Pendiente de FLUJO (mejoras no resueltas aún)**
- **Claridad de precio (resto de QW#4)**: renovación, vencimiento, promocional vs. captación, baja con exclusión, si el CP afecta → capa/acordeón de "cómo funciona este precio" o FAQs.
- **NIE / pasaporte**: online solo DNI. Añadir en el paso de identificación/tomador un **desvío claro** ("¿Tienes NIE o pasaporte? Te atendemos por teléfono/agenda"), en vez de dejar que choque.
- **Pago bancario**: online es TPV, pero se puede pedir domiciliación. Valorar microcopy en el paso de pago ("¿Prefieres domiciliación? Te ayudamos por teléfono").
- **Firma (cFirma) — HECHA (simulada)**: modal de confirmación ("¿Confirmas el envío?") + **caja gris placeholder** "PROCESO DE FIRMA" (el iframe Evicertia real no se diseña) con loading 5 s que avanza solo. Real: teléfono → confirmar → PIN por SMS → Evicertia. 2ª firma = contrato por email post-pago (avisar en confirmación).
- **Derogación (QW#24)**: doc = último recibo + copia de tarjeta; si la tarjeta no tiene fecha de alta → + recibo de hace un año. Email web@fiatc.es.
- **KO pedagógica (QW#22)**: sin construir.
- **Simulaciones** (añadir recién nacido, quitar hijo, añadir asegurado que vence, completa↔copago): cubierto por la **calculadora** (add/quitar) + pestañas de modalidad; validar que cubre los casos.
- **"El usuario no lee / pierde la pantalla"**: principio transversal → no abrir ventanas nuevas, no perder el contexto de tarificación (ya respetado en el prototipo con modales/capas).
