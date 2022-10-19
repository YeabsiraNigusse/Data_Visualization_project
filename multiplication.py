from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die1 = Die()
die2 = Die()
result = []
for x in range(1000):
    n = die1.roll()*die2.roll()
    result.append(n)
freq = []
for x in range(1,37):
   n = result.count(x)
   freq.append(n)

xvalues = list(range(1,37))
data = [Bar(x=xvalues,y=freq)]
x_axis_config = {'title': 'Result','dtick':'1'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiply of two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='html_files/diesProduct_dice.html')