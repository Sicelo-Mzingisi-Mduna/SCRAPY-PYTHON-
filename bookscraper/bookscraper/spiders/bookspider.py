import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        Books = response.css('article.product_pod')
        for book in Books:
            relative_url = book.css(' h3 a ::attr(href)').get()
            if 'catalogue/' in relative_url:
                string_1 = 'https://books.toscrape.com/'
                string_2 = relative_url
                book_url = string_1 + string_2
            else:
                string_1 = 'https://books.toscrape.com/catalogue/'
                string_2 = relative_url
                book_url = string_1 + string_2
            yield response.follow(book_url, callback=self.parse_book_page)
     
    def parse_book_page(self, response):
       pass      
            
    
        
 