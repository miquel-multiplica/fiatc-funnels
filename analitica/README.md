# Analítica y medición

Cómo se mide hoy el funnel de Salud, qué falta, y qué hay que dejar preparado para medir el
funnel nuevo.

| Archivo | Contenido | Úsalo para |
|---|---|---|
| `04-preguntas-cliente.md` | **Lista única y priorizada de preguntas**, agrupadas por interlocutor | **Preparar y conducir la sesión de analítica** |
| `00-como-se-mide-hoy.md` | Quién es dueño de qué, definiciones oficiales del cliente, ciclo de vida del lead en el CRM, qué se mide y qué no | Entender el punto de partida antes de proponer medición |
| `03-linea-base.md` | Cifras cerradas ago-25 → jul-26: pólizas por canal, conversión por rating y campaña, estacionalidad, ATC | Cualquier cifra del embudo; fijar objetivos |
| `02-medicion-funnel-nuevo.md` | Especificación de eventos por fuga, identificador de cotización, y qué medir para validar cada decisión del prototipo | Hablar con SEOCom y Héctor López |
| `01-clarity.md` | Plan de diagnóstico con Clarity, por prioridad y con hipótesis | Diagnosticar *por qué* se abandona en las fugas 1 y 2 |

## Por dónde empezar

Para **la sesión con el cliente**: `04-preguntas-cliente.md`, que es autocontenido.

Para **entender el terreno**: `00` (cómo se mide) → `03` (qué dicen los números) → `02` (qué
pedir) → `01` (cómo diagnosticar).

## Las cinco cosas que hay que saber

1. **El cierre offline es la norma.** 93 de cada 100 pólizas las cierra una persona; lo
   online es el 7,0%. El funnel es hoy un generador de leads, no un canal de venta directa.
2. **No existe identificador que una presupuesto, lead y contratación.** Se puede medir *si*
   mejora, no *por qué* — ni atribuir lo que se materializa en la pata telefónica.
3. **Dos confusores grandes y cuantificados**: la estacionalidad es ×2,3 entre el mejor mes y
   el peor, y la conversión varía ×4,5 según el rating (calidad del lead). El antes/después
   hay que leerlo segmentado, no en agregado.
4. **El tramo entre el clic en contratar y la firma no está instrumentado**, porque el iframe
   lo hacía invisible. El funnel nuevo no usa iframe: es la ocasión de arreglarlo, y solo
   existe una vez.
5. **Dos conclusiones que afectan a lo que podemos prometer** (`03` §6): con 18 pólizas
   online al mes, la métrica de éxito no puede ser la venta online —hay que comprometerse con
   el clic en contratar y las firmas, que sí tienen volumen—; y el cuestionario de salud, al
   derivar a revisión médica con un solo "Sí", **puede ser un techo estructural** cuya altura
   nadie ha medido.

## Aviso de uso

`00`, `01`, `02` y `03` son **razonamiento interno**: incluyen nuestras propias correcciones y
cifras que hemos tenido que rectificar. `04` está redactado para poder plantearse tal cual
delante del cliente.

Las cifras de `03` **sustituyen** las estimaciones de `contexto/01-embudo-y-datos.md` donde se
solapen: aquel documento cruzaba sesiones de GA4 2025 con leads de negocio 2026 y lo advertía
en cabecera.
