import os.path

from utils.function import *
from PdfCreator import PDF

if __name__ == '__main__':
    code = getFunctFromFile(os.path.dirname(os.path.abspath(__file__)))
    codeArray = createCodeAndSummarize(code)

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for func in codeArray:
        pdf.add_function(func)
    pdf_path = os.path.dirname(__file__) + '/output/'
    pdf.save(os.path.dirname(pdf_path, "test"))
    print(os.listdir(os.path.dirname(__file__) + '/output'))

