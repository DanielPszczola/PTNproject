import matplotlib.pyplot as plt
import seaborn as sns

class GraphGen:
    @staticmethod
    def plot_count(data, column):
        plt.figure(figsize=(10,6))
        sns.countplot(data=data, x=column)
        plt.title('Count Plot')
        plt.show()

    @staticmethod
    def plot_scatter(data, x_column, y_column):
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=data, x=x_column, y=y_column)
        plt.title('Scatter Plot')
        plt.show()

    @staticmethod
    def plot_histogram(data, column):
        plt.figure(figsize=(10,6))
        sns.histplot(data=data, x=column)
        plt.title('Histogram')
        plt.show()

    @staticmethod
    def plot_box(data, column):
        plt.figure(figsize=(10,6))
        sns.boxplot(data=data, x=column)
        plt.title('Box Plot')
        plt.show()

    @staticmethod
    def plot_bar(data, x_column, y_column):
        plt.figure(figsize=(10,6))
        sns.barplot(data=data, x=x_column, y=y_column)
        plt.title('Bar Plot')
        plt.show()

    @staticmethod
    def plot_heatmap(data):
        plt.figure(figsize=(10,6))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap')
        plt.show()
