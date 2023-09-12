# --- PDF MERGER ---
# 1. Place files that  you wish to merge into this folder.
# 2. Use merger.append() to combine each document or section of pages from a document.
# 3. Name the new document in merger.write("new-doc.pdf")
# 4. Run document.

from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("test1.pdf", pages=(0,7,1))
merger.append("test2.pdf")
merger.append("test3.pdf", pages=(8,10,1))

merger.write("test-combo1-3.pdf")
merger.close()