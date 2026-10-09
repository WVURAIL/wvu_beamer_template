#!/usr/bin/env python3
"""Prepare the four additional WVU pattern overlays from official PNG sources.

Requires Pillow. PDF output preserves the raster dimensions and alpha channel;
these files are not vector artwork. The original source files are unchanged.
"""

from pathlib import Path
import zlib

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
PATTERNS = {
    "distressed-lines": "Texture_DistressedLines.png",
    "rolling-hills": "Texture_RollingHills.png",
    "topo-dashed": "Texture_TopoDashed.png",
    "topo-morgantown": "Texture_Topo-Morgantown.png",
}


def pdf_stream(dictionary, data):
    return (
        b"<< " + dictionary + b" /Length " + str(len(data)).encode("ascii")
        + b" >>\nstream\n" + data + b"\nendstream"
    )


def write_pdf(path, image):
    """Embed the full-resolution white image and its 8-bit soft mask."""
    width, height = image.size
    dims = f"/Width {width} /Height {height}".encode("ascii")
    image_dict = (
        b"/Type /XObject /Subtype /Image " + dims
        + b" /ColorSpace /DeviceGray /BitsPerComponent 8 /Filter /FlateDecode"
    )
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] "
            "/Resources << /XObject << /Im0 5 0 R >> >> /Contents 4 0 R >>"
        ).encode("ascii"),
        pdf_stream(b"", f"q {width} 0 0 {height} 0 0 cm /Im0 Do Q".encode("ascii")),
        pdf_stream(image_dict + b" /SMask 6 0 R", zlib.compress(bytes([255]) * width * height, 9)),
        pdf_stream(image_dict, zlib.compress(image.getchannel("A").tobytes(), 9)),
    ]
    data = bytearray(b"%PDF-1.5\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, body in enumerate(objects, 1):
        offsets.append(len(data))
        data.extend(f"{number} 0 obj\n".encode("ascii") + body + b"\nendobj\n")
    xref = len(data)
    data.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode("ascii"))
    for offset in offsets[1:]:
        data.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    data.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref}\n%%EOF\n".encode("ascii")
    )
    path.write_bytes(data)


def main():
    for name, filename in PATTERNS.items():
        original = Image.open(ROOT / "sources" / filename).convert("RGBA")
        alpha = original.getchannel("A")
        if name == "rolling-hills":
            # Encode the source's shaded layers as white with varying opacity.
            alpha = ImageChops.multiply(alpha, original.convert("L"))
        overlay = Image.new("RGBA", original.size, "white")
        overlay.putalpha(alpha)
        overlay.save(ROOT / f"{name}-white.png", optimize=True)
        write_pdf(ROOT / f"{name}-white.pdf", overlay)
        print(f"{name}: {original.width} x {original.height}")


if __name__ == "__main__":
    main()
