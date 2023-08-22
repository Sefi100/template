import os
import nbformat as nbf
import nbconvert
from datetime import datetime


def pdfconvert(path, title, name, date = None):
    """
    Converts a jupyter notebook to pdf using latex. Includes additional functionality to specify the title and authors
    of the converted file
    :param path: full path of jupyter notebook to be exported
    :param title: title of output latex based pdf
    :param name: list, names of authors to be included in pdf
    :param date: date, today if not specified
    :return: None
    """
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')

    dt = nbf.read(path, nbf.NO_CONVERT)
    dt.metadata.update({'title': title})
    dt.metadata.update({'date': date})
    dt.metadata.update({'authors': [{'name': name[0]}, {'name': name[1]}]})
    nbf.write(dt, path, nbf.NO_CONVERT)
    exporter = nbconvert.PDFExporter(exclude_input=True)
    pdf_data, res = nbconvert.export(exporter, path)
    with open(res['metadata']['path']+'\\\\'+res['metadata']['name']+res['output_extension'], 'wb') as f:
        f.write(pdf_data)
    # os.system(f"jupyter nbconvert --to pdf --TemplateExporter.exclude_input=True {path}")


# dir_path = os.getcwd() + "ipynb_name.ipynb"
# pdfconvert(dir_path, "Title", ["Author_0", "Author_1"])
dir_path = os.getcwd() + "\\sample.ipynb"
pdfconvert(dir_path, "test", ["Györgyfalvai Fanni", "Schäffer Bálint"])
