class lazy:
    def __init__(self, fn):
        self._name = fn.__name__
        self._fn = fn

    def __get__(self, instance, owner):
        if instance is None:
            # when the attribute is accessed through the owner.
            return self

        value = self._fn(instance)
        instance.__dict__[self._name] = value
        return value
