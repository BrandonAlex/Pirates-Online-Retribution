from direct.stdpy import threading, thread
import sys

defaultText = '''
print [(x.parentId, x.zoneIdList) for x in base.cr._interests.values()]
'''

def __inject_wx(_):
    code = textbox.GetValue()
    exec (code, globals())

def openInjector_wx():
    import wx

    app = wx.App(redirect = False)

    frame = wx.Frame(None, title = "POR Developer Python Injector Tool", size=(640, 400), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
    panel = wx.Panel(frame)
    button = wx.Button(parent = panel, id = -1, label = "Inject", size = (50, 20), pos = (295, 0))
    global textbox
    textbox = wx.TextCtrl(parent = panel, id = -1, pos = (20, 22), size = (600, 340), style = wx.TE_MULTILINE)
    frame.Bind(wx.EVT_BUTTON, __inject_wx, button)

    frame.Show()
    app.SetTopWindow(frame)

    textbox.AppendText(defaultText)

    threading.Thread(target = app.MainLoop).start()

def __inject_tk():
    global text
    exec (text.get(1.0, "end"),globals())

def openInjector_tk():
    import Tkinter as tk
    from direct.stdpy import thread
    root = tk.Tk()
    root.geometry('640x400')
    root.title('TLOPO Injector')
    root.resizable(False,False)
    global text
    frame = tk.Frame(root)
    text = tk.Text(frame,width=70,height=20)
    text.pack(side="left")
    tk.Button(root,text="Inject",command=__inject_tk).pack()
    scroll = tk.Scrollbar(frame)
    scroll.pack(fill="y",side="right")
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    frame.pack(fill="y")

    thread.start_new_thread(root.mainloop,())

if '-wx' in sys.argv:
    openInjector_wx()
elif '-tk' in sys.argv:
    openInjector_tk()

import pirates.piratesbase.PiratesStart
