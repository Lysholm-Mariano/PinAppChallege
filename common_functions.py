import csv
import os


def csv_to_list(path):
    filePath = os.path.abspath(path)
    csvreader = open(filePath,"r")
    listed_items = list(csv.reader(csvreader, delimiter=","))
    csvreader.close
    return listed_items[0]