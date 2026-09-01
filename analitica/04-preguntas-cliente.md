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

**1.2 · El paso de precio a contratación: ¿por qué se pierde el 77%?**
*Con la dimensión `paso tarificadores` ya se mide: de **4.350 usuarios** en `salud-8-precio` a
**996** en `salud-datos-titular`, en 30 días. **Se pierde el 77,1%**, en línea con el 63-72%
de 2025.*
→ **Lo que falta no es el dato, es el detalle**: el evento de precio no lleva **modalidad ni
importe**, así que no se puede cruzar precio con abandono. Eso sí hay que pedirlo.
→ **Es la prioridad del proyecto**, y ahora se puede seguir semana a semana.

**1.3 · ¿Qué pasa entre los datos del titular y la dirección?**
*Contra lo que creíamos, **el tramo sí está medido**: 996 usuarios en datos del titular → 182
en dirección → 168 asegurado → 122 resumen → 110 cuestionario → 22 TPV, en 30 días. Y cuadra
por dos vías: 22 TPV frente a ~18 ventas online/mes, y 30 Teladoc frente a los 28/mes del CRM.*
→ **Ahí está el mayor muro de todo el embudo: se pierde el 81,7%**, más que en el precio. Nadie
lo había visto porque se daba el tramo por no instrumentado. ¿Es una pantalla, un campo, una
validación? ¿O el paso no se dispara para todos?
→ **Y lo que falta por medir**: la firma, la derogación y la forma de pago no aparecen como
pasos.
→ **Y una petición de fondo**: nombres consistentes. La numeración de Salud se salta el 2 y el
4, y varios pasos no llevan número.

**1.4 · Consentimiento: ¿se pueden distinguir dos marcas?**
*El CRM guarda hoy **una sola marca** para el consentimiento del tarificador.* En el funnel
nuevo hay **dos cosas distintas y deliberadamente separadas**: el opt-in comercial (email) y
la preferencia de canal para hablar de la solicitud (WhatsApp). ¿Se pueden almacenar y medir
por separado, con **canal, fecha y origen**?
→ **Desbloquea**: saber si el WhatsApp transaccional funciona, y el cumplimiento de la **Ley
ATC 10/2025**, que exige consentimiento granular por canal, revocable y trazable. Nada de eso
existe hoy. No es un ajuste de diseño: es trabajo de Sistemas con plazo.

**1.5 · ¿Se puede instalar Clarity dentro del tarificador?**
*Ya está confirmado que **hoy no ve nada dentro del iframe**: las grabaciones muestran un
rectángulo gris y registran "Clics: 0" aunque la sesión dure minutos.*
→ **Por qué importa**: sin eso, **las fugas 1, 2 y 3 no se pueden diagnosticar**, y son las dos
cuya causa no conocemos más el mayor muro del embudo. No es falta de volumen —hay 5.053
grabaciones en 30 días— es que el contenido no se captura.
→ **La pregunta concreta**: ¿se puede añadir el script de Clarity a la aplicación del
tarificador, la que va dentro del iframe? Si se puede y es rápido, desbloquea el diagnóstico
del funnel **actual**, que es el que da las cifras de la propuesta.
→ **Y si no se puede**: hay que decirlo abiertamente en la propuesta. El diagnóstico del *por
qué* llegaría solo con el funnel nuevo, que no usa iframe.

**1.6 · ¿Qué porcentaje de cuestionarios de salud tiene al menos un "Sí"?**
*O, dicho de otra forma: cuántas solicitudes acaban derivadas a revisión médica.*
→ **Ya casi respondida, y tranquiliza**: en 30 días hay **25 usuarios derivados a Teladoc
frente a 996 que inician contratación, un 2,5%** (`05` §2), coherente con los 28/mes del CRM.
**El cuestionario no es el techo de la venta online**, como habíamos temido.
→ **Lo que queda por saber** es la tasa sobre quien llega al cuestionario: 25 sobre 110 sería
un 23%, pero llegan tan pocos que el dato es frágil. Útil para dimensionar la pantalla de KO,
no para replantear el proyecto.

**1.7 · Accesos, y una ventana larga de Clarity**
GA4, GTM y Clarity para `enriclieder@multiplica.com` y `miquel@multiplica.com`. Periodo
**ago-25 a jul-26**, desglose mensual y, cuando exista, por dispositivo, fuente, canal y
campaña. Ramo Salud.
*De Clarity hace falta **varios meses**, no días: los dos exports de 3 días que tenemos se
contradicen entre sí y han obligado a aparcar el plan de diagnóstico.*
→ **Desbloquea**: el diagnóstico de Clarity de `analitica/01-clarity.md`, que es lo que
explica *por qué* se abandona en las fugas 1 y 2.

---

## 2. Las que cambiarían nuestro plan de trabajo

**2.1 · La fuga 3 cruzada por rating (calidad del lead)**
*La conversión varía ×4,5 según el rating: A 8,49%, B 3,80%, C 1,88%.* ¿Abandona un rating C
en la pantalla de precio mucho más que un A?
→ **Por qué importa**: si abandonan de forma muy distinta, el muro del precio es
sensibilidad al precio y hay poco que hacer desde el diseño. Si abandonan por igual, el muro
es de diseño y nos incumbe entero. **Es el cruce que más cambiaría nuestra priorización.**

**2.2 · Las tres fuentes dan repartos de dispositivo distintos**
*Clarity site 64/36, Clarity página del tarificador 76/24, y **GA4 en usuarios de los pasos
56/43**. Nos quedamos con el de GA4, porque cuenta personas que usan los pasos y no visitas a
la página contenedora — pero conviene que lo confirmen ellos.*
→ **Por qué importa**: con un 43% de escritorio, no es un caso secundario. Y su conversión
cambia de signo según el tramo (§2.6).

**2.3 · La ventana de 20 minutos**
*Una oportunidad espera 20 minutos antes de enviarse al call center, para verificar que no se
complete una compra online.* ¿Cuánta gente supera ese umbral y recibe llamada **estando aún
dentro del proceso**?
→ **Por qué importa**: el prototipo promete "2 min" para el precio, pero el cuestionario de
salud es **por asegurado**. Ahora sabemos que **una cotización media cubre a 1,88 personas**
(`05` §2), y Clarity da 2,2 min activos y 4,1 min totales de media en el tarificador, así que
el promedio queda lejos de los 20 minutos. **Falta la cola**: cuántos la superan.

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

**2.6 · En escritorio, ¿por qué solo el 13% pulsa "Contratar"?**
*De cada 100 usuarios que ven el precio, **33 inician la contratación en móvil y solo 13 en
escritorio** — móvil convierte ×2,5 en ese paso concreto. En cambio el escritorio completa
mejor el tarificador y remata mejor el pago.*
→ **Dos hipótesis con consecuencias opuestas**: si en escritorio se compara más —encaja con lo
que dice ATC sobre comparación activa—, es comportamiento y hay poco que hacer. Si es que **el
CTA funciona peor en esa pantalla**, es directamente accionable en el rediseño.
→ **Por qué importa**: la pantalla de resultados es la prioridad del proyecto, y esto dice que
puede tener un problema específico de escritorio que no habíamos mirado.

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

**3.6 · ¿Qué disparan exactamente `tarificador_inicio_salud` y `tarificador_conversion_salud`?**
*Ya no es bloqueante —el embudo real sale de la dimensión `paso tarificadores`— pero siguen sin
cuadrar: `tarificador_inicio_salud` da 12.501 en 4 semanas mientras `salud-codigo-postal` da
9.523 en 30 días.*
→ **Por qué importa**: para saber cuál de los dos es la entrada al embudo y no mezclarlos al
fijar objetivos.

**3.7 · ¿Por qué GA4 da ×1,8 las oportunidades del CRM?**
*GA4 da 189,9 conversiones de tarificador Salud al día (27 jul – 23 ago 2026). El CRM da 104,6
oportunidades/día en jul-26 y 99,4 en ago-25.* Y **agosto es temporada baja**, así que la
brecha va en el sentido contrario del esperable.
→ **Candidato principal, y es simple**: son **recuentos de eventos, no de registros únicos**.
Quien retrocede y reintenta dispara el paso otra vez; el CRM cuenta oportunidades únicas. Los
bots (28,8% según Clarity) y los leads duplicados que confirma `contexto/01` suman por encima.
→ **La petición concreta**: sacar el embudo en **usuarios activos**, no en recuento de eventos
—es solo añadir la métrica en la misma exploración—. Con eso se cierra la brecha y además se
puede contar personas. *(`Sesiones` no sirve aquí: es de ámbito sesión cruzada con una
dimensión de ámbito evento.)*

**3.8 · ¿Qué es exactamente `salud-1-seleccion-cliente`?**
*Solo 2.226 eventos en 30 días frente a 9.523 del código postal, y un **84,3% de móvil** frente
al 62% del resto de pasos. Y `salud-nif-cliente` es exactamente la mitad, 1.113.*
→ **Por qué importa**: si es la pantalla de "¿ya eres cliente?", la mayoría no pasa por ella y
no entendemos por dónde entran. Y ese sesgo de dispositivo apunta a que se muestra solo en
ciertos contextos.

**3.9 · ¿Por qué la taxonomía de pasos es inconsistente?**
*La numeración de Salud **se salta el 2 y el 4**, varios pasos no llevan número
(`salud-codigo-postal`, `salud-fecha-nacimiento`), y el segmento "Conversiones tarificador"
está parcheado a mano con `autos-neo-precios|vida-6-consentimiento|.*not set.*`.*
→ **Por qué importa**: el acuerdo es respetar su nomenclatura en el funnel nuevo, y su
nomenclatura no es homogénea. Conviene saber si hay una convención que desconocemos o si es
deuda acumulada, antes de replicarla.

**3.10 · ¿Filtra GA4 el tráfico de bots?**
*Clarity marca entre el 13% y el 66% de sesiones de bot según la ventana de 3 días que se
mire, y su propio desglose por tipo de bot **no respeta el rango de fechas** (sale idéntico en
dos exports de periodos distintos).*
→ **Por qué importa**: si GA4 no los filtra, todas las cifras del embudo están infladas en una
proporción que no conocemos. Es también uno de los candidatos a explicar la brecha de §3.7.

**3.11 · ¿Por qué Clarity cuenta 3,08 veces las sesiones de GA4?**
*Clarity da 7.880 sesiones/día (30 días, todo el site); GA4 da 2.557/día en un periodo casi
igual.*
→ **Candidato principal**: el **consentimiento de cookies**. Si GA4 solo dispara tras aceptar y
Clarity graba antes o al margen, GA4 pierde sistemáticamente la mayoría del tráfico.
→ **Por qué importa**: los porcentajes de las cuatro fugas salen de sesiones de GA4. Si la
pérdida es uniforme, las proporciones aguantan; si es sesgada —por ejemplo, si quien rechaza
cookies se comporta distinto— el embudo que usamos está torcido. Hay que saber al menos **qué
modo de consentimiento tiene GA4 configurado**.

**3.12 · ¿Cuánta conservación de datos tiene configurada GA4?**
*GA4 permite 2 o 14 meses. Se ha pedido el periodo **ago-25 a jul-26**, y agosto de 2025 queda
justo en el límite de los 14 meses.*
→ **Por qué importa**: si está en 2 meses, **el histórico ya no existe** en la interfaz y solo
se podría reconstruir desde BigQuery, si hay export activo. Conviene comprobarlo antes de
prometer cualquier comparación anual.

**3.13 · El 38,8% de sesiones del tarificador tiene un error de JavaScript**
*3.045 de 7.858 sesiones en 30 días, casi todas `script error.` — el error enmascarado por CORS,
que apunta al interior del iframe.*
→ **Por qué importa**: es mucho volumen. Si hay errores reales dentro del tarificador, parte de
las fugas podría ser técnica y no de diseño.
**3.14 · ¿Qué provoca "Redirección fallida"?**
*1.413 vistas en 4 semanas, más 475 de "404 Error".*
→ **Por qué importa**: no sabemos si está en el camino del funnel, pero 1.413 no es residual.



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
| **SEOCom** (etiquetado GA4/GTM) | 1.2, **1.5**, 1.7, 2.2, 2.4, **3.6 a 3.9**, 4 (nomenclatura) |
| **Héctor López** (iframe, data layer) | 1.1, 1.3, 1.4 (parte técnica), 2.5 |
| **Negocio / Diana** (datos) | 2.1, 3.1, 3.2, 3.3, 3.5 |
| **Marketing / Laura Solé** | **3.4** — perfiles de cliente y priorización de audiencias |
| **Negocio o Suscripción** | **1.6** — si esta sesión no puede responderla, hay que escalarla |
| **Sistemas** | 1.4 (almacenamiento y trazabilidad del consentimiento) |
| **Equipo de Laia Avilés** (CRM) | 2.3, 3.1 |
| **TrueIT** (contactabilidad) | sesión posterior |

Contactabilidad, CRM, consentimiento y testing con usuarios quedan para sesiones posteriores
con sus equipos. Testing con usuarios puede requerir a **Legal**.
