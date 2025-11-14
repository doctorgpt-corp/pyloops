"""Re-export generated API modules."""

from pyloops._generated import api

__all__ = ["api"]


def __getattr__(name: str):
    """Dynamically forward attribute access to _generated.api."""
    import importlib

    try:
        module = importlib.import_module(f"pyloops._generated.api.{name}")
        return module
    except ImportError:
        raise AttributeError(f"module 'pyloops.api' has no attribute '{name}'")
