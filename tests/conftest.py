import copy
from pathlib import Path
import sys
import pytest

from fastapi.testclient import TestClient

# Ensure `src` is importable as a module by adding src path to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import app as app_module


def _deepcopy_activities():
    return copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Arrange: テストごとに activities を元に戻す"""
    original = _deepcopy_activities()
    yield
    app_module.activities.clear()
    app_module.activities.update(original)
