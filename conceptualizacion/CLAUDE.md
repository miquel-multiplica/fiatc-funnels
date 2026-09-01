# Conceptualización — wireframe del funnel de Salud

Convenciones **del entregable**. Las de repositorio y proceso están en el `CLAUDE.md` de la
raíz, que se aplica igualmente.

## Archivo de trabajo actual
`conceptualizacion/funnel-salud-quickwins.html` — **este es el archivo activo**. Un solo
HTML autocontenido (CSS + HTML + JS inline), zero-build, se abre con `file://` y se publica
en GitHub Pages. Responsive: se valida desktop directo y mobile con el device mode de Chrome.
Reparto real, contando **usuarios de los pasos del tarificador**: **56% móvil / 43%
escritorio** (GA4, 30 días). El escritorio **no es un caso secundario**, y además su conversión
cambia de signo según el tramo. Ver `analitica/05-ga4-y-clarity.md` §2.

Evoluciona el prototipo original `propuesta/wireframe_propuesta.html` (documentado en
`propuesta/PROTOTIPO-PROPUESTA.md`), reutilizando piezas de UX/copy **sin** la carcasa de
iPhone ni el chatbot.

Es un **wireframe**: gris, sin marca. La capa visual con el design system de FIATC es la
fase de UI y vivirá en `ui/`.

También está aquí `userflow-figma-prompt.md`, el prompt para llevar el flujo a Figma.

## Documentación funcional
`conceptualizacion/FUNCIONAL.md` — mapa funcional completo: pantallas, los dos flujos y su
lógica condicional, resumen persistente, modales, loadings, qué está simulado y qué queda
abierto. **Mantenerlo al día** cuando cambie el flujo, se añada una pantalla o un modal, o
se cierre una decisión abierta.

## Principios de contenido
- **Fidelidad de copy**: nada inventado; sale de guiones de ATC, web y área privada de
  FIATC. Lo que sea redacción propia se marca como pendiente de validar.
- **Dos audiencias en resultados** (~40% portabilidad / ~59% primer seguro): el acordeón
  lleva un argumento para cada una y **se muestran siempre los dos**. En resultados no se
  conoce la audiencia: la portabilidad no se declara hasta `cOtra`. Ver `FUNCIONAL.md` §3.
- **Diez perfiles de cliente de Salud** definidos por FIATC en `contexto/04-perfiles-cliente.md`.
  Útiles para tono y jerarquía de coberturas: la mitad son digitales y comparadores, y tres
  (los de más edad) piden teléfono, oficina o trato humano.
- **"Tomador", nunca "titular"**, en todos los pasos de contratación. Indicación del cliente.
- **Consentimiento comercial** (Ley ATC, oct 2026): hoy un único canal, email, en `step6`.
  Ojo: es DISTINTO de la preferencia de canal de `step6b` ("¿Prefieres por WhatsApp?", para
  hablar de tu solicitud) — están separados a propósito y no deben juntarse. Ver
  `FUNCIONAL.md` §2.
- **Enumerar, no negar**: para acotar el alcance de un permiso, decir para qué se usa, nunca
  "nada de publicidad" — una negación contradice a quien haya aceptado publi un paso antes.

## Arquitectura del archivo
- Tokens de color: solo variables `--wf-0/10/20/30/40/60/90/100` (grises; 30 = `#DCE3EC`).
  Fuente Roboto. SVGs inline. Sin dependencias externas, sin emojis.
- **Shell app**: `body { height:100vh; display:flex; flex-direction:column; overflow:hidden }`;
  `.app-header { flex-shrink:0 }` (fijo, persigue el scroll); `.app-main { flex:1;
  min-height:0; overflow-y:auto }` (scroll interno). NO usar `position:sticky` en el header.
- **Header**: full-width. Desktop: título "Calcula tu seguro de salud" izq · logo centro ·
  "Hablemos" der. Mobile: sin título, logo centro, Hablemos der. Progress bar bajo el
  header. Clic en logo → `openExit()` (exit-intent).
- **Back**: mobile en la cabecera (`.app-back`); desktop (≥900) botón `.gutter-back` fixed
  pegado al borde izq de pantalla.
- **Navegación**: `PLANNED_FLOW = ['step0','stepCP','step1','step2','step4','step5','stepDNI','step6','step6b']`
  → `showStep/nextStep/prevStep`. `stepDNI` es condicional (solo si `isClient`);
  nextStep/prevStep lo saltan si no.
- **Modales** (patrón `.side-modal`): panel lateral derecho en desktop / bottom-sheet en
  mobile. IMPORTANTE: `.side-modal` lleva `overflow:hidden` para clipar el panel cerrado
  (`translateX(100%)`); sin eso desborda a la derecha y corta el header/modal.
- Animación de paso: fade + `translateX(24px)` (dcha→izq), 0.35s.

## Reglas visuales establecidas con el cliente
- **Azul claro `#CEE1F2` sin borde y sin ancho completo = informativo · blanco con borde
  `#C5CBD2` y ancho completo = seleccionable.** Se fijó al detectar que una píldora
  informativa era indistinguible de las tarjetas pulsables.
- **Acordeones: animar a la altura real** (`grid-template-rows: 0fr → 1fr`), nunca a un
  `max-height` fijo (cada respuesta tarda distinto y las largas se recortan).
- **Ninguna animación decide si algo se ve**: estado final visible por defecto, animación
  como capa añadida.
- **Un solo componente de loading** (`#stepLoading`) reutilizado con textos distintos; quien
  mute su título debe restaurarlo.
- **En mobile no hay drag & drop**: los campos de subida de archivo no lo prometen.
- **Reservar espacio para lo que cargue tarde** (imágenes, módulos, el resumen), en vez de
  dejar que empuje el contenido al aparecer. El tarificador actual tiene un CLS de 0,217, más
  del doble del umbral bueno, y en una pantalla de formulario eso hace pulsar donde no se
  quería. Ver `analitica/05-ga4-y-clarity.md` §4.

## Estado y pendientes
Detalle en `FUNCIONAL.md`; estado vivo en la memoria `project_funnel_build.md`.
Tarificación (step0→step7) y contratación (cDatos→cConfirm) COMPLETAS de punta a punta.
Firma y TPV son placeholders simulados (iban iframes de Evicertia/Sabadell). Índice de
navegación del prototipo al recargar, con datos demo sembrados.
La parte transaccional está **aprobada por negocio**; pendiente la revisión de TI y jurídico.

## Convenciones de edición
- Editar solo `funnel-salud-quickwins.html`. No crear archivos nuevos ni dependencias.
- Solo variables `--wf-*` para color. SVGs inline. Sin emojis.
- Escala tipográfica: 10/12/14/16/18/21/24/28/37 (+32/43 en desktop). Nada de 13, 15, 20, 22.
- No añadir comentarios salvo que el WHY sea no obvio.
