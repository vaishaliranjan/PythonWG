from bs4 import BeautifulSoup
import re
ITEM_HTML= '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''

class ParsedItemLocator:
    NAME_LOCATOR= "article.product_pod h3 a"
    LINK_LOCATOR= "article.product_pod h3 a"
    PARAGRAPH_LOCATOR= "article div.product_price p.price_color"
class ParsedItem:
    def __init__(self, page):
        self.soup= BeautifulSoup(page, "html.parser")

    def find_item_name(self):
        item_link= self.soup.select_one(ParsedItemLocator.NAME_LOCATOR)
        item_name = item_link.attrs['title']
        print(item_name)

    def find_item_href(self):
        item_link= self.soup.select_one(ParsedItemLocator.LINK_LOCATOR)
        item_name = item_link.attrs['href']
        print(item_name)



    def find_p(self):
        item_name = self.soup.select_one(ParsedItemLocator.PARAGRAPH_LOCATOR).string
        pattern='£([0-9]+\.[0-9]+)'
        matches= re.match(pattern,item_name)
        print(matches.group(1))

parsed = ParsedItem(ITEM_HTML)
parsed.find_p()
parsed.find_item_name()
parsed.find_item_href()