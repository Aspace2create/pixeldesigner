functList=["""
if self.curtool=="FreeDrawTool101":
    self.draw=QPixmap(self.screensize[0],self.screensize[1])
    self.draw.fill(QColor("transparent"))
    self.activelydrawn=SimpleItm(qimage=Image.new("RGBA",(self.view.viewport().rect().width(),self.view.viewport().rect().height()),(0, 0, 0,0)).toqimage(),pos=QPoint(0,0),parent=self)
    self.activelydrawn.setZValue(self.activelydrawn.zValue()+1)
    self.graphicsItems.append(self.activelydrawn)
    self.scene.addItem(self.activelydrawn)
"""]
functList.append("""
if self.curtool=="FreeDrawTool101":
    if self.curdrag:
        painter = QPainter(self.draw)
        p = painter.pen()
        p.setWidth(2)
        p.setColor(QColor(self.color))
        painter.setPen(p)
        pos=self.view.mapToScene(event.pos())
        painter.drawPoint(pos)
        painter.end()
        self.activelydrawn.reshape(self.draw.toImage())
    else:
        self.activelydrawn.reshape(crop_transparent(Image.fromqimage(self.draw.toImage())).toqimage())
        self.activelydrawn.original_image=self.activelydrawn.qimage
        self.activelydrawn.setPos(self.activelydrawn.snapToGrid(self.view.mapToScene(self.originpoint)))
        self.activelydrawn=None
        


""")
functList.append("""

        
""")

newQaction=ToolAction(QIcon(self.returnICO("brush")), "brush Tool", parent=self,func="self.manipbox.hide()",override=True,funclst=functList ,name="FreeDrawTool101",source=("Default Tool","Version 0.0.1","Move Tool"))
newQaction.setCheckable(True)
self.DefaultTools.append(newQaction)
self.toolbar.addAction(newQaction)
self.toolbar.insertSeparator(newQaction)
self.group.addAction(newQaction)
