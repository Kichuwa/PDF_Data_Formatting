import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for path in filepaths:
    filename = Path(path).stem
    title = filename.title()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{title}", ln=1)

pdf.output("animals.pdf")
