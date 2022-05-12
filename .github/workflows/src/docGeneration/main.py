import os.path

from utils.function import *

if __name__ == '__main__':
    print("path")
    print(os.path.abspath(__file__))
    code = getFunctFromFile(os.path.dirname(os.path.abspath(__file__)))

    codeArray = createCodeAndSummarize(code)
    print(codeArray)
