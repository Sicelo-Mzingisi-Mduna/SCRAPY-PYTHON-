import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        Books = response.css('article.product_pod')
        for book in Books:
            yield{
                
                'title' : book.css('h3 a::attr(title)').get(),
                'price' : book.css('.price_color::text').get(),
                'url' : book.css('h3 a::attr(href)').get()  
            }
