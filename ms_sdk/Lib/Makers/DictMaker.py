class DictMaker(dict):
    def  __getattr__(self, k):
        return self[k]


# class DictMaker(dict):
#     def __init__(self):
#         self.__getattr__ = self.get