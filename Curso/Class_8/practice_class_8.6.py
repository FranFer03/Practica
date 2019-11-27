from fpdf import FPDF

text = "Citrus"
text_1 = "Cultivo"

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.add_page()
pdf.set_text_color(255,0,0)
pdf.set_font("helvetica", size=14, style="BI")
pdf.cell(190, 10, text, ln=1, align="C", border=1)
pdf.set_text_color(50, 100, 0)
pdf.set_draw_color(0, 0, 255)
pdf.set_fill_color(255, 170, 20)
pdf.set_font("helvetica", size=9, style="B")
pdf.cell(190, 5, text_1, fill=1)
pdf.image("C:\Imagenes\Inglaterra.png", x=30, y=50, w=20)
pdf.ln(60)

pdf.output("C:\Imagenes\ejlinea.pdf")
