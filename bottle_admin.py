# coding: utf-8


class Admin(object):
    """
    Creates an admin interface for models
    """

    def __init__(self, app=None):
        self.app = app
        self._models = []

    def register(self, model=None, modeladmin=None):
        self._models.append((model, modeladmin))


admin = Admin()
