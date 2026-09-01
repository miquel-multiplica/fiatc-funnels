# Qué mirar en Clarity — plan de diagnóstico

Este documento dice **qué buscar, dónde y para qué decisión sirve cada hallazgo**. Es el
**plan**; la lectura de los datos que ya tenemos está en `analitica/05-ga4-y-clarity.md`.
Estado de la medición actual en `analitica/00-como-se-mide-hoy.md`; lo que hay que dejar
preparado para el funnel nuevo, en `analitica/02-medicion-funnel-nuevo.md`. Sustituye al
antiguo QW#12 ("diagnóstico Clarity"), que era un quick win pendiente: ya no es una tarea por
hacer, es un plan de trabajo.

> ## CONFIRMADO: Clarity no ve nada dentro del iframe
>
> El tarificador aparece en las grabaciones como un **rectángulo gris con el icono de "ojo
> tachado"**, el marcador de contenido no capturado. Y cada sesión registra **"Clics: 0"**
> aunque dure minutos, porque todos los clics ocurren dentro del iframe.
>
> **Consecuencia: las prioridades 1, 2 y 3 de este plan NO se pueden ejecutar sobre el funnel
> actual.** Todas dependen de comportamiento **dentro** del tarificador —*rage clicks*, foco en
> campos, scroll por paso, qué campo frena— y de eso no hay nada. No es falta de volumen: hay
> 5.053 grabaciones de `/calcular-seguro-medico` en 30 días. Es falta de visibilidad.
>
> **Y esto delimita bien el problema.** El *cuánto* sí lo tenemos: GA4 mide el embudo paso a
> paso con la dimensión `paso tarificadores` (`analitica/05-ga4-y-clarity.md` §2). Lo que falta
> es exclusivamente **el porqué**, que es justo lo que Clarity aportaría y hoy no puede.
>
> **Pero la ceguera no es total.** Clarity sí ve la página contenedora, y con el export
> filtrado por URL aparecen señales fuertes que sirven para medir la fricción **del tarificador
> como conjunto**, aunque no para atribuirla a un paso. Están en el apartado siguiente.
>
> **Este plan queda como plan para el funnel nuevo**, que no usa iframe y donde todo esto sí
> será medible (`analitica/02-medicion-funnel-nuevo.md`). Lo que sí se puede hacer hoy está en
> el apartado siguiente.
>
> Y explica algo de paso: que nadie en FIATC haya diagnosticado nunca las fugas 1 y 2 **no es
> negligencia, es que la herramienta no puede verlas**.

---

## Lo que sí se puede hacer hoy, filtrando por URL

Filtrar Clarity con un regex sobre `/calcular-seguro-medico` da 7.858 sesiones en 30 días y
señales aprovechables. **Cinco líneas de trabajo, sin instrumentar nada:**

1. **El clic atrás rápido está en el 22,82%, más de cuatro veces el del site (5,22%).** Casi
   una de cada cuatro sesiones del tarificador vuelve atrás de golpe. Es navegación del
   navegador, no un clic interno, así que se mide pese a la ceguera. **Es el mejor indicador de
   fricción que tenemos**, y se puede segmentar por dispositivo, origen y fecha, y seguir
   después del rediseño.
2. **El tiempo y su distribución.** La media es 2,2 min activos y 4,1 min totales, muy por
   debajo de la ventana de 20 minutos del CRM. Falta ver la cola: cuántas sesiones la superan
   (`analitica/04-preguntas-cliente.md` §2.3).
3. **El CLS del tarificador es 0,217**, más del doble del umbral bueno y el doble que el del
   site. En una pantalla de formulario el desplazamiento de layout es especialmente molesto, y
   el iframe cargando es el sospechoso. El LCP en cambio está bien (2,105s).
4. **Adónde se van al salir.** 353 sesiones acaban en `/solicitar-presupuesto` —el formulario
   alternativo—, y 693 en páginas de modalidad concretas (`completo`, `medifiatc`,
   `sin-hospitalizacion`). Lo primero es una fuga lateral; lo segundo dice que salen a buscar
   qué cubre cada modalidad.
5. **El 38,8% de sesiones tiene un error de JavaScript** (3.045 de 7.858, casi todas
   `script error.`, que es el error enmascarado por CORS del propio iframe). Mucho volumen para
   no mirarlo.

> ⚠ **Y una trampa que evitar**: las señales del **site** (clic inactivo 6,10%, clic atrás
> rápido 5,22%) no sirven como base de comparación del funnel, porque no incluyen nada de
> dentro del iframe. La base del funnel es la del export filtrado por URL, no la global.

---

## El plan, para cuando haya funnel sin iframe

El embudo pierde gente en cuatro sitios (`contexto/01-embudo-y-datos.md`). De dos de ellos
**no sabemos la causa**, y eso es lo que Clarity puede resolver:

| Fuga | Dónde | Pérdida | ¿Sabemos por qué? |
|---|---|---|---|
| 1 · Arranque | portada → código postal | −20% | **No** |
| 2 · Consentimiento | email + teléfono + RGPD | −22% a −30% | **No** |
| 3 · Precio → contratar | resultados | −63% a −72% | En parte (comparan) |
| 4 · Clic → firma | contratación | 8% de leads | No instrumentado |

Entre medias el embudo retiene el 94-99% por paso. **Los muros están en las transiciones.**

---

## Prioridad 1 · Fuga 2, el consentimiento

Es la más rentable de diagnosticar: se pierde entre uno de cada cuatro y uno de cada tres,
el paso es corto y cualquier arreglo es barato. Cuatro hipótesis, cada una con su prueba.

**A · Abandonan sin llegar a tocar nada.** Si la mayoría sale sin un solo clic ni foco en un
campo, el problema no es el formulario: es lo que la pantalla *promete* al aparecer. Se
mira con el tiempo en pantalla y el ratio de sesiones con interacción.
→ Si se confirma, se ataca con encuadre y expectativa, no con usabilidad.

**B · Un campo concreto los frena.** Buscar *rage clicks*, *dead clicks* y focos repetidos
sobre el mismo campo. Sospechosos: el teléfono (¿por qué lo pedís?) y el prefijo.
→ Si se confirma, es microcopy o quitar el campo del paso.

**C · El bloque legal.** Ver si hacen clic en el texto RGPD o en los enlaces de política, y
si vuelven después. Un *dead click* sobre texto legal no enlazado significa que intentaron
leerlo y no pudieron.
→ Si se confirma, es cómo se presenta el consentimiento, no qué se pide.

**D · La anomalía de marzo (70,1%).** Segmentar por fechas y comparar marzo con el resto.
Si el comportamiento es distinto, hubo un cambio —campaña, tráfico o despliegue— y eso
acota la causa mucho más rápido que cualquier hipótesis.

## Prioridad 2 · Fuga 1, el arranque

Un −20% antes de pedir nada es mucho, y el tráfico es bueno.

- **¿Ven el botón?** Profundidad de scroll en la portada. Si el CTA queda por debajo del
  fold en los móviles más comunes, ahí está la respuesta.
- **¿Pulsan cosas que no son botones?** *Dead clicks* sobre el banner de campaña, las cifras
  o los testimonios. Si la gente pulsa el "2 meses gratis" esperando algo, es una promesa
  sin destino.
- **¿Cuánto aguantan?** Salidas en menos de 5 segundos son tráfico equivocado, no diseño.
  Conviene saberlo antes de rediseñar nada.

## Prioridad 3 · Fuga 3, el muro del precio

Aquí sí tenemos una explicación —comparan con otras aseguradoras y comparadores— pero no
sabemos **qué hacen antes de irse**.

- **¿Abren el detalle del seguro?** Si casi nadie lo abre, el contenido que preparamos no
  se está viendo y el problema es de visibilidad.
- **¿Usan la calculadora?** Es el QW#1 y responde a un problema real (leads duplicados).
  Si no se usa, o no se entiende o no se ve.
- **¿Hacen scroll horizontal en las tarjetas?** En móvil las modalidades están en carrusel.
  Si no se desplazan, están decidiendo con una sola opción a la vista.
- **Tiempo antes de salir.** Salida rápida = descarte por precio. Salida lenta = estaban
  comparando en otra pestaña, y eso se combate con recordatorio, no con rediseño.

## Fuga 4 · lo que Clarity no puede darnos

El tramo **sí está medido** por GA4, con la dimensión `paso tarificadores`
(`analitica/05-ga4-y-clarity.md` §2). Lo que Clarity no puede dar es **qué ocurre dentro**: el
mayor muro está entre los datos del titular y la dirección, con un 81,7% de pérdida, y sin ver
la pantalla no se puede saber por qué.

---

## Antes de sacar conclusiones

- **Nunca leer pocos días.** El día de la semana mueve las métricas más que cualquier cosa
  que diseñemos: es lo que dejó este plan aparcado.
- **Filtrar bots y confirmar que la vista los excluye.** En 30 días son el **28,8%** del
  tráfico. Y ojo: Clarity cuenta ×3,08 las sesiones de GA4 a nivel de site (`05` §4), pero
  **menos** que GA4 en el tarificador (7.793 sesiones frente a 12.501 inicios). Al comparar hay
  que decir de dónde sale cada cifra.
- **Segmentar móvil y escritorio por separado.** Son dos comportamientos distintos y
  mezclarlos esconde los dos. A nivel de site el reparto es **64% móvil / 36% escritorio**, así
  que el escritorio **no es un caso secundario**: es más de un tercio.
- **Descartar el tráfico de rebote inmediato** al medir cualquier fuga: infla los números y
  no dice nada del diseño.
- **Leer las señales de fricción como tasa sobre sesiones implicadas**, no en absoluto: suben
  cuando sube la implicación, porque quien rebota sin mirar no llega a producir fricción.
- **No usar los "eventos inteligentes" ni los resúmenes de IA de Clarity.** Los eventos se
  desmienten solos entre exports (`05` §4), y los resúmenes de sesión inventan: en una sesión
  de 4:39 con 0 clics, el resumen automático concluye que el usuario "estaba enfocado en
  completar el formulario". No hay dato que lo sostenga.
- **No usar las señales del site como base del funnel.** Excluyen el tarificador por
  construcción (ver arriba). La base habrá que construirla con los primeros datos del funnel
  nuevo.
- **Una hipótesis, una prueba.** Cada hallazgo de arriba tiene una prueba concreta; si la
  grabación no la confirma ni la desmiente, no vale como evidencia.
- **Contrastar con GA4.** Clarity dice *qué hace* la gente; GA4, *cuántos*. Las cifras del
  embudo salen de GA4 (`contexto/01-embudo-y-datos.md`) y no se sustituyen con grabaciones.
  Pero **GA4 y el CRM no cuadran entre sí** —GA4 da ×1,8 las oportunidades (`05` §2)—, así
  que al citar un volumen hay que decir de qué herramienta sale.
