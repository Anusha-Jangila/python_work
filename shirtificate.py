from fpdf import FPDF
from PIL import Image

name = input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', "B", size=30)
        self.cell(80)
        self.cell(15, 10, "CS50 Shirtificate", align='C')
        self.ln(20)

pdf = PDF()
left_margin = 20
right_margin = 15
top_margin = 25
bottom_margin = 45
pdf.set_margins(left_margin, top_margin, right_margin)
pdf.set_auto_page_break(auto="False")

pdf.add_page()
pdf.image("shirtificate.png", w=170)

text_content = name +" took CS50"
pdf.set_xy(60,105)
pdf.set_text_color(255,255,255)
pdf.set_font('Arial', size=20)
pdf.multi_cell(100, 0, text=text_content)

pdf.output("shirtificate.pdf")
