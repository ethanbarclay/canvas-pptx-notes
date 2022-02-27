# canvas-pptx-notes
python script for downloading notes from presentations on a canvas course's modules

# how to use
1. `pip3 install -r requirements.txt`
2. Set API_URL, API_KEY, and COURSE_ID in canvas_pptx_notes.py
3. `python3 canvas_pptx_notes.py`

# standalone notes extractor
pptx_notes.py exists as a standalone pptx notes extractor script that can take any pptx file as input and output the respective notes

usage: `python3 pptx_notes.py --file presentation.pptx`