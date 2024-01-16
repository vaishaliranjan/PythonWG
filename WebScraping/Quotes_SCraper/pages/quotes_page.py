
from WebScraping.Quotes_SCraper.locators.quotes_page_locators import  QuotesPageLocators
from WebScraping.Quotes_SCraper.parsers.quote import QuoteParser
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tags_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.SEARCH_BUTTON
        )

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have any quotes tagged with '{tag_name}'."
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass