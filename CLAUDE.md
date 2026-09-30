# Medicina Interna: sitio de estudio

Sitio MkDocs Material, en español de Chile, con resúmenes de patologías de medicina interna para un interno de medicina. El usuario aprobó el formato y la profundidad de los resúmenes piloto: mantenerlos.

## Estructura

- `docs/<carpeta>/<patologia>.md`: un resumen por patología. Carpetas: `cardiologia`, `endocrinologia` (diabetes, nutrición y endocrinología), `infectologia`, `respiratorio`, `gastroenterologia`, `geriatria`, `hematologia` (hemato-oncología), `nefrologia`, `neurologia`, `reumatologia`.
- `datos/temario.yml`: las 385 situaciones clínicas de medicina interna del perfil EUNACOM v3 (junio 2026) con su nivel exigido. El campo `resumen` de cada ítem lista las páginas que lo cubren.
- `scripts/generar_indices.py`: genera `docs/<carpeta>/index.md`, `docs/urgencias/index.md`, el bloque de avance de `docs/index.md` y la sección `nav` de `mkdocs.yml`. **No editar esos archivos a mano.**
- `plantillas/resumen-patologia.md`: plantilla con las secciones obligatorias.
- `docs/assets/figuras/`: figuras (SVG propios o figuras con licencia abierta descargadas).
- `docs/javascripts/mermaid.min.js`: Mermaid local (no depende de CDN).

## Flujo para cada patología nueva

1. Investigar la **versión vigente** de las guías (ESC, ACC/AHA, ADA, KDIGO, GOLD, GINA, IDSA/ATS, ACG, EASL/AASLD, etc.) y los datos chilenos (MINSAL/GES, ENS, DEIS, consensos de sociedades chilenas). Indicar el año de cada guía.
2. Escribir la página siguiendo **exactamente** las secciones de la plantilla y el estilo de las páginas existentes (por ejemplo `docs/cardiologia/insuficiencia-cardiaca.md`): ficha, resumen en 60 segundos, definición, epidemiología mundial y Chile, etiología, fisiopatología (con diagrama Mermaid), clasificación, clínica, diagnóstico, laboratorio, imágenes, diagnóstico diferencial, tratamiento con dosis, complicaciones, pronóstico y seguimiento, perlas para el internado, 5–6 preguntas de repaso y referencias.
3. Recuadros propios: `guia`, `chile`, `alarma`, `dosis`, `perla`, `repaso` (este último plegable con `???`).
4. Imágenes: esquemas propios (Mermaid o SVG en `docs/assets/figuras/`) y figuras de artículos **solo con licencia CC BY / CC BY-SA / CC BY-NC** (verificar la licencia en la página del artículo), descargadas al repositorio y con autores, revista, año y licencia en el pie de figura. Nunca copiar figuras con derechos reservados (NEJM, JAMA, Lancet, UpToDate): enlazarlas.
5. Referencias: solo datos verificados. **Nunca inventar DOI, volúmenes ni páginas**; si no se pudo verificar, citar sin ese dato y con un enlace.
6. Agregar la ruta de la página en `resumen` de cada ítem de `datos/temario.yml` que cubra.
7. `python3 scripts/generar_indices.py && mkdocs build --strict` (sin advertencias).
8. Commit y push **después de cada patología** (así no se pierde trabajo si se corta la sesión). Mensajes de commit en español.
9. Cada varias patologías, volver a publicar la vista privada (ver abajo).

## Estilo

- Español de Chile: IECA, ARA-II, iSGLT2, arGLP-1, glicemia, hospitalizar, APS, GES, EUNACOM.
- Frases cortas y directas; números clave en negrita; tablas para clasificaciones, dosis y diagnósticos diferenciales.
- Sin emojis. Etiquetas (`tags`) disponibles: subespecialidad, `GES`, `Frecuente en sala`, `Urgencia`.

## Vista privada publicada

Artifact privado del usuario: https://claude.ai/artifact/WbZMx9NctfhHmxxrzhsZRA

Para actualizarlo: `mkdocs build --strict`, copiar `site/` a una carpeta temporal quitando los `*.map` y `sitemap.xml.gz`, y publicar `index.html` con el resto de los archivos en `files` y la carpeta como `root`, pasando la URL anterior como `url` (desde otra conversación hay que leer el artifact primero).

## Prioridad de los próximos temas

Ya están hechos (64 resúmenes): HTA, crisis hipertensiva, SCA, FA, TEP, EPOC, asma, LRA, sodio, potasio, ácido-base, CAD/EHH, hipoglicemia, sepsis, ITU, piel, meningitis/encefalitis, cirrosis, pancreatitis, HDA, HDB, delirium, ACV, anemias, dislipidemia, tiroides, urgencias oncológicas, epilepsia, PCR y arritmias, endocarditis, insuficiencia suprarrenal, litiasis biliar, diarrea y *C. difficile*, tuberculosis, monoartritis/gota, insuficiencia respiratoria aguda, cefalea, síndrome aórtico agudo, pericarditis/taponamiento, coagulopatías/CID/reversión de anticoagulantes, trombocitopenias, hantavirus/leptospirosis, influenza/COVID-19/bronquitis aguda, abstinencia alcohólica/Wernicke, Guillain-Barré/mielopatías/trauma raquimedular, TEC/hipertensión endocraneana, neumotórax/trauma torácico, CO/ahogamiento/cuerpo extraño, síndromes glomerulares (nefrótico/nefrítico/GNRP/nefritis lúpica), urolitiasis/cólico renal, abdomen agudo (incl. adulto mayor y diverticulitis), hepatitis aguda/insuficiencia hepática aguda, neumonía nosocomial/en inmunosuprimidos/infección asociada a catéter, VIH (con candidiasis orofaríngea y esofágica y diarrea en inmunosuprimidos), preeclampsia/síndrome hipertensivo del embarazo, calcio/fósforo/magnesio (tetania, hipercalcemia), varicela/herpes zóster/exantemas, flegmón cervical/absceso pulmonar/absceso cerebral, tétanos, trastornos del movimiento por fármacos (distonía aguda, SNM, serotoninérgico). Siguientes, en orden (urgencias aún sin `resumen` en `datos/temario.yml`):

1. Urgencias sin resumen: afagia aguda, fractura de cadera, agitación y agresividad, encefalopatías tóxico-metabólicas
2. Resto del temario (ítems sin `resumen` en `datos/temario.yml`)
