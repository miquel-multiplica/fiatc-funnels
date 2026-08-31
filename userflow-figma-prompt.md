# Prompt · Diagrama de flujo del funnel FIATC Salud (para el agente de Figma / FigJam)

## Instrucción para el agente

Crea un **diagrama de flujo de usuario (user flow)** del funnel de contratación de seguro de salud descrito abajo, en **FigJam**.

Convenciones visuales:
- **Rectángulo** = pantalla/paso.
- **Rombo (diamante)** = punto de decisión / bifurcación (pregunta con ramas).
- **Rectángulo redondeado / píldora** = inicio y finales (terminales).
- **Flechas** con etiqueta cuando la transición depende de una respuesta (p. ej. "Sí" / "No").
- Agrupa en **4 carriles o secciones** con títulos: `Tarificación`, `Resultados`, `Contratación`, `Flujos laterales`.
- Marca en un color distinto los **finales alternativos** (KO, guardar presupuesto, Hablemos) frente al **final feliz** (Confirmación).
- Flujo de arriba abajo (vertical) o izquierda a derecha, el que quede más limpio.

Usa exactamente los nombres de pantalla y las etiquetas de rama de la sección "Esquema de pasos".

---

## Esquema de pasos

### 1) Tarificación (lineal, con 1 rama)
1. **Portada** (`step0`) → Calcula tu precio
2. **Código postal** (`stepCP`)
3. **¿Para quién es el seguro?** (`step1`) — tú / tú + otros / otros
4. **Fechas de nacimiento** (`step2`)
5. **¿Cuándo quieres empezar?** (`step4`) — fecha de inicio
6. ◆ **DECISIÓN: ¿Ya eres cliente de FIATC?** (`step5`)
   - **Sí** → **DNI** (`stepDNI`) → continúa
   - **No** → continúa directo
7. **Email** (`step6`)
8. **Teléfono + consentimiento** (`step6b`)
9. **Cálculo** (loading) → Resultados

### 2) Resultados
10. **Resultados / comparador de planes** (`step7`)
    - Acciones secundarias (no avanzan el flujo): ver **Detalles del plan**, **Editar asegurados** (recalcular), **FAQs**, **Guardar presupuesto**.
11. ◆ **DECISIÓN: "Me interesa"** (modal, `#interesModal`) — 3 salidas:
    - **Contratar online ahora** → entra en **Contratación** (paso 12)
    - **Prefiero que me ayuden** → *[final lateral]* **Hablemos** (agendar llamada / teléfono)
    - **Guardar presupuesto** → *[final lateral]* **Presupuesto guardado** (captura email + consentimiento)

### 3) Contratación (con 2 ramas + 1 rama terminal)
12. **Datos del tomador** (`cDatos`)
13. **Contacto** (`cContacto`)
14. **Dirección** (`cDireccion`)
15. **Asegurado 1** (`cAseg1`)
16. **Asegurado 2** (`cAseg2`) *(condicional: solo si hay 2º asegurado)*
17. **Cuestionario de salud** (`cCuestionario`)
18. ◆ **DECISIÓN: ¿Alguna respuesta "Sí" en el cuestionario?**
    - **Sí (hay declaración)** → *[final/rama]* **KO – Un médico revisará tu solicitud** (`cKO`): derivación a revisión médica telefónica; el usuario espera la llamada (no continúa online). *Salidas: volver / Hablemos.*
    - **No (todo "No")** → continúa a la firma (paso 19)
19. **Confirma tu teléfono** (`cTelefono`) — para firmar online (PIN por SMS)
20. **Firma del cuestionario** (`cFirma`) — pantalla de firma (Evicertia, simulada)
21. ◆ **DECISIÓN: ¿Tienes seguro con otra compañía?** (`cOtra`)
    - **Sí** → **Derogación de carencias** (`cDerogacion`): subida opcional de documentos → continúa
    - **No** → continúa directo
22. **Forma de pago** (`cPago`) — periodicidad (mensual/trimestral/semestral/anual)
23. **Antes de continuar con el pago** (`cAntes`) — resumen del cargo + condiciones legales
24. **Pasarela de pago TPV** (`cTPV`) — iframe Banco Sabadell (simulado)
25. ⬤ **Confirmación** (`cConfirm`) *[final feliz]* — stepper: (1) seguro contratado ✓ · (2) firma del contrato pendiente (2ª firma, por email) · (3) descarga la app.
    - Post-flujo (fuera de pantalla): **2ª firma del contrato por email** (necesaria para activar la app).

### 4) Flujos laterales (accesibles desde varios pasos)
- **Hablemos** (contacto): agendar llamada / teléfono. Accesible desde la cabecera en todo el funnel y como salida de "Me interesa" y del KO.
- **Exit-intent** (al intentar salir): "¿Seguro que quieres salir?" → opción **Guardar presupuesto** (captura email) → Presupuesto guardado.
- **Recuperar presupuesto** (desde Portada): email → aterriza en Resultados.
- **Modales de apoyo** (no son pasos del flujo): Resumen flotante, Detalles del plan, Editar cálculo, FAQs por contexto, Descargar app (QR desktop / store mobile).

---

## Resumen de las ramificaciones (para el diagrama)

| # | Decisión | Rama A | Rama B |
|---|----------|--------|--------|
| 1 | ¿Ya eres cliente? (`step5`) | Sí → DNI → Email | No → Email |
| 2 | "Me interesa" (resultados) | Contratar online → Contratación | Ayuda (Hablemos) / Guardar presupuesto → finales laterales |
| 3 | ¿"Sí" en cuestionario? (`cCuestionario`) | Sí → **KO / Teladoc** (rama terminal) | No → Firma → … |
| 4 | ¿Otra compañía? (`cOtra`) | Sí → Derogación → Pago | No → Pago |

## Finales del flujo
- ⬤ **Confirmación** (`cConfirm`) — final feliz (+ 2ª firma por email post-flujo).
- **KO / revisión médica** (`cKO`) — el usuario no contrata online; espera llamada.
- **Hablemos** — deriva a asesor.
- **Presupuesto guardado** — retención para volver más tarde.

---

## (Opcional) Diagrama en Mermaid — por si el agente lo aprovecha

```mermaid
flowchart TD
  A([Portada]) --> CP[Código postal] --> Q[¿Para quién?] --> EDAD[Fechas nacimiento] --> INI[Fecha de inicio]
  INI --> CLI{¿Ya eres cliente?}
  CLI -- Sí --> DNI[DNI] --> MAIL[Email]
  CLI -- No --> MAIL
  MAIL --> TEL[Teléfono + consentimiento] --> LOAD[Cálculo] --> RES[Resultados]
  RES --> INT{Me interesa}
  INT -- Contratar online --> CDATOS[Datos tomador]
  INT -- Prefiero ayuda --> HAB([Hablemos])
  INT -- Guardar presupuesto --> SAVE([Presupuesto guardado])
  CDATOS --> CCONT[Contacto] --> CDIR[Dirección] --> CA1[Asegurado 1] --> CA2[Asegurado 2] --> CUES[Cuestionario de salud]
  CUES --> KO{¿Algún \"Sí\"?}
  KO -- Sí --> CKO([KO · revisión médica / Teladoc])
  KO -- No --> CTEL[Confirma teléfono] --> CFIRMA[Firma del cuestionario]
  CFIRMA --> OTRA{¿Otra compañía?}
  OTRA -- Sí --> DERO[Derogación de carencias] --> PAGO[Forma de pago]
  OTRA -- No --> PAGO
  PAGO --> ANTES[Antes de pagar: cargo + legal] --> TPV[TPV Sabadell] --> CONF([Confirmación])
```
