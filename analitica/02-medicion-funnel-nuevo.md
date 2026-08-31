# Qué dejar preparado para medir el funnel nuevo

Especificación para llevar a **SEOCom** (etiquetado) y **Héctor López** (data layer e
integración). El objetivo es que el funnel nuevo **nazca midiendo**, no que se instrumente
después.

Estado de partida en `analitica/00-como-se-mide-hoy.md`.

---

## Por qué ahora y no después

**Qué eventos se disparan es una decisión de diseño, no de analítica posterior.** Si se
define al construir, el funnel nace midiendo. Si se deja para después del lanzamiento, hay
que volver a tocar el código y se pierden los primeros meses de datos — justo los que dirán
si los quick wins funcionan.

Y hay una ventana que se cierra: **el funnel nuevo no usa iframe**. Eso elimina de raíz el
punto ciego de hoy, donde los eventos no cruzan la frontera del iframe y por eso el tramo
entre el clic y la firma no está instrumentado paso a paso. Es la ocasión de arreglarlo, y
solo existe una vez.

---

## 1. El identificador de presupuesto

**La petición número uno.** Hoy no existe ninguna relación entre presupuesto, lead y
contratación; lo confirmó su propio IT.

Lo que hace falta: que el funnel genere un **identificador único de cotización** que viaje
al CRM con el lead y sobreviva hasta la venta.

Lo que desbloquea:

- **Explicar la mejora, no solo verla.** El agregado dice "las ventas online subieron un
  30%"; el identificador dice de dónde salió: portabilidad o primer seguro, móvil o
  escritorio, qué modalidad.
- **Separar el efecto del funnel del ruido.** Un antes/después es vulnerable a lo que pase
  en paralelo, y los informes de FIATC cuantifican dos confusores grandes: la
  **estacionalidad es ×2,3** entre el mejor mes y el peor, y la conversión varía **×4,5
  según el rating**. Si el lanzamiento coincide con la promo estacional de "2 meses gratis"
  (septiembre–febrero), atribuir la subida al funnel es discutible. Ver
  `analitica/03-linea-base.md` §2 y §3.
- **Medir la pata del agente**, que es el 90% de las ventas. Si el funnel nuevo hace que
  lleguen leads mejor informados y el agente cierre más rápido, hoy eso es invisible: el
  mérito se lo lleva el teléfono.

> **Cómo plantearlo el día 2.** No como bloqueante: *"con lo que hay podemos medir el
> resultado; con un identificador podríamos además explicarlo y atribuir lo que hoy se
> atribuye al call center"*. Es más fuerte porque no exige nada para empezar.

---

## 2. Eventos por fuga

El embudo pierde gente en cuatro sitios y hoy dos de ellos no se pueden diagnosticar. Los
eventos deben cubrir **las transiciones**, que es donde están los muros: el tramo interno de
preguntas retiene el 94-99% por paso.

**Fuga 1 · arranque (−20%)**
Entrada al funnel · CP introducido · CP con selector de zona mostrado. Con eso se sabe si
se abandona antes de escribir nada o al encontrarse el primer campo.

**Fuga 2 · consentimiento (−22 a −30%)**
Paso mostrado · email introducido · teléfono introducido · consentimiento marcado, **por
canal** · envío. Es la fuga más rentable de diagnosticar y hoy no se sabe la causa. Sin
eventos separados no se puede distinguir "abandonan sin tocar nada" de "se atascan en el
teléfono", y cada una pide una solución opuesta.

**Fuga 3 · precio → contratar (−63 a −72%)**
Precio mostrado, **con la modalidad y el importe** · pestaña de modalidad cambiada · detalle
del seguro abierto · calculadora abierta y recálculo · **clic en contratar** (hoy no existe
como evento) · guardar presupuesto.

**Fuga 4 · clic → firma (~315 firmas/mes, 8% de los leads)**
Un evento por paso de contratación, y en particular: cuestionario iniciado y guardado por
asegurado · derivación a revisión médica · firma · TPV mostrado · pago completado. Es el
tramo que el iframe hacía invisible: se sabe cuántos firman, no cuántos se caen antes.

Ojo con la lectura: la mayoría de quien firma **cierra después con un agente**, no en el
TPV. Un descenso de pagos online no implica una fuga en el pago; sin el identificador de
cotización no se puede separar una cosa de la otra.

**Transversal en todos**: dispositivo, fuente, campaña, y el identificador de cotización.

---

## 3. Trazabilidad del consentimiento

No es analítica, es cumplimiento, pero se resuelve en el mismo sitio. La **Ley ATC 10/2025**
exige consentimiento granular por canal, revocable por canal y trazable. El CRM guarda hoy
**una sola marca**, sin canal, sin fecha y sin origen.

Lo mínimo a dejar preparado: **canal, fecha y origen** por cada consentimiento, y capacidad
de revocar uno sin tocar los demás.

Mientras eso no exista, el diseño no puede ofrecer más de un canal: no es una decisión
estética, es que el sistema no lo puede almacenar. Ver `analitica/00-como-se-mide-hoy.md` §5.

---

## 4. Qué hay que medir para validar cada decisión del prototipo

Las decisiones de diseño que hemos tomado son **hipótesis**. Esta tabla dice qué evento
convierte cada una en algo comprobable. Es la lista que hay que cruzar con SEOCom para que
no se quede ninguna sin instrumentar.

| Decisión del prototipo | Qué la valida | Hoy |
|---|---|---|
| **Mensaje dual** en resultados (portabilidad / primer seguro) | Una señal de portabilidad **en la entrada** —campaña o keyword— cruzada con el clic en contratar | Se declara ya en contratación: solo se sabe de quien compró → `04` §2.5 |
| **Clic en "Contratar"** — el CTA del muro del 63-72% | El evento en sí, con modalidad e importe mostrados | **No existe** → `04` §1.2 |
| **Agendar llamada** con franja horaria, frente al teléfono directo | Ruta elegida y conversión de cada una. ATC convierte al 11,31%, ×2,5 el funnel | Sin medir |
| **Consentimiento comercial** (email, `step6`) separado de la **preferencia de canal** (WhatsApp, `step6b`) | Dos marcas distinguibles, con canal, fecha y origen | Una sola marca → `04` §1.4 |
| **Cuestionario de salud** paso a paso, con progreso por asegurado | Un evento por asegurado guardado, y **el tiempo total** | Sin medir. Choca con la ventana de 20 min → `04` §2.3 |
| **Derivación a revisión médica** (la salida cuando el cuestionario se complica) | Volumen de derivaciones y qué pasa después | Sin medir. No sabemos ni el orden de magnitud |
| **Guardar presupuesto** y volver más tarde | Evento de guardado y de retorno — necesita el identificador | Sin medir → `04` §1.1 |
| **Calculadora de asegurados** y recálculo en resultados | Aperturas y recálculos, con el precio antes y después | Sin medir |
| **Pago anual** con el mensaje "De una vez y olvídate" | Reparto anual/mensual. El descuento es pequeño, así que el efecto es del copy | Sin medir |
| **Modal de dudas frecuentes** a dos columnas | Qué preguntas se abren: es señal directa de qué información falta en la página | Sin medir |
| **Loadings** antes de resultados y antes de confirmación | Abandono durante la espera | Sin medir |
| **Exit-intent** (clic en el logo) | Disparos y recuperaciones | Sin medir |

**Casi nada de esto se mide hoy**, y es esperable: son pantallas que aún no existen. El punto
es que **se decide ahora o se pierde**, porque después del lanzamiento hay que volver a tocar
el código y se van los primeros meses de datos.

Una decisión sigue abierta y la medición la resolvería: **editar asegurados en la pantalla de
resultados**. Si el recálculo se usa mucho, la edición vale la pena; si no, es complejidad
gratis.

---

## 5. Antes de dar nada por bueno

- **Respetar sus convenciones.** Si SEOCom ya tiene nomenclatura de eventos o un data layer
  definido, se usa. Inventar otra taxonomía en paralelo garantiza que nadie cruce los datos.
- **Replicar las definiciones del cliente** (Oportunidad, Oportunidad neta, gestionada,
  conversión) para que la línea base siga siendo comparable. Si el funnel nuevo cuenta
  distinto que el viejo, no se podrá decir si mejoró.
- **Segmentar por rating y por dispositivo desde el día uno.** El rating es gratis —ya está
  en sus informes— y sin él el antes/después es refutable. El dispositivo no está en ningún
  informe actual y hay que pedirlo.
- **Excluir afiliación y comparadores de la línea base.** Atrato, Adpepper y Kelisto suman
  2.267 oportunidades con 10 ventas (0,44%) y ya están cortados; dejarlos dentro ensucia la
  comparación. Ver `analitica/03-linea-base.md` §2.
- **Pedir entorno de pruebas.** Validar la medición antes de lanzar, no después.
- **Un evento sin dueño no existe.** Cada uno necesita alguien que lo implemente y alguien
  que lo verifique; con cinco actores en el reparto, lo que no se asigna se cae.
