import subprocess
import os

rootPath=os.path.dirname(__file__)

def SedLineNumber(lineNumber, fileName):
    print('--== SED ==--')
    fullCommand=f"{rootPath}\\bin\\sed -n '{lineNumber},{lineNumber}p' {fileName}"
    print(fullCommand)
    result = subprocess.run(fullCommand, stdout=subprocess.PIPE)
    textLine = result.stdout.decode('utf-8')
    # print(textLine)
    linesSed=textLine.splitlines()
    return linesSed

def SedReplaceLine(numLine, strLine, fileName):
    #NOTE: For NewFile is necessary change command wiht -i parameter and add new fileName and save buffer in it
    print('--== SED REP ==--')
    command=f'{numLine}s/.*/{strLine}/'
    print(command)
    fullCommand=f"{rootPath}\\bin\\sed -i '{command}' {fileName}"
    print(fullCommand)
    result = subprocess.run(fullCommand, stdout=subprocess.PIPE)
    
    textLine = result.stdout.decode('utf-8')
    print(textLine)

if __name__ == '__main__':
    pass
    # ret = SedLineNumber(4,'D:/Downloads/demo_sed.txt')    
    # ret = SedLineNumber(7004515,'D:/Downloads/2020_241_Ordenes_20200828.txt')    
    # dato="--==DATO REEMPLAZADO==--"
    # SedReplaceLine(21,dato,'D:\\Downloads\\demo_sed.txt')
    # dato="305;VIRTU USA LLC;0;0;XEXX010101000;0;8;3;0;840;E0150;403;419588;702;601;484;20200827;142510478;20200827;142510478;2203541814965;20200827;142510473;102;103;101;403;1;100;54.37;R;A;1;104;142526529;0;102;ROBERTO ARELLANO DE LA GARZA;20002;2537108;025019;1;309"
    # SedReplaceLine(21,dato,'D:\\Downloads\\demo_sed.txt')