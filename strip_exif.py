import os
from pathlib import Path
from PIL import Image
import piexif

# Add this dependency if you don't already have it:
# pip install piexif pillow

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".tif", ".tiff", ".webp"}

# EXIF tags to preserve (will be copied if present)
PRESERVE_TAGS = {
    piexif.ImageIFD.Artist,
    piexif.ImageIFD.Copyright,
    piexif.ImageIFD.XPAuthor,
    piexif.ImageIFD.XPTitle,
    piexif.ImageIFD.XPComment,
}


def strip_exif_from_image(input_path: Path, output_path: Path, keep_copy: bool = False):
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if keep_copy and "exif" in img.info:
            # Load existing EXIF
            orig_exif = piexif.load(img.info["exif"])
            new_exif = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "Interop": {}, "thumbnail": None}

            for tag in PRESERVE_TAGS:
                for ifd in ("0th", "Exif"):
                    if tag in orig_exif.get(ifd, {}):
                        new_exif[ifd][tag] = orig_exif[ifd][tag]

            exif_bytes = piexif.dump(new_exif)
            img.save(output_path, exif=exif_bytes, quality=95, optimize=True)
        else:
            img.save(output_path, quality=95, optimize=True)


def strip_exif_in_folder(input_dir: str, output_dir: str, keep_copy: bool):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    for root, _, files in os.walk(input_dir):
        for f in files:
            ext = Path(f).suffix.lower()
            if ext not in IMAGE_EXTENSIONS:
                continue

            in_path = Path(root) / f
            rel = in_path.relative_to(input_dir)
            out_path = output_dir / rel

            print(f"Processing: {in_path} -> {out_path}")
            strip_exif_from_image(in_path, out_path, keep_copy)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Remove EXIF metadata from photos.")
    parser.add_argument("input_dir", help="Source folder")
    parser.add_argument("output_dir", help="Destination folder")
    parser.add_argument(
        "--keep-copyright",
        action="store_true",
        help="Preserve copyright/artist details",
    )

    args = parser.parse_args()
    strip_exif_in_folder(args.input_dir, args.output_dir, args.keep_copyright)
