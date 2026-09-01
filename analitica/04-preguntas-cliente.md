# Preguntas para la sesión de analítica

Lista única y priorizada para la reunión con **SEOCom** (etiquetado) y **Héctor López**
(iframe y data layer). Cada pregunta es **autocontenida**: lleva su contexto, para qué sirve
y qué desbloquea, de forma que se pueda usar sin haber leído el resto de la carpeta.

El detalle está en `analitica/00-como-se-mide-hoy.md` (qué existe hoy),
`analitica/03-linea-base.md` (cifras cerradas) y `analitica/02-medicion-funnel-nuevo.md`
(especificación de eventos).

> **Uso.** Los otros documentos de la carpeta son razonamiento interno e incluyen nuestras
> propias correcciones. Este está redactado para poder plantearse tal cual delante del
> cliente.

---

## 1. Las que no deberían salir de la sesión sin respuesta

**1.1 · Identificador único de cotización**
*Hoy no existe ninguna relación entre presupuesto, lead y contratación; lo confirmó su propio
IT.* ¿Se puede generar un identificador en el funnel que viaje al CRM con el lead y sobreviva
hasta la venta?
→ **Desbloquea**: explicar la mejora, no solo verla. Y atribuir lo que hoy se lleva el call
center, que es el **93% de las pólizas**.
→ **Cómo plantearlo**: no como bloqueante. *"Con lo que hay podemos medir el resultado; con
un identificador podríamos además explicarlo."* Es más fuerte porque no exige nada para
empezar.

**1.2 · Evento de clic en "Contratar"**
*Es el mayor muro del embudo —se pierde entre el 63% y el 72%— y hoy no existe como evento.*
¿Se puede instrumentar?
→ **Desbloquea**: la fuga 3, que es la prioridad del proyecto.

**1.3 · El tramo entre el clic y la firma, paso a paso**
*Hoy no está instrumentado: el iframe lo hacía invisible. Sabemos que ~315 personas al mes
se caen entre el clic y la firma, pero no en qué paso — ni cuántas llegan a firmar.* **El
funnel nuevo no usa iframe**, así que es la ocasión de cerrarlo — y solo existe una vez.
→ **Desbloquea**: la fuga 4, hoy ciega.

**1.4 · Consentimiento: ¿se pueden distinguir dos marcas?**
*El CRM guarda hoy **una sola marca** para el consentimiento del tarificador.* En el funnel
nuevo hay **dos cosas distintas y deliberadamente separadas**: el opt-in comercial (email) y
la preferencia de canal para hablar de la solicitud (WhatsApp). ¿Se pueden almacenar y medir
por separado, con **canal, fecha y origen**?
→ **Desbloquea**: saber si el WhatsApp transaccional funciona, y el cumplimiento de la **Ley
ATC 10/2025**, que exige consentimiento granular por canal, revocable y trazable. Nada de eso
existe hoy. No es un ajuste de diseño: es trabajo de Sistemas con plazo.

**1.5 · Accesos**
GA4, GTM y Clarity para `enriclieder@multiplica.com` y `miquel@multiplica.com`. Periodo
**ago-25 a jul-26**, desglose mensual y, cuando exista, por dispositivo, fuente, canal y
campaña. Ramo Salud.
→ **Desbloquea**: el diagnóstico de Clarity de `analitica/01-clarity.md`, que es lo que
explica *por qué* se abandona en las fugas 1 y 2.

**1.6 · ¿Qué porcentaje de cuestionarios de salud tiene al menos un "Sí"?**
*O, dicho de otra forma: cuántas solicitudes acaban derivadas a revisión médica.*
→ **Por qué es la pregunta con más consecuencias de toda la lista**: un solo "Sí" en el
cuestionario deriva a revisión médica, y eso significa que no hay compra online. Como el
cuestionario es **por asegurado**, en una familia de cuatro los cuatro tienen que estar
limpios. Ese porcentaje es por tanto **el techo máximo de venta online que el canal puede
alcanzar**. Del volumen hay una pista —**112 derivaciones a Teladoc** en la tabla de estados
del CRM, frente a 1.260 caídas en el mismo tramo— pero no de la tasa, ni del periodo que
cubre ese 112.
→ **Qué cambia según la respuesta**: si la mayoría de solicitudes tienen algún "Sí", el 7% de
venta online está cerca de su techo y el límite es de suscripción, no de diseño. Si el techo
está en el 20% o más, hay margen amplio y el 7% es un problema de embudo. Son dos proyectos
distintos.
→ **Si esta sesión no puede responderlo**, escalarlo a negocio o a suscripción: no debería
quedarse sin respuesta. Ver `analitica/03-linea-base.md` §6.2.

---

## 2. Las que cambiarían nuestro plan de trabajo

**2.1 · La fuga 3 cruzada por rating (calidad del lead)**
*La conversión varía ×4,5 según el rating: A 8,49%, B 3,80%, C 1,88%.* ¿Abandona un rating C
en la pantalla de precio mucho más que un A?
→ **Por qué importa**: si abandonan de forma muy distinta, el muro del precio es
sensibilidad al precio y hay poco que hacer desde el diseño. Si abandonan por igual, el muro
es de diseño y nos incumbe entero. **Es el cruce que más cambiaría nuestra priorización.**

**2.2 · Desglose por dispositivo**
*No viene en ninguno de los tres informes recibidos.*
→ **Por qué importa**: es donde esperamos las diferencias de comportamiento más grandes, y el
prototipo se diseña mobile-first. Sin esto, el diagnóstico de Clarity va a ciegas en su
segmentación más básica.

**2.3 · La ventana de 20 minutos**
*Una oportunidad espera 20 minutos antes de enviarse al call center, para verificar que no se
complete una compra online.* ¿Cuánta gente supera ese umbral y recibe llamada **estando aún
dentro del proceso**?
→ **Por qué importa**: el prototipo promete "2 min" para el precio, pero el cuestionario de
salud con varios asegurados puede irse bastante más allá. Si el porcentaje es alto, hay una
fricción real que no habíamos contado y afecta a la promesa que hacemos en pantalla.

**2.4 · La anomalía de marzo en la fuga 2**
*El paso de consentimiento retuvo un 70,1% en marzo, muy por encima de su rango habitual.*
¿Hubo un cambio en el formulario, en el tráfico o en la medición?
→ **Por qué importa**: si fue un cambio de diseño, es la evidencia más barata que existe de
qué mueve esa fuga.

**2.5 · ¿Distinguen las campañas o las keywords la intención de portabilidad?**
*Del tipo "cambiar seguro de salud" frente a "seguro de salud precio".* La portabilidad se
declara ya dentro de la contratación, así que el ~40-41% está medido **sobre emisiones**: de
quien abandona en el precio no hay dato.
→ **Por qué importa**: son las dos audiencias de la pantalla de resultados (~40% portabilidad,
que compara contra su prima de renovación / ~59% primer seguro, que compara contra la sanidad
pública). Si la campaña o la keyword lo distinguen, **tenemos la segmentación en la entrada y
gratis**, y podríamos ver si el muro del precio les afecta igual.

---

## 3. Datos que faltan o no cuadran en los informes

**3.1 · Faltan 629 pólizas por explicar**
*El informe mensual da 3.125 pólizas. Las oportunidades convertidas son 2.382, más 114 de ATC
= 2.496. Faltan 629, un 20%.* ¿Es que una oportunidad genera varias pólizas, que hay pólizas
sin oportunidad previa, o que los dos informes usan cortes de fecha distintos?
→ **Por qué importa**: es el puente entre "conversión" y "póliza". Sin cerrarlo, cualquier
objetivo que fijemos es ambiguo.

**3.2 · Las 3.338 oportunidades sin rating**
*Dentro del total global, un 6,4% no tiene rating, y convierten al 7,25% — por encima de la
media, así que no son residuales.* ¿Se pueden sacar aparte con su origen? *(FIATC ya ofreció
sacar las de atención al cliente, y las ha enviado.)*

**3.3 · Oportunidades por mes: ¿4.318 o 3.600?**
*Los informes dan 51.814 en 12 meses (~4.318/mes). La cifra que manejábamos antes —25.449
desde enero 2026— no cuadra: ene-jul 2026 suman 27.207 en los informes nuevos.*
→ Probablemente sean **oportunidades netas frente a brutas**, o cortes de fecha distintos.
Conviene fijar cuál se usa como referencia.

**3.4 · ¿Existe cuantificación de los perfiles de cliente de Salud?**
*El PDF de modelo de negocio define **diez perfiles de cliente de Salud**, pero sin ningún
dato de tamaño ni de valor. En cambio, los siete arquetipos de audiencia sí están
cuantificados — y están declarados explícitamente como "otros ramos", así que dejan Salud
fuera.*
→ **Por qué importa**: sin saber qué peso tiene cada perfil no podemos priorizar a quién
optimizamos la pantalla de resultados, que es donde está el mayor muro. Hoy sabríamos hablarle
a los diez, pero no a cuál conviene.
→ **Y una segunda**: ¿la priorización de audiencias vale también para Salud? En el marco de
otros ramos, los seniors quedan en potencial MEDIO **pese a ser los que más seguros tienen y
más valoran la calidad**, porque no se plantean cambiar. Si en Salud pasa lo mismo, tiene
consecuencias de diseño. Ver `contexto/04-perfiles-cliente.md` §3.4.

**3.5 · ¿"Cotización" y "oportunidad" son lo mismo?**
*El PDF da **52.433 cotizaciones de Salud** en el último año. El informe de rating da **51.814
oportunidades** en ago-25 → jul-26. Son casi la misma cifra.*
→ **Por qué importa**: si cada cotización genera una oportunidad, entonces prácticamente todo
el que tarifica acaba como lead, y eso cambia cómo leemos la fuga 2 (el paso de
consentimiento) y de dónde salen las ~4.318 oportunidades al mes. Si son cosas distintas que
casualmente se parecen, hay que dejar de cruzarlas.

---

## 4. Acuerdos de proceso a cerrar en la sesión

- **Nomenclatura**: si SEOCom ya tiene taxonomía de eventos o un data layer definido, **se
  usa la suya**. Inventar otra en paralelo garantiza que nadie cruce los datos después.
- **Definiciones**: replicar las suyas (Oportunidad, Oportunidad neta, gestionada, conversión)
  para que la línea base siga siendo comparable. Si el funnel nuevo cuenta distinto que el
  viejo, no se podrá decir si mejoró.
- **Entorno de pruebas** para validar la medición **antes** de lanzar, no después.
- **Un dueño por evento.** Con cinco actores en el reparto —SEOCom, Héctor, equipo de Laia
  Avilés, TrueIT y Sistemas— lo que no se asigna se cae.
- **Fecha de lanzamiento registrada**, y si cae dentro o fuera de la promo estacional. La
  estacionalidad es **×2,3** entre el mejor mes y el peor: comparar contra el trimestre
  anterior diría más de la estación que del rediseño.

---

## 5. Quién responde qué

| Interlocutor | Le corresponden |
|---|---|
| **SEOCom** (etiquetado GA4/GTM) | 1.2, 1.5, 2.2, 2.4, 4 (nomenclatura) |
| **Héctor López** (iframe, data layer) | 1.1, 1.3, 1.4 (parte técnica), 2.5 |
| **Negocio / Diana** (datos) | 2.1, 3.1, 3.2, 3.3, 3.5 |
| **Marketing / Laura Solé** | **3.4** — perfiles de cliente y priorización de audiencias |
| **Negocio o Suscripción** | **1.6** — si esta sesión no puede responderla, hay que escalarla |
| **Sistemas** | 1.4 (almacenamiento y trazabilidad del consentimiento) |
| **Equipo de Laia Avilés** (CRM) | 2.3, 3.1 |
| **TrueIT** (contactabilidad) | sesión posterior |

Contactabilidad, CRM, consentimiento y testing con usuarios quedan para sesiones posteriores
con sus equipos. Testing con usuarios puede requerir a **Legal**.
