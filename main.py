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
    with open(path, "r") as text_output:
        text_output = text_output.readline()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=190, h=8, txt=f"{text_output}")

pdf.output("animals.pdf")
