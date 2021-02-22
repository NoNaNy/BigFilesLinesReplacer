#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 20, 2021 07:32:48 PM CST  platform: Windows NT
#    Feb 20, 2021 07:56:59 PM CST  platform: Windows NT
#    Feb 20, 2021 08:13:59 PM CST  platform: Windows NT
#    Feb 20, 2021 10:11:19 PM CST  platform: Windows NT
#    Feb 20, 2021 10:32:00 PM CST  platform: Windows NT
#    Feb 20, 2021 11:44:35 PM CST  platform: Windows NT
#    Feb 21, 2021 01:03:57 AM CST  platform: Windows NT
#    Feb 21, 2021 11:06:48 PM CST  platform: Windows NT

import time
import os
from tkinter.constants import DISABLED, NORMAL
import Grep
import Sed

from tkinter import filedialog

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

newLineText="--==NUEVA LINEA DE REEMPLAZO==--"
searchOptionString = "LineNumber"

def set_Tk_var():
    global valLblMessages
    valLblMessages = tk.StringVar()
    # valLblMessages.set('')

    global valTxtReplaceLine
    valTxtReplaceLine = tk.StringVar(value=newLineText)
    global valLblErrors
    valLblErrors = tk.StringVar()
    global resultList
    resultList=[]
    global valLstLines
    valLstLines = tk.StringVar(value=resultList)
    global valFileName
    valFileName = tk.StringVar(value='<= Abrir')
    global valTxtLineNumber
    valTxtLineNumber = tk.IntVar(value=1)
    global valTxtLineContent
    valTxtLineContent = tk.StringVar()
    
    global searchOption
    searchOption = tk.StringVar(value=searchOptionString)
    global isSetFileName
    isSetFileName = False

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    w.scrlListBox.bind("<<ListboxSelect>>", ListBox_SelectionChange, add=True)
    root.iconbitmap(f"{os.path.dirname(__file__)}\\editor.ico")

def ValidateLineNumber():
    if(searchOption.get() == "Content"):
        return

    print("Validating...")
    if(valTxtLineNumber.get()<=0 ):
        valLblErrors.set("Número de línea incorrecto.")
    else:
        valLblErrors.set("")
        
def ClearValues():
    print("Clearing...")
    resultList.clear()
    valLstLines.set(resultList)
    valTxtReplaceLine.set(newLineText)

def SearchRadioButton_Selected():
    global searchOptionString
    optionSelected = searchOption.get()

    if(searchOptionString!=optionSelected):
        searchOptionString=optionSelected
        ClearValues()

    if(optionSelected == "Content"):
        # print("Content")
        w.scrlListBox.configure(state='normal')
        w.txtLineNumber.configure(state='disabled')
        w.txtLineContent.configure(state='normal')
    else:
        # print("LineNumber")
        w.scrlListBox.configure(state='disabled')
        w.txtLineNumber.configure(state='normal')
        w.txtLineContent.configure(state='disabled')

def BtnOpenFile_Click():
    global isSetFileName
    fileName=filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files", "*.txt*"),
                                                       ("all files", "*.*")))
    if(not fileName):
        valLblErrors.set("No se especificó un archivo!")
        return

    fileUri=os.path.abspath(fileName)
    valFileName.set(fileUri)
    valLblErrors.set("")
    isSetFileName = True

def SetValuesToReplaceFields(textLine, lineNumber):
    valTxtReplaceLine.set(textLine)
    w.frmReplace.configure(text=f'Modificar línea [{lineNumber:,}]:')

def SearchButton_Click():
    global resultList
    print("Searching...")
    w.btnSearch.configure(state=DISABLED)
    if(isSetFileName):
        valLblErrors.set('')
        valLblMessages.set('Buscando...')
        root.update()
        swIni=time.perf_counter()
        if(searchOption.get() == "Content"):
            resLines=Grep.GrepByPattern(valTxtLineContent.get(),valFileName.get())
        else:
            resLines=Sed.SedLineNumber(valTxtLineNumber.get(),valFileName.get())
        swEnd=time.perf_counter()
    else: 
        valLblErrors.set("No se ha especificado un archivo...")
        w.btnSearch.configure(state=NORMAL)
        return

    print(f"Total time: {swEnd-swIni:0.4f} seconds")

    if(len(resLines)==0):
        valLblErrors.set('Sin resultados!')

    resultList=resLines
    valLstLines.set(resultList)
    valLblMessages.set('')
    w.btnSearch.configure(state=NORMAL)

    if(searchOption.get() == "LineNumber"):
        if(len(resultList)==1):
            SetValuesToReplaceFields(resultList[0],valTxtLineNumber.get())

def ListBox_SelectionChange(selection):
    global resultList

    indexList = w.scrlListBox.curselection(); 
    print(f"SelectionChange... {indexList}")       

    if(len(indexList)==0):
        return    

    textLine = resultList[indexList[0]]

    textSplit = textLine.split(':')
    valTxtLineNumber.set(int(textSplit[0]))
    SetValuesToReplaceFields(textSplit[1], valTxtLineNumber.get())

def ReplaceButton_Click():
    if(not valTxtReplaceLine.get()):
        valLblErrors.set('La línea de reemplazo esta vacía!')
        return
    
    w.btnReplace.configure(state=DISABLED)
    valLblMessages.set('Reemplazando...')
    root.update()
    swIni=time.perf_counter()
    Sed.SedReplaceLine(valTxtLineNumber.get(),valTxtReplaceLine.get(), valFileName.get())
    swEnd=time.perf_counter()
    print(f"Total time: {swEnd-swIni:0.4f} seconds")
    valLblMessages.set('¡Listo!')
    if(searchOption.get()=="LineNumber"):
        ClearValues()
    else:
        valTxtReplaceLine.set('')
    w.btnReplace.configure(state=NORMAL)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import EditorWindow
    EditorWindow.vp_start_gui()





