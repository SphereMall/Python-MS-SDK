class Collection:

    total = 0
    objects = {}
    meta = None

    pointer = 0

    def __init__(self, objects=None, meta=None):
        if objects:
            self.objects = objects
            try:
                self.total = len(objects)
            except BaseException:
                self.total = 1

        self.meta = meta

    def add(self, _object, id=None):
        self.objects.update({(id or self.total): _object})
        self.total += 1

    def getByIndex(self, index):
        return self.getRow(index)

    def count(self):
        return self.total

    def asArray(self):
        # TODO: Iterate  with other approach
        for item in self:
            pass
        return self.objects

    def getMeta(self):
        return self.meta

    def getRow(self, index):
        try:
            return self.objects[index]  # TODO test
        except BaseException:
            return None

    def current(self):
        return self.getRow(self.pointer)

    def next(self):
        row = self.getRow(self.pointer)
        if row:
            self.pointer += 1

    def key(self):
        return self.pointer

    def valid(self):
        isValid = (self.current() or False)
        if not isValid:
            self.pointer = 0

        return isValid
