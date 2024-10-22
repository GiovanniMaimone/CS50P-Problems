from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.pdf.set_auto_page_break(auto=False, margin=0)
        self.pdf.add_page()
        self.header()
        self.shirt()
        self.name_on_shirt(self.name)

    def header(self):
        self.pdf.set_font("helvetica", "B", 35)
        self.pdf.cell(
            0, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C"
        )

    def shirt(self):
        self.pdf.image("shirtificate.png", w=self.pdf.epw)

    def name_on_shirt(self,name):
        self.pdf.set_font("helvetica", "B", 22)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(68, 120, text=f"{name} took CS50")

    def save(self):
        self.pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    shirtificate = Shirtificate(name)
    shirtificate.save()


if __name__ == "__main__":
    main()
