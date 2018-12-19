mport PyPDF2
 
PDFfilename = "/home/guibax/Documents/Documents/IAC/Essential_Oil_Components_Ebook.pdf" 
 
pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
pg65 = pfr.getPage(65) #extract pg 2
writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
#add pages
writer.addPage(pg65)
#filename of your PDF/directory where you want your new PDF to be
NewPDFfilename = "/home;guibax/test.pdf" 
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
writer.write(outputStream) #write pages to new PDF
