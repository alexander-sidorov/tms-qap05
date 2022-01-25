from types import ModuleType
from typing import Any
from typing import Iterable
from typing import Optional

undefined = object()


def get_class(
    module: ModuleType,
    cls_name: str,
    *,
    expected_attrs_types: Optional[dict[str, Any]] = None,
    expected_public_attrs: bool = True,
    expected_bases: Iterable[type] = (),
) -> type:
    full_cls_name = f"{module.__name__}.{cls_name}"
    expected_attrs_types = expected_attrs_types or {}

    cls = getattr(module, cls_name, undefined)

    err = f"{full_cls_name} is not defined."
    assert cls is not undefined, err

    err = f"{full_cls_name} is {cls!r}: not a class."
    assert isinstance(cls, type), err

    for name, expected_type in expected_attrs_types.items():
        attr = getattr(cls, name, undefined)

        err = f"{full_cls_name}.{name} is not defined."
        assert attr is not undefined, err

        attr_type = type(attr)
        err = (
            f"{full_cls_name}.{name} is {attr!r}."
            f" Type is {attr_type!r} != {expected_type!r} (expected)."
        )
        assert isinstance(attr, expected_type), err

    if not expected_public_attrs:
        public_attrs = [
            attr for attr in cls.__dict__ if not attr.startswith("_")
        ]

        err = (
            f"No public attrs expected in {full_cls_name}."
            f" These found: {public_attrs}."
        )
        assert not public_attrs, err

    expected_bases = set(expected_bases)
    actual_bases = set(cls.mro())
    missing_bases = expected_bases - actual_bases
    s_missing_bases = ", ".join(typ.__name__ for typ in missing_bases)
    err = f"{full_cls_name} is not derived from {s_missing_bases}."
    assert not missing_bases, err

    return cls
