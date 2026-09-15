# Qué falta para la versión final del funnel de Salud

Mapa de lo que queda por hacer, y de quién depende cada cosa. **Solo lo que afecta al
entregable de diseño**: lo que es de IT está en `ux/SPECS.md` y lo de medición en `analitica/`.

Lo construido hoy está en `ux/FUNCIONAL.md`; el estado por bloque de la lógica condicional,
en `ux/SPECS.md`. Este documento es el complementario: lo que **no** está.

> **Alcance.** Esta es la primera fase y cubre **Salud**. Los demás ramos se atacan después de
> cerrar este, y no cuentan como pendiente aquí — son fase siguiente.

---

## 1. Diseño pendiente, se puede hacer ya

### 1.1 · El camino del "ya cliente"
Hoy `step5` pregunta si ya es cliente y, si dice que sí, `stepDNI` le pide el DNI. **Y ahí se
acaba**: el prototipo no hace nada con ese dato (`SPECS.md` A-02.4).

Son **dos trabajos distintos**, y conviene no confundirlos:

- **El pseudologin.** Qué pasa tras introducir el DNI: si se reconoce, si se recuperan datos,
  qué se le ahorra al usuario y qué pasa si no cuadra. Hoy no hay pantallas para nada de eso.
- **El funnel dentro del área privada.** Cómo se ve todo esto cuando el usuario entra ya
  identificado, **en escritorio y en la app**. Es prácticamente otro contexto de diseño: dos
  plataformas y una cabecera que no es la del funnel público.

Es el pendiente más grande de la lista, y el único que abre pantallas nuevas.

### 1.2 · Variante de tarjeta con precio tachado
Hoy la promo son **2 meses gratis**, que no tocan el precio, así que no hay nada que tachar.
Falta la variante **para cuando haya una promoción que sí afecte al precio**: tarjeta con el
precio anterior tachado y el nuevo destacado.

Viene del QW#4 de `contexto/03-backlog-quickwins.md`, que quedó como parcial por esto.

---

## 2. Esperando a terceros · sin trabajo de diseño por nuestra parte

Nada de esto se desbloquea diseñando. Está aquí para que no se pierda.

### 2.1 · Qué caduca, según ATC
El QW#4 no se puede redactar sin saberlo: **¿caduca el precio o la póliza?** De la respuesta
depende el copy del vencimiento. Pendiente de aclarar con ATC.

### 2.2 · El consentimiento comercial
Está diseñado y aplicado: un único canal, email (`SPECS.md` F-03). Lo que falta es **el
feedback de jurídico** sobre su parte. Hasta entonces la decisión de un solo canal es
provisional, pero no hay nada que rediseñar mientras tanto.

### 2.3 · WhatsApp como canal de contacto
**Ya está diseñado y deliberadamente oculto.** El cliente pidió el 31 de julio no ofrecerlo a
corto plazo porque la herramienta no está lista y los datos no viajan bien. El código está
conservado y comentado en el propio HTML:

```css
/* WHATSAPP: canal de contacto OCULTO a corto plazo (rev. cliente 31 jul).
   Rescatar quitando esta regla cuando la herramienta esté lista. */
.whatsapp-channel { display: none; }
```

Aparece en los tres modales que ofrecen contacto —Hablemos, exit-intent y el pie de las FAQ—,
así que **rescatarlo es quitar una regla CSS**. No confundir con la preferencia de canal de
`step6b`, que sí está activa y es otra cosa (`SPECS.md` F-03).

---

## 3. De IT, no nuestro

Aquí solo el puntero, para que la lista esté completa. El detalle y los escenarios están en
`ux/SPECS.md`.

- **Intercalar `cOtra` antes del KO.** El prototipo ya bifurca según haya un "Sí" o no; lo
  único que le falta es ese paso (`SPECS.md` F-05).
- **Firma y TPV**, que son placeholders donde irán los iframes de Evicertia y Sabadell
  (`FUNCIONAL.md` §9).
- **Los 26 enlaces inertes** (`onclick="return false;"`): legales, políticas y similares, que
  habrá que cablear.
- **El botón atrás del navegador**, que hoy saca del funnel porque el prototipo no usa la
  History API. No debería pasar en el funnel nuevo.

---

## Lo que se ha revisado y NO es pendiente

Comprobado en el código, para que nadie lo vuelva a abrir:

- **La bifurcación del KO existe.** `proceedFromQuest()` comprueba las respuestas y ramifica.
- **El bloque "Clínica Diagonal"** se muestra correctamente: `selectFilter()` le pone
  `display: block` solo en la pestaña *Con copago*, que es lo que pedía el QW#8. El
  `display: none` del CSS es el estado inicial.
- **Los botones de store** del modal de la app no son placeholders grises: son botones con el
  icono de cada tienda. En móvil sustituyen al QR por media query.
- **El CTA de resultados en escritorio.** El 13% frente al 33% de móvil es del **funnel
  actual**, no del nuestro: describe el problema que venimos a resolver, no uno que tengamos.
