#open dif seacher
import difflib
#open PDF
import PyPDF2
import re
#open Word

#file names
# ORIGINAL_WORD = 'FIBO_EM_1ANO_FGB_C1_QUI_CE_CAP2_EDIÇÃO_FINAL_VF_SEM_MARCAS.docx'
# P1_PDF = 'FIBO_EM_1ANO_FGB_C1_QUI_CE_CAP2_P1.pdf'
FILE_WORD = 'file_word.txt'
FILE_PDF = 'file_pdf.txt'
A = 'A.txt'
B = 'B.txt'

#opening files txt
with open(FILE_PDF, errors="ignore") as file_1:
    file_1_text = file_1.readlines()

with open(FILE_WORD, errors="ignore") as file_2:
    file_2_text = file_2.readlines()

# find differences:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt',
        tofile='file2.txt', lineterm=''):
    print(line)
