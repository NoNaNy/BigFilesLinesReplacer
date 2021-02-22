import subprocess
import os

rootPath=os.path.dirname(__file__)

def SedLineNumber(lineNumber, fileName):
    print('--== SED ==--')
    result = subprocess.run([f'{rootPath}\\bin\\sed','-n', f'\'{lineNumber},{lineNumber}p\'', fileName], stdout=subprocess.PIPE)
    textLine = result.stdout.decode('utf-8')
    linesSed=textLine.splitlines()
    # print(linesSed)
    return linesSed

def SedReplaceLine(numLine, strLine, fileName):
    #NOTE: For NewFile is necessary change command wiht -i parameter and add new fileName and save buffer in it
    print('--== SED REP ==--')
    command=f'{numLine}s/.*/{strLine}/'
    # print(command)
    args=[]
    args.append(f"{rootPath}\\bin\sed")
    args.append("-i")
    args.append(command)
    args.append(fileName)
    # result = subprocess.run(['sed', command, fileName], stdout=subprocess.PIPE)
    result = subprocess.run(args, stdout=subprocess.PIPE)
    
    textLine = result.stdout.decode('utf-8')
    print(textLine)

if __name__ == '__main__':
    # ret = SedLineNumber(4,'D:/Downloads/demo_sed.txt')    
    SedReplaceLine(21,"--==DATO REEMPLAZADO==--",'D:\\Downloads\\demo_sed.txt')