#!/usr/bin/python

'''
    QuIR: Quick Image Resize. This file was created to quickly resize images,
    since the author had to resize a lot of selected images. Very simple
    interface with minimal features.

    Framework adopted from Zetcode example on drag drop interface.
'''

import wx
import Image

XDIM = 320
YDIM = 240

class FileDrop(wx.FileDropTarget):
    def __init__(self, window, xdim, ydim):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.xdim = xdim
        self.ydim = ydim

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:
            try:
                self.window.Clear()
                self.window.WriteText('Loaded file')    # A little indication

                # Extract the values from the height and width field
                try:
                    xdim_val = int(self.xdim.GetValue().strip())
                    ydim_val = int(self.ydim.GetValue().strip())
                    
                    error = None
                except ValueError:
                    dlg=wx.MessageDialog(None, 'Please enter height and width.')
                    dlg.ShowModal()
                    error = True
                    
                if not error:
                    # Open the image file.
                    im = Image.open(name)
                    # Resize the image
                    im = im.resize((xdim_val, ydim_val), resample = 1)
                    # Save the image
                    im.save('resized_'+name.split('/')[-1])
                    
                    # Indication again
                    self.window.Clear()
                    self.window.WriteText('Image resized')
            except IOError, error:
                dlg = wx.MessageDialog(None,
                                       'Error opening file\n' + str(error))
                dlg.ShowModal()

class DropFile(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 200))
        self.panel = wx.Panel(self)

        self.xdim_field = wx.TextCtrl(self.panel, -1, size = (80,30))
                                    # Field for entering height
        self.ydim_field = wx.TextCtrl(self.panel, -1, size = (80,30))
                                    # Field for entering width

        # Set default values
        self.xdim_field.SetValue('640')
        self.ydim_field.SetValue('480')
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)   # Main sizer
        self.field_sizer = wx.BoxSizer(wx.HORIZONTAL)   # Sizer for data
        self.drop_sizer = wx.BoxSizer(wx.HORIZONTAL)     # Sizer for dropping
        
        self.h_box = wx.StaticBox(self.panel, label='Height')
        self.w_box = wx.StaticBox(self.panel, label='Width')
        
        self.h_sizer = wx.StaticBoxSizer(self.h_box, orient=wx.HORIZONTAL)
        self.w_sizer = wx.StaticBoxSizer(self.w_box, orient=wx.HORIZONTAL)

        self.h_sizer.Add(self.xdim_field, wx.ALL, 5)
        self.w_sizer.Add(self.ydim_field, wx.ALL, 5)
        
        self.field_sizer.Add(self.h_sizer)
        self.field_sizer.Add(self.w_sizer)
        
        self.text = wx.TextCtrl(self.panel, -1, size=(200, 200),
                                style = wx.TE_MULTILINE)
        # Add a little help
        help_txt = 'QuIR: Quick Image Resize.\n Set the height and width\
 and drop the image into this area and voila! your image is resized.'
        self.text.SetValue(help_txt)

        self.drop_sizer.Add(self.text)
        self.sizer.Add(self.field_sizer)
        self.sizer.Add(self.drop_sizer)
        
        dt = FileDrop(self.text, self.xdim_field, self.ydim_field)
        self.text.SetDropTarget(dt)

        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.Centre()
        self.Show(True)


app = wx.App()
DropFile(None, -1, 'QuIR')
app.MainLoop()
