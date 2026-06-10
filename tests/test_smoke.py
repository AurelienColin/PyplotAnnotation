"""Smoke tests for PyplotAnnotation.
Annotater.__init__ calls plt.subplots + plt.show (GUI); skip in headless CI.
"""
import os
import sys
import pytest

# matplotlib may fail to import on systems with numpy version mismatch
_mpl_exc = (ImportError, SystemError)


def test_import_module():
    """Module-level import: requires matplotlib, PIL, fire, numpy."""
    pytest.importorskip("matplotlib", exc_type=_mpl_exc)
    pytest.importorskip("PIL")
    pytest.importorskip("fire")
    pytest.importorskip("numpy")
    import PyplotAnnotation.PyplotAnnotation  # noqa: F401


def test_class_accessible():
    pytest.importorskip("matplotlib", exc_type=_mpl_exc)
    pytest.importorskip("PIL")
    pytest.importorskip("fire")
    pytest.importorskip("numpy")
    from PyplotAnnotation.PyplotAnnotation import Annotater
    assert callable(Annotater)


def test_colors_constant():
    pytest.importorskip("matplotlib", exc_type=_mpl_exc)
    pytest.importorskip("PIL")
    pytest.importorskip("fire")
    pytest.importorskip("numpy")
    from PyplotAnnotation.PyplotAnnotation import COLORS
    assert len(COLORS) > 0


def test_save_json(tmp_path):
    """save_json has no GUI dep; test its round-trip."""
    pytest.importorskip("matplotlib", exc_type=_mpl_exc)
    pytest.importorskip("PIL")
    pytest.importorskip("fire")
    pytest.importorskip("numpy")
    import json
    orig_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        from PyplotAnnotation.PyplotAnnotation import save_json
        save_json({"img.png": [[1, [(0, 0), (1, 1), (2, 0)]]]})
        with open("results.json") as f:
            data = json.load(f)
        assert "img.png" in data
    finally:
        os.chdir(orig_dir)


def test_annotater_init_skipped_headless():
    """Annotater.__init__ opens a matplotlib window; skip without display."""
    if not os.environ.get("DISPLAY") and sys.platform != "win32":
        pytest.skip("no display: matplotlib GUI init would fail in headless CI")
    pytest.importorskip("matplotlib", exc_type=_mpl_exc)
    pytest.importorskip("PIL")
    pytest.importorskip("fire")
    pytest.importorskip("numpy")
    from PyplotAnnotation.PyplotAnnotation import Annotater  # noqa: F401
