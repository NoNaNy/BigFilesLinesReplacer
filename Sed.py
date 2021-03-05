import subprocess
import os

rootPath=os.path.dirname(__file__)

def SedLineNumber(lineNumber, fileName):
    print('--== SED ==--')
    fullCommand=f"{rootPath}\\bin\\sed -n '{lineNumber}p;{lineNumber}q' {fileName}"
    print(fullCommand)
    result = subprocess.run(fullCommand, stdout=subprocess.PIPE)
    textLine = result.stdout.decode('utf-8')
    print(textLine)
    linesSed=textLine.splitlines()
    print(f"Found: {len(linesSed)} lines")
    return linesSed

def SedReplaceLine(numLine, strLine, fileName):
    #NOTE: For NewFile is necessary change command wiht -i parameter and add new fileName and save buffer in it
    print('--== SED REP ==--')
    command=f'{numLine}s/.*/{strLine}/1'
    print(command)
    fullCommand=f"{rootPath}\\bin\\sed -i '{command}' {fileName}"
    print(fullCommand)
    result = subprocess.run(fullCommand, stdout=subprocess.PIPE)
    
    textLine = result.stdout.decode('utf-8')
    print(textLine)

if __name__ == '__main__':
    pass
    fileName="D:/Downloads/2021_49_Ordenes_20210218.txt"
    lineNumber=145598
    ret = SedLineNumber(lineNumber,fileName)
    # dato="305;LUIS;DE LA CRUZ;CARRILLO;NEW_VALUE;CUCL910101HDFRRS05;1;9;15;484;06600;402;AST24903;702;603;484;20210218;110130343;20210218;110130343;2210840075609;20210218;110130000;102;101;103;403;1;69000;4.8000;HOTEL;*;1;104;150001783;0;102;EDSON GABRIEL NAVARRO DE LA ROSA;42305;1556283;025019;16083;307"
    # SedReplaceLine(lineNumber,dato,fileName)
    # ret = SedLineNumber(lineNumber,fileName)
    