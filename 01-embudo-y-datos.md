# FIATC Salud · Embudo y datos

> Dos fuentes con unidades distintas: **sesiones** (tabla GA4 ene-may 2025) y
> **oportunidades/leads** (datos negocio, enero-julio 2026). Los cruces entre ambas son
> órdenes de magnitud, no cifras exactas.

## Embudo consolidado

| Tramo | Dato | Fuente | Estado |
|---|---|---|---|
| Entrada al tarificador | ~4.200-6.500 sesiones/mes | GA4 2025 | — |
| Calidad del tráfico | >90% canales pull (directo, orgánico, SEM) — tráfico cualificado | Diana | Confirmado |
| **Fuga 1 · Arranque** (selección cliente → CP) | **-20%** | GA4 2025 | Causa desconocida (el tráfico es bueno) — diagnóstico Clarity pendiente |
| Tramo de preguntas (asegurados, edad, fecha, datos personales) | Retención 94-99% por paso | GA4 2025 | Sin problema. El nº de pasos no es el problema |
| **Fuga 2 · Consentimiento** (email + tel + RGPD) | **-22% a -30%** | GA4 2025 | Causas por diagnosticar. Anomalía: marzo 70,1% |
| Nace la "oportunidad" (lead) | 25.449 desde enero 2026 (~3.600/mes) | Diana | — |
| Ven precio | ~48-57% de las sesiones de entrada | GA4 2025 (producto pasos 1-7) | — |
| **Fuga 3 · Precio → clic Contratar** | **-63% a -72%** (solo 28-37% clica) | GA4 2025 | El mayor muro. Comparación activa contra otras aseguradoras y comparadores (Rastreator, Acierto). Algunos acaban contratando por otra vía |
| **Fuga 4 · Clic → firma del cuestionario** | 1.260 en 4 meses = 8% de los leads del periodo | Diana | Tramo NO instrumentado paso a paso. Los agentes telefónicos usan estos triggers para acompañar la contratación |
| Interior post-firma | Fluye | — | Los muros están en las transiciones, no dentro |

## Estados atascados en contratación (desde enero 2026)

| Estado | Volumen | Significado (confirmado por Diana) |
|---|---|---|
| Inicio de contratación sin proseguir | 1.260 (4 meses) | Clic en Contratar y caída en algún punto ANTES de firmar el cuestionario. No se sabe el paso exacto |
| W cuestionario no firmado | 56 | Se caen en el paso de firma del cuestionario (SMS) |
| W pendiente pago TPV | 88 | Se caen en el pago. Tiene circuito de recuperación (llamada + reenvío TPV + pago bancario) |
| W proviene de otra entidad | 19 | Caen en la pantalla de documentación O en la selección de forma de pago |
| W respuesta Teladoc | 112 | Marcaron respuesta del cuestionario que deriva a flujo Teladoc (= volumen de KOs) |

⚠ Pendiente confirmar si los W son foto actual o acumulado desde enero.

## Tabla funnel de sesiones (ene-may 2025, GA4)

Retención por paso. Paso 1 = pantalla de selección de cliente.

| Paso | Ene | Feb | Mar | Abr | May |
|---|---|---|---|---|---|
| Sesiones Paso 1 | 6.527 | 5.128 | 5.317 | 5.205 | 4.157 |
| 1. Código postal | 80,3% | 79,4% | 79,0% | 82,0% | 80,7% |
| 2. Nº asegurados | 96,5% | 95,3% | 94,5% | 95,3% | 94,7% |
| 3. Edad | 99,4% | 98,6% | 98,6% | 98,2% | 98,9% |
| 4. Fecha contratación | 98,5% | 99,3% | 98,6% | 99,3% | 98,7% |
| 5. Información personal | 99,2% | 99,3% | 98,2% | 98,1% | 99,2% |
| 6. Consentimiento | 77,1% | 77,8% | 70,1% | 79,6% | 75,4% |
| 7. Precio | 96,9% | 96,5% | 95,1% | 95,9% | 96,0% |
| 8. Clic contratar | 31,8% | 32,6% | 37,0% | 27,6% | 29,0% |
| **Total (llegan a precio)** | 56,2% | 55,2% | 47,5% | 57,1% | 53,5% |

Nota: todo el dato disponible es de época valle. Falta el cuadro de temporada alta (oct-dic),
que es cuando llega el pico de portabilidad (renovación de primas).

## Portabilidad (tabla de Anabel Vidal, 29 jul)

Unidad: asegurados (T. Aseg) — una familia de 4 cuenta 4. Presumiblemente sobre emisiones (a confirmar).

| Origen | 2025 | Ratio | 2026 (parcial ~7m) | Ratio |
|---|---|---|---|---|
| No proviene de cía | 4.071 | 59,49% | 2.882 | 58,29% |
| Proviene de cía | 2.772 | 40,51% | 2.062 | ~41,7% |
| **Total** | 6.843 | 100% | 4.944 | 100% |

Lecturas:
- **Portabilidad = ~40-41%, estable entre años.** Corrige el "la mayoría son portabilidad"
  dicho en el walkthrough: es un segmento grande pero NO mayoritario.
- **Dos audiencias en resultados, casi a partes iguales**: portabilidad (compara contra su
  prima de renovación; argumento = sin carencias desde el día uno) vs. primer seguro (~59%;
  compara contra la sanidad pública: listas de espera, rapidez, desde cuándo puede usarlo).
- Volumen crece: ~700 asegurados/mes 2026 vs. ~570/mes 2025, sin contar aún la campaña de fin de año.
- Pendiente: confirmar si es sobre emisiones y si existe el mismo split sobre cotizaciones
  (¿convierte distinto la portabilidad?).

## Matices transversales de interpretación

- **Decisión multi-sesión y consultada**: tarda días/semanas, se consulta en pareja (fuente ATC).
  Parte de la fuga 3 es pausa, no pérdida: el usuario vuelve como sesión nueva.
- **Leads duplicados confirmados**: re-cotizan desde cero para cambiar algo (p.ej. añadir un
  asegurado olvidado) → los volúmenes están inflados y las conversiones reales son mejores que
  las aparentes. El plan de medición debería deduplicar por email/DNI.
- **Casi nadie usa "Recuperar presupuesto"**, aunque el email automático con el presupuesto
  existe y su enlace aterriza directo en la página de precio (confirmado por IT). El problema
  es de visibilidad/uso, no técnico.
- Estacionalidad: pico ~2 meses antes de fin de año (reciben la nueva prima de su aseguradora).
  Otros disparadores: hijo nuevo, planear tenerlo, lista de espera pública.
