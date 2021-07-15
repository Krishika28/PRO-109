from numpy import mod
import plotly.figure_factory as ff
import pandas as p
import plotly.graph_objects as go
import statistics as s

df = p.read_csv("StudentsPerformance.csv")
list = df["writing score"].tolist()

mean = s.mean(list)
mode = s.mode(list)
median = s.median(list)
std = s.stdev(list)

print("Mean: ",mean)
print("Mode: ",mode)
print("Median: ",median)
print("Standard Devation: ",std)

sd1_start, sd1_end = mean - std, mean + std
sd2_start, sd2_end = mean - (2*std), mean + (2*std)
sd3_start, sd3_end = mean - (3*std), mean + (3*std)

count_data1 = 0
count_data2 = 0
for i in list:
    if(i > sd1_start and i<sd1_end):
        count_data1 = count_data1 +1
    if(i > sd2_start and i<sd2_end):
        count_data2 = count_data2 +1 
#   if(1 > sd3_start and i<sd3_end):
#      count_data3 = count_data3 +1

percentage_data1 = (count_data1/len(list)) *100
percentage_data2 = (count_data2/len(list)) *100
#percentage_data3 = (count_data3/len(list)) *100

print(percentage_data1, "of the data lies within 1st standard devation")
print(percentage_data2, "of the data lies within 2nd standard devation")
#print(percentage_data3, "of the data lies within 3rd standard devation")

fig = ff.create_distplot([list],["writing result"], show_hist=False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "mean"))


fig.add_trace(go.Scatter(x = [sd1_start, sd1_start], y = [0,0.17], mode = "lines", name = "1st Standard Devation"))
fig.add_trace(go.Scatter(x = [sd1_end, sd1_end], y = [0,0.17], mode = "lines", name = "1st Standard Devation"))


fig.add_trace(go.Scatter(x = [sd2_start, sd2_start], y = [0,0.17], mode = "lines", name = "2nd Standard Devation"))
fig.add_trace(go.Scatter(x = [sd2_end, sd2_end], y = [0,0.17], mode = "lines", name = "2nd Standard Devation"))


fig.add_trace(go.Scatter(x = [sd3_start, sd3_start], y = [0,0.17], mode = "lines", name = "3nd Standard Devation"))
fig.add_trace(go.Scatter(x = [sd3_end, sd3_end], y = [0,0.17], mode = "lines", name = "3nd Standard Devation"))

fig.show()