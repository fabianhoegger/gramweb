import scrapy


class CheckGradeSpider(scrapy.Spider):
    name = 'check_grade'
    allowed_domains = ['gram-web.ionio.gr']
    start_urls = ['http://gram-web.ionio.gr/unistudent/login.asp']
    def start_requests(self):
        return [scrapy.FormRequest("http://gram-web.ionio.gr/unistudent/login.asp",
                cookies={'login':'True','_ga':'GA1.2.907918764.1611845502', 'ASPSESSIONIDASDCSDSS':'DNDGNMPAKHPPFHIOLOPLIKED',
                '_gid':'GA1.2.1639919294.1612876337'})]

    def parse(self, response):
        return {'text':response.status}

"""    def make_requests_from_url(self,url):
        request=super(CheckGradeSpider,self).make_requests_from_url(url)
        request.cookies['login']='True'
        request.cookies['_ga']='GA1.2.907918764.1611845502'
        request.cookies['ASPSESSIONIDASDCSDSS']='DNDGNMPAKHPPFHIOLOPLIKED'
        request.cookies['_gid']='GA1.2.1639919294.1612876337'
        return request"""
