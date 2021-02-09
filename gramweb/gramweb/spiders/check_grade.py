import scrapy


class CheckGradeSpider(scrapy.Spider):
    name = 'check_grade'
    allowed_domains = ['gram-web.ionio.gr']
    start_urls = ['http://gram-web.ionio.gr/unistudent/login.asp']
    def start_requests(self):
        return [scrapy.FormRequest("http://gram-web.ionio.gr/unistudent/login.asp",
                cookies={'login':'True','_ga':'GA1.2.907918764.1611845502', 'ASPSESSIONIDASDCSDSS':'DNDGNMPAKHPPFHIOLOPLIKED',
                'rcva%5F':'6ADD6817AC67F2076FB9F188120CFF735FD22225124417B174B6EA30D09E6424560FAB8FDF81C5C5B908B63873840579A8694B2044CE5F0E3B17C3C8DF64C77E5B67E341BB9E132BE4D2A59981E8E23B3BAD176458B08DA128D0F488BC23C35EB9D02149DD6DE168D0E2537AF4229FFABCDCA5AA486D7982CDD661F6E2FEB114',
                'sessionId':'6288D63B%2DB5D5%2D4E98%2D9ED9%2D273C3D3193F3%2Csrv%3D195%2E130%2E124%2E81','_gid':'GA1.2.1639919294.1612876337'})]
    def parse(self, response):
        return {'text':response.xpath("//[@id='header']/text()").get()}
