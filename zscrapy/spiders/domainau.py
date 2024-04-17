import scrapy
from zscrapy.items import HouseItem 


class DomainauSpider(scrapy.Spider):
    name = "domainau"
    allowed_domains = ['www.domain.com.au']
    start_urls = ["https://www.domain.com.au/sale/melton-vic-3337/"]
    BASE_URL="https://www.domain.com.au"

    c_page = 1
    
    def parse(self, response):
        LIST_XPATH = '//*[@id="skip-link-content"]/div[1]/div[2]/ul/li'
        
        PRICE_XPATH = 'div/div[2]/div/div[1]/p/text()'
        ADDRESS1_XPATH = 'div/div[2]/div/a/h2/span[1]/text()[1]'
        ADDRESS2_XPATH = 'div/div[2]/div/a/h2/span[2]/text()[1]'
        BED_XPATH = 'div/div[2]/div/div[2]/div[1]/div/span[1]/span/text()'
        BATH_XPATH = 'div/div[2]/div/div[2]/div[1]/div/span[2]/span/text()'
        PARK_XPATH = 'div/div[2]/div/div[2]/div[1]/div/span[3]/span/text()'
        SQ_XPATH = 'div/div[2]/div/div[2]/div[1]/div/span[4]/span/text()'
        TYPE_XPATH = 'div/div[2]/div/div[2]/div[2]/span/text()'
    
        NEXT_XPATH = 'a[data-testid="paginator-navigation-button"]::attr(href)'

        for resource in response.xpath(LIST_XPATH):
            item = HouseItem() # Creating a new Item object
            item['price'] = resource.xpath(PRICE_XPATH).extract_first()
            item['address1'] = resource.xpath(ADDRESS1_XPATH).extract_first()
            item['address2'] = resource.xpath(ADDRESS2_XPATH).extract_first()            
            item['bed'] = resource.xpath(BED_XPATH).extract_first()
            item['bath'] = resource.xpath(BATH_XPATH).extract_first()
            item['parking'] = resource.xpath(PARK_XPATH).extract_first()
            item['sq'] = resource.xpath(SQ_XPATH).extract_first()
            item['type'] = resource.xpath(TYPE_XPATH).extract_first()
            
            yield item

        
        for link in response.css(NEXT_XPATH).getall():
            print(f"link :{link}")
            has_page = link.split("?page=")
            
            if len(has_page) > 1:        
                page = int(has_page[1])
            else: 
                page = 1
                
            if page > self.c_page:
                print('THANH LOG ===> next_page: {}'.format(page))
                self.c_page = page
                yield scrapy.Request(url=self.BASE_URL+link, callback=self.parse)
                
                        
    
    