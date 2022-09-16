from distutils import extension
import pathlib
from excel_automation import process_workbook
from pathlib import Path

path = Path()
for file in path.glob('*.xlsx'):
    process_workbook(open(file, "r"))