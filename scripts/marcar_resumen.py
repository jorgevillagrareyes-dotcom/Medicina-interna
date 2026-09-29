"""Marca en datos/temario.yml que una página cubre ciertas situaciones EUNACOM.

Uso:  python3 scripts/marcar_resumen.py cardiologia/hipertension-arterial.md 1.01.1.015 1.09.1.008
"""

from pathlib import Path
import sys

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVO = RAIZ / "datos" / "temario.yml"


class Dumper(yaml.SafeDumper):
    pass


def main():
    ruta, codigos = sys.argv[1], set(sys.argv[2:])
    if not (RAIZ / "docs" / ruta).exists():
        sys.exit(f"No existe docs/{ruta}")
    texto = ARCHIVO.read_text(encoding="utf-8")
    cabecera = "".join(l + "\n" for l in texto.splitlines() if l.startswith("#"))
    datos = yaml.safe_load(texto)
    encontrados = set()
    for grupo in datos["grupos"]:
        for fila in grupo["situaciones"] + grupo["urgencias"]:
            if str(fila["codigo"]) in codigos:
                encontrados.add(str(fila["codigo"]))
                resumen = fila.setdefault("resumen", [])
                if ruta not in resumen:
                    resumen.append(ruta)
    faltan = codigos - encontrados
    if faltan:
        sys.exit(f"Códigos no encontrados: {sorted(faltan)}")
    cuerpo = yaml.dump(datos, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=200)
    ARCHIVO.write_text(cabecera + cuerpo, encoding="utf-8")
    print(f"{ruta}: {len(encontrados)} situaciones marcadas")


if __name__ == "__main__":
    main()
