# Usage
# python3 docx_to_pdf.pdf path_to_folder_with_word_doc
import sys
import os
import comtypes.client

def word_to_pdf(_in, _out):
    pdf_format_key = 17
    file_in = os.path.abspath(_in)
    file_out = os.path.abspath(_out)
    worddoc = comtypes.client.CreateObject( 'Word.Application' )
    doc = worddoc.Documents.Open(file_in)
    doc.SaveAs( file_out, FileFormat = pdf_format_key )
    doc.Close()
    worddoc.Quit()

destination = sys.argv[1]
for file in os.listdir(destination):
    word_to_pdf(destination + "\\" + file, destination + "\\" + file + ".pdf")

