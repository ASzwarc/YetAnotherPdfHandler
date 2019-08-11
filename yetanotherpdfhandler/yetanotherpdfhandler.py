import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate(input_file, output_file):
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(input_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        if page_num % 2:
            page.rotateClockwise(180)
        else:
            page.rotateCounterClockwise(180)
        pdf_writer.addPage(page)
    
    with open(output_file, 'wb') as file_output:
        pdf_writer.write(file_output)

def merge(paths, output_file_name):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        pdf_writer.appendPagesFromReader(pdf_reader)
    
        with open(output_file_name, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("merge", help="merge pdfs into one with default name 'merged.pdf'")
    parser.add_argument("rotate", help="rotates provided file and saves it with default name 'rotated.pdf'")
    parser.parse_args()