from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die1 = Die(8)
die2 = Die(8)
results = []
for x in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
freq = []
max_result = die1.sides + die2.sides
for value in range(2,max_result+1):
    res = results.count(value)
    freq.append(res)
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values,y= freq)]
x_axis_config = {'title': 'Result','dtick':'1'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='html_files/d8.html')
