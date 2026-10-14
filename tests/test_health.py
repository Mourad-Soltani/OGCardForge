"""
Health tests for OGCardForge
Built by Mourad.Soltani
"""

import tempfile
from pathlib import Path
from ogcardforge import generate_og_card


def test_generate_basic_card():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "test.png"
        result = generate_og_card(
            title="Test Card",
            description="A simple health check",
            author="Mourad.Soltani",
            output=str(out),
        )
        assert result.exists()
        assert result.stat().st_size > 1000
        assert result.suffix == ".png"


def test_generate_with_custom_accent():
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "accent.png"
        result = generate_og_card(
            title="Accent Test",
            accent="#ff6b6b",
            output=str(out),
        )
        assert result.exists()
        assert result.stat().st_size > 1000
