from .hit_calling import get_ks

_TRAJECTORY_EXPORTS = {
    "slingshot",
    "test_common_trajectory",
    "test_differential_differentiation",
    "test_differential_progression",
}

__all__ = ["get_ks", *_TRAJECTORY_EXPORTS]


def __getattr__(name: str):
    if name in _TRAJECTORY_EXPORTS:
        from importlib import import_module

        module = import_module("scmorph.tl.trajectories")
        return getattr(module, name)
    raise AttributeError(f"module 'scmorph.tl' has no attribute {name!r}")
