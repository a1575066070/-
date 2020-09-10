import wx
import time

class GuaJiApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None, title = "guajiguaji",
                         size = (520,450),pos = (800,300))
        
        panel = wx.Panel(frame, -1)
        labelAll = wx.StaticText(panel,-1,'All Contents',pos = (210,5))
        self.textAll = wx.TextCtrl(panel,-1,size = (480,200),
                                   pos = (10,30),
                                   style = wx.TE_READONLY | wx.TE_MULTILINE)
        
        labelIn = wx.StaticText(panel,-1,'I say',pos = (230,230))
        self.textIn = wx.TextCtrl(panel, -1,size = (480,100),pos = (10,260),
                                  style = wx.TE_MULTILINE)
        
        self.buttonSend = wx.Button(panel,-1,"Send",
                                    size = (75,25),pos = (175,370))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSend, self.buttonSend)
        self.buttonCts = wx.Button(panel,-1,"Cts",
                                    size = (75,25),pos = (260,370))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCts, self.buttonCts)
        frame.Show()
        return True
    
def OnButtonSend(self,event):
    userinput = self.textin.GetValue()
    self.textIn.CTS()
    nowtime = time.ctime()
    inmsg = "You(%s):\n%s \n" %(nowtime,userinput)
    self.textAll.AppendText(inmsg)
def OnButtonCts(self,event):
    self.textAll.Cts()
      
    
if __name__ == "__main__":
    app = GuaJiApp()
    app.MainLoop()
    