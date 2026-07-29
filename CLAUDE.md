# FIATC Salud — Funnel responsive (quick wins)

## Archivo de trabajo actual
`funnel-salud-quickwins.html` (repo raíz) — **este es el archivo activo**. Un solo HTML autocontenido (CSS + HTML + JS inline), zero-build, se abre con `file://` y se publica en GitHub Pages. Responsive: se valida desktop directo y mobile con el device mode de Chrome.

Evoluciona el prototipo original `wireframe_propuesta.html` (documentado en `PROTOTIPO-PROPUESTA.md`), reutilizando piezas de UX/copy **sin** la carcasa de iPhone ni el chatbot.

## Base de conocimiento (inputs de la inmersión — NO editar como diario)
`README.md`, `00-contexto.md`, `01-embudo-y-datos.md`, `02-hallazgos-clave.md`, `03-backlog-quickwins.md` (26 quick wins priorizados). Fuente canónica del proyecto; leer ahí antes de decidir. Prioridad = página de resultados (fuga 63-72%).

## Principios de contenido
- **Fidelidad de copy**: nada inventado; sale de guiones de ATC, web y área privada de FIATC.
- **Dos audiencias en resultados** (~40% portabilidad "sin carencias desde el día uno" / ~59% primer seguro): mensaje dual condicional, no universal.
- **Consentimiento granular por canal** (Ley ATC, oct 2026): opt-in por canal, trazable.

## Arquitectura del archivo
- Tokens de color: solo variables `--wf-0/10/20/30/40/60/90/100` (grises; 30 = `#DCE3EC`). Fuente Roboto. SVGs inline. Sin dependencias externas, sin emojis.
- **Shell app**: `body { height:100vh; display:flex; flex-direction:column; overflow:hidden }`; `.app-header { flex-shrink:0 }` (fijo, persigue el scroll); `.app-main { flex:1; min-height:0; overflow-y:auto }` (scroll interno). NO usar `position:sticky` en el header.
- **Header**: full-width. Desktop: título "Calcula tu seguro de salud" izq · logo centro · "Hablemos" der. Mobile: sin título, logo centro, Hablemos der. Progress bar bajo el header. Clic en logo → `openExit()` (exit-intent).
- **Back**: mobile en la cabecera (`.app-back`); desktop (≥900) botón `.gutter-back` fixed pegado al borde izq de pantalla.
- **Navegación**: `PLANNED_FLOW = ['step0','stepCP','step1','step2','step4','step5','stepDNI','step6','step6b']` → `showStep/nextStep/prevStep`. `stepDNI` es condicional (solo si `isClient`); nextStep/prevStep lo saltan si no.
- **Modales** (patrón `.side-modal`): panel lateral derecho en desktop / bottom-sheet en mobile. Hablemos (contacto/agendar) y `#exitModal` (exit-intent). IMPORTANTE: `.side-modal` lleva `overflow:hidden` para clipar el panel cerrado (`translateX(100%)`); sin eso desborda a la derecha y corta el header/modal.
- Animación de paso: fade + `translateX(24px)` (dcha→izq), 0.35s.

## Estado por pantalla y pendientes
Ver la memoria `project_funnel_build.md` (estado vivo por pantalla + "para mañana" + decisión de calculadora QW#1). Resumen: step0→step7 (resultados, base) HECHOS; contratación pendiente.

## Convenciones de edición
- Editar solo `funnel-salud-quickwins.html`. No crear archivos nuevos ni dependencias.
- Solo variables `--wf-*` para color. SVGs inline. Sin emojis.
- No añadir comentarios salvo que el WHY sea no obvio.
- No commitear/push salvo que el usuario lo pida.
