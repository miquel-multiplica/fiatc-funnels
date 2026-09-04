# FIATC Salud — repositorio del proyecto

Reglas **de repositorio y proceso**. Las convenciones de cada entregable viven en el
`CLAUDE.md` de su carpeta, que se suma a este al trabajar ahí:

- `conceptualizacion/CLAUDE.md` — el wireframe del funnel
- `ui/CLAUDE.md` — cuando exista la fase de UI

## Estructura del repo
```
conceptualizacion/   el wireframe del funnel, su documentación funcional
                     (FUNCIONAL.md), la lógica condicional en escenarios
                     (SPECS.md) y el prompt del userflow para Figma
ui/                  (vacía) diseño visual sobre el design system de FIATC
analitica/           medición: cómo se mide hoy, línea base cerrada, qué dejar preparado
                     para el funnel nuevo, plan de Clarity y preguntas para el
                     cliente (00 a 04, con README de índice)
contexto/            inputs de la inmersión (00 a 04). Ni conceptualización ni UI:
                     es la investigación de partida, no lo que producimos
propuesta/           fase anterior, cerrada: el prototipo de la propuesta y su doc
utils/               serve.py, para abrir el prototipo por http:// en vez de file://
pruebas-descartadas/ alternativas exploradas y no elegidas
material-cliente/    lo que nos pasa FIATC · IGNORADO, ver abajo
README.md            portada e índice de la base de conocimiento
```

**Rutas en la documentación**: se escriben siempre **desde la raíz del repo**
(`conceptualizacion/FUNCIONAL.md`), no relativas al archivo que las menciona. Son prosa,
no enlaces, y así se leen igual desde cualquier documento.

## Material que NO se versiona
Este repo es **público** y el cliente puede verlo. Están en `.gitignore`:

- **`material-cliente/`** entera — todo lo que llega de FIATC (hoy, su design system del
  área privada). No es nuestro código. Lo que llegue del cliente va aquí, no a la raíz.
- **`prueba-*`** — patrón, no nombre exacto, para que renombrar una prueba no la saque del
  `.gitignore` por descuido. Hoy: `prueba-funnel-salud-estilos-app.html`.

Ojo: nada de esto viaja en un `git clone`. Conviene copia fuera de git.

## Base de conocimiento (inputs de la inmersión — NO editar como diario)
`README.md` y `contexto/`: `00-contexto.md`, `01-embudo-y-datos.md`, `02-hallazgos-clave.md`,
`03-backlog-quickwins.md` (26 quick wins priorizados) y `04-perfiles-cliente.md` (los diez
perfiles de cliente de Salud). Fuente canónica del proyecto; leer ahí antes de decidir.
Prioridad = página de resultados (fuga 63-72%).

## Publicación (GitHub Pages)
El sitio se monta con **lista blanca** en `.github/workflows/pages.yml`: copia los dos HTML
a `_site/` y publica solo eso, así que los `.md` no se sirven aunque estén en el repo.

Las URLs **no dependen de dónde vivan los archivos** —ambos aterrizan en la raíz de
`_site/`— pero al mover carpetas hay que actualizar esas rutas de origen en el workflow.

- Funnel: `…/fiatc-funnels/funnel-salud-quickwins.html`
- Propuesta inicial: `…/fiatc-funnels/wireframe_propuesta.html`

## Convenciones de git
- **No commitear/push salvo que el usuario lo pida.**
- **Un push por tanda, no uno por ajuste.** Cada push encola un deploy de Pages y cancela
  el anterior; con pushes seguidos la cola se congestiona, algún deploy muere por timeout
  (`deployment_queued` en bucle → `Timeout reached`) y el sitio se queda sirviendo una
  versión antigua sin avisar.
- **Verificar lo publicado con cache-buster y por tamaño**, no buscando una cadena: el CDN
  cachea 10 min (`max-age=600`).
  `curl -s -H 'Cache-Control: no-cache' "$URL?cb=$RANDOM"` y comparar `wc -c` con el local.
  Los `.md` no pasan por Pages y se ven al instante en GitHub.
- Si un deploy no arranca, mirar **si hay un run anterior en `waiting`/`queued`** bloqueando
  el grupo de concurrencia antes de tocar la configuración de Pages.
- **Un deploy en rojo no implica un sitio roto.** El workflow ignora los pushes que solo tocan
  `.md` (`paths-ignore`), pero si alguno falla igualmente, la comprobación válida es **por
  tamaño contra el local**, no el color del run: si los dos HTML coinciden, no hay nada que
  arreglar. Pasó tres veces con `Timeout reached` esperando `updating_pages` sin que hubiera
  nada nuevo que publicar.
