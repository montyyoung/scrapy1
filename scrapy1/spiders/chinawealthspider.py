import scrapy

class chinaWealthSpider(scrapy.Spider):
    name = "chinawealth"
    allowed_domains = ["chinawealth.com"]
    start_urls = [
        "http://www.chinawealth.com.cn/zzlc/jsp/lccp.jsp",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            productList = sel.xpath('a/productList').extract()
            #desc = sel.xpath('text()').extract()
            print title, productList, desc



