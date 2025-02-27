
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import pandas as pd
app = Dash(__name__)

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	global df
	filtered_df = df[df['score'] == value]
	return len(filtered_df)


if __name__ == '__main__':
    app.run(debug=True)
