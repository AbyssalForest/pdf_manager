from PyPDF2 import PdfMerger
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from fpdf import FPDF
from PIL import Image


class PDFManager():
    pdfs = []
    img_counter = 0

    def __init__(self):
        pass

    def select_files(self):
        while True:
            decision = input(
                'Enter plus to continue selecting files else press enter: ')
            if decision == "+":
                Tk().withdraw()
                filename = askopenfilename()
                print(filename)
                if filename != "":
                    self.pdfs.append(filename)
            else:
                break

    def img_to_pdf(self, filename):
        """ image = Image.open(filename)
        image.thumbnail((210, 297))
        image.save('image_tmp.png')
        print(image.size) """

        pdf = FPDF()
        pdf.add_page()
        pdf.image(filename, 0, 0, 210, 297)
        self.img_counter += 1
        name = f'tmp{self.img_counter}.pdf'
        pdf.output(name, "F")

        """ if os.path.exists("image_tmp.png"):
            os.remove("image_tmp.png") """

    def merge_pdfs(self):

        if self.pdfs:
            merger = PdfMerger()

            for pdf in self.pdfs:
                if pdf.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    self.img_to_pdf(pdf)
                    name = f'tmp{self.img_counter}.pdf'
                    merger.append(name)

                elif pdf.lower().endswith(".pdf"):
                    merger.append(pdf)

            merger.write("result.pdf")
            merger.close()

            for i in range(1, self.img_counter+1):
                name = f'tmp{i}.pdf'
                if os.path.exists(name):
                    print(f'temporary pdf with number: {i} deleted')
                    os.remove(name)


if __name__ == "__main__":
    p = PDFManager()
    p.select_files()
    p.merge_pdfs()
