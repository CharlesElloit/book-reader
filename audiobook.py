import os
import sys
import PyPDF2
import pyttsx3
import docx2txt


# file or book you wish to listen to
bookOrFileToRead = "loveAndRespect.pdf"


# This function only handles PDF file
def readPDFBooks(book):
    # This fuction only read pdf book
    bookToRead = open(book, "rb")
    pdfReader = PyPDF2.PdfFileReader(bookToRead)

    # Here we are getting the number of pages and
    # initialing the speech to response back.
    bookPages = pdfReader.numPages
    read_book = pyttsx3.init()

    # This loop will go through all the pages
    # of the book and read it out for you :)
    for numOfPages in range(1, bookPages):
        singleBookPage = pdfReader.getPage(numOfPages)
        pageText = singleBookPage.extractText()
        read_book.say(pageText)
        read_book.runAndWait()


# This function only read word docs file
def readWord_DocsBooks(book):
    bookToRead = docx2txt.process(book)
    read_book = pyttsx3.init()

    read_book.say(bookToRead)
    read_book.runAndWait()


# This will extrack the file from the path where the file is located
with open(os.path.join(sys.path[0], bookOrFileToRead), "r") as f:
    filePath = f.name
    head, tial = os.path.split(filePath)

    # Extracking the file extension for the filename
    fileExtension = os.path.splitext(tial)[1].lower()

    if fileExtension == ".docs":
        readWord_DocsBooks(tial)

    elif fileExtension == ".pdf":
        readPDFBooks(tial)

    else:
        print("This file format is not supportrd")
