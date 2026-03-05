from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

text_list = []

while True:
    line = input("enter a Text: ")
    if line.lower() == "END":
        break
    text_list.append(line)

styles = getSampleStyleSheet()

story = []

for text in text_list:
    story.append(Paragraph(text,styles["Normal"]))
pdf = SimpleDocTemplate("output.pdf")
pdf.build(story)
