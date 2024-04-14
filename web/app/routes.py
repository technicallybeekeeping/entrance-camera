from flask import render_template, send_from_directory
from app import app
import os
import logging


def get_root_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    grandparent_dir = os.path.dirname(parent_dir)

    return grandparent_dir


def should_be_hidden_file(file_name):
    if file_name.lower() == "readme.md" or file_name.lower().startswith('.'):
        return True
    else:
        return False


@app.route('/')
def index():
    logging.info("In index!!!")
    header_image_path = 'static/images/header_image.png'
    return render_template('index.html', header_image=header_image_path)


@app.route('/photos')
def photos():
    root_path = get_root_path()
    directory_path = root_path + '/photos'

    files = os.listdir(directory_path)
    sorted_files = sorted(files)  # Sort files alphabetically
    file_links = []
    for file_name in sorted_files:
        if (should_be_hidden_file(file_name) is True):
            continue
        logging.info("file_name=" + file_name)
        file_links.append({
            'name': file_name,
            'url': f"/photos/{file_name}"
        })
    return render_template('photos.html', file_links=file_links)


@app.route('/videos')
def videos():
    root_path = get_root_path()
    directory_path = root_path + '/videos'

    files = os.listdir(directory_path)
    sorted_files = sorted(files)  # Sort files alphabetically
    file_links = []
    for file_name in sorted_files:
        if (should_be_hidden_file(file_name) is True):
            continue
        logging.info("file_name=" + file_name)
        file_links.append({
            'name': file_name,
            'url': f"/videos/{file_name}"
        })
    return render_template('videos.html', file_links=file_links)


@app.route('/download/<path:directory_path>')
def download_directory(directory_path):
    root_path = get_root_path()

    return send_from_directory(root_path, directory_path)
