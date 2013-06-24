from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from trends.items import TrendsItem

class TrendsSpider(BaseSpider):
    name = 'trends'
    allowed_domains = ["apartments.com"]
    start_urls = ["http://www.apartments.com"]
     
    def parse(self, response):
        hxs = HtmlXpathSelector(response)
        state_urls = hxs.select('//a[@class="geo-link"]/@href').extract()
        for url in state_urls:
            yield Request(start_urls[0]+url, callback=self.parse_list)

    def parse_list(self, response): 
   
    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        name = str(hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/h1[@itemprop="name"]/text()').extract()[0])
        contact = str(hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/div[@itemprop="telephone"]/text()').extract()[0])
        street = str( hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/div[@id="address"]/a[@href="#media-map"]/span[@itemprop="streetAddress"]/text()').extract()[0])
        city = str(hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/div[@id="address"]/a[@href="#media-map"]/span[@itemprop="addressLocality"]/text()').extract()[0])
        state = str(hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/div[@id="address"]/a[@href="#media-map"]/span[@itemprop="addressRegion"]/text()').extract()[0])
        zipcode = str(hxs.select('//div[@id="basic-info"]/section[@id="property-info"]/div[@id="address"]/a[@href="#media-map"]/span[@itemprop="postalCode"]/text()').extract()[0])
        body = ['//div[@id="1-bed"]', '//div[@id="2-bed"]', '//div[@id="3-bed"]']
        items = []
        for i in body:
            if hxs.select(i) != []:
                price = str(hxs.select(i+'/span[@class="rent"]/text()').extract()[0]).split('-')
                lp = int(re.search('\d+', price[0]).group(0))
                if len(price) == 2:
                    hp = int(re.search('\d+', price[1]).group(0))
                else:
                    hp = lp
                deposit = int(re.search('\d+', str(hxs.select(i+'/span[@class="deposit"]/text()').extract()[0])).group(0))
                beds = int(re.search('\d+', str(hxs.select(i+'/span[@class="beds"]/text()').extract()[0])).group(0))
                baths = int(re.search('\d+', str(hxs.select(i+'/span[@class="baths"]/text()').extract()[0])).group(0))
                square_feet = str(hxs.select(i+'/span[@class="square-feet"]/text()').extract()[0]).split('-')
                ls = int(re.search('\d+', square_feet[0]).group(0))
                if len(square_feet) == 2:
                    hs = int(re.search('\d+', square_feet[1]).group(0))
                else:
                    hs = ls
                item = TrendsItem()
                item['name'] = name
                item['contact'] = contact
                item['street'] = street
                item['city'] = city
                item['state'] = state
                item['zipcode'] = zipcode
                item['lp'] = lp
                item['hp'] = hp
                item['ls'] = ls
                item['hs'] = hs
                item['deposit'] = deposit
                item['beds'] = beds
                item['baths'] = baths
                items.append(item) 
        return items
        
