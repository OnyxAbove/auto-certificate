from pypdf import PdfReader, PdfWriter

def create_pdf(filename):
    writer = PdfWriter()
    writer.add_blank_page(215.9, 279.4)

    with open(filename, 'wb') as file:
        writer.write(file)

if __name__ == '__main__':
    create_pdf('ty.pdf')