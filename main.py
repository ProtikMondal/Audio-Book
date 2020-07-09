import pyttsx3
import PyPDF2

harryPotter = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(harryPotter)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()
