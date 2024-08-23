from collections import defaultdict
import io
import re
import tabula

from pdf_utils import crop_pdf_images
from textract_utils import get_indices

pdf_path = "input/Request of windows.pdf"
result_path = "output/result.csv"
image_folder = "images"

crop_pdf_images(pdf_path, image_folder)

# Extract tables from the PDF file
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

pat_id = r"V_[A-Za-z0-9]+-\d+(?:\.\d+)?"
pat_antall = r"\d"
pat_bh = r"((\d )?\d{3}×(\d )?\d{3})|---"
pat_req = r"(E(I|W)? 30)"

page = 1
result = {}

# Iterate through tables and convert to DataFrame
for i, table in enumerate(tables):
    csv_buffer = io.StringIO()
    table.to_csv(csv_buffer, index=False)
    rows = csv_buffer.getvalue().splitlines()

    if rows[0].startswith("Unnamed:"):
        rows.pop(0)
    if not rows[0].startswith("ID") and not rows[0].startswith('"ID'):
        continue

    id = re.findall(pat_id, rows[0])
    antall = re.findall(pat_antall, rows[1])

    for row in rows[2:]:
        if row.startswith("BxH"):
            row_b_h = row[:-1]
            b = []
            h = []
            for m in re.findall(pat_bh, row):
                if m[0]:
                    bb, hh = m[0].replace(" ", "").split("×")
                    b.append(bb)
                    h.append(hh)
                else:
                    b.append("---")
                    h.append("---")
        if row.startswith("Brannkrav"):
            row_req = row[:-1]
            req = defaultdict(lambda: "---")
            try:
                indices = get_indices(f"{image_folder}/{page}.jpg")
                for i, m in enumerate(re.findall(pat_req, row)):
                    req[indices[i]] = m[0]
            except Exception as e:
                print(f"AWS Textract Error in Page {page}")

    if id[0] in result:
        continue

    for i in range(len(id)):
        result[id[i]] = ",".join([id[i], antall[i], b[i], h[i], req[i]])

    page += 1

with open(result_path, "w") as out:
    print("ID,Antall,Bredde (mm),Høyde (mm),Brannklasse,Pris", file=out)
    for i in result:
        print(result[i], file=out)
