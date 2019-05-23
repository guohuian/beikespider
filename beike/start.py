import scrapy
from scrapy.cmdline import execute

def main():
    # scrapy.cmdline.execute("scrapy crawl mybeike".split())
    # scrapy.cmdline.execute("scrapy crawl mybeike --nolog".split())
    scrapy.cmdline.execute("scrapy crawl citys".split())
if __name__ == '__main__':
    main()