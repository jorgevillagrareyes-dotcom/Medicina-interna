# Medicina Interna

Sitio de estudio personal con resúmenes de patologías de medicina interna ordenados por subespecialidad, basados en las guías clínicas vigentes y con epidemiología chilena.

## Ver el sitio en tu computador

```bash
pip install -r requirements.txt
mkdocs serve
```

Luego abre http://127.0.0.1:8000 en el navegador.

## Estructura

- `docs/<subespecialidad>/<patologia>.md`: resumen de cada patología.
- `datos/temario.yml`: temario de medicina interna del perfil EUNACOM v3 (2026) y qué resumen cubre cada situación clínica.
- `scripts/generar_indices.py`: genera los índices por subespecialidad, la página de urgencias y el menú (`python3 scripts/generar_indices.py`).
- `plantillas/resumen-patologia.md`: plantilla con las secciones que usa cada resumen.
- `mkdocs.yml`: configuración del sitio.
