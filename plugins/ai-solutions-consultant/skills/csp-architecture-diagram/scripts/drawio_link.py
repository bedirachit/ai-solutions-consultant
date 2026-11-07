#!/usr/bin/env python3
"""Turn a draw.io XML file into (1) a .drawio file and (2) a clickable link
that opens the diagram directly in draw.io (app.diagrams.net).

Usage:
    python3 drawio_link.py <diagram.xml|diagram.drawio> [--out <file.drawio>]

The link uses draw.io's "#R" raw-compressed format:
    https://app.diagrams.net/#R<urlencoded(base64(deflateRaw(encodeURIComponent(xml))))>
Links longer than ~8,000 characters can be truncated by some browsers or chat
clients; in that case share the .drawio file and the instructions printed.
"""
import argparse
import base64
import sys
import urllib.parse
import zlib
from pathlib import Path

ENCODE_URI_COMPONENT_SAFE = "-_.!~*'()"


def compress(xml: str) -> str:
    encoded = urllib.parse.quote(xml, safe=ENCODE_URI_COMPONENT_SAFE)
    deflater = zlib.compressobj(9, zlib.DEFLATED, -15)  # raw deflate
    raw = deflater.compress(encoded.encode("utf-8")) + deflater.flush()
    return base64.b64encode(raw).decode("ascii")


def wrap_mxfile(xml: str) -> str:
    xml = xml.strip()
    if xml.startswith("<mxfile"):
        return xml
    return f'<mxfile host="app.diagrams.net"><diagram name="Architecture">{xml}</diagram></mxfile>'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out")
    args = ap.parse_args()

    xml = Path(args.src).read_text(encoding="utf-8")
    model = xml.strip()
    if model.startswith("<mxfile"):
        start = model.find("<mxGraphModel")
        end = model.rfind("</mxGraphModel>")
        if start != -1 and end != -1:
            model = model[start:end + len("</mxGraphModel>")]

    out = Path(args.out) if args.out else Path(args.src).with_suffix(".drawio")
    out.write_text(wrap_mxfile(xml), encoding="utf-8")

    link = "https://app.diagrams.net/#R" + urllib.parse.quote(compress(model), safe="")
    print(f"DRAWIO_FILE={out}")
    print(f"DRAWIO_LINK={link}")
    print(f"LINK_LENGTH={len(link)}")
    if len(link) > 8000:
        print("WARNING=Link is long; also share the .drawio file (File > Open in draw.io).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
