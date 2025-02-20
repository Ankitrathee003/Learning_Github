# # Figure and Slider


# from dash import Dash, dcc, html, Input, Output, callback
# import plotly.express as px

# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(id='graph-with-slider'),
#     dcc.Slider(
#         df['year'].min(),
#         df['year'].max(),
#         step=None,
#         value=df['year'].min(),
#         marks={str(year): str(year) for year in df['year'].unique()},
#         id='year-slider'
#     )
# ])


# @callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[df.year == selected_year]

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig


# if __name__ == '__main__':
#     app.run(debug=True)





















# Dash App With Multiple Inputs
# from dash import Dash, dcc, html, Input, Output, callback
# import plotly.express as px

# import pandas as pd

# app = Dash(__name__)

# df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

# app.layout = html.Div([
#     html.Div([

#         html.Div([
#             dcc.Dropdown(
#                 df['Indicator Name'].unique(),
#                 'Fertility rate, total (births per woman)',
#                 id='xaxis-column'
#             ),
#             dcc.RadioItems(
#                 ['Linear', 'Log'],
#                 'Linear',
#                 id='xaxis-type',
#                 inline=True
#             )
#         ], style={'width': '48%', 'display': 'inline-block'}),

#         html.Div([
#             dcc.Dropdown(
#                 df['Indicator Name'].unique(),
#                 'Life expectancy at birth, total (years)',
#                 id='yaxis-column'
#             ),
#             dcc.RadioItems(
#                 ['Linear', 'Log'],
#                 'Linear',
#                 id='yaxis-type',
#                 inline=True
#             )
#         ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
#     ]),

#     dcc.Graph(id='indicator-graphic'),

#     dcc.Slider(
#         df['Year'].min(),
#         df['Year'].max(),
#         step=None,
#         id='year--slider',
#         value=df['Year'].max(),
#         marks={str(year): str(year) for year in df['Year'].unique()},

#     )
# ])


# @callback(
#     Output('indicator-graphic', 'figure'),
#     Input('xaxis-column', 'value'),
#     Input('yaxis-column', 'value'),
#     Input('xaxis-type', 'value'),
#     Input('yaxis-type', 'value'),
#     Input('year--slider', 'value'))
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#     dff = df[df['Year'] == year_value]

#     fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#                      y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#                      hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

#     fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

#     fig.update_xaxes(title=xaxis_column_name,
#                      type='linear' if xaxis_type == 'Linear' else 'log')

#     fig.update_yaxes(title=yaxis_column_name,
#                      type='linear' if yaxis_type == 'Linear' else 'log')

#     return fig


# if __name__ == '__main__':
#     app.run(debug=True)

























# Dash App With Multiple Outputs
# from dash import Dash, dcc, html, Input, Output, callback

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Input(
#         id='num-multi',
#         type='number',
#         value=5
#     ),
#     html.Table([
#         html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
#         html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
#         html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
#         html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
#         html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
#     ]),
# ])


# @callback(
#     Output('square', 'children'),
#     Output('cube', 'children'),
#     Output('twos', 'children'),
#     Output('threes', 'children'),
#     Output('x^x', 'children'),
#     Input('num-multi', 'value'))
# def callback_a(x):
#     return x**2, x**3, 2**x, 3**x, x**x


# if __name__ == '__main__':
#     app.run(debug=True)





# # Dash App With Chained Callbacks
# from dash import Dash, dcc, html, Input, Output, callback

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# all_options = {
#     'America': ['New York City', 'San Francisco', 'Cincinnati'],
#     'Canada': ['Montréal', 'Toronto', 'Ottawa']
# }
# app.layout = html.Div([
#     dcc.RadioItems(
#         list(all_options.keys()),
#         'America',
#         id='countries-radio',
#     ),

#     html.Hr(),

#     dcc.RadioItems(id='cities-radio'),

#     html.Hr(),

#     html.Div(id='display-selected-values')
# ])


# @callback(
#     Output('cities-radio', 'options'),
#     Input('countries-radio', 'value'))
# def set_cities_options(selected_country):
#     return [{'label': i, 'value': i} for i in all_options[selected_country]]


# @callback(
#     Output('cities-radio', 'value'),
#     Input('cities-radio', 'options'))
# def set_cities_value(available_options):
#     return available_options[0]['value']


# @callback(
#     Output('display-selected-values', 'children'),
#     Input('countries-radio', 'value'),
#     Input('cities-radio', 'value'))
# def set_display_children(selected_country, selected_city):
#     return f'{selected_city} is a city in {selected_country}'


# if __name__ == '__main__':
#     app.run(debug=True)















# Dash App With State
# from dash import Dash, dcc, html, Input, Output, callback

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Input(id="input-1", type="text", value="Montréal"),
#     dcc.Input(id="input-2", type="text", value="Canada"),
#     html.Div(id="number-output"),
# ])


# @callback(
#     Output("number-output", "children"),
#     Input("input-1", "value"),
#     Input("input-2", "value"),
# )
# def update_output(input1, input2):
#     return f'Input 1 is "{input1}" and Input 2 is "{input2}"'


# if __name__ == "__main__":
#     app.run(debug=True)







# Dash App With State
# from dash import Dash, dcc, html, Input, Output, callback

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Input(id="input-1", type="text", value="Montréal"),
#     dcc.Input(id="input-2", type="text", value="Canada"),
#     html.Div(id="number-output"),
# ])


# @callback(
#     Output("number-output", "children"),
#     Input("input-1", "value"),
#     Input("input-2", "value"),
# )
# def update_output(input1, input2):
#     return f'Input 1 is "{input1}" and Input 2 is "{input2}"'


# if __name__ == "__main__":
#     app.run(debug=True)











# from dash import Dash, dcc, html, Input, Output, State, callback

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div([
#     dcc.Input(id='input-1-state', type='text', value='Montréal'),
#     dcc.Input(id='input-2-state', type='text', value='Canada'),
#     html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
#     html.Div(id='output-state')
# ])


# @callback(Output('output-state', 'children'),
#               Input('submit-button-state', 'n_clicks'),
#               State('input-1-state', 'value'),
#               State('input-2-state', 'value'))
# def update_output(n_clicks, input1, input2):
#     return f'''
#         The Button has been pressed {n_clicks} times,
#         Input 1 is "{input1}",
#         and Input 2 is "{input2}"
#     '''


# if __name__ == '__main__':
#     app.run(debug=True)




from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.DataFrame({
    "x": [1,2,1,2],
    "y": [1,2,3,4],
    "customdata": [1,2,3,4],
    "fruit": ["apple", "apple", "orange", "orange"]
})

fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Selection Data**

                Choose the lasso or rectangle tool in the graph's menu
                bar and then select points in the graph.

                Note that if `layout.clickmode = 'event+select'`, selection data also
                accumulates (or un-accumulates) selected data if you hold down the shift
                button while clicking.
            """),
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
    ])
])


@callback(
    Output('hover-data', 'children'),
    Input('basic-interactions', 'hoverData'))
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@callback(
    Output('selected-data', 'children'),
    Input('basic-interactions', 'selectedData'))
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@callback(
    Output('relayout-data', 'children'),
    Input('basic-interactions', 'relayoutData'))
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)


if __name__ == '__main__':
    app.run(debug=True)
