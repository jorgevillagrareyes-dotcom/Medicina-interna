# Medicina Interna

Sitio de estudio personal con resúmenes de patologías de medicina interna ordenados por subespecialidad, basados en las guías clínicas vigentes y con epidemiología chilena.

## Ver el sitio en tu computador

```bash
pip install -r requirements.txt
mkdocs serve
```

Luego abre http://127.0.0.1:8000 en el navegador.

## Estructura

- `docs/<subespecialidad>/index.md`: listado de patologías de la subespecialidad (disponibles y pendientes).
- `docs/<subespecialidad>/<patologia>.md`: resumen de cada patología.
- `plantillas/resumen-patologia.md`: plantilla con las secciones que usa cada resumen.
- `mkdocs.yml`: configuración y menú del sitio.
