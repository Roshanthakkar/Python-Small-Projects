# pip install pyttsx3(python takes to speech version)
# also install in terminal (for pdf (pip install PyPDF2))
import pyttsx3
import PyPDF2

book = open('Unit-1_AdvOS_BCA-4.pdf ','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfReader.getPage(1)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()