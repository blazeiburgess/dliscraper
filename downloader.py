from os import mkdir
from os.path import exists
from requests import get
from glob import glob
from json import load
class Downloader(object):
    def __init__(self, courses_data, filename):
        self.courses_data = courses_data
        language = filename.split('/')[-1].split('.')[0]
        if not exists("output"):
            mkdir("output")
        self.base_folder = f"output/{language}"
        if not exists(self.base_folder):
            mkdir(self.base_folder)

    def _download_file(self, folder, url, filename=None):
        ext = url.split(".")[-1].lower()
        if not filename:
            filename = url.split('/')[-1]
        if filename.lower().find(ext) == -1:
            filename = f"{filename}.{ext}"

        local_filepath = f"{folder}/{filename}"
        if not exists(local_filepath):
            remote_file = get(url)
            with open(local_filepath,"wb") as f:
                for chunk in remote_file.iter_content(chunk_size=2048):
                    f.write(chunk)

    def download_from_course_data(self, course_data):
        course_folder = f"{self.base_folder}/{course_data['course_name']}"
        if not exists(course_folder):
            mkdir(course_folder)
        for ebook in course_data['ebooks']:
            self._download_file(course_folder, ebook)

        for audio in course_data['audio']:
            self._download_file(course_folder, audio['url'], audio['name'])
            

    def download_all(self):
        for course_data in self.courses_data:
            self.download_from_course_data(course_data)

if __name__ == '__main__':
    for course_file in glob("course_data/*.json"):
        with open(course_file,'r') as f:
            downloader = Downloader(load(f), course_file)
            downloader.download_all()
