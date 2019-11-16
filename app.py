import dash
import dash_html_components as html
import dash_core_components as dcc
import json
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'plot 1', 'value': 'Plotly_Optimizer_Parameters_3A_2019_10_31_15_28_55_2C_Realised_Parameters_Corner_Plot.json'},
            {'label': 'plot 2', 'value': 'Plotly_Optimizer_Parameters_3A_2019_11_08_14_02_15_2C_Realised_Parameters_Corner_Plot.json'},
            {'label': 'blank', 'value': 'blank.json'}

        ],
        value='Plotly_Optimizer_Parameters_3A_2019_11_08_14_02_15_2C_Realised_Parameters_Corner_Plot.json'
    ),
    dcc.Graph(id='output-graph')
])


@app.callback(
    dash.dependencies.Output('output-graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):

    with open(value) as json_file:
        data = json.load(json_file)

    return data


if __name__ == '__main__':
    app.run_server(debug=True)