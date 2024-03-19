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
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                string_1 = 'https://books.toscrape.com/'
                string_2 = next_page
                next_page_url = string_1 + string_2
            else:
                string_1 = 'https://books.toscrape.com/catalogue/'
                string_2 = next_page
                next_page_url = string_1 + string_2
            yield response.follow(next_page_url, callback=self.parse)
     
    def parse_book_page(self, response):
        yield{
            " Book_title " : response.css('#content_inner > article > div.row > div.col-sm-6.product_main > h1::text').get(),
        
            " Book_category " : response.css('#default > div > div > ul > li:nth-child(3) > a::text').get().strip(),
        
            " Book_description " : response.css('#content_inner > article > p::text').get(),
            
            "Product type" : response.css('tr:nth-child(2) > td::text').get(),
            
            "Price (incl. tax)" : response.css('tr:nth-child(4) > td::text').get(),
            
            " Availability " : response.css('tr:nth-child(6) > td::text').get()
        }
        
        
             
            
    
        
 