# Funnel de Salud — documentación funcional

Documenta **`funnel-salud-quickwins.html`**, el prototipo activo. Es el mapa funcional
para quien tenga que integrarlo: qué pantallas hay, en qué orden, qué es condicional,
qué está simulado y qué decisiones de negocio quedan abiertas.

Para el prototipo anterior, ver `PROTOTIPO-PROPUESTA.md` (`wireframe_propuesta.html`).
Para el porqué de cada mejora, ver `03-backlog-quickwins.md`.

> **Alcance del entregable.** Esto es una propuesta de diseño y UX, no una
> especificación funcional cerrada. Las reglas de negocio (cuándo derivar a revisión
> médica, cuándo cobrar, qué validaciones aplican) las decide FIATC y las implementa IT.
> Donde el prototipo toma una decisión de negocio, se marca abajo como **abierto**.

---

## 1. Estructura general

Un solo HTML autocontenido (CSS + HTML + JS inline), sin dependencias ni build. Se abre
con `file://` y se publica en GitHub Pages.

**Shell tipo app**: `body` a `100vh` con `overflow:hidden`; cabecera fija que no scrollea
(`.app-header`, `flex-shrink:0`); el scroll vive en `.app-main`. La cabecera es
`position:relative` para dar referencia a los elementos que cuelgan de ella.

**Una pantalla activa a la vez**: todas las pantallas son `div.step` y solo la que lleva
`.active` se muestra. La navegación no cambia de URL ni recarga.

### Índice del prototipo
Al recargar aparece un índice (`#devIndex`) que permite saltar a cualquier pantalla con
datos demo sembrados (`seedDemo`). Es una herramienta de demo, **no forma parte del
producto**: va deliberadamente sin diseñar para que no se confunda con el funnel.

Saltar por el índice omite las animaciones de entrada y los tooltips de presentación,
porque no hay recorrido previo que las justifique.

---

## 2. Flujo de tarificación

```
PLANNED_FLOW = step0 · stepCP · step1 · step2 · step4 · step5 · [stepDNI] · step6 · step6b
                                                                     ↓
                                                              loading (~4,8 s)
                                                                     ↓
                                                                   step7
```

| Pantalla | Qué hace |
|---|---|
| `step0` | Portada: promesa, banner de campaña, prueba social, acordeón de beneficios |
| `stepCP` | Código postal. Si el CP tiene varias localidades, aparece un selector de zona |
| `step1` | Para quién es el seguro: sólo yo / yo y otros / otros sin incluirme |
| `step2` | Fechas de nacimiento, una por asegurado. Permite añadir y quitar |
| `step4` | Fecha de inicio de cobertura |
| `step5` | ¿Ya eres cliente de FIATC? |
| `stepDNI` | **Condicional**: solo si respondió que sí en `step5` |
| `step6` | Email, con sugerencias de dominio |
| `step6b` | Teléfono con prefijo internacional + consentimiento por canal |
| `step7` | Resultados |

**Navegación**: `showStep` / `nextStep` / `prevStep` sobre `PLANNED_FLOW`.
`stepDNI` se salta en ambos sentidos cuando `isClient` es `false`.

**Fuera del flujo lineal**: `stepRecover` (recuperar un presupuesto guardado por email,
entra directo a resultados).

### Consentimiento por canal (`step6b`)
Opt-in **independiente por canal** — email, WhatsApp, teléfono — cada uno con su toggle,
no un consentimiento único. Responde a la Ley ATC 10/2025 (ver `project_ley_atc`): el
consentimiento debe ser granular, revocable por canal y trazable.

---

## 3. Resultados (`step7`)

Pantalla prioritaria del proyecto: es donde se concentra la fuga (63–72%).

- Pestañas de modalidad que reencuadran el título según el filtro elegido.
- Tarjetas de producto con la más popular destacada y centrada al entrar.
- **Calculadora** (`#calcModal`): permite cambiar asegurados y CP y recalcular sin
  volver atrás en el funnel.
- **Detalle del seguro** (`#detailModal`): se rellena leyendo la propia tarjeta.
- **"Me interesa"** (`#interesModal`): confirma plan y anticipa el proceso antes de
  entrar en contratación.

**Mensaje dual**: ~40% del tráfico viene con portabilidad ("sin carencias desde el día
uno") y ~59% es primer seguro. El copy debe ser condicional a cada audiencia, no
universal.

---

## 4. Flujo de contratación

```
CONTRAT_FLOW = cDatos · cContacto · cDireccion · cAseg1 · cAseg2 · cCuestionario
               · cTelefono · cFirma · cOtra · [cDerogacion] · cPago · cAntes · cTPV
               ↓ (cuestionario con algún "Sí")
             cKO
```

| Pantalla | Qué hace |
|---|---|
| `cDatos` | Datos del tomador |
| `cContacto` | Confirmación de email y teléfono |
| `cDireccion` | Dirección; CP autorrellena ciudad y provincia (no editables) |
| `cAseg1` / `cAseg2` | Datos por asegurado. Permite copiar los del titular |
| `cCuestionario` | Un cuestionario de salud por asegurado, en modal (`#questModal`) |
| `cKO` | **Bifurcación**: derivación a revisión médica telefónica |
| `cTelefono` | Confirmación del móvil para la firma |
| `cFirma` | **Placeholder**: aquí va el iframe de Evicertia |
| `cOtra` | ¿Vienes de otra compañía? |
| `cDerogacion` | **Condicional**: solo si viene de otra compañía |
| `cPago` | Modalidad de pago |
| `cAntes` | Resumen legal y del cargo antes de pagar |
| `cTPV` | **Placeholder**: aquí va el iframe del TPV de Sabadell |
| `cConfirm` | Confirmación, con stepper de lo que queda por hacer |

**Navegación**: `showContrat` / `nextContrat` / `prevContrat` sobre `CONTRAT_FLOW`, con su
propia barra de progreso. `cDerogacion` se salta en ambos sentidos si `comesFromOther`
es `false`.

### El resumen persistente
Acompaña toda la contratación y se va rellenando paso a paso (`updateResumen`): una
sección deja de estar "pendiente" cuando su dato ya se ha recogido.

- **Mobile**: barra inferior a sangre (`.resumen-fab`).
- **Desktop ≥900px**: carrito en la cabecera (`.hcart`), separado del "Hablemos" por una
  línea vertical.
- **En `cConfirm` no aparece**: allí el resumen se abre solo desde la tarjeta central.

**Presentación al entrar** (`playResumenIntro`, solo la primera vez): el paso carga 1,8 s
sin el resumen a la vista; después entra animado — en mobile sube desde abajo, en desktop
gana ancho y empuja el "Hablemos" hacia la izquierda — y a los 2,55 s aparece un tooltip
que explica para qué sirve. El tooltip se va solo a los 7 s, se cierra con su X y
desaparece al abrir el resumen.

El retardo va dentro de la animación CSS (`animation-delay` con `fill-mode: both`), no en
un temporizador. Y el resumen está **desplegado por defecto**: la animación es una capa
añadida, nunca la que decide si se ve. Si dependiera de ella, un fallo dejaría a la
persona sin ver su precio.

### Cuestionario de salud
Modal a pantalla casi completa, una pregunta por vez. Marcar "Sí" abre un campo de
detalle y la siguiente pregunta no aparece hasta pulsar "Continuar"; marcar "No" revela
la siguiente directamente. Se guarda con "Guardar respuestas" y la tarjeta del paso pasa
a "Completado" con opción de editar.

Cuando todos los cuestionarios están completos aparece el botón de salida
(`proceedFromQuest`).

---

## 5. Lógica condicional — resumen

| Condición | Efecto |
|---|---|
| `isClient` | Incluye o salta `stepDNI` |
| `comesFromOther` | Incluye o salta `cDerogacion` |
| Algún "Sí" en el cuestionario | Salta a `cKO` **(abierto, ver §8)** |
| `intentMode` / `insuredCount` | Nº de bloques de asegurado y etiquetas |
| `pagoSelected` | Textos del cargo en `cAntes` y `cConfirm` |
| `reachedResults` | "Guardar presupuesto" en el exit-intent |

---

## 6. Modales y overlays

Todos siguen el patrón `.side-modal`: **panel lateral derecho en desktop, bottom-sheet en
mobile**.

| Id | Para qué |
|---|---|
| `hablemosModal` | Contacto. Tres vistas: canales · agendar llamada · confirmación |
| `faqModal` | Preguntas frecuentes, con 4 contextos según la pantalla |
| `exitModal` | Exit-intent: se dispara al pulsar el logo |
| `calcModal` | Recalcular asegurados y CP desde resultados |
| `detailModal` | Detalle de coberturas de un producto |
| `interesModal` | Confirmación de plan antes de contratar |
| `resumenModal` | Resumen desplegado de la contratación |
| `questModal` | Cuestionario de salud |
| `firmaConfirmModal` | Confirmación previa a la firma |
| `appModal` | Descarga de la app: QR en desktop, botón de store en mobile |

`.side-modal` lleva `overflow:hidden` para clipar el panel cerrado (`translateX(100%)`).
Sin eso desborda a la derecha y recorta la cabecera.

### Agendar llamada
Pide **email, teléfono y franja horaria**. Cinco franjas reales de FIATC en chips, todas
visibles: `10h a 12h` · `12h a 14h` · `14h a 16h` · `16h a 18h` · `18h a 20h`. Selección
única. La confirmación repite el teléfono y la franja elegidos en lugar de un "te
llamamos" genérico.

Se llega desde tres sitios y comparten la misma vista: el modal de Hablemos, el
exit-intent y el pie de las FAQ (`agendarOrigin` controla a dónde vuelve el botón atrás).

### FAQ
Cuatro contextos con su propio juego de preguntas: `resultados` (13), `asegurados` (4),
`cuestionario` (5), `confirmacion` (6). En **desktop ≥901px** la modal va a dos columnas
—preguntas a la izquierda, contacto en la columna gris de la derecha, cada una con su
scroll— y muestra 6 preguntas, así que solo `resultados` conserva el "Ver más". En mobile
es una columna y mantiene su recuento original.

---

## 7. Pantallas de espera

Hay **un solo** componente de loading (`#stepLoading`), reutilizado con textos distintos:

| Momento | Título | Duración |
|---|---|---|
| Antes de resultados | "Ya lo tenemos…" | ~4,2 s |
| Recálculo de precio | "Recalculando…" | — |
| Tras el TPV, antes de confirmar | "Estamos confirmando tu pago" | ~4,8 s |

El título se muta en cada uso, así que **quien lo cambie debe restaurarlo**: `showLoading`
lo devuelve a "Ya lo tenemos…" por eso.

Además, `cFirma` simula el proceso de firma con un spinner y avanza solo a los 5 s.

---

## 8. Decisiones de negocio abiertas

Lo que el prototipo resuelve de una manera concreta pero que FIATC debe confirmar:

1. **Dónde derivar cuando hay un "Sí" en el cuestionario.** Hoy salta directo a `cKO` y
   corta el proceso entero: no llega a firma, ni a pago, ni a confirmación. Está
   pendiente decidir si la derivación debe ocurrir ahí, más adelante (por ejemplo antes
   del pago, para no cobrar sin revisar el riesgo) o solo como aviso en la confirmación.
2. **`cKO` está fuera de `CONTRAT_FLOW`**, así que al entrar deja `contratIdx` en `-1` y
   el botón atrás devuelve a resultados en lugar de al cuestionario. El arreglo depende
   de la decisión anterior.
3. **Copy del tooltip del resumen** ("Consulta aquí tu resumen: seguro, asegurados y
   precio. Se actualiza a cada paso.") es redacción propia: no sale de guiones de ATC ni
   de la web. Pendiente de validar.
4. **Duplicidad en `cDerogacion`**: el título dice que se pueden enviar los documentos por
   email después de contratar, y la nota gris de abajo repite la idea y además da la
   dirección (`web@fiatc.es`). Hay que quedarse con uno de los dos sitios.

---

## 9. Lo que está simulado

Nada de esto es funcional; son maquetas para enseñar el recorrido completo.

- **Firma** (`cFirma`): caja gris con spinner. En real, iframe de Evicertia.
- **TPV** (`cTPV`): formulario de tarjeta imitando la pasarela. En real, iframe de Sabadell.
- **Datos**: todos demo. Los campos se autorrellenan al pulsarlos para agilizar la demo.
- **CP**: solo un código tiene varias localidades, para poder mostrar el caso.
- **Precios y descuentos**: fijos, no hay tarificador detrás.
- **Nº de póliza** (`MED-089341`), email y teléfono: siempre los mismos.

---

## 10. Convenciones

- **Un solo archivo.** No crear dependencias ni archivos nuevos.
- **Color solo con variables `--wf-*`** (grises; `30 = #DCE3EC`). Sin colores literales.
- **SVG inline**, siempre outline (`stroke`, `fill="none"`), nunca filled. Sin emojis.
- **Escala tipográfica**: 10/12/14/16/18/21/24/28/37, más 32/43 en desktop. Nada de 13, 15, 20, 22.
- **Fidelidad de copy**: nada inventado; sale de guiones de ATC, la web y el área privada.
  Lo que sea redacción propia se marca como pendiente de validar.
- **Comentarios solo cuando el "por qué" no es obvio.**

### Reglas visuales que conviene no romper

- **Azul claro `#CEE1F2` sin borde y sin ancho completo = informativo. Blanco con borde
  `#C5CBD2` y ancho completo = seleccionable.** Se estableció al detectar que una píldora
  informativa era indistinguible de las tarjetas pulsables de debajo.
- **Los acordeones animan a la altura real** (`grid-template-rows: 0fr → 1fr`), no a un
  `max-height` fijo: con un tope fijo cada respuesta tarda distinto —anima espacio
  vacío— y las que se pasan del tope quedan recortadas.
- **Ninguna animación debe decidir si algo se ve.** Estado final visible por defecto y la
  animación como capa añadida.
