# pip install PyPDF2

# FOR PIP UPDATE -- IN CASE
# python.exe -m pip install --upgrade pip


import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

page1 = pdf_reader.pages[0]
# print(page1)
print(page1.extract_text())