import scrapy

class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    parking = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    desc = scrapy.Field()
    type = scrapy.Field()
    sq = scrapy.Field()
    next = scrapy.Field()
    pass

# class RentItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     title = scrapy.Field()
#     url = scrapy.Field()
#     Bed = scrapy.Field()
#     Bath = scrapy.Field()
#     Parking = scrapy.Field()
#     address = scrapy.Field()
#     desc = scrapy.Field()
#     type = scrapy.Field()
#     agent_co = scrapy.Field()

#     pass