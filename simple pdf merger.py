#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install pdfmerger


# In[ ]:


from pathlib import Path
from PyPDF2 import PdfMerger

print("""
⚠️  IMPORTANT NOTICE ⚠️
Please ensure all PDF files in the folder are named in the correct
alphabetical or numerical order before continuing.

Examples:
  ✔ 01.pdf, 02.pdf, 03.pdf
  ✔ A.pdf, B.pdf, C.pdf
  ✖ 1.pdf, 10.pdf, 2.pdf

Files will be merged in sorted order.
""")

# Ask for PDF folder
while True:
    pdf_folder = Path(input("Enter the folder path containing PDFs: ").strip())

    if pdf_folder.exists() and pdf_folder.is_dir():
        break
    else:
        print("❌ Invalid folder. Please try again.")

# Ask for output file name
output_name = input("Enter a name for the merged PDF (without .pdf): ").strip()

# Ensure .pdf extension
if not output_name.lower().endswith(".pdf"):
    output_name += ".pdf"

output_path = pdf_folder / output_name

merger = PdfMerger()

pdfs = sorted(pdf_folder.glob("*.pdf"))

if not pdfs:
    print("❌ No PDF files found in the folder.")
else:
    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

    print("\n✅ Merge complete!")
    print(f"📄 Merged PDF name : {output_name}")
    print(f"📁 Saved location  : {output_path.resolve()}")

