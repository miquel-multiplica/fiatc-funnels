# Línea base ago-25 → jul-26

Lectura de los tres informes que envió FIATC el 31 de agosto de 2026. Es la **primera vez
que tenemos el periodo completo, con una sola unidad y desglose mensual**, que es justo lo
que se había pedido para la reunión del día 2.

> **Fuente**: `material-cliente/` (no versionado) — `Pólizas mensual Salud.xlsx`,
> `Evolución conversión Salud.xlsx`, `Evolución ATC.xlsx`. Periodo ago-25 a jul-26, ramo
> SALU. Sustituye las cifras estimadas de `contexto/01-embudo-y-datos.md` donde se solapen.

---

## 1. Pólizas por canal

| Mes | Online | Agente | Total | % online |
|---|---|---|---|---|
| ago-25 | 15 | 186 | 201 | 7,5% |
| sep-25 | 12 | 201 | 213 | 5,6% |
| oct-25 | 13 | 231 | 244 | 5,3% |
| nov-25 | 27 | 361 | 388 | 7,0% |
| dic-25 | 28 | 383 | 411 | 6,8% |
| ene-26 | 21 | 277 | 298 | 7,0% |
| feb-26 | 28 | 256 | 284 | 9,9% |
| mar-26 | 17 | 230 | 247 | 6,9% |
| abr-26 | 13 | 202 | 215 | 6,0% |
| may-26 | 12 | 202 | 214 | 5,6% |
| jun-26 | 21 | 177 | 198 | 10,6% |
| jul-26 | 13 | 199 | 212 | 6,1% |
| **Total** | **220** | **2.905** | **3.125** | **7,0%** |

**Este informe corrige el anterior.** El dato previo de agente (1.948) **no incluía el call
center externo**; FIATC lo advirtió al enviarlo. Los 957 que faltaban bajan el peso de lo
online de 10,1% a **7,0%**. Es la cifra a usar de aquí en adelante.

> **Confirmado por una segunda fuente del cliente.** El PDF *Información negocio: Modelo
> actual* (pág. 2) da la contratación 100% online de **Salud en el 6%**, frente al 30% del
> total de ramos, y **52.433 cotizaciones** de Salud en el último año. Coincide con el 7,0%
> de aquí dentro del redondeo. Ver `contexto/04-perfiles-cliente.md` §4.

Lo online se mueve entre 12 y 28 pólizas al mes sin tendencia: **es ruido, no serie**. Con
volúmenes así, un mes suelto no dice nada y hay que leer trimestres.

---

## 2. Oportunidades y conversión

51.814 oportunidades en 12 meses (~4.318/mes) y 2.382 convertidas: **4,60% de conversión
global**. Confirma el ~5% que estimábamos. La conversión mensual es notablemente estable
(3,60%–5,07%) **mientras el volumen se dobla**, lo que apunta a que la calidad del tráfico
aguanta los picos.

### Rating: el eje que más separa la conversión

El rating es la **calidad del lead**, no tiene nada que ver con salud ni con riesgo
asegurable. No está definido en ninguna parte de la documentación ni de los informes, así
que queda anotado aquí.

| Rating | Oportunidades | % del total | Ventas | Conversión |
|---|---|---|---|---|
| A | 10.653 | 20,6% | 904 | **8,49%** |
| B | 27.372 | 52,8% | 1.039 | **3,80%** |
| C | 10.451 | 20,2% | 197 | **1,88%** |
| Sin rating | 3.338 | 6,4% | 242 | 7,25% |

**Un rating A convierte 4,5 veces más que un C**, y ninguna palanca de diseño del funnel va
a mover la conversión tanto como eso.

#### El rating es en buena medida un proxy del canal

Los datos lo confirman: **correlaciona muy fuerte con el origen del tráfico**.

| Canal | Oportunidades | % A | % B | % C |
|---|---|---|---|---|
| WEB Fiatc (SEO, directo, app) | 9.622 | **43%** | 47% | 10% |
| SEM · BING | 758 | 35% | 63% | 2% |
| SEM · Extension | 2.555 | 25% | 58% | 17% |
| SEM · Google | 29.383 | 19% | 60% | 21% |
| Newsletter | 716 | 2% | 51% | 47% |
| SEM · Google Landing | 1.740 | 2% | 22% | **76%** |
| RRSS | 945 | 3% | 13% | **85%** |
| Kelisto | 320 | 0% | 25% | **75%** |
| Atrato / Adpepper | 1.911 | 0% | 97% | 3% |
| *media global* | *51.814* | *21%* | *53%* | *20%* |

Coherente con que FIATC diga que las oportunidades de atención al cliente **"no disponen de
un rating"**: lo asigna el sistema de captación online, no el de suscripción.

#### Qué implica para el proyecto

**Es un buen control, precisamente porque el funnel no puede influir en él.** El rating lo
determina de dónde vino el lead, no lo que pase dentro del embudo. Así que:

- **El antes/después del funnel nuevo hay que leerlo por rating**, no solo en agregado. Si
  cambia la mezcla de tráfico, la conversión global se mueve sin que el diseño haya cambiado
  nada. Sale gratis: el rating ya viene en sus informes, no hace falta el identificador de
  cotización.
- **Matiza el "tráfico cualificado" de la inmersión.** Es cierto que el 91,7% son canales
  pull, pero dentro de eso la calidad no es homogénea: la web propia es 43% rating A y SEM ·
  Google —el 60% del volumen— se queda en la media (19% A, 21% C).
- **Buena parte del ×4,5 es una historia de captación, no de embudo.** Conviene no
  atribuirse ni cargar con lo que decide el mix de medios.

#### La pregunta que sí vale la pena hacer
**¿Cómo se comporta la fuga 3 —el muro del precio— por rating?** Si un rating C abandona en
el precio mucho más que un A, es sensibilidad al precio y hay poco que hacer desde el diseño.
Si abandonan por igual, el muro es de diseño y nos incumbe entero. Es el cruce que más
cambiaría nuestro plan de trabajo, y con sus informes debería ser barato de sacar.

### Canal de origen

| Origen | Oportunidades | % | Conversión |
|---|---|---|---|
| SEM · Google | 31.355 | 60,5% | 4,64% |
| WEB Fiatc | 10.446 | 20,2% | 5,99% |
| SEM · Extension | 2.734 | 5,3% | 5,49% |
| SEM · Google Landing | 1.856 | 3,6% | 1,99% |
| Atrato | 1.275 | 2,5% | 0,63% |
| RRSS | 983 | 1,9% | 1,73% |
| SEM · BING | 812 | 1,6% | 6,90% |
| Newsletter | 761 | 1,5% | 0,79% |
| Adpepper | 671 | 1,3% | 0,30% |
| Kelisto | 321 | 0,6% | 0,00% |
| resto | <400 | | |

Dos cosas:

- **Confirma el "tráfico cualificado" de la inmersión**: SEM + web propia son el **91,7%**
  de las oportunidades. El problema del funnel no es a quién le llega.
- **Afiliación y comparadores no funcionan**: Atrato + Adpepper + Kelisto suman 2.267
  oportunidades y **10 ventas (0,44%)**. Los tres aparecen a cero en los últimos meses, así
  que ya se han cortado. Conviene no meterlos en la línea base de comparación.

---

## 3. Estacionalidad: ×2,3 entre el mejor mes y el peor

Oportunidades: **nov-25 = 7.087** frente a **ago-25 = 3.080**. Pólizas: 411 frente a 198.

**Es la consecuencia metodológica más importante de estos informes.** El pico
octubre-diciembre coincide con la ventana de la promo estacional (sept-feb). Si el funnel
nuevo se lanza y se compara contra el trimestre inmediatamente anterior, el resultado dirá
más de la estación que del rediseño — en cualquiera de las dos direcciones.

Lo que hay que fijar antes de lanzar:

- **Comparar mes contra el mismo mes del año anterior**, no contra el trimestre previo.
- **Registrar la fecha exacta de lanzamiento** y si cae dentro o fuera de la promo.
- **Leer por rating** (§2) para separar mezcla de tráfico y efecto del diseño.

Refuerza el argumento del identificador de cotización de
`analitica/02-medicion-funnel-nuevo.md` §1: con estacionalidad ×2,3 y una brecha de rating
×4,5, un antes/después agregado es fácil de discutir.

---

## 4. ATC convierte 2,5 veces más que el funnel

`Evolución ATC.xlsx`: 1.008 oportunidades, 114 convertidas, **11,31%** — frente al 4,60% del
funnel. Con un pico en nov-25 (252 oportunidades).

Es poco volumen (2% del total) pero el ratio importa: **el contacto humano convierte mucho
mejor**. Da soporte de datos a decisiones del prototipo que hasta ahora eran de criterio:
"Hablemos" siempre visible, agendar llamada con franja horaria, la salida a llamada cuando
el cuestionario de salud se complica. **No son escapes del funnel, son la ruta que más
convierte.**

Ojo con el sesgo: quien llama a ATC ya viene con intención alta, así que el 11,31% no es
trasladable a "si llamáramos a todo el mundo convertiríamos al 11%".

---

## 5. Descuadres que hay que resolver el día 2

**629 pólizas sin explicar.** El informe mensual da 3.125 pólizas; las oportunidades
convertidas son 2.382, más 114 de ATC = 2.496. Faltan 629 (20%). Puede ser que una
oportunidad genere varias pólizas, que haya pólizas sin oportunidad previa, o que los dos
informes cuenten periodos de alta distintos. **Es exactamente el tipo de trampa de
denominador que ya nos ha costado una cifra mal**, así que conviene cerrarlo antes de
construir nada encima.

**3.338 oportunidades sin rating** (6,4%) dentro del total global, además de las 1.008 de
ATC que no entran en el informe. Convertirían al 7,25%, muy por encima de la media, así que
no son residuales.

**Oportunidades/mes: 4.318, no 3.600.** La cifra que usábamos (25.449 desde enero 2026) no
cuadra con estos informes: ene-jul 2026 suman 27.207. Probablemente sean oportunidades netas
frente a brutas, o cortes de fecha distintos. Al comparar hay que decir cuál se usa.

---

## 6. Qué implica para lo que podemos prometer

Dos conclusiones que salen de esta línea base y que afectan al planteamiento del proyecto,
no al diseño de las pantallas.

### 6.1 · La métrica de éxito no puede ser la venta online

Son **18 pólizas al mes**, entre 12 y 28, sin tendencia. Con ese volumen, una mejora del 50%
son **+9 pólizas al mes**: indistinguible de la variación normal de un mes cualquiera.

Es decir: **si el entregable promete "más ventas online", no vamos a poder demostrarlo en
meses**, ni aunque el rediseño funcione muy bien. No es un problema de instrumentación —es de
tamaño de muestra— y por tanto no lo arregla ningún identificador ni ningún evento nuevo.

Lo que hay que hacer es comprometerse con **métricas intermedias que sí tienen volumen**:

| Métrica | Volumen mensual | Sirve para |
|---|---|---|
| Clic en "Contratar" | miles de sesiones | La fuga 3, que es la prioridad. Un cambio del 10% se ve |
| Firmas del cuestionario | ~315 | La fuga 4. Con 315 al mes, un cambio del 10% también se ve |
| Pólizas online | ~18 | **Nada, a corto plazo.** Se lee por trimestres o por año |

No es rebajar la ambición: es elegir dónde se mide para que el resultado sea defendible.

### 6.2 · El cuestionario de salud puede ser un techo estructural

Esta no sale de los informes, sino de cruzarlos con nuestra propia decisión de flujo. En
`conceptualizacion/FUNCIONAL.md` §8.1, marcada como DECIDIDO: **un solo "Sí" en el
cuestionario lleva a `cKO`**, que es terminal, sin firma y sin compra online. Y el
cuestionario es **por asegurado**.

Así que el máximo de venta online alcanzable es **la proporción de solicitudes en las que
todos los asegurados responden "No" a todo**. En una familia de cuatro, los cuatro tienen que
estar limpios. **Nunca hemos preguntado cuánta gente es.**

Y de ahí depende cómo se lee todo lo demás:

- **Si la mayoría de solicitudes tienen algún "Sí"**, el 7% de venta online puede estar ya
  cerca de su techo estructural. El límite sería de **suscripción, no de diseño**, y habría
  que reformular lo que el proyecto puede prometer.
- **Si el techo está en el 20% o más**, hay mucho margen y el 7% sí es un problema de embudo.

Es una pregunta abierta, no una conclusión, y es **barata de responder**: el porcentaje de
cuestionarios con al menos un "Sí", o el volumen de derivaciones a revisión médica. Planteada
en `analitica/04-preguntas-cliente.md` §1.6.

> **Relacionado**: la **ventana de 20 minutos** (`analitica/00-como-se-mide-hoy.md` §3) cobra
> otro sentido con el cuestionario por asegurado delante. Una familia de cuatro tarda de
> sobra más de 20 minutos, así que el agente llama a gente que está a medio proceso. Puede
> ser parte de la explicación del reparto online/teléfono.

---

## 7. Qué pedir todavía

FIATC ofreció sacar aparte las oportunidades que entran por atención al cliente sin rating.
**Sí interesa**, y ya han enviado la de ATC. Falta:

- El resto de oportunidades **sin rating** (las 3.338 de §5), con su origen.
- Aclaración del descuadre de las 629 pólizas (§5).
- **La fuga 3 (muro del precio) cruzada por rating** (§2). Es lo que más cambiaría nuestro
  plan: distingue sensibilidad al precio de problema de diseño.
- Desglose **por dispositivo** — no viene en ninguno de los tres informes y es donde
  esperamos las diferencias más grandes de comportamiento.
