import pandas as pd

class DataProcessor:
    @staticmethod
    def filter_data(data, column, value):
        return data[data[column] == value]

    @staticmethod
    def sort_data(data, column, ascending=True):
        return data.sort_values(by=column, ascending=ascending)

    @staticmethod
    def convert_categorical_to_numeric(data, column):
        data[column] = data[column].astype('category').cat.codes
        return data

    @staticmethod
    def extract_columns(data, columns):
        return data[columns]
