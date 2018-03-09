import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot
import json

file_name = input("What is the file name? ")
with open(file_name, "r") as f:
    data = json.load(f)
    xs = [item[0] for item in data["data"]]
    ys = [item[1] for item in data["data"]]
    plot.plot(xs, ys)
    plot.savefig("JSON_plot.png")
    plot.close()