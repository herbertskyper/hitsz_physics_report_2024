# -*encoding:gbk*-
from PyPDF2 import PdfReader, PdfWriter

# �г�����Ҫƴ�ӵ�PDF�ļ�
pdf_files = ['./pdf1.pdf','./pdf2.pdf']
pdf_writer = PdfWriter()

for pdf_file in pdf_files:
    # ��PDF�ļ�
    f = open(pdf_file, 'rb')
    pdf_reader = PdfReader(f)
    # ��ÿһҳ��ӵ�PdfFileWriter������
    if pdf_file==pdf_files[0]:
        for page_num in range(4):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    else:
        for page_num in range(1,len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# д�뵽һ���µ�PDF�ļ���
with open('./���ձ���/merged.pdf', 'wb') as out:
    pdf_writer.write(out)

