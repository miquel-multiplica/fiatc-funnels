# Qué dicen los exports de GA4 y Clarity

Primera vez que vemos datos crudos de las dos herramientas. Sirven sobre todo para **saber
cómo está instrumentado el funnel hoy**, que era el primer punto de la reunión.

> **Fuentes**, todas en `material-cliente/` (no versionado):
> - **GA4** — `Informe_panorámico.csv`, propiedad "GA4 - Web FIATC", **27 jul – 23 ago 2026**
>   (4 semanas).
> - **Clarity A** — `..._08-24-2026 08 08.csv`, **22–24 ago 2026**: sábado, domingo y lunes.
> - **Clarity B** — `..._09-01-2026 09 36.csv`, **30 ago – 1 sep 2026**: domingo, lunes y
>   martes, ya con la vuelta al trabajo.

> ⚠ **Los datos de Clarity son PROVISIONALES** hasta disponer de periodos más amplios. Las
> dos ventanas son de 3 días y se contradicen entre sí, así que **no se cita ninguna cifra de
> Clarity como conclusión**. Ver §4.

> **Ninguna de las tres muestras sirve para fijar cifras.** Las dos de Clarity son de **3
> días** y son de **todo el web**, no del funnel: solo 422 y 686 sesiones tocan
> `/calcular-seguro-medico`. Y al compararlas entre sí (§4) se descubre que **no se parecen en
> casi nada**, lo que es en sí el hallazgo más útil. La línea base sigue siendo
> `analitica/03-linea-base.md`; esto sirve para entender el **instrumento**.

---

## 1. Cómo está instrumentado hoy, evento por evento

GA4 tiene **47 eventos**. Los del tarificador siguen tres patrones:

| Patrón | Para qué | Ramos que lo tienen |
|---|---|---|
| `tarificador_<ramo>` | se dispara **varias veces por sesión** (ver §2) | 13 ramos |
| `tarificador_inicio_<ramo>` | entrada al tarificador | **solo 5**: salud, hogar, decesos, dental, esquí |
| `tarificador_conversion_<ramo>` | fin del tarificador | 7, más `conversion_general` |

Para Salud, los tres existen: `tarificador_salud` 62.458 · `tarificador_inicio_salud` 12.501
· `tarificador_conversion_salud` 5.316.

**Lo que NO existe, y es lo que más nos importa:**

- **Ningún evento de precio mostrado.**
- **Ningún evento de clic en "Contratar"** — el muro del 63-72%. Confirma
  `analitica/04-preguntas-cliente.md` §1.2 con evidencia directa.
- **Ningún evento del tramo de contratación**: ni cuestionario, ni firma, ni TPV, ni pago.
  La medición **se acaba** en `tarificador_conversion_salud`.

Otros hallazgos de la lista de eventos:

- `solicitar_llamada_tarificadores` = **501**. Ya existe un evento de petición de llamada
  desde los tarificadores, aunque no distingue ramo. Relevante para la ruta de agendar
  llamada del prototipo.
- `click_phone` = 2.840, en todo el site.
- `click_enlaces_faqs_salud` = **69** y `click_documentacion_salud` = **1**. Los eventos
  existen pero apenas se disparan: o no se usan esos enlaces, o están mal etiquetados.
- **La nomenclatura es inconsistente**: `tarificador_asv` frente a
  `tarificador_conversion_viaje`, `tarificador_embarc` frente a
  `tarificador_conversion_embarcaciones`. Importa porque el acuerdo era respetar su
  taxonomía (`analitica/02-medicion-funnel-nuevo.md` §6) — y su taxonomía no es homogénea.

**Salud es el 49,8% de todas las conversiones de tarificador** de la compañía (5.316 de
10.685). La mitad de la captación se juega en este funnel.

---

## 2. El funnel de Salud, con lo que hay

`tarificador_salud` (62.458) **no puede ser entradas**: serían el 87% de las 71.592 sesiones
de todo el web, imposible habiendo trece ramos. Así que se dispara **varias veces por
sesión** — probablemente una por paso. Encaja: el ratio es **5,0 veces** por inicio, y la
curva de retención de `contexto/01-embudo-y-datos.md` predice **~6,0 pasos** por sesión.

Con eso, el único embudo que GA4 permite construir hoy para Salud es de dos puntos:

| | 4 semanas | Equivalente mensual |
|---|---|---|
| Entradas (`tarificador_inicio_salud`) | 12.501 | ~13.500 |
| Fin del tarificador (`tarificador_conversion_salud`) | 5.316 | ~5.755 |
| **Completan** | **42,5%** | |

Dos cosas que chocan y hay que preguntar:

**Las entradas son 2-3 veces las que teníamos.** `contexto/01` daba 4.200-6.500 sesiones/mes
entrando al tarificador (GA4 2025). Aquí salen ~13.500/mes. O el tráfico ha crecido mucho, o
las dos cifras no miden lo mismo.

**GA4 da casi el doble de conversiones que oportunidades tiene el CRM.**

| Comparación | Por día | GA4 respecto al CRM |
|---|---|---|
| GA4, 27 jul – 23 ago 2026 | 189,9 | — |
| CRM jul-26 (3.244) | 104,6 | **×1,81** |
| CRM ago-25 (3.080) | 99,4 | **×1,91** |
| CRM media anual (4.318/mes) | 142,0 | ×1,34 |

Y el sentido de la brecha es el contrario del esperable: **agosto es temporada baja**, así que
el dato de GA4 debería quedar *por debajo* de la media anual, no un 34% por encima.

Tres candidatos, y no son excluyentes:

1. **Bots**, aunque no basta por sí solo. Clarity los cifra entre el **13% y el 66%** del
   tráfico según la ventana (§4). Con un 13% no se explica un ×1,8; haría falta que GA4
   contase además otra cosa.
2. **Leads duplicados**, que `contexto/01` ya confirma: la gente re-cotiza desde cero.
3. **`conversion` no es lo mismo que "oportunidad"**: puede marcar el fin del formulario
   aunque no se cree lead en el CRM.

**Hasta saber cuál es, no se puede usar GA4 y CRM en la misma frase.** Es la misma trampa de
denominador de `analitica/03-linea-base.md` §5, ahora entre herramientas.

---

## 3. El punto ciego, cuantificado

**"Tarificador" es un único título de página con 271.704 vistas**: el **58%** de todos los
`page_view` del site. Todo el tarificador —los trece ramos y todos sus pasos— colapsa en un
solo título.

Por eso **no se puede construir ningún embudo por pasos desde vistas de página**, y todo
depende de los eventos `tarificador_*`. Es el punto ciego del iframe, medido.

### Pero hay más rastro del que creíamos

Algunos pasos de contratación **sí tienen título propio**, y nadie ha construido el embudo
con ellos. En 4 semanas:

| Título de página | Vistas |
|---|---|
| Cuestionario Salud | **500** |
| Condiciones solicitud contratación online | 98 |
| Forma de pago | 80 |
| Firma electrónica rechazada | 52 |

Y encajan por orden de magnitud con los estados del CRM de `contexto/01` (4 meses): **56** "W
cuestionario no firmado" frente a 52 firmas rechazadas, **88** "W pendiente pago TPV" frente a
80 vistas de forma de pago.

**Es una vía para acotar la fuga 4 antes de instrumentar nada.** Con la cautela de que los
periodos no coinciden y de que no sabemos si "Cuestionario Salud" es el cuestionario de salud
del prototipo o otra cosa. Se pregunta en §5.

### Una página de error con mucho tráfico
**"Redirección fallida" tiene 1.413 vistas** en 4 semanas, y "404 Error" otras 475. No
sabemos qué las provoca ni si están en el camino del funnel, pero 1.413 no es residual.

---

## 4. Clarity queda aparcado hasta tener una ventana grande

**Decisión tomada**: no se construye nada sobre estos datos. Las dos ventanas disponibles son
de **3 días** cada una, son de **todo el web** —no del funnel— y **no se parecen entre sí**.

| Métrica | A · 22-24 ago<br>*sáb, dom, lun* | B · 30 ago-1 sep<br>*dom, lun, mar* | Variación |
|---|---|---|---|
| Sesiones | 10.874 | 19.135 | +76% |
| **Sesiones de bot** | **21.525** | **2.843** | **−87%** |
| **Móvil / escritorio** | **83% / 17%** | **65% / 35%** | **+113% escritorio** |
| Usuarios recurrentes | 8,1% | 14,7% | +82% |
| Clic atrás rápido | 4,09% | 5,44% | +33% |
| Clic de salida | 5,50% | 10,10% | +84% |
| Sesiones en `/calcular-seguro-medico` | 422 | 686 | +63% |

La diferencia se explica sola —A es fin de semana en plena vacación, B llega al 1 de
septiembre con la vuelta al trabajo— y ahí está el problema: **el día de la semana mueve las
métricas más que cualquier cosa que podamos diseñar.** Con 140-230 sesiones diarias en la
página del tarificador, tampoco hay volumen para segmentar por hipótesis.

**Qué hace falta antes de retomarlo**: una ventana de varios meses, segmentada por dispositivo
y con los bots excluidos, y saber si Clarity graba dentro del iframe
(`analitica/04-preguntas-cliente.md` §1.5). El plan de diagnóstico está listo y esperando en
`analitica/01-clarity.md`.

### Tres cosas que sí conviene retener del instrumento

No son cifras para usar, son cautelas sobre la herramienta:

- **El desglose por tipo de bot no respeta el rango de fechas**: sale idéntico en los dos
  exports, de periodos distintos. Y los tipos se solapan entre sí. No es utilizable.
- **Los "eventos inteligentes" no son fiables.** "Finalización de la compra" pasa de 13 a 260
  sesiones mientras el panel de Compras registra **2**. Son heurísticas automáticas: no valen
  como métrica de negocio.
- **Las señales de fricción hay que leerlas como tasa sobre sesiones implicadas.** Suben todas
  en la ventana con más implicación, porque quien rebota sin mirar no llega a producir
  fricción.

### Y dos pistas que no dependen de la ventana

- **`evicertia.com` aparece como referente en las dos** (242 y 637 sesiones). Son personas
  **volviendo** del paso de firma, así que hay rastro del tramo de contratación por explotar.
- **El rendimiento sale mal en las dos**: LCP ~2,9s e INP 216ms, ambos en "necesita mejora"
  (umbrales <2,5s y <200ms). El CLS en cambio mejora de 0,162 a 0,0865. Que LCP e INP se
  repitan apunta a un problema real, pero **conviene confirmarlo con la ventana larga** antes
  de convertirlo en argumento.

---

## 5. Qué cambia en nuestras preguntas

**Ya respondidas, total o parcialmente:**

- **No existe evento de clic en "Contratar"** ni nada del tramo de contratación. Confirmado
  con la lista de eventos, no de oídas.
- **El móvil domina** el tráfico en cualquier ventana, lo que respalda el mobile-first. El
  reparto exacto **no está resuelto** y §2.2 sigue abierta: hay que pedirlo a GA4 con periodo
  largo, no a Clarity (§4).
- **Hay rastro parcial de contratación** en títulos de página, que nadie usa.

**Nuevas, para añadir a la sesión:**

1. **¿Qué dispara exactamente `tarificador_inicio_salud` y `tarificador_conversion_salud`?**
   De eso depende que el 42,5% signifique algo, y es la pregunta que desatasca todo lo demás.
2. **¿Por qué GA4 da ×1,8 las oportunidades del CRM?** ¿Filtra bots? ¿Deduplica?
3. **¿Qué es "Cuestionario Salud" como título de página**, y se puede construir el embudo de
   contratación con los títulos que ya existen?
4. **¿Qué provoca "Redirección fallida"** y sus 1.413 vistas en 4 semanas?
5. **¿Por qué 8 de los 13 ramos no tienen evento de inicio?** Salud lo tiene, pero dice algo
   de cómo se mantiene el etiquetado.
