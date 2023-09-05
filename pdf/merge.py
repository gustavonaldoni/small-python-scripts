import PyPDF2

file1 = './1.pdf'
file2 = './2.pdf'

def merge_pdf(file1: str, file2: str, final_file: str) -> bool:
    pdf_merger = PyPDF2.PdfMerger()

    file1 = open(file1, 'rb')
    pdf1 = PyPDF2.PdfReader(file1)

    file2 = open(file2, 'rb')
    pdf2 = PyPDF2.PdfReader(file2)

    pdf_merger.append(pdf1)
    pdf_merger.append(pdf2)

    file1.close()
    file2.close()

    pdf_merger.write(final_file)

if __name__ == '__main__':
    file1 = input("Escreva o nome do primeiro arquivo PDF: ")
    file2 = input("Escreva o nome do segundo arquivo PDF: ")

    final = input("Escreva o nome do arquivo final: ")

    try:
        merge_pdf(file1, file2, final)
    except Exception as e:
        print('Burro. Algo deu errado!')
        print(e)