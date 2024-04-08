from flask import render_template, send_from_directory
from app import app
import os
import logging


def should_be_hidden_file(file_name):
    if file_name.lower() == "readme.md" or file_name.lower().startswith('.'):
        return True
    else:
        return False


@app.route('/')
def index():
    header_image_path = 'static/images/header_image.png'
    return render_template('index.html', header_image=header_image_path)


@app.route('/photos')
def photos():
    directory_path = '/Users/merpenbeck/src/techbee/entrance-camera/photos'
    logging.warning("in photos")
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
    directory_path = '/Users/merpenbeck/src/techbee/entrance-camera/videos'
    logging.warning("in videos")
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
    root_directory = '/Users/merpenbeck/src/techbee/entrance-camera'
    # root_directory = '/home/techbee/Desktop/entrance-camera'

    full_directory_path = root_directory + '/' + directory_path
    logging.info("full_directory_path = " + full_directory_path)
    return send_from_directory(root_directory, directory_path)
