import subprocess
import os

rootPath=os.path.dirname(__file__)

def GrepByPattern(pattern, fileName):
    print('--== GREP ==--')
    result = subprocess.run([f'{rootPath}\\bin\\grep','-n', f'\'{pattern}\'', fileName], stdout=subprocess.PIPE)
    textLine = result.stdout.decode('utf-8')
    # print(textLine)
    linesGrep=textLine.splitlines()
    # print(len(linesGrep))

    return linesGrep
    # lineNumber = textLine[0:textLine.find(':')]
    # lines = textLine.split(':')

    # print(lineNumber)
    # print(lines[0])



if __name__ == '__main__':
    # ret = GrepByPattern('092534868',"D:\Downloads\demo_sed.txt")
    # ret = GrepByPattern('084044388',"D:\Downloads\demo_sed.txt")
    ret = GrepByPattern('084044388','D:/Downloads/demo_sed.txt')