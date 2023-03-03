"""
GOAL: Create a Basic Image Viewer App

- We will need to crete Frame
- Will need to create Panel
- Need to add Text and Widgets on it
- Need to Bind Button with Event to open the images
- Need to browse image
- Need to show image when selected or file path is typed



How to Run
install wxpython
run the script
"""


import wx


class ImageViewer(wx.App):
    def __init__(self, size):
        wx.App.__init__(self, size)
        self.frame = wx.Frame(None, wx.ID_ANY, 'Image Viewer', (50,50), size)
        self.panel = wx.Panel(self.frame, wx.ID_ANY, size= (250,250))
        self.img_control = wx.StaticBitmap(self.panel)
        self.photoTxt = wx.TextCtrl(self.panel, pos=(0, 250))

        self.frame.Show()
        self.runapp()


    def add_text(self, **kwargs):
         wx.StaticText(self.panel, **kwargs)

    @staticmethod
    def bindevent(obj, func):
         obj.Bind(wx.EVT_BUTTON, func)

    def browsefile(self, event):

        wildcard = "Image files (*.jpg;*.png)|*.jpg;*.png"
        
        dialog = wx.FileDialog(None, "Choose an image", wildcard=wildcard, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.photoTxt.SetValue(path)
            self.handleview()
        dialog.Destroy()

    def searchfile(self, event):
        self.handleview()

    

    def handleview(self):
        path= self.photoTxt.GetValue()
        max_size = [200,200]
        image = wx.Image(path, wx.BITMAP_TYPE_ANY)
        image.Rescale(max_size[0], max_size[1], quality=wx.IMAGE_QUALITY_HIGH)
        self.img_control.SetBitmap(wx.Bitmap(image))
        self.panel.Refresh()

    # def searchfile(self):

        
    
    def runapp(self):
        self.add_text(label ='Image Viewer')
        button = wx.Button(self.panel, label="Browse", pos=(250, 250))
        view_button = wx.Button(self.panel, label= 'View', pos= (160, 250) )
        self.bindevent(button, self.browsefile)
        self.bindevent(view_button, self.searchfile)



if __name__ == '__main__': 
    app = ImageViewer(size= (350,350))
    app.MainLoop()