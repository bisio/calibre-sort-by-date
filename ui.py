from calibre.gui2.actions import InterfaceAction

AscendingOrder = 0
DescendingOrder = 1

class SortByDatePlugin(InterfaceAction):
    name='Sort By Date'
    action_spec = ('Sort By Date Plugin',None,'Run Sort By Date Plugin','Ctrl+Shift+t')
    
    def genesis(self):
        print 'called genesis in SortByDatePlugin'
        self.qaction.triggered.connect(self.sort)

    def sort(self):
        model = self.gui.library_view.model()
        idx = model.column_map.index("timestamp")
        self.gui.library_view.sortByColumn(idx,DescendingOrder)

