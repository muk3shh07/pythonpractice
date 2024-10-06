import pypdf2
a = pypdf2.PdfFileReader('pdfExtract/THE 48 LAWS OF POWER - Robert Greene.pdf')
print(a.documentInfo)