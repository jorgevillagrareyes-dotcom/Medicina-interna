"""Genera los índices del sitio a partir de datos/temario.yml y datos/temario-otras.yml.

Escribe:
  - docs/<carpeta>/index.md para cada subespecialidad de medicina interna (tabla EUNACOM con enlaces)
  - docs/urgencias/index.md (todas las situaciones de urgencia de medicina interna)
  - docs/<carpeta>/index.md para cada otra especialidad (cirugia, traumatologia, ...)
  - el bloque de avance de docs/medicina-interna/index.md
  - el bloque de especialidades de docs/index.md (portada)
  - la sección nav de mkdocs.yml

Uso:  python3 scripts/generar_indices.py
"""

from collections import OrderedDict
from pathlib import Path
import os
import re

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"

CARPETAS = OrderedDict(
    [
        ("cardiologia", "Cardiología"),
        ("endocrinologia", "Endocrinología, diabetes y nutrición"),
        ("infectologia", "Enfermedades infecciosas"),
        ("respiratorio", "Enfermedades respiratorias"),
        ("gastroenterologia", "Gastroenterología"),
        ("geriatria", "Geriatría"),
        ("hematologia", "Hemato-oncología"),
        ("nefrologia", "Nefrología"),
        ("neurologia", "Neurología"),
        ("reumatologia", "Reumatología"),
    ]
)

# Otras especialidades: carpeta -> (ícono, descripción corta). El temario está en datos/temario-otras.yml.
ICONOS = {
    "cirugia": ("medical-bag", "Cirugía general, anestesia y urología"),
    "traumatologia": ("bone", "Fracturas, luxaciones, columna y ortopedia"),
    "ginecologia-obstetricia": ("human-pregnant", "Embarazo, parto, puerperio y ginecología"),
    "pediatria": ("baby-face-outline", "Recién nacido, niño y adolescente"),
}

OK = ':material-check-circle:{ .ok title="Resumen disponible" }'
PEND = ':material-clock-outline:{ .pend title="Pendiente" }'

LEYENDA = """## Cómo leer los niveles EUNACOM

| Columna | Valor | Qué se espera del examinado |
|---|---|---|
| **Diagnóstico** | **Específico** | Llegar de forma autónoma al diagnóstico específico, incluido el diagnóstico diferencial y el uso de exámenes |
| | **Sospecha** | Sospechar el diagnóstico, conocer los criterios de derivación y los estudios que hará el especialista |
| **Tratamiento** | **Completo** | Tratar hasta la resolución, derivando solo los casos complejos |
| | **Inicial** | Hacer el tratamiento inicial y derivar en condiciones adecuadas y oportunas |
| **Seguimiento** | **Completo** | Controlar al paciente, derivando solo los casos complejos |
| | **Derivar** | Derivar el seguimiento al especialista, conociendo sus aspectos generales |
| | **No requiere** | La situación no requiere seguimiento |

Fuente: [Perfil de Conocimientos EUNACOM, versión 3 (junio 2026)](https://www.eunacom.cl/contenidos/Perfil2026.pdf), vigente desde el examen de diciembre de 2026.
"""


def titulo_pagina(ruta_doc):
    """Devuelve el H1 de una página de docs/."""
    for linea in (DOCS / ruta_doc).read_text(encoding="utf-8").splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return Path(ruta_doc).stem.replace("-", " ").capitalize()


def enlace(desde_carpeta, ruta_doc):
    return os.path.relpath(DOCS / ruta_doc, DOCS / desde_carpeta).replace(os.sep, "/")


def celda_resumen(carpeta, fila):
    rutas = fila.get("resumen") or []
    if not rutas:
        return PEND
    partes = [f"[{titulo_pagina(r)}]({enlace(carpeta, r)})" for r in rutas]
    return OK + " " + " · ".join(partes)


def tabla(carpeta, filas):
    lineas = [
        "| Código | Situación | Diagnóstico | Tratamiento | Seguimiento | Resumen |",
        "|---|---|---|---|---|---|",
    ]
    for f in filas:
        lineas.append(
            f"| {f['codigo']} | {f['nombre']} | {f['dx']} | {f['tto']} | {f['seg']} | {celda_resumen(carpeta, f)} |"
        )
    return "\n".join(lineas)


def paginas_de(carpeta):
    return sorted(
        (p for p in (DOCS / carpeta).glob("*.md") if p.name != "index.md"),
        key=lambda p: titulo_pagina(f"{carpeta}/{p.name}"),
    )


def tabla_generales(carpeta, filas):
    lineas = ["| Código | Tema | Resumen |", "|---|---|---|"]
    for f in filas:
        lineas.append(f"| {f['codigo']} | {f['nombre']} | {celda_resumen(carpeta, f)} |")
    return "\n".join(lineas)


def contar(filas):
    return sum(1 for f in filas if f.get("resumen")), len(filas)


def main():
    datos = yaml.safe_load((RAIZ / "datos" / "temario.yml").read_text(encoding="utf-8"))
    grupos = datos["grupos"]

    total_hechas = total = 0

    for carpeta, titulo in CARPETAS.items():
        propios = [g for g in grupos if g["carpeta"] == carpeta]
        filas = [f for g in propios for f in g["situaciones"] + g["urgencias"]]
        hechas, n = contar(filas)
        total_hechas += hechas
        total += n

        partes = [
            "---\nhide:\n  - toc\n---\n",
            f"# {titulo}\n",
            f"Temario según el perfil EUNACOM v3 (2026). Cada situación indica el nivel exigido y el enlace al resumen cuando ya está escrito.\n",
            f'!!! info "Avance"\n    **{hechas} de {n}** situaciones clínicas de esta subespecialidad tienen resumen.\n',
        ]
        paginas = paginas_de(carpeta)
        if paginas:
            partes.append("## Resúmenes disponibles\n")
            partes.append(
                "\n".join(f"- {OK} [{titulo_pagina(f'{carpeta}/{p.name}')}]({p.name})" for p in paginas) + "\n"
            )
        varios = len(propios) > 1
        for g in propios:
            nivel = "###" if varios else "##"
            if varios:
                partes.append(f"## {g['titulo']} ({g['codigo']})\n")
            partes.append(f"{nivel} Situaciones clínicas\n")
            partes.append(tabla(carpeta, g["situaciones"]) + "\n")
            if g["urgencias"]:
                partes.append(f"{nivel} Situaciones clínicas de urgencia\n")
                partes.append(tabla(carpeta, g["urgencias"]) + "\n")
        partes.append(LEYENDA)
        (DOCS / carpeta / "index.md").write_text("\n".join(partes), encoding="utf-8")

    # Urgencias de todas las subespecialidades
    partes = [
        "---\nhide:\n  - toc\n---\n",
        "# Urgencias y paciente crítico\n",
        "Todas las **situaciones clínicas de urgencia** del perfil EUNACOM v3 de medicina interna, agrupadas por subespecialidad. Útil para preparar los turnos.\n",
    ]
    for g in grupos:
        if not g["urgencias"]:
            continue
        hechas, n = contar(g["urgencias"])
        partes.append(f"## {g['titulo']} ({hechas}/{n})\n")
        partes.append(tabla("urgencias", g["urgencias"]) + "\n")
    partes.append(LEYENDA)
    (DOCS / "urgencias").mkdir(exist_ok=True)
    (DOCS / "urgencias" / "index.md").write_text("\n".join(partes), encoding="utf-8")

    # Otras especialidades
    otras = yaml.safe_load((RAIZ / "datos" / "temario-otras.yml").read_text(encoding="utf-8"))["especialidades"]
    resumen_otras = []
    for esp in otras:
        carpeta, titulo = esp["carpeta"], esp["titulo"]
        filas = [f for g in esp["grupos"] for k in ("situaciones", "urgencias", "generales") for f in g[k]]
        hechas, n = contar(filas)
        paginas = paginas_de(carpeta) if (DOCS / carpeta).exists() else []
        resumen_otras.append((esp, hechas, n, len(paginas)))
        partes = [
            "---\nhide:\n  - toc\n---\n",
            f"# {titulo}\n",
            f'!!! info "En preparación"\n    **{hechas} de {n}** temas de {titulo.lower()} tienen resumen. '
            "Esta es la lista de temas que se van a escribir, según el perfil EUNACOM v3 (2026); "
            "los temas pendientes están marcados con :material-clock-outline:.\n",
        ]
        if paginas:
            partes.append("## Resúmenes disponibles\n")
            partes.append(
                "\n".join(f"- {OK} [{titulo_pagina(f'{carpeta}/{p.name}')}]({p.name})" for p in paginas) + "\n"
            )
        varios = len(esp["grupos"]) > 1
        for g in esp["grupos"]:
            nivel = "###" if varios else "##"
            if varios:
                partes.append(f"## {g['titulo']} ({g['codigo']})\n")
            partes.append(f"{nivel} Situaciones clínicas\n")
            partes.append(tabla(carpeta, g["situaciones"]) + "\n")
            if g["urgencias"]:
                partes.append(f"{nivel} Situaciones clínicas de urgencia\n")
                partes.append(tabla(carpeta, g["urgencias"]) + "\n")
            if g["generales"]:
                partes.append(f"{nivel} Conocimientos generales\n")
                partes.append(tabla_generales(carpeta, g["generales"]) + "\n")
        partes.append(LEYENDA)
        (DOCS / carpeta).mkdir(exist_ok=True)
        (DOCS / carpeta / "index.md").write_text("\n".join(partes), encoding="utf-8")

    # Bloque de avance en la página de medicina interna
    portada = DOCS / "medicina-interna" / "index.md"
    texto = portada.read_text(encoding="utf-8")
    n_paginas = sum(len(paginas_de(c)) for c in CARPETAS)
    bloque = (
        "<!-- avance:inicio -->\n"
        f'!!! info "Avance del temario"\n'
        f"    **{n_paginas} resúmenes** escritos, que cubren **{total_hechas} de {total}** situaciones clínicas "
        f"de medicina interna del perfil EUNACOM v3 (2026).\n"
        "<!-- avance:fin -->"
    )
    texto = re.sub(r"<!-- avance:inicio -->.*?<!-- avance:fin -->", bloque, texto, flags=re.S)
    portada.write_text(texto, encoding="utf-8")

    # Tarjetas de especialidades en la portada
    tarjetas = [
        '<div class="grid cards" markdown>\n',
        "-   :material-stethoscope:{ .lg .middle } **[Medicina interna](medicina-interna/index.md)**\n\n    ---\n\n"
        f"    **{n_paginas} resúmenes** · {total_hechas} de {total} temas EUNACOM · "
        "10 subespecialidades y urgencias\n",
    ]
    for esp, hechas, n, n_pag in resumen_otras:
        icono, desc = ICONOS.get(esp["carpeta"], ("book-open-variant", ""))
        estado = f"**{n_pag} resúmenes** · {hechas} de {n} temas" if n_pag else f"En preparación · {n} temas pendientes"
        tarjetas.append(
            f"-   :material-{icono}:{{ .lg .middle }} **[{esp['titulo']}]({esp['carpeta']}/index.md)**\n\n    ---\n\n"
            f"    {desc}. {estado}\n"
        )
    tarjetas.append("</div>")
    inicio = DOCS / "index.md"
    texto = inicio.read_text(encoding="utf-8")
    bloque = "<!-- especialidades:inicio -->\n" + "\n".join(tarjetas) + "\n<!-- especialidades:fin -->"
    texto = re.sub(r"<!-- especialidades:inicio -->.*?<!-- especialidades:fin -->", bloque, texto, flags=re.S)
    inicio.write_text(texto, encoding="utf-8")

    # Navegación de mkdocs.yml (una pestaña por especialidad)
    nav = ["nav:", "  - Inicio: index.md", "  - Medicina interna:", "      - medicina-interna/index.md"]
    for carpeta, titulo in CARPETAS.items():
        nav.append(f"      - {titulo}:")
        nav.append(f"          - {carpeta}/index.md")
        for p in paginas_de(carpeta):
            nav.append(f'          - "{titulo_pagina(f"{carpeta}/{p.name}")}": {carpeta}/{p.name}')
    nav.append("      - Urgencias: urgencias/index.md")
    for esp, _, _, n_pag in resumen_otras:
        carpeta = esp["carpeta"]
        nav.append(f"  - {esp['titulo']}:")
        nav.append(f"      - {carpeta}/index.md")
        for p in paginas_de(carpeta):
            nav.append(f'      - "{titulo_pagina(f"{carpeta}/{p.name}")}": {carpeta}/{p.name}')
    nav += [
        "  - Acerca de:",
        "      - Cómo se hacen los resúmenes: acerca/metodologia.md",
        "      - Temas GES y etiquetas: acerca/etiquetas.md",
    ]
    config = RAIZ / "mkdocs.yml"
    cfg = config.read_text(encoding="utf-8")
    cfg = cfg[: cfg.index("\nnav:\n") + 1] + "\n".join(nav) + "\n"
    config.write_text(cfg, encoding="utf-8")

    print(f"{n_paginas} resúmenes; {total_hechas}/{total} situaciones cubiertas")


if __name__ == "__main__":
    main()
