import os.path

from utils.function import *

if __name__ == '__main__':

    code = getFunctFromFile(os.path.dirname(os.path.abspath(__file__)))

    codeArray = createCodeAndSummarize(code)
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for func in codeArray:
        pdf.cell(0, 10, func[0], 0, 1)
        pdf.cell(0, 10, func[1][0]['summary_text'], 0, 1)
    pdf.save("test")