from app.ui_utils.main_page.tab_mods_set import MainPage_ModsSet
from app.ui_utils.main_page.tab_server_open import MainPage_ServerOpen
from app.ui_utils.main_page.tab_server_set import MainPage_ServerSet


class MainPage(MainPage_ServerOpen, MainPage_ServerSet, MainPage_ModsSet):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._bind_events()

