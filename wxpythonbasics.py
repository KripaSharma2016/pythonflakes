'''
Created on Feb 1, 2017

@author: kripa
'''
import wx

def sayHello(event):
    print("yes button got pressed....")

app = wx.App()
win = wx.Frame(None, title="myAPP", size=(400,400))
panel = wx.Panel(win)
loadButton = wx.Button(panel, label='click', pos=(30,70))
loadButton.Bind(wx.EVT_BUTTON, sayHello)
win.Show()
app.MainLoop()
        