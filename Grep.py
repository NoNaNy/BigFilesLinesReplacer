import subprocess
import os

rootPath=os.path.dirname(__file__)

def GrepByPattern(pattern, fileName):
    print('--== GREP ==--')
    
    fullCommand = f"{rootPath}\\bin\\grep -n '{pattern}' {fileName}"
    print(fullCommand)

    #MODE 1
    result = subprocess.run(fullCommand, stdout=subprocess.PIPE)
    textLine = result.stdout.decode('utf-8')
    #******************

    # print(textLine)
    linesGrep=textLine.splitlines()
    print(f"Found: {len(linesGrep)} lines")

    return linesGrep


if __name__ == '__main__':
    pass
    # ret = GrepByPattern('092534868',"D:\Downloads\demo_sed.txt")
    # ret = GrepByPattern('084044388',"D:\Downloads\demo_sed.txt")
    # ret = GrepByPattern('084044388','D:/Downloads/demo_sed.txt')
    # ret = GrepByPattern('VIRTU USA','D:/Downloads/2020_241_Ordenes_20200828.txt')