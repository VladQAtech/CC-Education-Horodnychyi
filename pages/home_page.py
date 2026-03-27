from playwright.sync_api import Page


class HomePage:
    """Page Object for the Promova homepage (https://promova.com).

    Encapsulates locators and interactions for the main marketing page,
    including the hero section, CTA button, language selector, and navigation.
    """

    URL = "https://promova.com"

    def __init__(self, page: Page) -> None:
        self.page = page

        # Hero section
        self.hero_heading = self.page.locator("h1")

        # Primary CTA button
        self.try_promova_button = self.page.locator(
            "a:has-text('TRY PROMOVA'), button:has-text('TRY PROMOVA')"
        )

        # Language selector buttons (e.g. "English", "Spanish", "French" pills/tabs)
        self.language_selector_buttons = self.page.locator(
            "[data-testid='language-selector'] button, "
            ".language-selector button, "
            "nav [class*='language'] button"
        )

        # Top navigation menu
        self.navigation_menu = self.page.locator("nav, [role='navigation']").first

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def navigate(self) -> None:
        """Open the Promova homepage and wait until it is fully loaded."""
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def get_hero_title(self) -> str:
        """Return the visible text of the hero heading."""
        return self.hero_heading.first.inner_text()

    def click_try_promova(self) -> None:
        """Click the primary 'TRY PROMOVA' call-to-action button."""
        self.try_promova_button.first.click()

    def select_language(self, language_name: str) -> None:
        """Click the language selector button matching *language_name*.

        Args:
            language_name: Visible label of the language button, e.g. 'Spanish'.
        """
        self.page.locator(
            f"button:has-text('{language_name}'), "
            f"[data-testid='language-selector'] :text('{language_name}')"
        ).first.click()
