import PyPDF2
import sys

def rotate_pdf(input_file, output_file):
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

if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    print(f"Rotating file {input_file_name} and saving as {output_file_name}")
    rotate_pdf(input_file_name, output_file_name)