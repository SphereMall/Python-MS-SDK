class Entity(dict):
    def __getattr__(self, k):
        return self[k]
