from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def pdf_page_appender(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    # pdf_writer.write(self, the stored pages of the pdfs get written into this file mention in brackets) differs
    # from out.write(the thing you want to write in this file)
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    pass


def page_appender():
    folder_name = input("Copy the path where all your pdfs are stored in and past it here: ")
    output_name = input("How do you want to call your merged pdf? ")

    # change directory to the folder where the pdfs are stored
    try:
        os.chdir(folder_name)
        all_docs = os.listdir()
        pdfs = [pdf for pdf in all_docs if pdf.endswith('.pdf')]
        pdfs.sort()
        print(pdfs)
        pdf_page_appender(pdfs, f'{output_name}.pdf')
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except OSError as oe:
        print(oe)
    pass


def pdf_page_inserter(output_name, **kwargs):
    pass


def page_inserter():
    folder_name = input("Folder path to your files: ")
    output_name = input("Name of Output File: ")

    try:
        os.chdir(folder_name)
        all_docs = os.listdir()
        pdfs = [pdf for pdf in all_docs if pdf.endswith('.pdf')]

    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except OSError as oe:
        print(oe)
    pass


if __name__ == '__main__':
    choice = input("Do you want to append pages (type a) or do you want to insert pages at specific locations in a "
                   "pdf (type b)?")
    if choice == "a":
        page_appender()
    elif choice == "b":
        page_inserter()
    else:
        print("Error. Your input matches no option.")