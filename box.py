from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import datetime,threading,json,sys,os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.stdout = open("data\\logs\\"+str(datetime.datetime.now()).split(" ")[0]+".log","a",encoding="utf-8")
print(f"---------------------------------{str(datetime.datetime.now().hour)}:{str(datetime.datetime.now().minute)}:{str(datetime.datetime.now().second)}-------------------------------")

setups = json.load(open("data\\config\\settings.json","r",encoding="utf-8"))
langs = json.load(open("data\\language\\"+setups["language"]+".json","r",encoding="utf-8"))["languages"]
tw = ""
app = None

def loga(s:str,id="3DBOX"):
    text = f"[{str(datetime.datetime.now().hour)}:{str(datetime.datetime.now().minute)}:{str(datetime.datetime.now().second)}][{id}] {s.capitalize()}"
    print(text)

class SettingsWindow(QMainWindow,object):
    def __init__(self):
        loga("Initing Settings")
        super().__init__(parent=startwindow)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setMinimumSize(self.width(),self.height())
        self.setMaximumSize(self.width(),self.height())

        self.langk.clear()
        sn = json.load(open("data\\language\\"+setups["language"]+".json","r",encoding="utf-8"))["show_name"]
        self.langk.addItem(sn)
        self.file = {}
        for w in os.listdir("data\\language"):
            sn = json.load(open("data\\language\\"+w,"r",encoding="utf-8"))["show_name"]
            if w != setups["language"]+".json":
                self.langk.addItem(sn)
            self.file[sn] = w
        self.Determine.clicked.connect(self.dsetup)
        self.cancel.clicked.connect(self.close)

        loga("Settings OK")
        self.show()
    
    def dsetup(self):
        global langs
        setups["language"] = self.file[self.langk.currentText()].split(".")[0]
        json.dump(setups,open("data\\config\\settings.json","w",encoding="utf-8"))
        langs = json.load(open("data\\language\\"+setups["language"]+".json","r",encoding="utf-8"))["languages"]
        self.retranslateUi(self)
        startwindow.retranslateUi(startwindow)
        self.close()

    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(318, 170)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 301, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.langk = QComboBox(self.centralwidget)
        self.langk.setObjectName(u"langk")
        self.langk.setGeometry(QRect(170, 30, 131, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 311, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(self.layoutWidget)
        self.cancel.setObjectName(u"cancel")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(11)
        self.cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.cancel)

        self.Determine = QPushButton(self.layoutWidget)
        self.Determine.setObjectName(u"Determine")
        self.Determine.setFont(font1)

        self.horizontalLayout.addWidget(self.Determine)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", langs[3], None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", langs[5], None))
        self.cancel.setText(QCoreApplication.translate("SettingsWindow", langs[6], None))
        self.Determine.setText(QCoreApplication.translate("SettingsWindow", langs[7], None))
    # retranslateUi

class StartWindow(QMainWindow,object):
    def __init__(self):
        loga("Initing Window")
        super().__init__()
        self.setupUi(self)
        self.setMinimumSize(self.width(),self.height())
        self.setMaximumSize(self.width(),self.height())
		
        self.setWindowIcon(QIcon("icon.ico"))
        self.setup()

        self.worldList.itemClicked.connect(self.cc)
        self.setings.clicked.connect(self.ss)
        self.DelteWorld.clicked.connect(self.delworld)
        self.JoinWorld.clicked.connect(self.joinworld)

        self.show()


    def setup(self):
        loga("Window Setuping")
        self.worldList.clear()
        for w in os.listdir("data\\world"):
            self.worldList.addItem(".".join(w.split(".")[0:-1]))
        self.worldList.addItem(langs[2])

    def cc(self):
        item = self.worldList.selectedItems()[0]
        self.JoinWorld.setEnabled(True)
        for x in range(self.worldList.count()-1):
            if (item.text() == self.worldList.item(x).text()):
                self.DelteWorld.setEnabled(True)
                break
        else:
            self.DelteWorld.setEnabled(False)
    
    def ss(self):
        self.setwin = SettingsWindow()
    
    def delworld(self):
        item = self.worldList.selectedItems()[0]
        if (QMessageBox.information(self,langs[8],langs[9],QMessageBox.No,QMessageBox.Yes) == QMessageBox.Yes):
            os.remove("data\\world\\"+item.text()+".world")
            loga("delte world: "+item.text()+" suffciy")
            self.setup()
            QMessageBox.information(self,langs[8],langs[10])
    
    def joinworld(self):
        global tw,app
        # threading.Timer(1,self.close).start()
        tw = self.worldList.selectedItems()[0].text()
        self.hide()
        if self.DelteWorld.isEnabled() == False:
            self.aa = creaworldw()
            if app:
                self.close()
            else:
                self.show()
                return
        app = BOX3D(tw)
        app.run()
        self.close()
        

    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(581, 537)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 501, 51))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.worldList = QListWidget(self.centralwidget)
        QListWidgetItem(self.worldList)
        self.worldList.setObjectName(u"worldList")
        self.worldList.setGeometry(QRect(10, 60, 561, 411))
        self.JoinWorld = QPushButton(self.centralwidget)
        self.JoinWorld.setObjectName(u"JoinWorld")
        self.JoinWorld.setEnabled(False)
        self.JoinWorld.setGeometry(QRect(10, 480, 271, 41))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(13)
        self.JoinWorld.setFont(font1)
        self.setings = QPushButton(self.centralwidget)
        self.setings.setObjectName(u"setings")
        self.setings.setGeometry(QRect(520, 10, 51, 41))
        icon = QIcon("asstes\\theme\\gui\\settings_icon.png")
        self.setings.setIcon(icon)
        self.setings.setIconSize(QSize(32, 32))
        self.DelteWorld = QPushButton(self.centralwidget)
        self.DelteWorld.setObjectName(u"DelteWorld")
        self.DelteWorld.setEnabled(False)
        self.DelteWorld.setGeometry(QRect(290, 480, 281, 41))
        self.DelteWorld.setFont(font1)
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"2DBox", None))
        self.label.setText(QCoreApplication.translate("StartWindow", langs[0], None))

        __sortingEnabled = self.worldList.isSortingEnabled()
        self.worldList.setSortingEnabled(False)
        # ___qlistwidgetitem = self.worldList.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("StartWindow", langs[2], None))
        self.worldList.setSortingEnabled(__sortingEnabled)

        self.JoinWorld.setText(QCoreApplication.translate("StartWindow", langs[1], None))
#if QT_CONFIG(tooltip)
        self.setings.setToolTip(QCoreApplication.translate("StartWindow", langs[3], None))
#endif // QT_CONFIG(tooltip)
        self.setings.setText("")
        self.DelteWorld.setText(QCoreApplication.translate("StartWindow", langs[4], None))
    # retranslateUi

class creaworldw(QMainWindow,object):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setMinimumSize(self.width(),self.height())
        self.setMaximumSize(self.width(),self.height())

        self.pushButton.clicked.connect(self.joiworld)
        self.pushButton_2.clicked.connect(self.close)

        self.show()

    def joiworld(self):
        global app,tw
        tw = self.worldnamel.text()
        self.hide()
        app = BOX3D(tw)
        app.run()
        self.close()

    def setupUi(self, creaworldw):
        if not creaworldw.objectName():
            creaworldw.setObjectName(u"creaworldw")
        creaworldw.resize(391, 154)
        self.centralwidget = QWidget(creaworldw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 361, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.worldnamel = QLineEdit(self.centralwidget)
        self.worldnamel.setObjectName(u"worldnamel")
        self.worldnamel.setGeometry(QRect(10, 60, 371, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.worldnamel.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 110, 91, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift")
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 110, 91, 31))
        self.pushButton_2.setFont(font2)
        creaworldw.setCentralWidget(self.centralwidget)

        self.retranslateUi(creaworldw)

        QMetaObject.connectSlotsByName(creaworldw)
    # setupUi

    def retranslateUi(self, creaworldw):
        creaworldw.setWindowTitle(QCoreApplication.translate("creaworldw", langs[2], None))
        self.worldnamel.setText(langs[12])
        self.label.setText(QCoreApplication.translate("creaworldw", langs[11], None))
        self.pushButton.setText(QCoreApplication.translate("creaworldw", langs[7], None))
        self.pushButton_2.setText(QCoreApplication.translate("creaworldw", langs[6], None))
    # retranslateUi

def update():
    if app.player.y < -10:
        app.player.y = 128
        app.player.x = 0
        app.player.z = 0

def eplinse(text,path):
    content = ""
    for s in text[::-1]:
        if s == '-':
            content += "-"
            continue
        elif s == '\n':
            content += "\n"
            continue
        content += chr(ord(s)-32)
    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

def readpass(path):
    with open(path,"r",encoding="utf-8") as f:
        text = f.read()
    content = ""
    for s in text[::-1]:
        if s == '-':
            content += "-"
            continue
        elif s == '\n':
            content += "\n"
            continue
        content += chr(ord(s)+32)
    # print(content)
    # with open("temp","w",encoding="utf-8") as f:
    #     f.write(content)
    return content

class Player_camera(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.wplist = ["stone","grass_block","leave","stone_bricks","smooth_stone","end_stone","amethyst_block","ice","iron_ore"]
        self.wpindex = 0
        self.head = Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\{self.wplist[self.wpindex]}.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5))

    def toDict(self):
        return {"wpindex":self.wpindex,"position":str(Vec3(self.x,128,self.z))}

    def input(self,key):
        super().input(key)
        # print(key,"player")
        if key in "123456789":
            self.wpindex = int(key)-1
            destroy(self.head)
            self.head = Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\{self.wplist[self.wpindex]}.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5))
            if (self.wplist[self.wpindex] == "door"):
                self.head.scale = Vec3(1/16,2,1)
        elif "scroll down" in key:
            self.wpindex +=1
            if self.wpindex>=9:
                self.wpindex = 0
            destroy(self.head)
            self.head = Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\{self.wplist[self.wpindex]}.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5))
            if (self.wplist[self.wpindex] == "door"):
                self.head.scale = Vec3(1/16,2,1)
        elif "scroll up" in key:
            self.wpindex -=1
            if self.wpindex<=-1:
                self.wpindex = 8
            destroy(self.head)
            self.head = Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\{self.wplist[self.wpindex]}.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5))
            if (self.wplist[self.wpindex] == "door"):
                self.head.scale = Vec3(1/16,2,1)

class Box(Button):
    def __init__(self,_type:str,position,model="cube",_color=color.white,parent=scene,origin_y=0.5):
        super().__init__(model=model,color=_color,position=position,texture="asstes\\2DBox\\texture\\block\\"+_type+".png",parent=parent,origin_y=origin_y)
        if (_type=="door"):
            self.scale = Vec3(1/16,2,1)
            self.y += 1
        self._type = _type
        self.__position = position
        self.__model = model
        self.oy = origin_y
    
    def toDict(self):
        return {"type":self._type,"position":str(self.__position),"model":self.__model,"origin_y":self.oy}

class BOX3D(Ursina):
    def __init__(self, world):
        super().__init__()
        loga("Game Initing")
        self.blockData = []
        self.gk = ["bedrock","stone","stone","grass_block"]
        self.stat = 0
        self.wname = world
        self.tim = threading.Timer(20,self.save)
        self.tim.start()
        self.setup()

    def setup(self):
        global apps
        Sky()
        self.player = Player_camera()
        self.loadWorld(self.wname)
        self.player.spaces = 0
        # self.test = Text("666")
        # Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\stone.png",parent=camera.ui,rotation=(-45,20,-45),position=(0.5,0.1),scale=(0.2,0.2,0.2))
        try:
            apps.close()
        except:
            pass
    
    def loadWorld(self,world):
        try:
            texta = readpass(f"data\\world\\{world}.world").split("\n")
            self.player.position = Vec3(0,128,0)
            data = eval(texta[-1])
            for block in data:
                self.blockData.append(Box(block["type"],eval(block["position"]),model=block["model"],parent=scene,origin_y=0.5))
            try:
                playerdata = eval(texta[0])
                self.player.wpindex = playerdata["wpindex"]
                destroy(self.player.head)
                self.player.head = Entity(model="cube",texture=f"asstes\\2DBox\\texture\\block\\{self.player.wplist[self.player.wpindex]}.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5))
            except:
                self.save()
            
        except:
            self.CreateNewWorld()

    def CreateNewWorld(self):
        self.player.position = Vec3(0,128,0)
        for x in range(-8,8):
            for y in range(len(self.gk)):
                for z in range(-8,8):
                    self.blockData.append(Box(model="cube",_color=color.white,position=(x,y,z),_type=self.gk[y],parent=scene,origin_y=0.5))

    def quit(self):
        self.save()
        loga("game exit")
        self.tim.cancel()
        quit()

    def input(self,key):
        if ("shift" in key):
            self.player.speed = 1
        else:
            self.player.speed = 5
        if ("control" in key):
            self.player.speed = 7
        else:
            self.player.speed = 5
        super().input(key)
        if (key == "escape" and self.stat==0):
            self.player.on_disable()
            self.stat = 1
        elif (key == "escape" and self.stat==1):
            self.player.on_enable()
            self.stat = 0
        elif ("escape" in key and "shift" in key):
            self.quit()
        elif ("mouse1" in key and key != "mouse1 up"):
            for block in self.blockData:
                if block.hovered and block.position[0]-self.player.x<10 and block.position[1]-self.player.y<15 and block.position[2]-self.player.z<10 and block._type != "bedrock":
                    loga("delte block "+str(block))
                    self.blockData.remove(block)
                    destroy(block)
                    break
        elif ("mouse3" in key and key != "mouse3 up"):
            # Entity(model="cube",texture="asstes\\2DBox\\texture\\block\\stone.png",parent=camera.ui,rotation=(-35,-30,-5),position=(0.5,-0.6),scale=(0.5,0.5,0.5)).animate_rotation()
            for block in self.blockData:
                if block.hovered and block.position[0]-self.player.x<10 and block.position[1]-self.player.y<15 and block.position[2]-self.player.z<10:
                    self.blockData.append(Box(self.player.wplist[self.player.wpindex],position=block.position+mouse.normal,parent=scene,origin_y=0.5))
                    loga("new block "+str(block))
                    break
        elif  (key == "space hold"):
            self.player.jump()
    
    def save(self):
        loga("saving world")
        saveData = []
        for block in self.blockData:
            if block.position[1] < 128:
                data = block.toDict()
                saveData.append(data)
        eplinse(str(self.player.toDict())+"\n"+str(saveData),f"data\\world\\{self.wname}.world")
        loga("saved world")
        self.tim.cancel()
        self.tim = threading.Timer(20,self.save)
        self.tim.start()
    
if __name__ == "__main__":
    apps = QApplication(sys.argv)
    startwindow = StartWindow()
    sys.exit(apps.exec_())
    