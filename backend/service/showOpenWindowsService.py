from Xlib import display

class ShowOpenWindowsService:
    def showOpenWindow():
        d = display.Display()
        root = d.screen().root

        query = root.query_tree()

        windowList = []
        for c in query.children:
            # returns window name or None
            name = c.get_wm_name()
            if name: 
                windowList.append(name)

        return windowList


