---
tags:
  - Nefrología
  - Endocrinología
  - Frecuente en sala
  - Urgencia
---

# Hiponatremia e hipernatremia

<div class="ficha" markdown>

**Subespecialidad**
Nefrología · Endocrinología · Paciente hospitalizado

**Guías principales**
Guía europea de hiponatremia ESE/ESICM/ERBP 2014 y su actualización "Hyponatraemia-treatment standard 2024"

**Otras fuentes**
Panel de expertos estadounidense 2013 (Verbalis) · Estudio SALSA 2021 · Adrogué y Madias

**EUNACOM**
1.03.1.017 SIADH (específico, completo, completo) · 1.09.1.010 Hiponatremia crónica asintomática · 1.09.2.007 Hiponatremia aguda grave · 1.09.1.007 Hipernatremia, poliuria · 1.03.1.015 Diabetes insípida

**Revisado**
Septiembre 2026

</div>

!!! abstract "Resumen en 60 segundos"
    - La natremia refleja el **balance de agua**, no el de sodio. La hiponatremia es casi siempre un **exceso relativo de agua** (con ADH elevada) y la hipernatremia, un **déficit de agua**.
    - **Hiponatremia** (Na < 135 mEq/L): el trastorno electrolítico **más frecuente** en hospitalizados. Primero descarta **hiperglicemia** y **pseudohiponatremia**; luego usa **osmolalidad urinaria** y **sodio urinario** para orientar la causa.
    - **Síntomas graves** (vómitos, convulsiones, compromiso de conciencia): **NaCl 3 % 150 mL EV en 20 minutos** (o 100 mL), repetir hasta **subir 5 mEq/L**.
    - **Límite de corrección**: **≤ 10 mEq/L en 24 horas** (≤ 8 si hay alto riesgo de **desmielinización osmótica**: Na ≤ 105, alcoholismo, desnutrición, hipokalemia, daño hepático).
    - **SIADH**: hiponatremia hipotónica, **euvolémica**, orina concentrada (> 100 mOsm/kg) y **sodio urinario > 30**, con tiroides y suprarrenal normales. Tratamiento: **restricción hídrica**, **urea**, tratar la causa.
    - **Hipernatremia** (Na > 145): adultos mayores sin acceso al agua, pacientes críticos, diabetes insípida. Calcular el **déficit de agua** y corregir **≤ 10–12 mEq/L en 24 h** en la crónica.

## Definición

| Trastorno | Definición | Gravedad |
|---|---|---|
| **Hiponatremia** | **Na plasmático < 135 mEq/L** | **Leve** 130–134 · **moderada** 125–129 · **profunda** < 125 mEq/L |
| **Hipernatremia** | **Na plasmático > 145 mEq/L** | Grave > 155–160 mEq/L |

**Según el tiempo de evolución**:

- **Aguda**: < 48 horas documentadas (riesgo de **edema cerebral**; se puede corregir más rápido).
- **Crónica**: ≥ 48 horas o de duración desconocida (el cerebro se adaptó; riesgo de **desmielinización osmótica** si se corrige rápido). **Ante la duda, tratarla como crónica.**

## Epidemiología

### Mundial

- La hiponatremia afecta a **~ 15–30 % de los pacientes hospitalizados** y hasta **~ 7 %** de los adultos mayores ambulatorios.
- Incluso la hiponatremia **leve crónica** se asocia a **caídas, fracturas, deterioro de la atención y mayor mortalidad**.
- La hipernatremia afecta a **~ 1–3 % de los hospitalizados** y a **~ 10 %** de los pacientes en UCI; se asocia a mortalidad de **~ 30–50 %** (sobre todo por la enfermedad de base).

### Chile

!!! chile "Datos nacionales"
    - No hay registros nacionales; las frecuencias en hospitales chilenos son similares a las internacionales.
    - Causas locales frecuentes de hiponatremia: **tiazidas** (hidroclorotiazida, muy usada en HTA en APS), **ISRS** en adultos mayores, **postoperatorio**, neumonía y la "**potomanía**" por cerveza.
    - El **SIADH** tiene nivel de tratamiento y seguimiento **completo** en el perfil EUNACOM: el médico general debe manejarlo.

## Etiología y fisiopatología

### Regulación normal

- La **osmolalidad plasmática** (285–295 mOsm/kg) se mantiene gracias a la **sed** y a la **hormona antidiurética (ADH o vasopresina)**, que aumenta la reabsorción de agua libre en el túbulo colector (acuaporina 2).
- **Osmolalidad calculada** = 2 × Na + glucosa/18 + BUN/2,8.
- **Tonicidad efectiva** = 2 × Na + glucosa/18 (la urea no es osmol efectivo).
- La ADH se libera por **hiperosmolalidad** y también por estímulos **no osmóticos**: **hipovolemia** o volumen arterial efectivo bajo (IC, cirrosis), **dolor, náuseas, estrés, cirugía**, fármacos.

### Hiponatremia: pasos previos

1. **Descartar hiponatremia hipertónica o isotónica**:
    - **Hiperglicemia** (o manitol): el agua sale de las células y diluye el sodio. **Na corregido = Na + 1,6–2,4 × [(glucosa − 100)/100]**.
    - **Pseudohiponatremia** (osmolalidad normal): **hipertrigliceridemia** o **hiperproteinemia** (mieloma) con métodos de medición indirectos.
2. Si la **osmolalidad plasmática es < 275 mOsm/kg**, es una **hiponatremia hipotónica** (la verdadera).

### Causas de hiponatremia hipotónica

``` mermaid
flowchart TD
    A["Hiponatremia hipotónica<br/>(osmolalidad plasmática < 275)"] --> B{"Osmolalidad urinaria"}
    B -->|"≤ 100 mOsm/kg<br/>(ADH suprimida)"| C["Ingesta excesiva de agua o<br/>baja ingesta de solutos:<br/>polidipsia primaria, potomanía de cerveza,<br/>dieta de 'té y tostadas'"]
    B -->|"> 100 mOsm/kg<br/>(ADH activa)"| D{"Sodio urinario"}
    D -->|"≤ 30 mEq/L<br/>(volumen arterial efectivo bajo)"| E["Hipovolemia extrarrenal:<br/>vómitos, diarrea, tercer espacio<br/>—<br/>Hipervolemia:<br/>IC, cirrosis, síndrome nefrótico"]
    D -->|"> 30 mEq/L"| F{"Volemia clínica y<br/>uso de diuréticos"}
    F -->|"Diuréticos o ERC"| G["Tiazidas (la causa farmacológica<br/>más frecuente), ERC"]
    F -->|"Hipovolemia"| H["Pérdida renal de sal:<br/>insuficiencia suprarrenal primaria,<br/>síndrome de pérdida cerebral de sal,<br/>vómitos (bicarbonaturia)"]
    F -->|"Euvolemia"| I["SIADH<br/>hipotiroidismo grave<br/>insuficiencia suprarrenal secundaria<br/>(déficit de glucocorticoides)"]
```

*Figura 1. Enfoque diagnóstico de la hiponatremia hipotónica. Esquema propio basado en la guía europea 2014.*

### SIADH (síndrome de secreción inapropiada de ADH)

!!! guia "Criterios diagnósticos de SIADH"
    **Esenciales**:

    - **Osmolalidad plasmática efectiva < 275 mOsm/kg**.
    - **Osmolalidad urinaria > 100 mOsm/kg** (con hipotonicidad).
    - **Euvolemia clínica**.
    - **Sodio urinario > 30 mEq/L** con ingesta normal de sal y agua.
    - **Función tiroidea y suprarrenal normales**.
    - Sin uso reciente de diuréticos.

    **Complementarios**: ácido úrico < 4 mg/dL, BUN bajo, FENa > 0,5 %, FEUrea > 55 %, falta de corrección con suero fisiológico y corrección con restricción hídrica.

**Causas de SIADH**

| Grupo | Ejemplos |
|---|---|
| **Sistema nervioso central** | ACV, **hemorragia subaracnoidea**, TEC, meningitis y encefalitis, tumores, psicosis aguda |
| **Pulmonar** | **Neumonía** (incluida *Legionella*), **tuberculosis**, ventilación mecánica, asma, EPOC |
| **Neoplasias** (ADH ectópica) | **Cáncer pulmonar de células pequeñas** (el más característico), cáncer de cabeza y cuello, páncreas, linfomas |
| **Fármacos** | **ISRS** y otros antidepresivos, **carbamazepina y oxcarbazepina**, antipsicóticos, **ciclofosfamida**, vincristina, cisplatino, **opioides**, **AINE**, **MDMA (éxtasis)**, desmopresina, oxitocina |
| **Otros** | **Dolor**, **náuseas**, **postoperatorio**, VIH, ejercicio de resistencia prolongado, idiopático (adultos mayores) |

### Hipernatremia

Casi siempre hay un **déficit de agua** en una persona que **no puede beber** (adulto mayor dependiente, compromiso de conciencia, paciente intubado, lactante).

| Mecanismo | Causas |
|---|---|
| **Pérdidas extrarrenales de agua** | Fiebre, sudoración, **quemaduras**, taquipnea, **diarrea osmótica**, vómitos, drenajes |
| **Pérdidas renales** | **Diuresis osmótica** (hiperglicemia, urea en recuperación de LRA, manitol), diuréticos de asa, fase poliúrica de la NTA o posobstructiva |
| **Diabetes insípida central** (déficit de ADH) | **Neurocirugía**, TEC, tumores hipotalámicos o hipofisarios, infiltrativas (histiocitosis, sarcoidosis), idiopática |
| **Diabetes insípida nefrogénica** (resistencia a ADH) | **Litio** (la más frecuente en adultos), **hipercalcemia**, **hipokalemia**, obstrucción urinaria crónica, enfermedad renal |
| **Ganancia de sodio** (poco frecuente) | **Suero hipertónico**, **bicarbonato de sodio**, ingesta de agua de mar, hiperaldosteronismo (leve) |
| **Falta de acceso al agua o de sed** | Demencia, postración, hipodipsia en adultos mayores |

## Clasificación

### Hiponatremia

- Por **natremia**: leve, moderada, profunda.
- Por **tiempo**: aguda (< 48 h) o crónica (≥ 48 h).
- Por **síntomas** (guía europea):
    - **Moderadamente graves**: náuseas sin vómitos, **confusión**, cefalea.
    - **Graves**: **vómitos**, dificultad respiratoria, **somnolencia anormal**, **convulsiones**, **coma** (Glasgow ≤ 8).
- Por **osmolalidad** (hipotónica, isotónica, hipertónica) y **volemia** (hipovolémica, euvolémica, hipervolémica).

### Hipernatremia

- Por **volemia**: hipovolémica (pérdidas de agua y sodio), euvolémica (pérdida de agua pura: diabetes insípida, pérdidas insensibles) o hipervolémica (ganancia de sodio).

## Clínica

**Hiponatremia**: los síntomas dependen de la **velocidad de instalación** más que de la cifra.

- **Aguda**: **edema cerebral**: cefalea, náuseas, **vómitos**, confusión, **convulsiones**, coma, **herniación**, paro respiratorio. Edema pulmonar neurogénico.
- **Crónica**: inespecífica: fatiga, **inestabilidad de la marcha**, **caídas**, déficit de atención, confusión leve; a menudo "asintomática".

**Hipernatremia**:

- **Sed** intensa (si el paciente está consciente), **letargia, irritabilidad, debilidad**, hiperreflexia, mioclonías, **convulsiones**, coma.
- **Hemorragias cerebrales** por retracción del cerebro y tracción de vasos (en la hipernatremia aguda grave).
- **Poliuria** en la diabetes insípida (> 3 L/día con orina diluida).

## Diagnóstico

### Hiponatremia: exámenes clave

1. **Glicemia**, lípidos y proteínas (descartar pseudohiponatremia e hiperglicemia).
2. **Osmolalidad plasmática** (medida).
3. **Osmolalidad urinaria** (muestra aislada).
4. **Sodio urinario** (muestra aislada) y potasio urinario.
5. **Evaluación clínica de la volemia**.
6. **TSH** y **cortisol matinal** (antes de diagnosticar SIADH).
7. Creatinina, BUN, ácido úrico, potasio, bicarbonato.

!!! perla "La volemia clínica es poco confiable"
    La evaluación clínica del volumen tiene baja sensibilidad. Por eso la guía europea propone **empezar por la osmolalidad y el sodio urinarios**, y usar la volemia después. Una prueba con **suero fisiológico** (1–2 L) corrige la hiponatremia hipovolémica, pero **empeora el SIADH**.

### Hipernatremia: exámenes clave

- **Osmolalidad urinaria**:
    - **> 600–800 mOsm/kg**: el riñón concentra bien → **pérdidas extrarrenales** o ingesta insuficiente.
    - **< 300 mOsm/kg** con poliuria: **diabetes insípida**.
    - **300–600 mOsm/kg**: diuresis osmótica, diabetes insípida parcial, diuréticos.
- **Glicemia, BUN, calcio, potasio**.
- **Diabetes insípida**: respuesta a la **desmopresina** (la osmolalidad urinaria sube > 50 % en la central; no cambia en la nefrogénica), **prueba de deprivación de agua** o **copeptina** (estimulada con suero hipertónico o arginina), en centros especializados.

## Laboratorio

| Examen | Hiponatremia | Hipernatremia |
|---|---|---|
| **Osmolalidad plasmática** | < 275 mOsm/kg (hipotónica) | > 295 mOsm/kg |
| **Osmolalidad urinaria** | ≤ 100: exceso de agua o poco soluto · > 100: ADH activa | > 600: extrarrenal · < 300: diabetes insípida |
| **Sodio urinario** | ≤ 30: volumen efectivo bajo · > 30: SIADH, diuréticos, suprarrenal, pérdida renal | Útil en ganancia de sodio (muy alto) |
| **Otros** | TSH, cortisol, ácido úrico, BUN, glicemia, triglicéridos | Glicemia, calcio, potasio, litemia |

## Imágenes

- **TC o RM de cerebro**: compromiso de conciencia, convulsiones o sospecha de causa neurológica (hemorragia, tumor).
- **Radiografía o TC de tórax**: buscar neumonía, tuberculosis o **cáncer pulmonar** en el SIADH.
- **RM de hipófisis** en la diabetes insípida central.
- **RM de cerebro** (secuencias T2/FLAIR) si se sospecha **síndrome de desmielinización osmótica** (lesiones en la protuberancia central y extrapontinas, que pueden aparecer 2–4 semanas después).

## Diagnóstico diferencial

- **Hiperglicemia** y **pseudohiponatremia** (ver arriba).
- **SIADH** versus **síndrome de pérdida cerebral de sal** (hemorragia subaracnoidea): en el segundo hay **hipovolemia**; el tratamiento es opuesto (volumen y sal, no restricción).
- **Insuficiencia suprarrenal** (primaria: hiperkalemia, hipotensión; secundaria: puede imitar un SIADH).
- **Hipotiroidismo** grave (causa poco frecuente de hiponatremia).
- **Polidipsia primaria** (pacientes psiquiátricos) versus diabetes insípida (en ambos hay poliuria con orina diluida, pero en la polidipsia el sodio es bajo o normal-bajo).

## Tratamiento

### Hiponatremia con síntomas graves (cualquier duración)

!!! alarma "Emergencia: vómitos, convulsiones, somnolencia, coma"
    1. **NaCl 3 % 150 mL EV en 20 minutos** (guía europea; o **100 mL en 10 minutos** según el panel estadounidense).
    2. Controlar el **Na a los 20 minutos** y repetir el bolo (hasta **2–3 veces**) hasta que el **Na suba 5 mEq/L** o mejoren los síntomas.
    3. Una vez logrado: **detener el suero hipertónico**, mantener una vía con **suero fisiológico** en volumen mínimo y **tratar la causa**.
    4. **Límite**: no subir más de **10 mEq/L en las primeras 24 horas** (8 mEq/L si hay alto riesgo) y **8 mEq/L en cada 24 horas siguientes**, hasta llegar a 130 mEq/L.
    5. Controlar el Na **cada 4–6 horas** (o más seguido) mientras sea necesario.

    El estudio **SALSA** (2021) mostró que los **bolos rápidos intermitentes** de NaCl 3 % son tan seguros como la infusión continua lenta y corrigen antes. La **guía 2024** prefiere los bolos para la hiponatremia sintomática.

### Hiponatremia con síntomas moderados

- **Un bolo de 150 mL de NaCl 3 %** (o infusión lenta) y tratar la causa, con meta de **+5 mEq/L en 24 horas**, sin superar los 10 mEq/L.

### Hiponatremia crónica leve o sin síntomas graves

- **Tratar la causa**: suspender fármacos (tiazidas, ISRS), corregir la hipovolemia, tratar el hipotiroidismo o la insuficiencia suprarrenal.
- **Según el tipo**:

| Tipo | Tratamiento |
|---|---|
| **Hipovolémica** | **Suero fisiológico 0,9 %** (o cristaloides balanceados), con control estrecho: al corregir la volemia se suprime la ADH y puede haber una **corrección rápida** con diuresis acuosa abundante |
| **SIADH** | **Restricción hídrica** (< 500–800 mL/día o 500 mL menos que la diuresis diaria) como primera línea. Si falla: **urea oral 15–30 g/día** (0,25–0,5 g/kg/día), **tabletas de sal** + diurético de asa, **iSGLT2** (empagliflozina, evidencia reciente), o **tolvaptán** (antagonista de V2; en dosis bajas, con control estrecho por riesgo de sobrecorrección y hepatotoxicidad; evitar en daño hepático) |
| **Hipervolémica** (IC, cirrosis) | **Restricción hídrica**, **diuréticos de asa**, optimizar el tratamiento de la IC; en la cirrosis, suspender diuréticos si Na < 125 y considerar albúmina |
| **Baja ingesta de solutos** (potomanía) | Suspender la cerveza, dieta normal con proteínas y sal (riesgo alto de sobrecorrección) |

!!! perla "Por qué el suero fisiológico empeora el SIADH"
    En el SIADH el riñón excreta el sodio pero retiene el agua. Si la osmolalidad urinaria es mayor que la del suero infundido (~ 308 mOsm/kg), el sodio se elimina concentrado y parte del agua se queda: la natremia **baja más**. Regla práctica: si la **suma del Na + K urinarios es mayor que el Na plasmático**, la restricción hídrica sola no funcionará.

### Sobrecorrección

Si el Na sube más de lo permitido (sobre todo en pacientes de alto riesgo):

- **Suspender** el suero hipertónico y los otros aportes de sodio.
- **Agua libre**: **suero glucosado al 5 %** (~ 3 mL/kg/h o bolos de 10 mL/kg) para volver a bajar el Na.
- **Desmopresina 2–4 µg EV** cada 6–8 horas para frenar la diuresis acuosa.
- En pacientes de alto riesgo, algunos usan la desmopresina **de forma preventiva** junto con el suero hipertónico ("clamp").

!!! alarma "Síndrome de desmielinización osmótica"
    Aparece **2–6 días después** de una corrección rápida de una hiponatremia crónica: **disartria, disfagia, cuadriparesia, síndrome de enclaustramiento**, alteración de conciencia. **Riesgo alto**: Na ≤ 105 mEq/L, **alcoholismo**, **desnutrición**, **hipokalemia**, **daño hepático** avanzado, trasplante hepático. Es en gran parte irreversible: la **prevención** es la clave.

### Fórmula de Adrogué-Madias (estimar el cambio del Na con 1 L de solución)

**Δ Na = (Na infundido + K infundido − Na plasmático) / (agua corporal total + 1)**

- **Agua corporal total** = peso × 0,6 (hombre joven), 0,5 (mujer joven u hombre mayor), 0,45 (mujer mayor).
- Contenido de Na: NaCl 3 % = 513 mEq/L; 0,9 % = 154; Ringer lactato = 130; glucosado 5 % = 0.
- Es solo una estimación: **siempre controlar el Na** (la fórmula no considera la diuresis).

### Hipernatremia

1. **Calcular el déficit de agua**: **Déficit (L) = agua corporal total × [(Na actual / 140) − 1]**.
2. **Velocidad**:
    - **Crónica** (≥ 48 h): bajar **≤ 10–12 mEq/L en 24 horas** (~ 0,5 mEq/L/h). Estudios recientes sugieren que una corrección algo más rápida es segura en adultos, pero el límite clásico sigue siendo el recomendado para el examen.
    - **Aguda** (< 48 h, por ejemplo por sal o diabetes insípida aguda): se puede corregir más rápido (~ 1 mEq/L/h).
3. **Qué dar**: **agua libre** por vía oral o sonda (la preferida) o **suero glucosado al 5 %** EV (controlar la glicemia); si hay **hipovolemia** con inestabilidad, primero **suero fisiológico** para restaurar la perfusión y luego soluciones hipotónicas.
4. **Sumar las pérdidas en curso** (diuresis, fiebre, drenajes).
5. **Tratar la causa**:
    - **Diabetes insípida central**: **desmopresina** (intranasal 10–20 µg, oral 0,1–0,4 mg o EV/SC 1–2 µg).
    - **Diabetes insípida nefrogénica**: suspender el litio si es posible, corregir calcio y potasio, **dieta baja en sal y proteínas**, **tiazidas**, amilorida (en la inducida por litio), AINE.

## Complicaciones

- **Hiponatremia aguda**: edema cerebral, convulsiones, herniación, paro respiratorio, muerte.
- **Hiponatremia crónica**: caídas, fracturas, osteoporosis, deterioro cognitivo.
- **Sobrecorrección**: síndrome de desmielinización osmótica.
- **Hipernatremia**: hemorragias cerebrales, rabdomiólisis, convulsiones, **edema cerebral** si se corrige demasiado rápido la hipernatremia crónica (sobre todo en niños).

## Pronóstico y seguimiento

- La hiponatremia es un **marcador de gravedad** en IC, cirrosis, neumonía y cáncer.
- Control del Na **cada 2–6 horas** durante la corrección activa y luego diario.
- Al alta: revisar fármacos (tiazidas, ISRS), educar sobre restricción hídrica en el SIADH y **controlar la natremia en 1–2 semanas**.
- En el SIADH sin causa clara: buscar **cáncer pulmonar** (sobre todo en fumadores).

## Perlas para el internado

!!! perla "Para la sala y el turno"
    - **Siempre calcula el Na corregido por la glicemia** antes de diagnosticar hiponatremia.
    - Paciente hospitalizado con hiponatremia: revisa los **sueros que está recibiendo** (los sueros hipotónicos como el glucosado o el "suero mixto" en el postoperatorio son causa frecuente), el **dolor**, las **náuseas** y los **fármacos**.
    - **No des suero fisiológico "a ciegas"** a una hiponatremia: si es un SIADH, la empeoras.
    - La **mujer mayor con tiazidas** es la hiponatremia típica del policlínico.
    - Un paciente que **orina mucho durante la corrección** (diuresis acuosa) está en riesgo de **sobrecorrección**: controla el Na más seguido.
    - En la **hemorragia subaracnoidea**, distingue SIADH de pérdida cerebral de sal: **no restrinjas agua** a un paciente hipovolémico (riesgo de vasoespasmo).
    - En la hipernatremia del adulto mayor postrado, lo más importante es el **acceso al agua**: agua libre por boca o sonda.
    - **Litio + poliuria + hipernatremia** = diabetes insípida nefrogénica.

## Preguntas de repaso

??? repaso "1. Mujer de 76 años que usa hidroclorotiazida, con Na 118 mEq/L y una convulsión en urgencia. ¿Cuál es el manejo inicial?"
    **Hiponatremia con síntomas graves**: **NaCl 3 % 150 mL EV en 20 minutos**, control del Na a los 20 minutos y repetir hasta **subir 5 mEq/L**; luego suspender el hipertónico, tratar la causa (**suspender la tiazida**) y no superar **8–10 mEq/L en 24 horas** (tiene factores de riesgo). Controlar el Na cada 4–6 horas.

??? repaso "2. Hombre de 65 años, fumador, con Na 124 mEq/L, euvolémico, osmolalidad urinaria 520 mOsm/kg, Na urinario 60 mEq/L, TSH y cortisol normales. ¿Diagnóstico y conducta?"
    **SIADH**. Tratamiento: **restricción hídrica**, suspender fármacos que lo causen, y si no responde, **urea oral** o tabletas de sal con diurético de asa. **Buscar la causa**: en un fumador, descartar **cáncer pulmonar de células pequeñas** (TC de tórax).

??? repaso "3. ¿Cuál es la velocidad máxima de corrección de una hiponatremia crónica y por qué?"
    **≤ 10 mEq/L en las primeras 24 horas** (≤ 8 mEq/L si hay alto riesgo: Na ≤ 105, alcoholismo, desnutrición, hipokalemia o daño hepático). Una corrección más rápida puede producir el **síndrome de desmielinización osmótica**.

??? repaso "4. Paciente postrado de 85 años con fiebre y Na 162 mEq/L, peso 50 kg. ¿Cuál es su déficit de agua y cómo lo corriges?"
    Agua corporal total ≈ 50 × 0,45 = 22,5 L. Déficit = 22,5 × (162/140 − 1) ≈ **3,5 L**. Reponer con **agua libre por sonda o suero glucosado 5 %**, sumando las pérdidas en curso (fiebre), bajando el Na **≤ 10–12 mEq/L en 24 horas**, y tratar la infección.

??? repaso "5. Paciente con trastorno bipolar en tratamiento con litio, con poliuria de 6 L/día, orina diluida y Na 149 mEq/L. ¿Qué tiene y cómo se trata?"
    **Diabetes insípida nefrogénica por litio**. Asegurar el acceso al agua, evaluar con psiquiatría la suspensión del litio, y tratar con **amilorida** (bloquea la entrada del litio a la célula del túbulo colector), **tiazida** y dieta baja en sal y proteínas. La desmopresina no sirve.

## Referencias

1. Spasovski G, et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. *Eur J Endocrinol.* 2014;170:G1–G47 (y *Nephrol Dial Transplant.* 2014;29 Suppl 2:i1–i39).
2. Spasovski G, et al. Hyponatraemia-treatment standard 2024. *Nephrol Dial Transplant.* 2024;39:1583–1592. doi:[10.1093/ndt/gfae162](https://doi.org/10.1093/ndt/gfae162)
3. Verbalis JG, et al. Diagnosis, evaluation, and treatment of hyponatremia: expert panel recommendations. *Am J Med.* 2013;126(10 Suppl 1):S1–S42.
4. Baek SH, et al. Risk of Overcorrection in Rapid Intermittent Bolus vs Slow Continuous Infusion Therapies of Hypertonic Saline for Patients With Symptomatic Hyponatremia (SALSA). *JAMA Intern Med.* 2021;181:81–92.
5. Adrogué HJ, Madias NE. Hyponatremia. *N Engl J Med.* 2000;342:1581–1589.
6. Adrogué HJ, Madias NE. Hypernatremia. *N Engl J Med.* 2000;342:1493–1499.
7. Refardt J, et al. A Randomized Trial of Empagliflozin to Increase Plasma Sodium Levels in Patients with the Syndrome of Inappropriate Antidiuresis. *J Am Soc Nephrol.* 2020;31:615–624.
