# FIATC · Mejora del funnel de Salud — Contexto del proyecto

> Fecha de consolidación: 29 julio 2026
> Este documento da el contexto mínimo para entender el resto de archivos (01-04).

## Qué es este proyecto

Multiplica (agencia digital) trabaja para FIATC (mutua de seguros española) en la mejora del
funnel de conversión de sus tarificadores online. Proyecto ganado por RFP. Fase actual:
**quick wins sobre el tarificador de Salud** (horizonte 0-3 meses, ~40h de diseño), sin tocar
el motor de tarificación (core) ni los campos obligatorios.

Objetivos del pliego más relevantes para esta fase:
- Aumentar leads cualificados y conversión lead → venta
- Reducir dependencia de llamadas outbound no consentidas (Ley ATC entra en vigor en octubre 2026)
- Dar al usuario control sobre cómo quiere ser contactado
- Aumentar tasa de finalización y confianza en el proceso

## Punto de partida del diseño

La base sobre la que se trabaja es el **prototipo de la propuesta**
(`https://miquel-multiplica.github.io/fiatc-prototipo/wireframe_mobile.html`), presentado en la
fase de RFP. La versión final acordada del funnel de quick wins se construye evolucionando ese
prototipo con la evidencia y las validaciones recogidas en estos documentos — no se parte de cero.
El prototipo es por tanto un input necesario junto a estos archivos.

## El funnel actual de Salud (resumen del flujo)

1. **Pantalla inicial**: No soy cliente / Sí soy cliente / Recuperar presupuesto anterior
2. **Tarificación**: provincia (CP) → nº asegurados → edades → fecha contratación → datos personales
3. **Consentimiento**: email + teléfono + RGPD (aquí nace el "lead", que FIATC llama **"oportunidad"**)
4. **Resultados**: parrilla de modalidades con precio (Completo sin/con copago, Reembolso, Sin hospitalización...) y botón Contratar
5. **Contratación**: datos tomador → dirección → resumen asegurados → cuestionario de salud (6 preguntas Sí/No + peso/altura) → firma del cuestionario (Evicertia, vía SMS) → ¿estás asegurado en otra compañía? → [si sí: pantalla de derogación de carencias — pide enviar la documentación por email a web@fiatc.es] → forma de pago (anual 4% dto. / mensual) → TPV Sabadell → confirmación
6. **Post-pago**: email de bienvenida + **segunda firma** (contrato, por email). Si no firman → bloqueo de la app

### Bifurcación del cuestionario de salud
- Si alguna respuesta implica KO → el usuario no puede seguir online → **Teladoc** (proveedor externo)
  le llama para un cuestionario telefónico más profundo → si supera, contratación offline;
  si no, no contrata o contrata con exclusiones
- La pantalla que ve el usuario en el KO no explica el motivo ni qué pasará ("hemos recibido tu solicitud, te contactaremos")

## Actores y sistemas

| Actor / sistema | Papel |
|---|---|
| Negocio FIATC (Diana, Anabel Vidal) | Owner del funnel, fuente de datos de oportunidades |
| ATC (Atención al Cliente) | Llamadas entrantes, acompañan contrataciones atascadas, reclaman doc de derogación. Fuente de user research indirecto |
| Teladoc | Cuestionario de salud telefónico cuando hay KO online |
| Evicertia | Firma digital del cuestionario (SMS) |
| Evolution | Core de gestión de pólizas |
| Marketing Cloud | Emails automáticos (presupuesto, bienvenida) |
| TPV Sabadell | Pasarela de pago |
| GA4 + Clarity | Analítica web y comportamental |
| IT FIATC | Desarrollo interno del tarificador (integrado hoy por iframe en la web) |

## Vocabulario

- **Oportunidad** = lead (término interno FIATC; usarlo en entregables)
- **Portabilidad** = usuario que viene de otra aseguradora (puede derogar carencias)
- **Derogación de carencias** = eliminar los periodos de espera si acredita seguro anterior (envía póliza anterior + último recibo)
- **Carencia** = periodo tras contratar en que ciertas coberturas no se pueden usar (distinta de **preexistencia** = condición de salud previa del asegurado, que puede acabar en exclusión)
- **KO** = respuesta del cuestionario que impide contratar online estándar

## Fuentes de la información consolidada

1. Pliego técnico y administrativo (RFP)
2. Documento de flujo de contratación Salud (PPT de FIATC, e-commerce)
3. Respuestas escritas de ATC a nuestro cuestionario (23 jul) — user research indirecto
4. Sesión de walkthrough con negocio (27 jul) — dudas de flujo + primeros volúmenes
5. Tabla de funnel de sesiones ene-may 2025 (GA4/analítica FIATC)
6. Email de Diana con aclaraciones sobre estados y tráfico (28 jul)
7. Sesión con IT (28 jul) — viabilidad técnica del backlog
8. Tabla de portabilidad de Anabel Vidal (29 jul)

## Principios de trabajo acordados

- Quick wins = cambios de contenido, secuencia y comunicación **sin tocar el core**
- Fidelidad al copy de FIATC: nada inventado; el contenido sale de lo que FIATC ya comunica
  (guiones de ATC, área privada, web)
- Muchos pasos de baja carga cognitiva > pocos pasos densos (un concepto por pantalla)
- No adelantar la captura de contacto: el contrato implícito del tarificador es "datos por precio"
- La agendación de llamada NO se elimina: negocio quiere mantenerla, se reencuadra como elección del usuario (modal)
