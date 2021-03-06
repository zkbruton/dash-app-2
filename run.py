import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
import os
import dash_table as dt
import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx'
df_albon = pd.read_excel(url)


server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',    
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Input(id='my-id', value='initial value', type="text"),
    html.Div(id='my-div'),
    html.Br(),
    dt.DataTable(style_table={'overflowX':'scroll'},
               style_cell={'minWidth':'45px'},
               style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
               style_data_conditional=[{'if':{'row_index':'odd'},
                                        'backgroundColor':'#f8f8f8'}],
               columns=[{"name": i, "id": i} for i in df_albon.columns],
               style_as_list_view=True,
               data=df_albon.to_dict('records')),
    html.Br()
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
