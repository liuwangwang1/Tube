from faker import Faker
from .base_utils import Singleton

class Tube(Singleton):

    def __init__(self):
        self.faker = Faker("zh_CN")

    @staticmethod
    def faker():
        return Faker('zh_CN')

    def longitude(self):
        """
        随机经度生成 生效区间 东西经 [180, -180]
        :return:
        """
        return self.faker.longitude()

    def latitude(self):
        """
        随机维度生成 生效区间 南北纬 [90, -90]
        :return:
        """
        return self.faker.latitude()

    def country(self):
        """
        随机国家生成
        :return:
        """
        return self.faker.country()

    def company_prefix(self):
        """
        随机公司生成
        :return:
        """
        return self.faker.company_prefix()

    def geo_coordinate(self):
        """
        随机公司生成
        :return:
        """
        return self.faker.geo_coordinate()

    def company_suffix(self):
        """
        随机公司性质
        :return:
        """
        return self.faker.company_suffix()
