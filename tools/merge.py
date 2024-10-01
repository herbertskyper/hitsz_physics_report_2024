# -*encoding:gbk*-
from PyPDF2 import PdfReader, PdfWriter

# 列出你想要拼接的PDF文件
pdf_files = ['./pdf1.pdf','./pdf2.pdf']
pdf_writer = PdfWriter()

for pdf_file in pdf_files:
    # 打开PDF文件
    f = open(pdf_file, 'rb')
    pdf_reader = PdfReader(f)
    # 将每一页添加到PdfFileWriter对象中
    if pdf_file==pdf_files[0]:
        for page_num in range(4):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    else:
        for page_num in range(1,len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# 写入到一个新的PDF文件中
with open('./最终报告/merged.pdf', 'wb') as out:
    pdf_writer.write(out)

