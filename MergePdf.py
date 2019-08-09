from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output_file_name):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        pdf_writer.appendPagesFromReader(pdf_reader)
    
        with open(output_file_name, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == '__main__':
    directory = ''
    filenames = []
    paths = [directory + '\\' + filename for filename in filenames]

    merge_pdfs(paths, directory + '\\' + '')