from pathlib import Path
import PyPDF2
pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("pages _ ",pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print("page zero",pageObj.extractText())
pdfFileObj.close()
# pdf_path = (Path.home()/ "creating-and-modifying-pdfs"/ "practice_files"/ "Pride_and_Prejudice.pdf")