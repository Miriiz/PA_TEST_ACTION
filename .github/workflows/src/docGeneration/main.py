from utils.function import *

if __name__ == '__main__':
    print("path")
    print(os.path.dirname(__file__))
    code = getFunctFromFile(os.path.dirname(__file__))

    codeArray = createCodeAndSummarize(code)
    print(codeArray)
