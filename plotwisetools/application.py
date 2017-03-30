import matplotlib.pyplot as plt

class Application:
    def __init__(self, filepath):
        self.labels = []
        self.sizes = []
        self.filepath = filepath

    def run(self):
        print("Hello world!")

    def plot(self):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = self.labels
        sizes = self.sizes
        explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
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
