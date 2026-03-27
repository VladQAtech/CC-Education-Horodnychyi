"""
Visual regression test suite for the Promova web homepage.

This module contains snapshot-based visual tests that capture screenshots of
key UI sections and assert they match previously approved baseline images.
Run with: pytest -m visual
"""

import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

BASE_URL = "https://promova.com"


@pytest.mark.visual
def test_homepage_hero_visual(page: Page) -> None:
    """Screenshot the hero section and assert it matches the stored snapshot."""
    home = HomePage(page)
    home.navigate(BASE_URL)

    hero = page.locator("[data-testid='hero-section']")
    hero.wait_for(state="visible")

    screenshot = hero.screenshot()
    expect(page).to_have_screenshot("homepage_hero.png")


@pytest.mark.visual
def test_homepage_nav_visual(page: Page) -> None:
    """Screenshot the navigation bar and assert it matches the stored snapshot."""
    home = HomePage(page)
    home.navigate(BASE_URL)

    nav = page.locator("nav")
    nav.wait_for(state="visible")

    screenshot = nav.screenshot()
    expect(page).to_have_screenshot("homepage_nav.png")


@pytest.mark.visual
def test_homepage_language_selector_visual(page: Page) -> None:
    """Screenshot the language selector section and assert it matches the stored snapshot."""
    home = HomePage(page)
    home.navigate(BASE_URL)

    language_selector = page.locator("[data-testid='language-selector']")
    language_selector.wait_for(state="visible")

    screenshot = language_selector.screenshot()
    expect(page).to_have_screenshot("homepage_language_selector.png")
