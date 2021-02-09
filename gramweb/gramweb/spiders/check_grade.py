import scrapy
from scrapy.http import FormRequest

class CheckGradeSpider(scrapy.Spider):
    name = 'check_grade'
    allowed_domains = ['gram-web.ionio.gr']
    start_urls = ['http://gram-web.ionio.gr/unistudent/login.asp']

    def authentication_failed(response):
        return {'status':response.status}

    def parse(self, response):
        return [scrapy.FormRequest.from_response(response,
            formdata={'userName': 'p16chai', 'pwd': 't1SCwT6t','submit1':'%C5%DF%F3%EF%E4%EF%F2','loginTrue':'login'},
            callback=self.after_login
        )]
    def after_login(self,response):
        if not response:
            self.logger.error("Login failed")
            return
        else:
            return {'status':response.status,'title':response.xpath("//span[@class='title']/text()").get()}
