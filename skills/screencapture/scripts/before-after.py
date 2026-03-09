#!/usr/bin/env python3
"""Create a before/after comparison image from two screenshots."""

import sys
from PIL import Image, ImageDraw, ImageFont

def main():
    if len(sys.argv) < 4:
        print("Usage: before-after.py <before.png> <after.png> <output.png> [--label-before TEXT] [--label-after TEXT]")
        sys.exit(1)

    before_path = sys.argv[1]
    after_path = sys.argv[2]
    output_path = sys.argv[3]

    label_before = "Before"
    label_after = "After"

    # Parse optional labels
    for i, arg in enumerate(sys.argv):
        if arg == "--label-before" and i + 1 < len(sys.argv):
            label_before = sys.argv[i + 1]
        if arg == "--label-after" and i + 1 < len(sys.argv):
            label_after = sys.argv[i + 1]

    before = Image.open(before_path)
    after = Image.open(after_path)

    # Scale to same height
    target_h = min(before.height, after.height, 400)
    b_resized = before.resize((int(before.width * target_h / before.height), target_h), Image.LANCZOS)
    a_resized = after.resize((int(after.width * target_h / after.height), target_h), Image.LANCZOS)

    # Layout
    padding = 30
    label_h = 45
    arrow_w = 70
    total_w = padding + b_resized.width + arrow_w + a_resized.width + padding
    total_h = padding + label_h + target_h + padding

    canvas = Image.new('RGB', (total_w, total_h), (26, 26, 46))
    draw = ImageDraw.Draw(canvas)

    # Font
    font = None
    for font_path in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        try:
            font = ImageFont.truetype(font_path, 26)
            break
        except (IOError, OSError):
            continue
    if font is None:
        font = ImageFont.load_default()

    before_x = padding
    after_x = padding + b_resized.width + arrow_w
    img_y = padding + label_h

    # Labels
    for label, x, w, color in [
        (label_before, before_x, b_resized.width, (255, 120, 120)),
        (label_after, after_x, a_resized.width, (120, 255, 120)),
    ]:
        bbox = draw.textbbox((0, 0), label, font=font)
        lw = bbox[2] - bbox[0]
        draw.text((x + (w - lw) // 2, padding + 5), label, fill=color, font=font)

    # Images
    canvas.paste(b_resized, (before_x, img_y))
    canvas.paste(a_resized, (after_x, img_y))

    # Arrow
    acx = before_x + b_resized.width + arrow_w // 2
    acy = img_y + target_h // 2
    draw.line([(acx - 18, acy), (acx + 18, acy)], fill=(200, 200, 200), width=3)
    draw.polygon([(acx + 18, acy - 8), (acx + 18, acy + 8), (acx + 30, acy)], fill=(200, 200, 200))

    # Borders
    for x, w in [(before_x, b_resized.width), (after_x, a_resized.width)]:
        draw.rectangle([x - 2, img_y - 2, x + w + 1, img_y + target_h + 1], outline=(70, 70, 110), width=2)

    canvas.save(output_path, quality=95)
    print(f"Saved {output_path} ({canvas.size[0]}x{canvas.size[1]})")


if __name__ == "__main__":
    main()
