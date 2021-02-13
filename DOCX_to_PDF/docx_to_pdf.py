# Usage
# python3 docx_to_pdf YOUR_DOCUMENT.docx YOUR_EXPORT_PDF.pdf
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

word_to_pdf(sys.argv[1], sys.argv[2])

