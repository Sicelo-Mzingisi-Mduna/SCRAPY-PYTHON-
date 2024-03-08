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
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                string_1 = 'https://books.toscrape.com/'
                string_2 = next_page
                next_page = string_1 + string_2
            else:
                string_1 = 'https://books.toscrape.com/catalogue/'
                string_2 = next_page
                next_page = string_1 + string_2
            yield response.follow(next_page, callback=self.parse)
        
