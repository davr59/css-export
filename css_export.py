import configparser
import re
import urllib.request

import PIL.Image
import requests

_CONFIG_INI = 'config.ini'
_DEFAULT_CONFIG = 'DEFAULT'
_HCTI_API_ENDPOINT_CONFIG = 'HCTI_API_ENDPOINT'
_HCTI_API_USER_ID = 'HCTI_API_USER_ID'
_HCTI_API_KEY = 'HCTI_API_KEY'

config = configparser.ConfigParser()
config.read(_CONFIG_INI)


class ImageInfo:
    def __init__(self, width, height, body_text, css_text, destination_file_path, is_rgba):
        self.width = width
        self.height = height
        self.body_text = body_text
        self.css_text = css_text
        self.destination_file_path = destination_file_path
        self.is_rgba = is_rgba

    @staticmethod
    def read_html_body_css(html_file_path):
        file = open(html_file_path, 'r')
        contents = file.read()
        body_groups = re.search(r'<body>([\s\S]*)</body>', contents)
        style_groups = re.search(r'<style>([\s\S]*)</style>', contents)
        return body_groups.group(1), style_groups.group(1)


class Exporter:
    def export_image(self, image_info):
        data = {'html': image_info.body_text,
                'css': image_info.css_text}
        image = requests.post(url=config[_DEFAULT_CONFIG]['HCTI_API_ENDPOINT'], data=data,
                              auth=(config[_DEFAULT_CONFIG]['HCTI_API_USER_ID'], config[_DEFAULT_CONFIG]['HCTI_API_KEY']))
        url = image.json()['url']
        urllib.request.opener = urllib.request.build_opener()
        urllib.request.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(urllib.request.opener)
        url = '{0}?width={1}&height={2}'.format(
            url, image_info.width, image_info.height)
        urllib.request.urlretrieve(url, image_info.destination_file_path)
        if not image_info.is_rgba:
            PIL.Image.open(image_info.destination_file_path).convert(
                'RGB').save(image_info.destination_file_path)
