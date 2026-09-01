# Cómo se mide hoy el funnel de Salud

Qué existe, qué no, quién es dueño de cada pieza y cuál es la línea base. Es material de
**referencia**: se consulta antes de proponer medición, no se edita como diario.

> **Fuente**: respuestas de Laura Solé (FIATC, Marketing Online & Ecommerce) al cuestionario
> de medición, 20 de agosto de 2026.

> **Reparto con `contexto/01-embudo-y-datos.md`**, para no duplicar ni contradecirse:
> aquel documento es el canónico de **qué pasa en el embudo** —los porcentajes de las cuatro
> fugas, la tabla GA4 de retención por paso, los estados atascados del CRM, la portabilidad—
> y este es el canónico de **cómo se mide y quién lo mide**, más la línea base cerrada.
> Cuando una cifra aparezca en los dos, manda `analitica/03-linea-base.md`, que es la única
> con periodo y unidad únicos.

---

## 1. Quién es dueño de qué

Ningún equipo controla la medición de punta a punta. Son cinco actores:

| Pieza | Responsable |
|---|---|
| Etiquetado analítico (GA4, GTM) | **SEOCom** (agencia externa) |
| Iframe del tarificador y data layer | **Héctor López** (FIATC) |
| Integraciones con CRM | equipo de **Laia Avilés** (FIATC) |
| Contactabilidad · plataforma Evolution | **TrueIT** (proveedor) |
| Consentimiento a nivel técnico | **Sistemas** (FIATC) |

Consecuencia práctica: cualquier cambio de medición que cruce el tarificador y el CRM
necesita coordinar al menos a tres. No es un problema de voluntad, es de reparto.

---

## 2. Definiciones oficiales del cliente

Hasta ahora el proyecto usaba "lead" y "conversión" sin definición cerrada. Estas son las
suyas, y son las que hay que usar al comparar cifras:

| Término | Nombre interno | Definición |
|---|---|---|
| **Lead** | Oportunidad | Cualquier alta de oportunidad que entra en el CRM |
| **Lead cualificado** | Oportunidad neta | Todas menos las descartadas por: Posible bot · Datos incorrectos · Tel. erróneo · Validador teléfono · Inactividad chat · Transferencia ATC |
| **Contacto efectivo** | Oportunidad gestionada | Las que han tenido contacto comercial |
| **Conversión** | — | Oportunidades que derivan en venta de póliza |

Siguen dos ratios distintos: **% conversión sobre oportunidades** y **% conversión sobre
oportunidades gestionadas**. Al citar un porcentaje hay que decir cuál de los dos es.

---

## 3. Ciclo de vida de un lead en el CRM

```
Pendiente enviar a EVO  →  Sin gestionar  →  En proceso  →  Cierre
   (ventana 20 min)         (en Evolution)    (agente ya
                                               contactó)
```

- **Pendiente enviar a EVO** — la oportunidad espera 20 minutos mientras se verifica que no
  se complete una compra online.
- **Sin gestionar** — pasada la ventana, el lead va a Evolution (plataforma de llamadas) y
  espera al primer contacto de un agente.
- **En proceso** — un agente ha contactado y gestiona comercialmente.
- **Pendiente Gestión Proveedor** — equivalente a "Sin gestionar" para el Call Center externo.

**Cierre**, con tres salidas y sus submotivos:

| Convertido | Descartado | Rechazado |
|---|---|---|
| venta | Abandono proceso | Política de suscripción Fiatc |
| | Consulta precio | Por precio |
| | Contrata FIATC por otro canal | Riesgo no asegurable |
| | Datos incorrectos | |
| | Máximos intentos EVO | |
| | Posible Bot | |
| | Tel. erróneo | |
| | Transferencia a ATC | |
| | Validador tel. | |

Dos submotivos son oro para el proyecto: **"Abandono proceso"** y **"Consulta precio"**
cuantifican desde el CRM la misma fuga que GA4 ve como el muro del precio. Son dos fuentes
independientes del mismo fenómeno.

### La ventana de 20 minutos afecta al diseño
Si alguien tarda más de 20 minutos en completar, el lead ya se ha enviado al call center y
recibirá llamada **aunque esté comprando**. El prototipo promete "2 min" para el precio,
pero el cuestionario de salud de varios asegurados puede irse bastante más allá. Conviene
saber cuánta gente supera ese umbral.

---

## 4. Línea base (agosto 2025 – julio 2026)

Cifras cerradas de los informes de FIATC (ago-25 a jul-26). Detalle y lectura completa en
`analitica/03-linea-base.md`.

| | |
|---|---|
| Contrataciones **online** | **220** · ~18/mes |
| Contrataciones **cerradas por agente** | **2.905** · ~242/mes |
| Total pólizas | **3.125** |
| Peso de lo online | **7,0%** |
| Oportunidades | **51.814** · ~4.318/mes |
| Conversión global sobre oportunidades | **4,60%** |
| Conversión **online** sobre oportunidades | **0,42%** |

> **Corrección.** Antes se manejaba 1.948 ventas de agente y un 10,1% de peso online. El
> dato de agente **no incluía el call center externo**; lo advirtió FIATC al enviar el
> informe completo. Con los 957 que faltaban, el peso de lo online baja de 10,1% a **7,0%**,
> coherente con el ~6% que da negocio de memoria. Cualquier cifra anterior a estos informes
> queda sustituida por esta tabla.

**El cierre offline es la norma en Salud, no una anomalía.** Es un dato conocido del negocio
y hay que tomarlo como punto de partida, no como problema a resolver.

**Lo que esto significa.** El funnel es hoy un **generador de leads que cierra el call
center**, no un canal de venta directa: 93 de cada 100 pólizas las cierra una persona. No
invalida el proyecto —justo ahí está el margen— pero cambia la métrica de éxito: duplicar
las ventas online seguiría dejando el canal en minoría. Y significa que **la mayor parte del
efecto de una mejora del funnel se juega en la pata telefónica**, donde hoy no es
atribuible.

### La fuga 4: el 1.260 son caídas, no firmas
`contexto/01-embudo-y-datos.md` lo define en **dos sitios que hay que leer juntos**. La fila
de la fuga 4 da *"1.260 en 4 meses = 8% de los leads del periodo"*, y siete líneas más abajo
su tabla de estados del CRM nombra ese mismo 1.260: **"Inicio de contratación sin proseguir —
clic en Contratar y caída en algún punto ANTES de firmar el cuestionario"** (fuente: Diana).

Así que son **~315 caídas al mes, no 315 firmas**, y la fuga 4 queda coherente con las otras
tres: todas son pérdida. **Cuántos firman no se sabe**, porque el tramo no está instrumentado
paso a paso — el iframe lo hacía invisible. Ese hueco lo cierra el funnel nuevo, que no usa
iframe. Ver `analitica/02-medicion-funnel-nuevo.md` §3.

Los estados vecinos de esa misma tabla acotan dónde se cae después del clic: **56** no firman
el cuestionario, **88** se caen en el pago con TPV, **19** en documentación o forma de pago y
**112** se derivan a Teladoc. Con el aviso que da el propio documento: **falta confirmar si
esos estados son foto actual o acumulado desde enero**, así que no se pueden convertir en
tasas.

> **Cuidado al cruzar cifras.** Las fugas 1-3 están medidas en **sesiones de GA4 (2025)** y
> la fuga 4 en **leads de negocio (2026)**. `contexto/01-embudo-y-datos.md` lo advierte en
> cabecera: los cruces entre ambas fuentes son órdenes de magnitud, no cifras exactas. Por
> eso el periodo único agosto 2025 – julio 2026 que se ha pedido para el día 2 importa.

---

## 5. Qué se mide y qué no

**Disponible**
- Inicios y presupuestos generados
- Leads y contrataciones
- Contrataciones online frente a cerradas por agente
- Informes internos: oportunidades por estado, conversión por canal y tipo de campaña,
  conversión por rating
- Contactabilidad, vía Evolution / TrueIT
- Conversión por canal de la oportunidad

**No disponible** — y esto es lo que condiciona el trabajo:

| Vacío | Por qué importa |
|---|---|
| **No existe identificador que una presupuesto → lead → contratación** | Se puede medir *si* mejora, pero no *por qué*, ni atribuir la mejora que se materializa en la pata telefónica. Confirmado con su IT |
| Sin evento específico de clic en "contratar" | Es justo el muro del 63-72%. Se ve en GA4, no en CRM |
| Precios mostrados, sin detalle | No se puede cruzar precio con abandono |
| **Consentimiento: una única marca**, sin canal, ni fecha, ni origen | Ver abajo |
| Tasas de aceptación por canal | No se miden |

### El consentimiento es el vacío más urgente
El CRM guarda **una sola marca** para el consentimiento recogido en el tarificador. Hoy la
web muestra un único checkbox de *"Deseo recibir comunicaciones promocionales"*.

Eso explica una decisión de diseño que hasta ahora parecía solo comercial: **el diseño de
tres toggles por canal no era implementable**. Se redujo a un canal (email) y ahora sabemos
que el sistema no podía almacenar tres.

Pero abre un problema con fecha: la **Ley ATC 10/2025** exige consentimiento granular por
canal, revocable por canal y **trazable** (canal, fecha, origen). Nada de eso existe. No es
un ajuste de diseño, es trabajo de Sistemas con plazo. Ver `contexto/` y la memoria
`project_ley_atc`.

---

## 6. Reunión del 2 de septiembre

Con SEOCom (analítica) y Héctor López (iframe y data layer). Accesos a GA4, GTM y Clarity
solicitados para `enriclieder@multiplica.com` y `miquel@multiplica.com`. Periodo acordado:
**agosto 2025 – julio 2026**, con desglose mensual y, cuando exista, por dispositivo,
fuente, canal y campaña. Foco en Salud.

Puntos a cerrar:

1. Cómo se mide hoy el funnel de Salud, evento por evento.
2. Qué se captura dentro y fuera del iframe.
3. Eventos y estructura del data layer actual.
4. Vacíos de medición.
5. **Qué dejar preparado para el funnel nuevo** → ver `analitica/02-medicion-funnel-nuevo.md`.

**Las preguntas propias, priorizadas y con su contexto, están en
`analitica/04-preguntas-cliente.md`** — que es la lista canónica y autocontenida. No
duplicarlas aquí: si se añade una, va allí.

La de más consecuencias es **qué porcentaje de cuestionarios de salud tiene algún "Sí"**
(`04` §1.6): marca el techo máximo de la venta online. Del volumen hay una pista —112
derivaciones a Teladoc— pero no de la tasa.

Contactabilidad, CRM, consentimiento y testing con usuarios quedan para sesiones posteriores
con sus equipos, a la vuelta de vacaciones. Testing con usuarios puede requerir a **Legal**.
