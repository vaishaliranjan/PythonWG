from WebScraping.Quotes_SCraper.locators.quote_locators import QuoteLocator
class QuoteParser:
    def __init__(self, parent):
        self.parent= parent

    @property
    def content(self):
        locator= QuoteLocator.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocator.TAGS
        return self.parent.select_one(locator).string