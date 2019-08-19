import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "International Cornhole Stats from 1940s"
mytitle = "Average Cornhole Percentage for 3 Hall of Famers"
x_values = ['1940', '1941', '1942', '1943', '1944', '1945']
y1_values = [703, 757, 803, 832, 769, 720]
y2_values = [690, 660, 789, 750, 708, 635]
y3_values = [701, 648, 804, 789, 692, 705]
color1 = '#0431B4'
color2 = '#BE81F7'
color3 = '#9003fc'
name1 = 'Leroy "Lightbulb" Williams'
name2 = 'Jeb "HotPocket" Smith'
name3 = 'Tyrone "Time Out" Monroe'
tabtitle = 'Cornhole'
sourceurl = 'https://www.cornhole-reference.com'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
