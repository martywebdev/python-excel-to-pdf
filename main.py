import pandas as pd
import glob
from fpdf import FPDF, XPos, YPos
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
pdf_path = Path("PDFs")
pdf_path.mkdir(parents=True, exist_ok=True)
for filepath in filepaths:

    pdf = FPDF()
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")


    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Invoice nr.{invoice_nr}")
    pdf.ln()  # Move to the next line

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Date.{date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")  # df is dataframe
    header = df.columns
    header = [col.replace("_", " ").title() for col in header]  # Format headers
    pdf.set_font("Times", "B", 10)
    pdf.set_text_color(80, 80, 80)

    for col in header:
        if col == "Product Name":
            pdf.cell(70, 8, col, border=1)
        else:
            pdf.cell(30, 8, col, border=1)
    pdf.ln()  # Move to the next line

    for index, row in df.iterrows():
        # print(row)
        pdf.set_font("Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(30, 8, str(row['product_id']), border=1)
        pdf.cell(70, 8, str(row['product_name']), border=1)
        pdf.cell(30, 8, str(row['amount_purchased']), border=1)
        pdf.cell(30, 8, str(row['price_per_unit']), border=1)
        pdf.cell(30, 8, str(row['total_price']), new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=1)

    #total sum of total_price
    pdf.set_font("Times", "B", 10)
    for col in header:
        if col == "Product Name":
            pdf.cell(70, 8, '', border=1)
        elif col == "Total Price":
            pdf.cell(30, 8, str(df['total_price'].sum()), border=1)
        else:
            pdf.cell(30, 8, '', border=1)
    pdf.ln()
    # add company name and logo
    pdf.set_font("Times", "B", 14)
    pdf.cell(30, 8, "Marty's Company", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.image("pythonhow.png", x=pdf.get_x(), y=pdf.get_y(), w=10)

    pdf.output(f"{pdf_path}/{filename}.pdf")
