import os
os.system('cls')
from PyPDF2 import PdfFileWriter, PdfFileReader

pdfwriter = PdfFileWriter()

pdf = PdfFileReader('packingslip.pdf') # Nome do arquivo antigo

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))

passw = 'tiago123' #Senha escolhida
pdfwriter.encrypt(passw)

with open("modificado.pdf", 'wb') as f: # Nome do arquivo novo
    pdfwriter.write(f)
    f.close()














