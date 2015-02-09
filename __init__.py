from calibre.customize import InterfaceActionBase

class SortByDateBase(InterfaceActionBase):

    name = 'Sort By Date'
    author = 'Andrea Bisognin'
    supported_platforms = ['windows', 'osx', 'linux']
    version             = (1, 0, 3)
    

    actual_plugin = 'calibre_plugins.sort_by_date.ui:SortByDatePlugin'

    def is_customizable(self):
        return False

    

