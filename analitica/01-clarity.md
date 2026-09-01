# Qué mirar en Clarity — plan de diagnóstico

Este documento dice **qué buscar, dónde y para qué decisión sirve cada hallazgo**. Es el
**plan**; la lectura de los datos que ya tenemos está en `analitica/05-ga4-y-clarity.md`.
Estado de la medición actual en `analitica/00-como-se-mide-hoy.md`; lo que hay que dejar
preparado para el funnel nuevo, en `analitica/02-medicion-funnel-nuevo.md`. Sustituye al
antiguo QW#12 ("diagnóstico Clarity"), que era un quick win pendiente: ya no es una tarea por
hacer, es un plan de trabajo.

> ## APARCADO hasta tener una ventana grande
>
> ⚠ **Los datos de Clarity que hay hoy son PROVISIONALES** y no deben citarse como
> conclusión. El plan está listo, pero **no se ejecuta todavía**. Las dos ventanas de Clarity disponibles
> son de 3 días, de todo el web, y **no se parecen entre sí**: el móvil pasa del 83% al 65% y
> los bots de 21.525 a 2.843 (`analitica/05-ga4-y-clarity.md` §4). En la página del
> tarificador hay 140-230 sesiones al día, insuficiente para segmentar por hipótesis.
>
> **Qué hace falta para retomarlo:**
>
> 1. **Una ventana de varios meses**, segmentada por dispositivo y con los bots excluidos.
> 2. **Saber si Clarity graba dentro del iframe** del tarificador. Las fugas 1, 2 y 3 pasan
>    ahí dentro; si no lo graba, las prioridades 1 y 2 **no se pueden ejecutar** tal como
>    están escritas. Preguntado en `analitica/04-preguntas-cliente.md` §1.5.

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

El tramo entre el clic y la firma **no está instrumentado paso a paso**. Clarity graba, pero
sin eventos definidos no hay embudo que medir. Antes de analizar, hay que instrumentar.

---

## Antes de sacar conclusiones

- **Nunca leer pocos días.** El día de la semana mueve las métricas más que cualquier cosa
  que diseñemos: es lo que dejó este plan aparcado.
- **Filtrar bots y confirmar que la vista los excluye.** Clarity los cifra entre el 13% y el
  66% del tráfico según la ventana, y ni el caso bueno es inocuo.
- **Segmentar móvil y escritorio por separado.** Son dos comportamientos distintos y
  mezclarlos esconde los dos. El móvil domina siempre, pero el reparto exacto está sin
  resolver: hay que mirar el peso real en el periodo que se analice.
- **Descartar el tráfico de rebote inmediato** al medir cualquier fuga: infla los números y
  no dice nada del diseño.
- **Leer las señales de fricción como tasa sobre sesiones implicadas**, no en absoluto: suben
  cuando sube la implicación, porque quien rebota sin mirar no llega a producir fricción.
- **No usar los "eventos inteligentes" de Clarity** como métrica de negocio: son heurísticas
  automáticas y se desmienten solas entre exports (`05` §4).
- **Fijar la base de comparación con la propia ventana larga**, no con las fotos de 3 días.
  Un valor del funnel solo significa algo al lado del valor del site en el mismo periodo.
- **Una hipótesis, una prueba.** Cada hallazgo de arriba tiene una prueba concreta; si la
  grabación no la confirma ni la desmiente, no vale como evidencia.
- **Contrastar con GA4.** Clarity dice *qué hace* la gente; GA4, *cuántos*. Las cifras del
  embudo salen de GA4 (`contexto/01-embudo-y-datos.md`) y no se sustituyen con grabaciones.
  Pero **GA4 y el CRM no cuadran entre sí** —GA4 da ×1,8 las oportunidades (`05` §2)—, así
  que al citar un volumen hay que decir de qué herramienta sale.
