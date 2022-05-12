import os.path

from utils.function import *

if __name__ == '__main__':

    code = getFunctFromFile(os.path.dirname(os.path.abspath(__file__)))

    codeArray = createCodeAndSummarize(code)
    print(codeArray)
