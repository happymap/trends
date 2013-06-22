from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from trends.items import TrendsItem

class TrendsSpider(BaseSpider):
    name = 'trends'
    allowed_domains = ["apartments.com"]
    start_urls = ["http://www.apartments.com/California/Mountain-View/Archstone-Mountain-View/1107480"]
    

    def buildItem(body):
        if hxs.select(body) != []:
            price = str(hxs.select(body+'/span[@class="rent"]/text()').extract()[0]).split('-')
            lp = re.search('/d+', price[0])
            if len(price1) == 2:
                hp = re.search('/d+', price[1])
            else:
                hp = lp1
            deposit = re.search('/d+' ,str(hxs.select(body+'/span[@class="deposit"]/text()').extract()[0]))
            beds = 1
            baths = re.search('/d+', str(hxs.select(body+'/span[@class="baths"]/text()').extract()[0]))
            square_feet = str(hxs.select(body+'/span[@class="square-feet"]/text()').extract()[0]).splite('-')
            ls = re.search('/d+', square_feet[0])
            if len(square_feet) == 2:
                hs = re.search('/d+', square_feet[1])
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


    def parse(self, response):
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
            buildItem(i)
        return items
        
