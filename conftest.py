"""Global pytest configuration. Real fixtures arrive Day 1."""
import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the application under test."""
    return "https://www.saucedemo.com"