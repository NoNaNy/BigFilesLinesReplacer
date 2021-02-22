#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 21, 2021 11:09:57 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import EditorWindow_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    
    EditorWindow_support.set_Tk_var()
    top = MainWindow (root)
    EditorWindow_support.init(root, top)
    root.mainloop()

w = None
def create_MainWindow(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_MainWindow(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    EditorWindow_support.set_Tk_var()
    top = MainWindow (w)
    EditorWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MainWindow():
    global w
    w.destroy()
    w = None

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x600+288+143")
        top.minsize(120, 1)
        top.maxsize(600, 1422)
        top.resizable(1,  1)
        top.title("Editor de líneas de reporte")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(takefocus="1")

        self.btnReplace = tk.Button(top)
        self.btnReplace.place(relx=0.383, rely=0.9, height=38, width=118)
        self.btnReplace.configure(activebackground="#ececec")
        self.btnReplace.configure(activeforeground="#000000")
        self.btnReplace.configure(background="#d9d9d9")
        self.btnReplace.configure(command=EditorWindow_support.ReplaceButton_Click)
        self.btnReplace.configure(disabledforeground="#a3a3a3")
        self.btnReplace.configure(foreground="#000000")
        self.btnReplace.configure(highlightbackground="#d9d9d9")
        self.btnReplace.configure(highlightcolor="black")
        self.btnReplace.configure(pady="0")
        self.btnReplace.configure(text='''Reemplazar''')

        self.frmSearch = tk.LabelFrame(top)
        self.frmSearch.place(relx=0.017, rely=0.122, relheight=0.268
                , relwidth=0.967)
        self.frmSearch.configure(relief='groove')
        self.frmSearch.configure(foreground="black")
        self.frmSearch.configure(text='''Buscar:''')
        self.frmSearch.configure(background="#d9d9d9")
        self.frmSearch.configure(highlightbackground="#d9d9d9")
        self.frmSearch.configure(highlightcolor="black")

        self.rdbLineNumber = tk.Radiobutton(self.frmSearch)
        self.rdbLineNumber.place(relx=0.017, rely=0.112, relheight=0.161
                , relwidth=0.297, bordermode='ignore')
        self.rdbLineNumber.configure(activebackground="#ececec")
        self.rdbLineNumber.configure(activeforeground="#000000")
        self.rdbLineNumber.configure(anchor='w')
        self.rdbLineNumber.configure(background="#d9d9d9")
        self.rdbLineNumber.configure(command=EditorWindow_support.SearchRadioButton_Selected)
        self.rdbLineNumber.configure(disabledforeground="#a3a3a3")
        self.rdbLineNumber.configure(foreground="#000000")
        self.rdbLineNumber.configure(highlightbackground="#d9d9d9")
        self.rdbLineNumber.configure(highlightcolor="black")
        self.rdbLineNumber.configure(justify='left')
        self.rdbLineNumber.configure(text='''Número de Línea''')
        self.rdbLineNumber.configure(value="LineNumber")
        self.rdbLineNumber.configure(variable=EditorWindow_support.searchOption)

        self.txtLineNumber = tk.Entry(self.frmSearch)
        self.txtLineNumber.place(relx=0.052, rely=0.323, height=21, relwidth=0.3
                , bordermode='ignore')
        self.txtLineNumber.configure(background="white")
        self.txtLineNumber.configure(disabledforeground="#a3a3a3")
        self.txtLineNumber.configure(font="TkFixedFont")
        self.txtLineNumber.configure(foreground="#000000")
        self.txtLineNumber.configure(highlightbackground="#d9d9d9")
        self.txtLineNumber.configure(highlightcolor="black")
        self.txtLineNumber.configure(insertbackground="black")
        self.txtLineNumber.configure(justify='center')
        self.txtLineNumber.configure(selectbackground="blue")
        self.txtLineNumber.configure(selectforeground="white")
        self.txtLineNumber.configure(textvariable=EditorWindow_support.valTxtLineNumber)
        self.txtLineNumber.configure(validate="focusout")
        ValidateLineNumber = self.txtLineNumber.register(EditorWindow_support.ValidateLineNumber)
        self.txtLineNumber.configure(validatecommand=(ValidateLineNumber))

        self.rdbLineContent = tk.Radiobutton(self.frmSearch)
        self.rdbLineContent.place(relx=0.017, rely=0.484, relheight=0.161
                , relwidth=0.297, bordermode='ignore')
        self.rdbLineContent.configure(activebackground="#ececec")
        self.rdbLineContent.configure(activeforeground="#000000")
        self.rdbLineContent.configure(anchor='w')
        self.rdbLineContent.configure(background="#d9d9d9")
        self.rdbLineContent.configure(command=EditorWindow_support.SearchRadioButton_Selected)
        self.rdbLineContent.configure(disabledforeground="#a3a3a3")
        self.rdbLineContent.configure(foreground="#000000")
        self.rdbLineContent.configure(highlightbackground="#d9d9d9")
        self.rdbLineContent.configure(highlightcolor="black")
        self.rdbLineContent.configure(justify='left')
        self.rdbLineContent.configure(text='''Contenido''')
        self.rdbLineContent.configure(value="Content")
        self.rdbLineContent.configure(variable=EditorWindow_support.searchOption)

        self.txtLineContent = tk.Entry(self.frmSearch)
        self.txtLineContent.place(relx=0.052, rely=0.665, height=21
                , relwidth=0.921, bordermode='ignore')
        self.txtLineContent.configure(background="white")
        self.txtLineContent.configure(disabledforeground="#a3a3a3")
        self.txtLineContent.configure(font="TkFixedFont")
        self.txtLineContent.configure(foreground="#000000")
        self.txtLineContent.configure(highlightbackground="#d9d9d9")
        self.txtLineContent.configure(highlightcolor="black")
        self.txtLineContent.configure(insertbackground="black")
        self.txtLineContent.configure(selectbackground="blue")
        self.txtLineContent.configure(selectforeground="white")
        self.txtLineContent.configure(state='disabled')
        self.txtLineContent.configure(textvariable=EditorWindow_support.valTxtLineContent)

        self.btnSearch = tk.Button(self.frmSearch)
        self.btnSearch.place(relx=0.81, rely=0.273, height=48, width=88
                , bordermode='ignore')
        self.btnSearch.configure(activebackground="#ececec")
        self.btnSearch.configure(activeforeground="#000000")
        self.btnSearch.configure(background="#d9d9d9")
        self.btnSearch.configure(command=EditorWindow_support.SearchButton_Click)
        self.btnSearch.configure(disabledforeground="#a3a3a3")
        self.btnSearch.configure(foreground="#000000")
        self.btnSearch.configure(highlightbackground="#d9d9d9")
        self.btnSearch.configure(highlightcolor="black")
        self.btnSearch.configure(pady="0")
        self.btnSearch.configure(text='''Buscar''')

        self.lblErrors = tk.Label(self.frmSearch)
        self.lblErrors.place(relx=0.379, rely=0.248, height=29, width=237
                , bordermode='ignore')
        self.lblErrors.configure(activebackground="#f9f9f9")
        self.lblErrors.configure(activeforeground="black")
        self.lblErrors.configure(background="#d9d9d9")
        self.lblErrors.configure(disabledforeground="#a3a3a3")
        self.lblErrors.configure(foreground="#ff0000")
        self.lblErrors.configure(highlightbackground="#d9d9d9")
        self.lblErrors.configure(highlightcolor="black")
        self.lblErrors.configure(textvariable=EditorWindow_support.valLblErrors)

        self.lblMessages = tk.Label(self.frmSearch)
        self.lblMessages.place(relx=0.362, rely=0.497, height=23, width=247
                , bordermode='ignore')
        self.lblMessages.configure(background="#d9d9d9")
        self.lblMessages.configure(disabledforeground="#a3a3a3")
        self.lblMessages.configure(foreground="#0000ff")
        self.lblMessages.configure(text='''Label''')
        self.lblMessages.configure(textvariable=EditorWindow_support.valLblMessages)

        self.frmResult = tk.LabelFrame(top)
        self.frmResult.place(relx=0.017, rely=0.4, relheight=0.368
                , relwidth=0.967)
        self.frmResult.configure(relief='groove')
        self.frmResult.configure(foreground="black")
        self.frmResult.configure(text='''Resultados:''')
        self.frmResult.configure(background="#d9d9d9")
        self.frmResult.configure(highlightbackground="#d9d9d9")
        self.frmResult.configure(highlightcolor="black")

        self.scrlListBox = ScrolledListBox(self.frmResult)
        self.scrlListBox.place(relx=0.017, rely=0.136, relheight=0.805
                , relwidth=0.967, bordermode='ignore')
        self.scrlListBox.configure(background="white")
        self.scrlListBox.configure(cursor="xterm")
        self.scrlListBox.configure(disabledforeground="#a3a3a3")
        self.scrlListBox.configure(font="TkFixedFont")
        self.scrlListBox.configure(foreground="black")
        self.scrlListBox.configure(highlightbackground="#d9d9d9")
        self.scrlListBox.configure(highlightcolor="#d9d9d9")
        self.scrlListBox.configure(selectbackground="#e1f0ff")
        self.scrlListBox.configure(selectforeground="white")
        self.scrlListBox.configure(selectmode='single')
        self.scrlListBox.configure(state='disabled')
        self.scrlListBox.configure(listvariable=EditorWindow_support.valLstLines)

        self.frmReplace = tk.LabelFrame(top)
        self.frmReplace.place(relx=0.017, rely=0.78, relheight=0.103
                , relwidth=0.967)
        self.frmReplace.configure(relief='groove')
        self.frmReplace.configure(foreground="black")
        self.frmReplace.configure(text='''Reempazar:''')
        self.frmReplace.configure(background="#d9d9d9")
        self.frmReplace.configure(highlightbackground="#d9d9d9")
        self.frmReplace.configure(highlightcolor="black")

        self.txtReplace = tk.Entry(self.frmReplace)
        self.txtReplace.place(relx=0.017, rely=0.419, height=21, relwidth=0.955
                , bordermode='ignore')
        self.txtReplace.configure(background="white")
        self.txtReplace.configure(disabledforeground="#a3a3a3")
        self.txtReplace.configure(font="TkFixedFont")
        self.txtReplace.configure(foreground="#000000")
        self.txtReplace.configure(highlightbackground="#d9d9d9")
        self.txtReplace.configure(highlightcolor="black")
        self.txtReplace.configure(insertbackground="black")
        self.txtReplace.configure(selectbackground="blue")
        self.txtReplace.configure(selectforeground="white")
        self.txtReplace.configure(textvariable=EditorWindow_support.valTxtReplaceLine)

        self.frmFile = tk.LabelFrame(top)
        self.frmFile.place(relx=0.017, rely=0.0, relheight=0.108, relwidth=0.967)

        self.frmFile.configure(relief='groove')
        self.frmFile.configure(foreground="black")
        self.frmFile.configure(text='''Archivo:''')
        self.frmFile.configure(background="#d9d9d9")
        self.frmFile.configure(highlightbackground="#d9d9d9")
        self.frmFile.configure(highlightcolor="black")

        self.lblFileName = tk.Label(self.frmFile)
        self.lblFileName.place(relx=0.19, rely=0.462, height=23, width=457
                , bordermode='ignore')
        self.lblFileName.configure(activebackground="#f9f9f9")
        self.lblFileName.configure(activeforeground="black")
        self.lblFileName.configure(anchor='w')
        self.lblFileName.configure(background="#d9d9d9")
        self.lblFileName.configure(disabledforeground="#a3a3a3")
        self.lblFileName.configure(foreground="#000000")
        self.lblFileName.configure(highlightbackground="#d9d9d9")
        self.lblFileName.configure(highlightcolor="black")
        self.lblFileName.configure(text='''<= Abrir archivo''')
        self.lblFileName.configure(textvariable=EditorWindow_support.valFileName)

        self.btnOpenFile = tk.Button(self.frmFile)
        self.btnOpenFile.place(relx=0.017, rely=0.462, height=28, width=68
                , bordermode='ignore')
        self.btnOpenFile.configure(activebackground="#ececec")
        self.btnOpenFile.configure(activeforeground="#000000")
        self.btnOpenFile.configure(background="#d9d9d9")
        self.btnOpenFile.configure(command=EditorWindow_support.BtnOpenFile_Click)
        self.btnOpenFile.configure(disabledforeground="#a3a3a3")
        self.btnOpenFile.configure(foreground="#000000")
        self.btnOpenFile.configure(highlightbackground="#d9d9d9")
        self.btnOpenFile.configure(highlightcolor="black")
        self.btnOpenFile.configure(pady="0")
        self.btnOpenFile.configure(text='''Archivo''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()




