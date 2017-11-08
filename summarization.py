from fileinput import filename

from gensim.summarization import summarize
from os import listdir
from os.path import isfile, join
import os


class Summarizer:

    def __init__(self, folder):
        self.sources = []
        self.load(folder)

    def load(self, folder):
        path = os.path.dirname(os.path.abspath(__file__)) + "\\" + folder
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            filename = join(path, file)
            with open(filename, 'r', encoding='utf-8') as text_file:
                text = text_file.read()
                self.sources.append(text)

    def summarize_all(self):
        result = []
        for source_text in self.sources:
            summary = summarize(source_text)
            result.append(summary)
        return result


