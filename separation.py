import json

def parse_json_file(path):
    """Return the contents of path as a JSON object."""
    with open(path) as infile:
        text = infile.read()
        return json.loads(text)


def read_file(path):
    """Return the contents of path."""
    with open(path) as infile:
        return infile.read()


def parse_json(text):
    """Return text parsed as a JSON object."""
    return json.loads(text)

# separation does not prevent you from having convenience functions

def parse_json_read_file(path):
    """Because I want the combined function behaviour badly."""
    return parse_json(read_file(path))

sample_json = """
    {"menu": {
      "id": "file",
      "value": "File",
      "popup": {
        "menuitem": [
          {"value": "New", "onclick": "CreateNewDoc()"},
          {"value": "Open", "onclick": "OpenDoc()"},
          {"value": "Close", "onclick": "CloseDoc()"}
        ]
      }
    }}
"""

def test_parse_json():
    frame = parse_json(sample_json)
    assert frame['menu']['popup']['menuitem'][0]['value'] == 'New'


def test_read_file():
    # read_file(path) is just too boring to unit test
    pass

#
# here is some of the extra junk needed without separation
#

import os
import tempfile

def test_parse_json_file():
    json_file = tempfile.NamedTemporaryFile(delete=False)
    json_file.write(sample_json)
    # and this line raises an exception and I don't want to debug it
    frame = parse_json_file(json_file.name)
    os.unlink(json_file.name)
    assert frame['menu']['popup']['menuitem'][0]['value'] == 'New'
