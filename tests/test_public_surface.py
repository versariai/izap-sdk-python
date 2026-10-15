from __future__ import annotations

import importlib
import importlib.util
import tomllib
from pathlib import Path

import pytest

import izap
import izap.models
from izap._generated import models as generated_models

ROOT = Path(__file__).resolve().parent.parent
API_MODULES = sorted(p.stem for p in (ROOT / "src" / "izap" / "api").glob("*.py") if p.stem != "__init__")
EXAMPLES = sorted((ROOT / "examples").glob("*.py"))


def test_top_level_exports_resolve() -> None:
    for name in izap.__all__:
        assert hasattr(izap, name), name


@pytest.mark.parametrize("module_name", API_MODULES)
def test_every_endpoint_has_sync_and_async_functions(module_name: str) -> None:
    module = importlib.import_module(f"izap.api.{module_name}")

    assert module.__all__
    for endpoint in module.__all__:
        functions = getattr(module, endpoint)
        assert callable(functions.sync_detailed), f"{module_name}.{endpoint}"
        assert callable(functions.asyncio_detailed), f"{module_name}.{endpoint}"
        # Endpoints without a response model only get the *_detailed forms.
        assert hasattr(functions, "sync") == hasattr(functions, "asyncio"), f"{module_name}.{endpoint}"


def test_models_re_export_everything_generated() -> None:
    assert sorted(izap.models.__all__) == sorted(generated_models.__all__)


def test_current_business_operations_are_generated() -> None:
    """Business-scoped ops are resolved via the ``business-id`` header, never a path param (GOG-4065)."""
    from izap.api import businesses, chats, messages, whatsapp_cloud

    assert {"get_current_business", "update_current_business", "get_current_business_hours"} <= set(businesses.__all__)
    assert "list_current_business_chats" in chats.__all__
    assert "get_current_business_chat_message_details" in messages.__all__
    assert {"list_current_whats_app_numbers", "get_current_whats_app_business_account_info"} <= set(
        whatsapp_cloud.__all__
    )


def test_version_matches_pyproject() -> None:
    assert tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"] == izap.__version__


@pytest.mark.parametrize("example", EXAMPLES, ids=[p.name for p in EXAMPLES])
def test_examples_import_cleanly(example: Path) -> None:
    spec = importlib.util.spec_from_file_location(f"example_{example.stem}", example)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert callable(module.main)
