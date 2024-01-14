import fitz  # PyMuPDF

path = "TEMAY2022result.pdf"
output_file = "temp.txt"

pdf_document = fitz.open(path)

all_text = ""

for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    all_text += page.get_text()

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_text)

print("DONE...!")

pdf_document.close()
