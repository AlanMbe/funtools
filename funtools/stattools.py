import matplotlib.pyplot as plt

class StatsTool:
    def __init__(self, data):
        """init"""
        self.data = data

def plot_line(self, labels=None, title="Line Plot", xlabel="X-Axis", ylabel="Y-Axis"):
    """Draw a line plot"""
    plt.figure(figsize=(10, 6))
    plt.plot(self.data, label=labels if labels else 'Data', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_bar(self, labels=None, title="Bar Plot", xlabel="Categories", ylabel="Values"):
    """Draw a bar plot"""
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(self.data)), self.data, tick_label=labels if labels else range(len(self.data)), color='g')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_pie(self, labels=None, title="Pie Chart"):
    """Draw a pie chart"""
    plt.figure(figsize=(8, 8))
    plt.pie(self.data, labels=labels if labels else range(len(self.data)), autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.show()

def show_histogram(self, bins=10, title="Histogram", xlabel="Values", ylabel="Frequency"):
    """Draw a histogram"""
    plt.figure(figsize=(10, 6))
    plt.hist(self.data, bins=bins, color='c', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
