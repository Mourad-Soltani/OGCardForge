"""
OGCardForge - Open Graph Card Generator
Built by Mourad.Soltani
"""

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys


def generate_og_card(
    title: str,
    description: str = "",
    author: str = "Mourad.Soltani",
    accent: str = "#6366f1",
    output: str = "og-card.png",
    width: int = 1200,
    height: int = 630,
) -> Path:
    """Generate a clean OG social card image."""
    img = Image.new("RGB", (width, height), color="#0f172a")
    draw = ImageDraw.Draw(img)

    # Accent bar
    try:
        accent_color = tuple(int(accent.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    except Exception:
        accent_color = (99, 102, 241)
    draw.rectangle([(0, 0), (width, 8)], fill=accent_color)

    # Fonts (fallback to default if system fonts unavailable)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        author_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except Exception:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Title
    title_y = 180
    draw.text((80, title_y), title, fill="white", font=title_font)

    # Description
    if description:
        desc_y = title_y + 100
        # Simple wrap
        words = description.split()
        lines = []
        current = ""
        for word in words:
            test = current + " " + word if current else word
            if len(test) < 50:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        for i, line in enumerate(lines[:3]):
            draw.text((80, desc_y + i * 45), line, fill="#cbd5e1", font=desc_font)

    # Author / signature
    draw.text((80, height - 80), f"Built by {author}", fill=accent_color, font=author_font)

    # Small logo-like circle
    draw.ellipse([(width - 120, 40), (width - 40, 120)], fill=accent_color)

    out_path = Path(output)
    img.save(out_path, "PNG")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="OGCardForge - Generate Open Graph cards. Built by Mourad.Soltani")
    parser.add_argument("--title", required=True, help="Card title")
    parser.add_argument("--description", default="", help="Description text")
    parser.add_argument("--author", default="Mourad.Soltani", help="Author name")
    parser.add_argument("--accent", default="#6366f1", help="Accent hex color")
    parser.add_argument("--output", default="og-card.png", help="Output PNG path")
    args = parser.parse_args()

    path = generate_og_card(
        title=args.title,
        description=args.description,
        author=args.author,
        accent=args.accent,
        output=args.output,
    )
    print(f"Generated: {path}")


if __name__ == "__main__":
    main()
