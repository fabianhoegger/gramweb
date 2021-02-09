import scrapy


class CheckGradeSpider(scrapy.Spider):
    name = 'check_grade'
    allowed_domains = ['gram-web.ionio.gr']
    start_urls = ['http://gram-web.ionio.gr/unistudent/login.asp']
    def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
        pass

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
            formdata={'userName': 'p16chai', 'pwd': 't1SCwT6t','submit1':'%C5%DF%F3%EF%E4%EF%F2','loginTrue':'login',
            'c02c71ae0d90143449b5882db85ca536c':'E98D85C6167EE8468D7BA9E0CAE05836D923D5D392C0BCD00A27A937AB379FDA2454E0E6C2D45F2F6FE8260078500E7DAC28FDE1A11682311BD68CC918B560900169729911FEB9C1987F077382287BEBA1626F2106E0D1199F4674ADC938DE44'},
            callback=self.after_login
        )
    def after_login(self,response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        else:
            return {'status':response.status,'title':response.xpath("//span[@class='title']/text()").get()}
