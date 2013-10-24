"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""
from flask import Blueprint, render_template, request


from utils import list_to_csv, csv_to_list
from config import csv_read_file, csv_write_file

views = Blueprint('views', __name__)

sample_data_list = [
    ['http://s5.tinypic.com/ny8hf7_th.jpg', ['do', 'not', 'say', 'these', 'words'], 'ignore_field', 'ignore_field1'],
    ['http://s5.tinypic.com/1111845_th.jpg', ['do', 'not', 'say', 'these', 'words'], 'ignore_field', 'ignore_field1'],
    ['http://s5.tinypic.com/111188w_th.jpg', ['do', 'not', 'say', 'these', 'words'], 'ignore_field', 'ignore_field1']
]

LIST_INDEX = 0
IMAGE_DATA_LIST = []
CSV_WRITE_DATA = []

@views.route('/')
@views.route('/index')
def index():
    """Render website's index page."""
    return render_template('index.html')


@views.route('/tag', methods=['GET', 'POST'])
def tag_images():
    """
    reads all the rows from read_csv_file into a list, displays one image url and name to the user at a time
    using a global counter, and keeps going until the end of the list is reached. At this point, a "Done Template"
    will be displayed, the counter will be reset, and the read_csv_file will be deleted. Once a user submits
    a tag, it will be appended to the corresponding list data item, and then written out to the write_csv_file.

    :return: rendered form with list(image_url, image_name) as context
    """
    global LIST_INDEX

    # create a sample read_csv_file using the image_list_data at the top
    # list_to_csv(csv_read_file, sample_data_list)

    # read the read_csv_file into a list
    IMAGE_DATA_LIST = csv_to_list(csv_read_file)

    image_data = IMAGE_DATA_LIST[LIST_INDEX]

    new_image_data = image_data[:]
    for value in request.form.values():
        if value is not None:
            new_image_data.append(value)

        CSV_WRITE_DATA.append(new_image_data)
        LIST_INDEX += 1
        if LIST_INDEX == len(IMAGE_DATA_LIST):
            LIST_INDEX = 0
            list_to_csv(csv_write_file, CSV_WRITE_DATA)
            return render_template('done.html')
        image_data = IMAGE_DATA_LIST[LIST_INDEX]

    return render_template('show_image.html', image_data=image_data)

