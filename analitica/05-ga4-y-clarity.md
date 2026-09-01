# Qué dicen los exports de GA4 y Clarity

Primera vez que vemos datos crudos de las dos herramientas. Sirven sobre todo para **saber
cómo está instrumentado el funnel hoy**, que era el primer punto de la reunión.

> **Fuentes**, todas en `material-cliente/` (no versionado):
> - **GA4 · embudo de Salud por paso y dispositivo** — `analisis analytics salud ultimos 30
>   dias.csv`, **2–31 ago 2026**. Es el fichero más valioso de todos.
> - **GA4 · panorámico** — `Informe_panorámico_GA4.csv`, **27 jul – 23 ago 2026**. Aporta la
>   lista de eventos y los 7.157 títulos de página.
> - **GA4 · página del tarificador** — `Pàgines_i_pantalles_...csv`, **2–31 ago 2026**.
> - **Clarity · site** — `..._09-01-2026 15 45.csv`, **3 ago – 1 sep 2026**, 30 días.
> - **Clarity · filtrado a `/calcular-seguro-medico`** — `..._18 28 url...csv`, mismos 30 días.
>
> *(Las dos ventanas de 3 días de Clarity que se usaron al principio se han borrado: eran
> engañosas y están superadas por la de 30 días. Lo que enseñaron está en §4.)*

---

## 1. Cómo está instrumentado hoy

Hay que mirar **dos capas**, y la segunda es la que importa. Durante días dimos por hecho que
el tramo de contratación no se medía, y era falso: **estábamos mirando solo la lista de nombres
de evento**, donde las dimensiones personalizadas no aparecen.

### La capa de eventos

GA4 tiene **47 eventos**. Los del tarificador siguen tres patrones:

| Patrón | Para qué | Ramos que lo tienen |
|---|---|---|
| `tarificador_<ramo>` | se dispara **varias veces por sesión** | 13 ramos |
| `tarificador_inicio_<ramo>` | entrada al tarificador | **solo 5**: salud, hogar, decesos, dental, esquí |
| `tarificador_conversion_<ramo>` | fin del tarificador | 7, más `conversion_general` |

En esta capa, efectivamente, **no hay ningún evento de precio, de clic en "Contratar" ni del
tramo de contratación**.

### La capa de dimensiones personalizadas — aquí está el embudo

Existen dos dimensiones que no salen en ninguna lista de eventos:

- **`tarificador`** — identifica el ramo.
- **`paso tarificadores`** — **el paso concreto**, con el formato `<ramo>-<nº>-<nombre>`:
  `salud-7-consentimiento`, `salud-8-precio`, `vida-6-consentimiento`, `autos-neo-precios`.

**Con eso, el embudo de Salud existe paso a paso y llega hasta el pago** (§2). No hace falta
instrumentar nada para diagnosticar cuantitativamente las cuatro fugas: hace falta *usarlo*.

### Lo que esto corrige

- **El clic en "Contratar" sí se mide**, no como evento sino como transición entre pasos. De
  ahí salía ya el 63-72% de la fuga 3 de `contexto/01-embudo-y-datos.md`.
- **La fuga 4 no es ciega.** Hay pasos de contratación: datos del titular, dirección, datos del
  asegurado, cuestionario, TPV, y las salidas a Teladoc.
- **Lo que el iframe impide no es medir, es *ver***. GA4 mide con la dimensión de paso; Clarity
  no puede grabar dentro (§4). El punto ciego es del *porqué*, no del *cuánto*.

### Otros hallazgos de la lista de eventos

- `solicitar_llamada_tarificadores` = **501**. Ya existe un evento de petición de llamada desde
  los tarificadores, aunque no distingue ramo.
- `click_phone` = 2.840, en todo el site.
- `click_enlaces_faqs_salud` = **69** y `click_documentacion_salud` = **1**: existen pero
  apenas se disparan.
- **La nomenclatura es inconsistente** en las dos capas. En eventos, `tarificador_asv` frente a
  `tarificador_conversion_viaje`. En pasos, la numeración de Salud **se salta el 2 y el 4** y
  varios pasos no llevan número (`salud-codigo-postal`, `salud-fecha-nacimiento`). Importa
  porque el acuerdo era respetar su taxonomía
  (`analitica/02-medicion-funnel-nuevo.md` §6) — y su taxonomía no es homogénea.
- **El segmento "Conversiones tarificador" está apañado a mano**: enumera
  `autos-neo-precios|vida-6-consentimiento|.*not set.*`. Alguien tuvo que parchear las
  inconsistencias entre ramos, y eso lo hace frágil.

**Salud es el 49,8% de todas las conversiones de tarificador** de la compañía (5.316 de
10.685). La mitad de la captación se juega en este funnel.

---

## 2. El embudo de Salud, paso a paso

De `analisis analytics salud ultimos 30 dias v2.csv`, **2–31 ago 2026**, con **usuarios activos
y recuento de eventos** en paralelo. Los usuarios son la cifra buena: los eventos se repiten
cuando alguien retrocede, y algunos pasos se disparan una vez por asegurado.

### Tarificación

| Paso | Usuarios | Paso a paso | Eventos/usuario |
|---|---|---|---|
| `salud-codigo-postal` | 7.048 | — | 1,35 |
| `salud-3-num-asegurados` | 6.754 | 95,8% | 1,36 |
| `salud-fecha-nacimiento` | 6.470 | 95,8% | **1,88** |
| `salud-5-fechas-contratacion-salud` | 6.265 | 96,8% | 1,38 |
| `salud-6-lead` | 6.155 | 98,2% | 1,30 |
| `salud-7-consentimiento` | 4.986 | **81,0%** | 1,34 |
| `salud-8-precio` | 4.350 | 87,2% | 1,30 |

**Del código postal al precio se conserva el 61,7%.** En usuarios el embudo es monótono, cosa
que en eventos no pasaba.

**El lead nace en el paso 6, antes del consentimiento y antes del precio.** Quien se pierde en
el consentimiento —el 19%— **ya es un lead**.

Fuera de esa secuencia: **`salud-1-seleccion-cliente` 1.803 usuarios** y **`salud-nif-cliente`
767**, la rama de "ya soy cliente". Solo 1.803 de 7.048 pasan por esa pantalla, y su reparto es
**85% móvil** frente al 56% del resto. Hay que preguntar qué es (`04` §3.8).

### El número de asegurados por cotización, por fin

`salud-fecha-nacimiento` da **12.149 eventos entre 6.470 usuarios = 1,88**, y
`salud-datos-asegurado` da **1,99**. Es decir, **una cotización media cubre a dos personas**.

Importa porque condiciona tres cosas del prototipo: la **longitud del cuestionario de salud**,
que es por asegurado; el riesgo de superar la **ventana de 20 minutos** del CRM; y el peso del
**precio familiar** frente al individual.

### Contratación

| Paso | Usuarios | Paso a paso | Eventos/usuario |
|---|---|---|---|
| `salud-datos-titular` | 996 | — | 1,29 |
| `salud-direccion-titular` | 182 | **18,3%** | 1,84 |
| `salud-datos-asegurado` | 168 | 92,3% | 1,99 |
| `salud-resumen-asegurado` | 122 | 72,6% | 1,53 |
| `salud-pre-cuestionario-salud` | 110 | 90,2% | 1,05 |
| `salud-cuestionario-salud-resumen` | 96 | — | 1,51 |
| `salud-pago-tpv` | **22** | 20,0% | 1,00 |

Salidas: `contratar-fin-salud-teladoc` 25 usuarios, `-teladoc-proviene` 5,
`cuestionario-proviene-salud` 22, `si-proviene-salud` 9, `contratar-fin-salud-proviene` 10.

### Dos corroboraciones que validan el conjunto

- **`salud-pago-tpv` = 22 usuarios en 30 días**, frente a las **~18 ventas online al mes** de
  la línea base (`analitica/03-linea-base.md` §1). Y su ratio eventos/usuario es **1,00**: cada
  persona llega al TPV una sola vez.
- **Teladoc = 30 usuarios** (25 + 5), frente a los **112 en 4 meses = 28/mes** de los estados
  del CRM de `contexto/01-embudo-y-datos.md`.

### Los muros, y el mayor no es el que pensábamos

| Transición | | Se pierde |
|---|---|---|
| Dirección → TPV | 182 → 22 | 87,9% |
| **Datos del titular → dirección** | 996 → 182 | **81,7%** |
| **Precio → inicio de contratación** | 4.350 → 996 | **77,1%** |
| Código postal → precio | 7.048 → 4.350 | 38,3% |

**De 7.048 personas que empiezan, 22 pagan: el 0,31%.**

El muro del precio, que es la prioridad declarada del proyecto, **no es el mayor**. Entre los
datos del titular y la dirección se pierde el **81,7%**, y nadie lo había visto porque se daba
el tramo por no instrumentado. Es el primer sitio donde mirar (`04` §1.3).

### El KO del cuestionario es marginal

**25 usuarios derivados a Teladoc sobre 996 que inician contratación: un 2,5%.** Cierra la
hipótesis del techo estructural de `analitica/03-linea-base.md` §6.2.

### Dispositivo: se invierte según el tramo

En usuarios el reparto es **55,8% móvil, 43,4% escritorio, 0,7% tablet** — bastante más
escritorio que en eventos (61,8/37,5), porque **cada usuario de móvil dispara más eventos**.

Y la conversión **cambia de signo según el tramo**:

| Tramo | Móvil | Escritorio | |
|---|---|---|---|
| Tarificación (CP → precio) | 54,8% | **69,3%** | escritorio ×1,3 |
| **Precio → inicia contratación** | **32,6%** | 13,1% | **móvil ×2,5** |
| Datos titular → TPV | 1,7% | **3,5%** | escritorio ×2,1 |
| Extremo a extremo | 0,30% | 0,32% | igual |

**Escritorio completa mejor el tarificador, móvil pulsa mucho más "Contratar", escritorio
remata mejor.** Y de punta a punta se igualan.

El dato llamativo es el del medio: **en escritorio, de cada 100 que ven el precio solo 13
inician la contratación, frente a 33 en móvil.** Puede ser que en escritorio se compare más
—encaja con lo que dice ATC—, o que el CTA funcione peor en esa pantalla. Si es lo segundo, es
directamente accionable en nuestro rediseño. Preguntado en `04` §2.6.

### Y una explicación mucho más simple para el ×1,8

Barajábamos bots o consentimiento de cookies. La explicación probable es que **eran recuentos de
eventos, no de personas**: el ratio medio es de **1,3 eventos por usuario**. Con usuarios, la
brecha con el CRM debería encogerse mucho. Pendiente de comprobar en `04` §3.7.

---

## 3. El punto ciego es del *porqué*, no del *cuánto*

**"Tarificador" es un único título de página con 271.704 vistas**: el **58%** de todos los
`page_view` del site. Los trece ramos y todos sus pasos colapsan en un solo título, así que
**desde vistas de página no se puede construir ningún embudo**.

Pero eso ya no es el problema que creíamos, porque **la dimensión `paso tarificadores` sí da el
embudo** (§2). Lo que el iframe impide es *ver* lo que pasa dentro: Clarity no graba ahí (§4),
así que sabemos **cuánta gente se cae en cada paso y no por qué**.

Un detalle que lo confirma: la página `/calcular-seguro-medico` registra **9.949 eventos** en 30
días, mientras los pasos de Salud suman **65.952**. Los eventos de paso **no se atribuyen a esa
URL** — viven bajo la del iframe. Por eso filtrar GA4 por esa URL no devuelve el embudo, y hay
que usar la dimensión de paso.

### Rastro en títulos de página, ahora secundario

Algunos pasos tienen título propio —`Cuestionario Salud` 500, `Condiciones solicitud
contratación online` 98, `Forma de pago` 80, `Firma electrónica rechazada` 52, en 4 semanas—.
Encajan por orden de magnitud con los estados del CRM, pero **la dimensión de paso es mejor
fuente** y los deja como comprobación cruzada.

### Una página de error con mucho tráfico

**"Redirección fallida" tiene 1.413 vistas** en 4 semanas y "404 Error" otras 475. No sabemos
qué las provoca ni si están en el camino del funnel, pero 1.413 no es residual.

---

## 4. Clarity: 30 días, y el tarificador filtrado por URL

Hay un export **filtrado a `/calcular-seguro-medico`** (regex sobre la URL, 30 días, 7.858
sesiones) que es con diferencia el dato más útil de Clarity, porque aísla el funnel del resto
del web. Va primero; la comparación de ventanas viene después.

### El tarificador contra el resto del site

| Métrica | Site (30d) | **Tarificador (30d)** | Relación |
|---|---|---|---|
| Sesiones | 236.400 | **7.858** | — |
| % bots | 28,8% | **17,9%** | ×0,62 |
| **Móvil** | 64,4% | **75,6%** | ×1,17 |
| **Escritorio** | 35,6% | **24,4%** | ×0,69 |
| Páginas por sesión | 1,35 | **2,63** | ×1,95 |
| Profundidad de scroll | 46,96% | 41,25% | ×0,88 |
| **Tiempo activo** | 39s | **133s** (2,2 min) | ×3,41 |
| **Tiempo total** | 110s | **247s** (4,1 min) | ×2,25 |
| Clic inactivo | 6,10% | **10,59%** | ×1,74 |
| **Clic atrás rápido** | 5,22% | **22,82%** | **×4,37** |
| Clic de salida | 10,58% | 11,48% | ×1,09 |
| LCP | 2,916s | **2,105s** | ×0,72 |
| INP | 216ms | 224ms | ×1,04 |
| **CLS** | 0,103 | **0,217** | ×2,11 |

**Y esto matiza lo que decía antes este documento:**

**El funnel es más móvil que el site: 75,6% frente a 64,4%.** El escritorio baja al **24,4%**,
no el 36% del site. Refuerza el mobile-first, y corrige la nota que había puesto en
`conceptualizacion/CLAUDE.md`.

**Sí hay una señal de fricción medible, y es fuerte: el clic atrás rápido está en el 22,82%,
más de cuatro veces el del site.** Casi una de cada cuatro sesiones del tarificador acaba
volviendo atrás de golpe. Es navegación del navegador, no un clic dentro del iframe, así que
**Clarity sí lo captura pese a la ceguera**. Es el mejor indicador de fricción que tenemos hoy
sobre el funnel, y se puede segmentar por dispositivo, origen y fecha.

**El problema de rendimiento del tarificador es el CLS, no el LCP.** Justo lo contrario de lo
que se deducía del dato global.

> **Las tres Core Web Vitals, y dónde estamos** (bueno / millorable / malo):
> - **LCP** — cuánto tarda en aparecer el elemento visible más grande. ≤2,5s / 2,5-4s / >4s.
>   **Tarificador 2,105s: bueno.**
> - **CLS** — cuánto se mueve el contenido mientras carga. ≤0,1 / 0,1-0,25 / >0,25.
>   **Tarificador 0,217: millorable, en la parte alta.**
> - **INP** — cuánto tarda la página en reaccionar a un toque. ≤200ms / 200-500ms / >500ms.
>   **Tarificador 224ms: entrando en millorable.**

En una pantalla de **formulario** el CLS pesa más que en cualquier otra: si el contenido se
mueve después de que el usuario haya apuntado a un campo o a un botón, **pulsa donde no
quería**. Y con un 76% de móvil, con objetivos pequeños y el dedo tapando la pantalla, se paga
más caro. El sospechoso obvio es **el iframe cargando y redimensionándose**.

**Se corrige por construcción en el funnel nuevo**, que no lleva iframe. Lo que sí conviene es
que el prototipo **reserve espacio** para lo que cargue tarde, en vez de dejar que empuje el
contenido al llegar.

**El tiempo medio en el tarificador es de 2,2 min activos y 4,1 min totales.** La ventana del
CRM son 20 minutos, así que **de media se queda muy por debajo**. Falta la distribución para
saber cuánta gente se va a la cola, pero el promedio tranquiliza (`04` §2.3).

**Y hay una fuga lateral que no habíamos visto**: desde el tarificador, **353 sesiones van a
`/solicitar-presupuesto`**, un formulario alternativo. Son personas que abandonan el tarificador
y piden presupuesto por otra vía. Además **693 sesiones visitan páginas de modalidad concretas**
—`completo` 360, `medifiatc` 243, `sin-hospitalizacion` 90—, o sea gente saliendo a leer qué
cubre cada modalidad. Eso respalda directamente el trabajo de detalle de coberturas en
resultados.

**Casi todo el mundo entra desde dentro del site**: `www.fiatc.es` es el referente de 6.933 de
las 7.858 sesiones. Aparecen también **40 sesiones desde `chatgpt.com`**.

**Y un 38,8% de las sesiones tienen un error de JavaScript** (3.045 de 7.858, casi todas
`script error.`). En una página con un iframe de otro origen, `script error.` es el error
enmascarado por CORS, así que probablemente viene de dentro del tarificador. Conviene
confirmarlo: es mucho volumen para dejarlo sin mirar.

### La comparación de ventanas, y por qué no se leen pocos días

La ventana de 30 días resuelve la contradicción que había entre las dos fotos de 3 días: **la
anómala era A**, no las dos. B coincide con los 30 días casi punto por punto.

| Métrica | A · 22-24 ago<br>*3d, sáb-lun* | B · 30ago-1sep<br>*3d, dom-mar* | **C · 3ago-1sep<br>30 días** |
|---|---|---|---|
| Sesiones | 10.874 | 19.135 | **236.400** |
| Sesiones/día | 3.625 | 6.378 | **7.880** |
| % bots (sobre total + bots) | 66,4% | 12,9% | **28,8%** |
| **Móvil** | 83,3% | 64,6% | **64,4%** |
| **Escritorio** | 16,7% | 35,4% | **35,6%** |
| Usuarios recurrentes | 8,1% | 14,7% | **15,2%** |
| Páginas por sesión | 1,26 | 1,35 | **1,35** |
| Profundidad de scroll | 43,65% | 47,59% | **46,96%** |
| Tiempo activo | 35s | 40s | **39s** |
| Clic inactivo | 5,29% | 6,15% | **6,10%** |
| Clic atrás rápido | 4,09% | 5,44% | **5,22%** |
| Clic de salida | 5,50% | 10,10% | **10,58%** |
| Sesiones en `/calcular-seguro-medico` | 422 | 686 | **7.793** (260/día) |
| LCP | 2,96s | 2,88s | **2,916s** |
| INP | 216ms | 216ms | **216ms** |
| CLS | 0,162 | 0,0865 | **0,103** |

**A se desvía 18,9 puntos en móvil y 37,7 en bots; B se desvía 0,1 puntos en móvil.** A era un
fin de semana en plena vacación y además parece que coincidió con un pico de bots. La lección
sigue en pie: **una foto de 3 días puede engañar del todo**.

### El reparto de dispositivo, y las tres herramientas no coinciden

| Fuente | Qué mide | Móvil | Escritorio |
|---|---|---|---|
| Clarity, site | sesiones, 30 días | 64% | 36% |
| Clarity, `/calcular-seguro-medico` | sesiones, 30 días | 76% | 24% |
| **GA4, pasos de Salud** | **usuarios, 30 días** | **56%** | **43%** |

**Para decisiones de diseño manda el de GA4**, porque cuenta **personas que usan realmente los
pasos del tarificador**, no visitas a la página que lo contiene. Clarity mide el contenedor y
en sesiones, no en usuarios.

Y con ese reparto, **el escritorio es el 43%: no es un caso secundario**. Más el detalle de
que su conversión cambia de signo según el tramo (§2).

### Hay volumen, pero no visibilidad: Clarity no ve dentro del iframe

**Confirmado.** El tarificador aparece en las grabaciones como un **rectángulo gris con el
icono de "ojo tachado"** —el marcador de contenido no capturado— y las sesiones registran
**"Clics: 0"** aunque duren minutos, porque los clics pasan dentro del iframe.

**Matiz importante**: la ceguera es del *interior* del iframe, no de la página. Clarity sí
captura la navegación y los clics de la página contenedora, y de ahí salen señales fuertes
—clic atrás rápido 22,82%, clic inactivo 10,59%— que se ven arriba. Lo que no hay es **nada a
nivel de campo o de paso**.

El volumen está: **5.053 grabaciones** de `/calcular-seguro-medico` en 30 días, de 7.793
sesiones. Lo que falta es qué se ve en ellas.

**Consecuencia**: las fugas 1, 2 y 3 pasan dentro del tarificador, así que **no se pueden
diagnosticar con Clarity hoy**. El plan de `analitica/01-clarity.md` queda como plan para el
funnel nuevo, que no usa iframe.

Dos efectos secundarios que importan:

- **Las señales de fricción del site excluyen el funnel por construcción.** Ese 6,10% de clic
  inactivo o 5,22% de clic atrás rápido no incluyen ni un clic del tarificador, así que **no
  sirven como base de comparación** para nada del embudo.
- **Los resúmenes de IA de Clarity inventan.** En una sesión de 4:39 con 0 clics registrados,
  el resumen automático concluye que el usuario "estaba enfocado en completar el formulario".
  No hay dato que lo sostenga.

**Lo que sí sobrevive, y es más útil de lo que parece**: el **tiempo en la página del
tarificador** se mide igual. Sacar su distribución responde **cuánta gente supera la ventana de
20 minutos** del CRM (`04` §2.3), que hoy es una incógnita. También son visibles el referente de
entrada y el dispositivo por sesión. Detalle en `analitica/01-clarity.md`.

### GA4 y Clarity coinciden, si se comparan bien

Aquí hubo un error de método propio que conviene dejar escrito, porque estuvo a punto de
convertirse en una alarma. Se comparó **Clarity site 3 ago–1 sep (30d)** con **GA4 site 27 jul–23
ago (28d)**: 7.880 sesiones/día frente a 2.557, un **×3,08**. Se llegó a plantear que GA4
pudiera estar perdiendo dos tercios del tráfico por el consentimiento de cookies.

**Periodos distintos, todo el web, y "sesión" no significa lo mismo en las dos herramientas.**
Comparando como toca —misma URL, mismo periodo, misma métrica:

| | Periodo | Usuarios |
|---|---|---|
| Clarity, `/calcular-seguro-medico` | 3 ago – 1 sep | **7.003 únicos** |
| **GA4, primer paso `salud-codigo-postal`** | 2 – 31 ago | **7.048** |

**Difieren un 0,6%.** Las dos herramientas cuentan prácticamente lo mismo, y eso es una
**validación fuerte del embudo de §2**: dos sistemas independientes, con tecnologías distintas,
ven a la misma gente.

Queda una cifra descolgada: el informe de páginas de GA4 da **3.706 usuarios activos** para esa
URL, la mitad. **Y tiene explicación**: los eventos de paso no se atribuyen a esa URL, viven
bajo la del iframe, así que el informe de página pierde a quien usa el tarificador sin generar
una vista de página propia. Es la misma razón por la que filtrar GA4 por URL no devuelve el
embudo (§3).

Del desajuste a nivel de site no sabemos la causa, pero **ya no es un problema del proyecto**:
las cifras que usamos son las del embudo, y ahí las dos fuentes cuadran.

### Tres cautelas sobre la herramienta

- **"Compras" registra 2 sesiones** tanto en la ventana de 3 días como en la de 30. La misma
  cifra exacta en periodos distintos: el panel está roto o mide algo que casi nunca ocurre.
- **Los "eventos inteligentes" no son fiables.** "Finalización de la compra" da 795 sesiones
  en 30 días frente a esas 2 compras. Son heurísticas automáticas: no valen como métrica de
  negocio.
- **INP sale exactamente 216ms en las tres ventanas.** Que un percentil 75 no se mueva ni un
  milisegundo en tres periodos distintos es raro; conviene confirmarlo con otra fuente antes de
  usarlo como argumento.

### Dos pistas que se refuerzan con los 30 días

- **`evicertia.com` es el cuarto referente con 10.106 sesiones** (337/día), ya por delante de
  TikTok. Son personas **volviendo** del paso de firma, en todos los ramos. Es el rastro más
  gordo que tenemos del tramo de contratación y nadie lo está usando.
- **El rendimiento**: LCP 2,916s por encima del umbral bueno (<2,5s), CLS 0,103 justo en la
  frontera (<0,1) e INP 216ms con la reserva de arriba. Con dos tercios de móvil, el LCP es el
  que merece atención.

---

## 5. Qué cambia en nuestras preguntas

**Respondidas, y hay que dejar de preguntarlas:**

- **Existe el embudo de Salud paso a paso, y llega hasta el pago.** No hay que instrumentar
  nada para diagnosticar cuantitativamente las cuatro fugas.
- **El clic en "Contratar" se mide** como transición entre pasos, aunque no exista como evento.
- **El KO del cuestionario es el 2,5%** de quien inicia contratación: no es el techo de la
  venta online.
- **El reparto de dispositivo**: 61,8% móvil / 37,5% escritorio en el conjunto, y **la cuota de
  móvil cae al avanzar**. En el tarificador según Clarity, 76/24.

**Nuevas, para la sesión:**

1. **¿Qué es `salud-1-seleccion-cliente`?** Solo 2.226 eventos frente a 9.523 del código
   postal, y 84,3% móvil frente al 62% del resto.
2. **¿Por qué la numeración de pasos se salta el 2 y el 4**, y por qué varios pasos no llevan
   número?
3. **¿Por qué el segmento "Conversiones tarificador" está parcheado a mano** con
   `autos-neo-precios|vida-6-consentimiento|.*not set.*`?
4. **¿Se puede sacar el embudo en sesiones o usuarios**, no en recuentos de eventos? Es lo que
   resolvería el ×1,8 con el CRM y permitiría contar personas.
5. **¿Qué pasa entre los datos del titular y la dirección**, donde se pierde el 81,7%?
