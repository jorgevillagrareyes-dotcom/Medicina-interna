"""Marca en datos/temario-otras.yml los ítems que cubre una página.

Uso:  python3 scripts/marcar_resumen_otras.py <ruta dentro de docs/> <código> [<código> ...]
"""

import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "datos" / "temario-otras.yml"


def main():
    ruta, codigos = sys.argv[1], set(sys.argv[2:])
    if not (RAIZ / "docs" / ruta).exists():
        sys.exit(f"No existe docs/{ruta}")
    datos = yaml.safe_load(ARCHIVO.read_text(encoding="utf-8"))
    marcados = set()
    for esp in datos["especialidades"]:
        for sec in esp["secciones"]:
            for k in ("situaciones", "urgencias", "generales"):
                for it in sec[k]:
                    if it["codigo"] in codigos:
                        lista = it.setdefault("resumen", [])
                        if ruta not in lista:
                            lista.append(ruta)
                        marcados.add(it["codigo"])
    faltan = codigos - marcados
    if faltan:
        sys.exit(f"Códigos no encontrados: {sorted(faltan)}")
    ARCHIVO.write_text(yaml.safe_dump(datos, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    print(f"{ruta}: {len(marcados)} temas marcados")


if __name__ == "__main__":
    main()
