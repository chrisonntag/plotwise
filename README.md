# plotwise [NOT MAINTAINED]

This tiny script creates pie diagrams out of exported [Splitwise](https://www.splitwise.com/) data. 
It was originally implemented in order to have an overview of how much money i've spent on vacation for 
each category (Hotel, Transportation, Food, etc.).

![Example image](https://raw.githubusercontent.com/chrisonntag/plotwise/master/expenses.png)

## Usage

Simply download the code, install all requirements in a virtual environment 
and append the file with ```-f <yourfile>``` like so:

```bash
$ pip install -r requirements.txt
$ plotwise.py -f <path-to-your-file>
```

Don't forget to activate your venv before: ```source path/to/venv/bin/activate```
