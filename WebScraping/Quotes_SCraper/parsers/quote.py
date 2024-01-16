from WebScraping.Quotes_SCraper.locators.quote_locators import QuoteLocator

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocator.CONTENT_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tag(self):
        locator = QuoteLocator.TAGS_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text