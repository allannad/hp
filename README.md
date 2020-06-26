# Harry Potter project
**Harry Potter Spells Visualization**

This command line program takes a user input of a spell, jinx, charm or curse. It creates a graph of the times the input has been mentioned across each Harry Potter book.

The text of each book is read from [this website](http://www.glozman.com/textpages.html), as is the [list of incantations](https://www.pojo.com/harry-potter-spell-list/).

Set up virtual environment in command line:
1. `conda create -n hp-env python=3.7`
2. `conda activate hp-env`

Install packages in command line terminal:
1. `pip install urllib.request`
2. `pip install regex`

Run Code:
`python spells.py`