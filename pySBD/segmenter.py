# -*- coding: utf-8 -*-
from pySBD.languages import Language
from pySBD.processor import Processor
from pySBD.cleaner import Cleaner


class Segmenter(object):

    def __init__(self, language="en", clean=False, doc_type=None):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.clean = clean
        self.doc_type = doc_type

    def segment(self, text):
        if not text:
            return []
        if self.clean:
            text = Cleaner(text, doc_type=self.doc_type).clean()
        processor = Processor(text)
        segments = processor.process()
        return segments


if __name__ == "__main__":
    text = "Saint Maximus (died 250) is a Christian saint and martyr.[1] The emperor Decius published a decree ordering the veneration of busts of the deified emperors."
    # ["Saint Maximus (died 250) is a Christian saint and martyr.[1]", "The emperor Decius published a decree ordering the veneration of busts of the deified emperors."
    print("Input String:\n{}".format(text))
    seg = Segmenter(language="en", clean=True)
    segments = seg.segment(text)
    print("\n################## Processing #######################\n")
    print("Number of sentences: {}\n".format(len(segments)))
    print("Sentences found:\n{}\n".format(segments))
    print("\n################## Output #######################\n")
    for ind, sent in enumerate(segments, start=1):
        print("{} -> {}".format(ind, sent))
