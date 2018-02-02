from ms_sdk.Entities.Company import Company
from ms_sdk.Lib.Mappers.Mapper import Mapper


class CompaniesMapper(Mapper):

    def doCreateObject(self, array):
        return Company(array)