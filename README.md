# OGCardForge

**Built by Mourad.Soltani**

A minimal, offline CLI tool to generate beautiful Open Graph / social preview card images (1200×630 PNG) from title, description, and optional author or accent color.

Perfect for indie hackers, bloggers, and developers who want consistent, professional social cards without depending on external SaaS APIs.

## Features

- Generates clean, modern social cards
- Customizable title, description, author, accent color
- Offline — no API keys required
- Simple CLI interface
- Health checks included

## Installation

```bash
pip install -r requirements.txt
```

Or for development:

```bash
pip install -e .
```

## Usage

```bash
python -m ogcardforge --title "My Product Launch" --description "The simplest way to generate OG cards" --author "Mourad.Soltani" --output card.png
```

Options:

- `--title` (required): Card title
- `--description`: Subtitle / description
- `--author`: Author or brand name
- `--accent`: Hex color for accent (default #6366f1)
- `--output`: Output file path (default og-card.png)

## Health Test

```bash
pytest tests/test_health.py
```

## Requirements

- Python 3.9+
- Pillow

## License

MIT — see LICENSE

---

Signature: Mourad.Soltani
