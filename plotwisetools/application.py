import sys, csv, traceback
import matplotlib.pyplot as plt
from collections import defaultdict

class ApplicationExit(BaseException):
    pass

class Application:
    def __init__(self, filepath):
        self.columns = defaultdict(list)
        self.filepath = filepath
        self.expenses = {}

    def sumUpList(self, lis):
        summedUp = 0.0
        for el in lis:
            summedUp = summedUp + float(el)
        
        return summedUp

    def parseColumn(self, name):
        if not self.columns:
            try:
                data = csv.DictReader(open(self.filepath, 'r'))
                for row in data: # read a row as {column1: value1, column2: value2,...}
                    for (k,v) in row.items(): # go over each column name and value 
                        self.columns[k].append(v)
            except Exception as e:
                print("Unable to read *.csv file")
                traceback.print_exc(file=sys.stdout)
                raise ApplicationExit()
        return self.columns[name]

    def run(self):
        # TODO: make column names and numbers more human readable, e.g. 2 = category
        """
        for cat, expense in self.parseColumn('Kategorie'), self.parseColumn('Kosten'):
            if not cat in self.expenses:
                self.expenses[cat] = [expense]
            else:
                self.expenses[cat].append(expense)
        """
        for k,v in zip(self.parseColumn('Kategorie'), self.parseColumn('Kosten')):
            self.expenses.setdefault(k, []).append(v)
        self.plotExpenses()
                
    def plotExpenses(self):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = [key for key in self.expenses]
        sizes = [self.sumUpList(self.expenses[key]) for key in self.expenses]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

def main(filepath="export.csv"):
    try:
        app = Application(filepath)
        app.run()
    except ApplicationExit:
        sys.exit(1)
    except EOFError:
        sys.stderr.write("\nError: Unexpected end of input\n")
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130) # Standard UNIX exit code for SIGINT
