# Funnel de Salud — lógica condicional, en formato de escenarios

Las **asunciones de comportamiento** que hace el prototipo, escritas para que **IT las
confirme o las corrija punto por punto**. Formato OpenSpec adaptado:

- **Asunciones** (`A-`) — qué asume el prototipo, sin detalles de implementación.
- **Escenarios** (`ESC-`) — casos verificables (Given / When / Then).

> **Por qué dice "asume" y no "debe".** Este es un entregable de **diseño y UX**. Las reglas
> de negocio —cuándo derivar a revisión médica, cuándo cobrar, qué validaciones aplican— las
> decide FIATC y las implementa IT. Lo que hay aquí es lo que el prototipo da por supuesto
> para poder enseñar el recorrido completo: una lista para validar, no una especificación que
> imponemos.

**Este documento es el único propietario de la lógica condicional.** El mapa de pantallas, el
porqué de cada decisión de diseño y las convenciones están en
`conceptualizacion/FUNCIONAL.md`, que apunta aquí y no la duplica.

Cada bloque lleva su **estado**: `decidido` (acordado con negocio), `pendiente` (falta que
alguien se pronuncie) o `simulado` (el prototipo lo finge para la demo).

---

## F-01 · Navegación por los dos flujos · `decidido`

### Asunciones

- A-01.1 El prototipo asume **dos flujos independientes**, cada uno con su propia barra de
  progreso: tarificación (`step0` → `step6b`, y de ahí a resultados) y contratación
  (`cDatos` → `cConfirm`).
- A-01.2 El orden de tarificación es: `step0` · `stepCP` · `step1` · `step2` · `step4` ·
  `step5` · `[stepDNI]` · `step6` · `step6b` → pantalla de espera → `step7`.
- A-01.3 El orden de contratación es: `cDatos` · `cContacto` · `cDireccion` · `cAseg1` ·
  `cAseg2` · `cCuestionario` · `cTelefono` · `cFirma` · `cOtra` · `[cDerogacion]` · `cPago` ·
  `cAntes` · `cTPV` · `cConfirm`.
- A-01.4 Los pasos entre corchetes son condicionales y **se saltan en los dos sentidos**:
  tanto al avanzar como al volver atrás.
- A-01.5 Solo hay **una pantalla activa a la vez**. La navegación no cambia de URL ni recarga.

### Escenarios

**ESC-01.A — Salto de un paso condicional al avanzar**
- Given: el usuario está en el paso anterior a uno condicional que no le corresponde
- When: avanza
- Then: aterriza en el siguiente paso aplicable, sin ver el condicional

**ESC-01.B — Salto de un paso condicional al retroceder**
- Given: el usuario está en el paso posterior a uno condicional que no le corresponde
- When: pulsa atrás
- Then: aterriza en el paso aplicable anterior, sin ver el condicional

> **A confirmar con IT**: hoy el prototipo no gestiona el botón atrás **del navegador**, que
> saca del funnel entero. En el funnel real debería retroceder un paso.

---

## F-02 · ¿Ya es cliente de FIATC? · `decidido`

### Asunciones

- A-02.1 El prototipo pregunta en `step5` si la persona ya es cliente.
- A-02.2 Si responde que **sí**, asume que hay que pedirle el DNI en `stepDNI`.
- A-02.3 Si responde que **no**, `stepDNI` no existe para ese recorrido.
- A-02.4 El prototipo **no hace nada con el DNI**: no lo valida ni recupera datos previos del
  cliente. Qué se hace con él es decisión de IT.

### Escenarios

**ESC-02.A — Cliente existente**
- Given: el usuario está en `step5`
- When: responde que ya es cliente
- Then: el siguiente paso es `stepDNI`

**ESC-02.B — Cliente nuevo**
- Given: el usuario está en `step5`
- When: responde que no es cliente
- Then: el siguiente paso es `step6`, sin pasar por `stepDNI`

---

## F-03 · Los dos permisos · `pendiente de jurídico`

Son **dos cosas de naturaleza distinta** y están en pantallas separadas a propósito. El
porqué está en `FUNCIONAL.md` §2.

### Asunciones

- A-03.1 En `step6` el prototipo pide **consentimiento comercial**: opt-in para recibir
  información sobre productos y ofertas, con texto legal y "Leer más".
- A-03.2 Ese consentimiento es **de un solo canal, email**. El prototipo asume que FIATC
  renuncia a publicidad por WhatsApp y teléfono para quien pase por este funnel.
- A-03.3 En `step6b` el prototipo pide una **preferencia de canal para la propia solicitud**
  ("¿Prefieres por WhatsApp?"). **No es publicidad** y no lleva texto legal.
- A-03.4 Los dos son **opcionales**: ni marcarlos ni dejarlos sin marcar bloquea el avance.
- A-03.5 El prototipo asume que el sistema puede **almacenarlos por separado**, con canal,
  fecha y origen. Hoy el CRM guarda una sola marca (`analitica/00-como-se-mide-hoy.md` §5).

### Escenarios

**ESC-03.A — Avanzar sin marcar nada**
- Given: el usuario está en `step6` o `step6b`
- When: avanza sin marcar el permiso
- Then: el sistema le deja continuar sin error

**ESC-03.B — Los dos permisos son independientes**
- Given: el usuario ha aceptado el consentimiento comercial en `step6`
- When: llega a `step6b`
- Then: la preferencia de canal aparece sin marcar, y viceversa

> **A resolver antes de implementar**: la **Ley ATC 10/2025** exige consentimiento granular
> por canal, revocable por canal y trazable. Con un canal único la granularidad es trivial,
> pero la trazabilidad no existe hoy. Pendiente de jurídico.

---

## F-04 · Número de asegurados · `decidido`

### Asunciones

- A-04.1 En `step1` el prototipo pregunta para quién es el seguro: solo la persona, ella y
  otros, u otros sin incluirla.
- A-04.2 Esa respuesta determina **cuántos bloques de asegurado** aparecen en `step2`
  (fechas de nacimiento) y en `cAseg1` / `cAseg2` (datos), y **las etiquetas** de cada uno.
- A-04.3 El usuario puede **añadir y quitar** asegurados en `step2`, y también recalcular
  desde la calculadora de resultados sin volver atrás en el funnel.
- A-04.4 Hay **un cuestionario de salud por asegurado**, no uno por solicitud.

### Escenarios

**ESC-04.A — Un solo asegurado**
- Given: el usuario elige "solo para mí" en `step1`
- Then: aparece un único bloque de fecha de nacimiento y, en contratación, un solo
  cuestionario de salud

**ESC-04.B — Varios asegurados**
- Given: el usuario elige incluir a otras personas
- Then: aparece un bloque por asegurado, con su etiqueta, y en contratación un cuestionario
  por cada uno

**ESC-04.C — Recálculo desde resultados**
- Given: el usuario está en `step7`
- When: cambia el número de asegurados en la calculadora
- Then: el precio se recalcula sin salir de resultados y sin perder el recorrido

> **Dato de contexto**: una cotización real cubre **1,88 asegurados de media**
> (`analitica/05-ga4-y-clarity.md` §2), así que el caso normal son dos personas, no una.

---

## F-05 · Cuestionario de salud y camino KO · `decidido, no implementado`

El comportamiento está acordado; el prototipo lo simplifica a propósito.

### Asunciones

- A-05.1 El cuestionario son **8 preguntas por asegurado**, una a la vez, en modal.
- A-05.2 Marcar **"Sí"** abre un campo de detalle y la siguiente pregunta **no aparece** hasta
  pulsar "Continuar". Marcar **"No"** revela la siguiente directamente.
- A-05.3 El prototipo asume que **cualquier "Sí"** deriva a revisión médica telefónica
  (`cKO`). No asume nada sobre **qué respuestas** lo provocan: eso es criterio de suscripción
  de FIATC.
- A-05.4 En el camino KO el recorrido es `cCuestionario` → `cOtra` → `cKO`. **Pasa por
  `cOtra`** porque la portabilidad interesa igualmente.
- A-05.5 El camino KO **se salta `cTelefono` y `cFirma`**: no se firma nada mientras la
  solicitud está pendiente de revisión médica.
- A-05.6 `cKO` es **terminal**. Las salidas son volver a resultados o hablar con un asesor.
- A-05.7 Si no hay ningún "Sí", el flujo sigue completo y normal.

### Escenarios

**ESC-05.A — Algún "Sí" en el cuestionario**
- Given: el usuario ha completado los cuestionarios con al menos una respuesta afirmativa
- When: continúa
- Then: pasa por `cOtra` y después a `cKO`, sin `cTelefono` ni `cFirma`

**ESC-05.B — Portabilidad dentro del camino KO**
- Given: el usuario ha llegado a `cOtra` dentro del camino KO
- When: responde que sí o que no
- Then: en los dos casos va a `cKO`

**ESC-05.C — Ningún "Sí"**
- Given: el usuario ha respondido "No" a todas las preguntas de todos los asegurados
- Then: el flujo continúa por `cTelefono` → `cFirma` → `cOtra` → … → `cConfirm`

**ESC-05.D — Cuestionario incompleto**
- Given: falta algún cuestionario por completar
- Then: la tarjeta del paso mantiene el tag `Pendiente` y no aparece el botón de salida

**ESC-05.E — Cuestionario completo**
- Given: todos los cuestionarios están guardados
- Then: cada tarjeta muestra `8 / 8` en oscuro con opción de editar, **sin tag de
  "Completado"**, y aparece el botón para continuar

> **Por qué no hay tag verde**: prometería un resultado que aún no está decidido. Si se marcó
> algún "Sí", lo que viene es una llamada de revisión médica, no un "todo en orden". Ver
> `FUNCIONAL.md` §4.
>
> **Lo que el prototipo NO implementa**: hoy salta directo de `cCuestionario` a `cKO`, y `cKO`
> queda fuera del flujo. Es una simplificación deliberada — todas las pantallas son
> alcanzables desde el índice— y la bifurcación real la integra IT.
>
> **Dato de contexto**: la derivación a Teladoc afecta al **2,5%** de quien inicia
> contratación (`analitica/05-ga4-y-clarity.md` §2), así que es un camino minoritario.

---

## F-06 · Portabilidad · `decidido`

### Asunciones

- A-06.1 El prototipo pregunta en `cOtra` si la persona viene de otra compañía.
- A-06.2 Si responde que **sí**, asume que hay que pasar por `cDerogacion` para recoger la
  documentación que permite derogar las carencias.
- A-06.3 Si responde que **no**, `cDerogacion` no existe para ese recorrido.
- A-06.4 En `cDerogacion` subir la documentación es **opcional**: se puede enviar más tarde a
  `web@fiatc.es`.
- A-06.5 Cuando viene de otra compañía, la confirmación (`cConfirm`) **añade un paso** de
  envío de documentación, y la descarga de la app pasa a ser el paso 4.
- A-06.6 La portabilidad se declara **aquí y no antes**, así que en resultados el funnel
  todavía no sabe de qué audiencia se trata.

### Escenarios

**ESC-06.A — Viene de otra compañía**
- Given: el usuario está en `cOtra`
- When: responde que sí
- Then: el siguiente paso es `cDerogacion`, y la confirmación incluirá el paso de
  documentación

**ESC-06.B — Primer seguro**
- Given: el usuario está en `cOtra`
- When: responde que no
- Then: el siguiente paso es `cPago`, y la confirmación no menciona documentación

**ESC-06.C — Enviar la documentación más tarde**
- Given: el usuario está en `cDerogacion`
- When: elige enviarla más tarde
- Then: puede continuar sin adjuntar nada, y la confirmación mantiene el paso pendiente

---

## F-07 · Modalidad de pago · `decidido`

### Asunciones

- A-07.1 El usuario elige la periodicidad de pago en `cPago`.
- A-07.2 Esa elección determina **los textos del cargo** en `cAntes` (resumen legal previo) y
  en `cConfirm`: importe del primer cargo y cuándo llega el siguiente.
- A-07.3 El prototipo asume que **el cobro ocurre en el TPV**, antes de la firma, y que de ahí
  sale ya un número de póliza.
- A-07.4 La cobertura **no empieza con el pago**: empieza cuando se firma. El prototipo lo
  refleja en el copy de `cConfirm`.

### Escenarios

**ESC-07.A — El resumen del cargo refleja la periodicidad elegida**
- Given: el usuario ha elegido una periodicidad en `cPago`
- When: llega a `cAntes`
- Then: el importe del primer cargo y la fecha del siguiente corresponden a esa periodicidad

**ESC-07.B — Confirmación con la cobertura subordinada a la firma**
- Given: el usuario ha completado el pago
- Then: la confirmación celebra el alta y da el número de póliza, pero condiciona el inicio
  de la cobertura a que firme

> **A confirmar con IT**: que se cobre antes de firmar es una decisión de negocio que el
> prototipo hereda del flujo actual, no una propuesta nuestra.

---

## F-08 · Guardar y recuperar presupuesto · `parcialmente simulado`

### Asunciones

- A-08.1 El prototipo asume que un presupuesto **se puede guardar por email** y recuperarse
  más tarde.
- A-08.2 Recuperarlo entra **directo a resultados** (`stepRecover` → `step7`), sin repetir el
  recorrido.
- A-08.3 La opción de guardar aparece en el exit-intent **solo si la persona ya ha visto el
  precio**. Antes de eso no hay nada que guardar.
- A-08.4 El exit-intent se dispara **al pulsar el logo**, que en el prototipo hace de gesto de
  salida. En el funnel real el disparador lo decide IT.

### Escenarios

**ESC-08.A — Exit-intent antes de ver el precio**
- Given: el usuario no ha llegado a resultados
- When: se dispara el exit-intent
- Then: no se le ofrece guardar el presupuesto

**ESC-08.B — Exit-intent después de ver el precio**
- Given: el usuario ya ha visto resultados
- When: se dispara el exit-intent
- Then: se le ofrece guardar el presupuesto por email

**ESC-08.C — Recuperar un presupuesto**
- Given: el usuario llega desde un enlace de presupuesto guardado
- Then: aterriza en resultados con su precio, sin pasar por el cuestionario de tarificación

> **Dato de contexto**: hoy lo usa el **2,6%** de quien entra al tarificador
> (`analitica/05-ga4-y-clarity.md` §2), y `contexto/01-embudo-y-datos.md` dice que el enlace
> funciona: el problema es de visibilidad, no técnico.

---

## Lo que este documento NO cubre

- **El mapa de pantallas y el porqué de cada decisión de diseño** → `FUNCIONAL.md`.
- **Las reglas de negocio de FIATC**: criterios de suscripción, tarifas, validaciones. No son
  nuestras y no las asumimos más allá de lo listado arriba.
- **Lo que está simulado** (firma, TPV, precios, datos demo) → `FUNCIONAL.md` §9.
- **Convenciones de código y reglas visuales** → `FUNCIONAL.md` §10 y
  `conceptualizacion/CLAUDE.md`.
