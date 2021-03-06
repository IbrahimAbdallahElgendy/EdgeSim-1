import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import  FormatStrFormatter
import sys
import os

#this is the Absolute path
# DATA_FILE_PATH = str(sys.argv[0][0:sys.argv[0].index("\src")] + "main\resources\data\ResultData")
#Relative path , which determined by the caller
DATA_FILE_PATH = str(sys.argv[0][0:sys.argv[0].index("src")]) + "src\main\\resources\data\ResultData"

class Algorithm_Data:
    def __init__(self, Algorithm):
        self.Algorithm = Algorithm
        self.Data = [0]
'''
Read result file
'''
algorithm_data_list = []
with open(DATA_FILE_PATH, encoding='utf-8') as ResultData_Reader:
    for line in ResultData_Reader:
        if "Algorithm" in line.split(" ")[0]:
            algorithm = Algorithm_Data(line.split(":")[1])
            algorithm_data_list.append(algorithm)
        else:
            line_data = line.split(" ")
            for data in line_data:
                data = data.split(",")
                if len(data) == 4:
                    algorithm_data_list[-1].Data.append(float(data[2]))
                    
'''
line chart
'''
# set the image size of the output
figsize = 7.5, 6
figure, ax = plt.subplots(num="DELAY", figsize=figsize)

'''
set the scale
'''
#set the coordinate range of value
plt.ylim(0, 50)
plt.xlim(0, len(algorithm_data_list[-1].Data)+1)
#set the scale
#set the x major scale label to a multiple of 5
xmajorLocator = MultipleLocator(20);
#set the format of the x-axis label text
xmajorFormatter = FormatStrFormatter('%3.0f')
#Set the x-axis minor scale label to a multiple of 1
xminorLocator = MultipleLocator(1)
#Load x-axis settings
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
#Set the y-axis main scale label to a multiple of 0.05%
ymajorLocator = MultipleLocator(10)
#Set the format of the y-axis label text
ymajorFormatter = FormatStrFormatter('%3.0f')
#Set this y-axis minor tick label to a multiple of 0.2
yminorLocator = MultipleLocator(1)
#Load y-axis settings
# ax.yaxis.set_major_locator(ymajorLocator)
# ax.yaxis.set_major_formatter(ymajorFormatter)
# # Shows the position of the subscale label, but no label text
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
# ax.xaxis.grid(True, which='major')  # The grid of the x-axis uses the major scale
# ax.yaxis.grid(True, which='minor')  # The grid of the y-axis uses the minor scale

'''
Set the font of the axis
'''
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 18,
        }
# Set the font of the scale value
label_font = {'family': 'Times New Roman',
              'weight': 'bold',
              'size': 16,}
plt.xlabel(label_font)
plt.ylabel(label_font)
'''
Drawing
'''
for algorithm in algorithm_data_list:
    if "KNAPSACK" in algorithm.Algorithm:
        plt.plot(algorithm.Data, color = 'red', marker= "o", linewidth=2, markersize = 10, label=algorithm.Algorithm)
    elif "GREEDY" in algorithm.Algorithm:
        plt.plot(algorithm.Data, color = 'blue', marker= ">", linewidth=2, markersize = 10, label=algorithm.Algorithm)
    elif "LFU" in algorithm.Algorithm:
        plt.plot(algorithm.Data, color = 'orange', marker= "p",linewidth=2, markersize = 10, linestyle="--", label=algorithm.Algorithm)
    elif "LRU" in algorithm.Algorithm:
        plt.plot(algorithm.Data, color = 'green', marker= "*", linewidth=2, markersize = 10, linestyle=":", label=algorithm.Algorithm)
    else:
        plt.plot(algorithm.Data, linewidth=2, label=algorithm.Algorithm)



plt.xlabel("Time Silce", font)
plt.ylabel("Delay(s)", font)

'''
Set legend
'''
font_legend = {'family': 'Times New Roman', 'weight': 'bold', 'size': 12}
plt.legend(prop=font_legend, loc=1, numpoints=1, ncol = 1)

ltext = plt.gca().get_legend().get_texts()

plt.show()
