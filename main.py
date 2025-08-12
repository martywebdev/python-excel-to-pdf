import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
pdf_path = Path("PDFs")
pdf_path.mkdir(parents=True, exist_ok=True)
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") #df is dataframe

    pdf = FPDF()
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")


    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Date.{date}")

    pdf.output(f"{pdf_path}/{filename}.pdf")
