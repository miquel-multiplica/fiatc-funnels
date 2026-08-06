# FIATC Salud — Funnel responsive (quick wins)

## Archivo de trabajo actual
`funnel-salud-quickwins.html` (repo raíz) — **este es el archivo activo**. Un solo HTML autocontenido (CSS + HTML + JS inline), zero-build, se abre con `file://` y se publica en GitHub Pages. Responsive: se valida desktop directo y mobile con el device mode de Chrome.

Evoluciona el prototipo original `wireframe_propuesta.html` (documentado en `PROTOTIPO-PROPUESTA.md`), reutilizando piezas de UX/copy **sin** la carcasa de iPhone ni el chatbot.

Hay material de trabajo que **no se versiona** porque este repo es público y el cliente
puede verlo: está en `.gitignore` y documentado en la memoria del proyecto, no aquí.

## Documentación funcional
`FUNCIONAL.md` — mapa funcional completo del archivo activo: pantallas, los dos flujos y
su lógica condicional, resumen persistente, modales, loadings, qué está simulado y qué
decisiones de negocio quedan abiertas. **Mantenerlo al día** cuando cambie el flujo, se
añada una pantalla o un modal, o se cierre una de las decisiones abiertas.

## Base de conocimiento (inputs de la inmersión — NO editar como diario)
`README.md`, `00-contexto.md`, `01-embudo-y-datos.md`, `02-hallazgos-clave.md`, `03-backlog-quickwins.md` (26 quick wins priorizados). Fuente canónica del proyecto; leer ahí antes de decidir. Prioridad = página de resultados (fuga 63-72%).

## Principios de contenido
- **Fidelidad de copy**: nada inventado; sale de guiones de ATC, web y área privada de FIATC.
- **Dos audiencias en resultados** (~40% portabilidad "sin carencias desde el día uno" / ~59% primer seguro): mensaje dual condicional, no universal.
- **Consentimiento granular por canal** (Ley ATC, oct 2026): opt-in por canal, trazable. Vive en `step6` (email). Ojo: es DISTINTO de la preferencia de canal de `step6b` ("¿Prefieres por WhatsApp?", para hablar de tu solicitud) — están separados a propósito y no deben juntarse. Ver `FUNCIONAL.md` §2.
- **Enumerar, no negar**: para acotar el alcance de un permiso, decir para qué se usa, nunca "nada de publicidad" — una negación contradice a quien haya aceptado publi un paso antes.

## Arquitectura del archivo
- Tokens de color: solo variables `--wf-0/10/20/30/40/60/90/100` (grises; 30 = `#DCE3EC`). Fuente Roboto. SVGs inline. Sin dependencias externas, sin emojis.
- **Shell app**: `body { height:100vh; display:flex; flex-direction:column; overflow:hidden }`; `.app-header { flex-shrink:0 }` (fijo, persigue el scroll); `.app-main { flex:1; min-height:0; overflow-y:auto }` (scroll interno). NO usar `position:sticky` en el header.
- **Header**: full-width. Desktop: título "Calcula tu seguro de salud" izq · logo centro · "Hablemos" der. Mobile: sin título, logo centro, Hablemos der. Progress bar bajo el header. Clic en logo → `openExit()` (exit-intent).
- **Back**: mobile en la cabecera (`.app-back`); desktop (≥900) botón `.gutter-back` fixed pegado al borde izq de pantalla.
- **Navegación**: `PLANNED_FLOW = ['step0','stepCP','step1','step2','step4','step5','stepDNI','step6','step6b']` → `showStep/nextStep/prevStep`. `stepDNI` es condicional (solo si `isClient`); nextStep/prevStep lo saltan si no.
- **Modales** (patrón `.side-modal`): panel lateral derecho en desktop / bottom-sheet en mobile. Hablemos (contacto/agendar) y `#exitModal` (exit-intent). IMPORTANTE: `.side-modal` lleva `overflow:hidden` para clipar el panel cerrado (`translateX(100%)`); sin eso desborda a la derecha y corta el header/modal.
- Animación de paso: fade + `translateX(24px)` (dcha→izq), 0.35s.

## Estado por pantalla y pendientes
Detalle en `FUNCIONAL.md`; estado vivo y pendientes en la memoria `project_funnel_build.md`.
Resumen: tarificación (step0→step7) y contratación (cDatos→cConfirm) COMPLETAS de punta a
punta. Firma y TPV son placeholders simulados (iban iframes de Evicertia/Sabadell). Índice
de navegación del prototipo al recargar, con datos demo sembrados.
Falta: pulido/feedback de cliente y las 4 decisiones abiertas de `FUNCIONAL.md` §8.

## Reglas visuales establecidas con el cliente
- **Azul claro `#CEE1F2` sin borde y sin ancho completo = informativo · blanco con borde `#C5CBD2` y ancho completo = seleccionable.** Se fijó al detectar que una píldora informativa era indistinguible de las tarjetas pulsables.
- **Acordeones: animar a la altura real** (`grid-template-rows: 0fr → 1fr`), nunca a un `max-height` fijo (cada respuesta tarda distinto y las largas se recortan).
- **Ninguna animación decide si algo se ve**: estado final visible por defecto, animación como capa añadida.
- **Un solo componente de loading** (`#stepLoading`) reutilizado con textos distintos; quien mute su título debe restaurarlo.

## Convenciones de edición
- Editar solo `funnel-salud-quickwins.html`. No crear archivos nuevos ni dependencias.
- Solo variables `--wf-*` para color. SVGs inline. Sin emojis.
- No añadir comentarios salvo que el WHY sea no obvio.
- No commitear/push salvo que el usuario lo pida.
- **Un push por tanda, no uno por ajuste.** Cada push encola un deploy de Pages y cancela el anterior; con pushes seguidos la cola se congestiona, algún deploy muere por timeout (`deployment_queued` en bucle → `Timeout reached`) y el sitio se queda sirviendo una versión antigua sin avisar.
- **Verificar lo publicado con cache-buster y por tamaño**, no buscando una cadena: el CDN cachea 10 min (`max-age=600`). `curl -s -H 'Cache-Control: no-cache' "$URL?cb=$RANDOM"` y comparar `wc -c` con el archivo local. Los `.md` no pasan por Pages y se ven al instante en GitHub.
