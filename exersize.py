import glob
from fpdf import FPDF
from pathlib import Path
from fpdf.enums import XPos, YPos

for filepath in Path("txt").glob("*.txt"):
    pdf = FPDF("P", "mm")
    pdf.add_page()

    filename = filepath.stem  # filename without extension

    pdf.set_font("Helvetica", size=16, style='B')
    pdf.cell(0, 10, f"{filename}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, filepath.read_text(encoding="utf-8"))  # read file content

    Path("exercises").mkdir(parents=True, exist_ok=True)
    pdf.output(str(Path("exercises") / f"{filename}.pdf"))



# filepaths = glob.glob("txt/*.txt")

# for path in filepaths:
#     with open(path) as f:
#         pdf = FPDF("P", "mm")
#         pdf.add_page()
#         filename = Path(path).stem
#         pdf.set_font("Helvetica", size=16, style='B')
#         pdf.cell(0, 10, f"{filename}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)  # Title
#         pdf.ln(5)  # Space below title
#         pdf.set_font("Helvetica", size=12)
#         pdf.multi_cell(0, 10, f.read())  # Paragraph text
#
#         Path("exercises").mkdir(parents=True, exist_ok=True)
#         pdf.output(f"exercises/{filename}.pdf")
