#!python3
from pptx import Presentation
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, nargs='+', help='powerpoint file')
args = parser.parse_args()

def process_presentation(presentation):
    try:
        if presentation == args.file: prs = Presentation(args.file[0])
        else: prs = Presentation(presentation)
    except: prs = Presentation(presentation)
    with open(prs.core_properties.title + '.txt', 'a') as text_file:
        for slide in prs.slides:
            if len(slide.notes_slide.notes_text_frame.text) != 0:
                text_file.write(slide.shapes.title.text + '\n' +
                                slide.notes_slide.notes_text_frame.text + '\n\n\n')
    # delete empty files
    if os.stat(prs.core_properties.title + '.txt').st_size == 0: 
        os.remove(prs.core_properties.title + '.txt')
        
process_presentation(args.file)