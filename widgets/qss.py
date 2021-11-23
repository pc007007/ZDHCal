class Qss:
    def __init__(self, style='default'):
        self.default()
        if style == 'default':
            self.default()

    def default(self):
        # 主程序toolbutton样式
        self.button = """
            QToolButton,QPushButton{
                background-color:transparent;
                padding-right:5px;
                padding-left:5px;
                border: None;
                }
            QToolButton:hover,QPushButton:hover{
                background-color:rgb(201,222,245);
                }
        """
        self.button_blue = """
            QToolButton,QPushButton{
                background-color:rgb(66,133,244);
                border-radius: 3px;
                color: white;
                padding-right:5px;
                padding-left:5px;
                border: None;
                }
            QToolButton:hover,QPushButton:hover{
                background-color:rgb(201,222,245);
                }
        """
        self.button_red = """
            QToolButton,QPushButton{
                background-color:rgb(219,68,55);
                border-radius: 3px;
                color: white;
                padding-right:5px;
                padding-left:5px;
                border: None;
                }
            QToolButton:hover,QPushButton:hover{
                background-color:rgb(201,222,245);
                }
        """
        self.button_green = """
            QToolButton,QPushButton{
                background-color:rgb(15,157,88);
                border-radius: 3px;
                color: white;
                padding-right:5px;
                padding-left:5px;
                border: None;
                }
            QToolButton:hover,QPushButton:hover{
                background-color:rgb(201,222,245);
                }
        """
        self.button_yellow = """
            QToolButton,QPushButton{
                background-color:rgb(244,180,0);
                border-radius: 3px;
                color: white;
                padding-right:5px;
                padding-left:5px;
                border: None;
                }
            QToolButton:hover,QPushButton:hover{
                background-color:rgb(201,222,245);
                }
        """
        # 主程序文件条toolbar样式
        self.toolbar_afc = """
            QToolBar{
                border: 1px solid rgb(204,206,219);
                background-color: rgb(238,238,242);
                margin: 5px;
                margin-right:0px;
                margin-left: 0px;
                }
        """
        # 主程序menu样式
        self.menu = """
            QMenu{
                background-color: white;
                border:1px solid rgb(82,130,164);
                }
        """
        self.listView_fileDirectory = """
            QListView{
                border: None;
                }
        """
        self.toolButton_fileDirectory = """
            QToolButton {
                qproperty-icon: None;
                image: url(:/resource/ExpandRight_16x.svg);
                background-color: transparent;
                border: None;
                }

            QToolButton:hover {
                background-color: rgb(201,222,245);
                border: None;
                }
            QToolButton:open {
                image: url(:/resource/ExpandDown_16x.svg);
                }
            QToolButton::menu-indicator {
                image: url(menu_indicator.png);
                subcontrol-origin: padding;
                subcontrol-position: bottom right;
                }
            """
