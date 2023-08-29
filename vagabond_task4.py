
import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import numpy as np

colors = {
    'background': '#F2F2F2',
    'text': '#022859',
    'graph': '#A65233'
}

df = pd.read_csv('cleaned_data.csv')
df['year'] = pd.to_datetime(df['date']).dt.strftime('%Y')
app = Dash(__name__)

header = html.H1('Soul Foods: Pink Morsel Price Changes Over Year', 
                  id = 'header',
                  style = {'textAlign': 'left', 'color': colors['text']})

region_picker = dcc.Dropdown(df['region'].unique(), value = df['region'], 
                                 id = 'region_picker',
                                 style = {'padding': 10, 'flex': 1})
region_picker_wrap = html.Div([
                    html.H3(children = 'Choose the region to be shown:',
                            style = {'textAlign': 'left', 'color': colors['text'], 'padding': 10, 'flex': 1}),
                    html.Br(),
                    region_picker,
                    html.Br(),
                    html.H3(children = 'Choose the color:',
                            style = {'textAlign': 'left', 'color': colors['text'], 'padding': 10, 'flex': 1}),
                    dcc.Dropdown(
                                id='color',
                                options=[
                                    {'label': 'Navy', 'value': '#001f3f'},
                                    {'label': 'Aqua', 'value': '#7FDBFF'},
                                    {'label': 'Teal', 'value': '#39CCCC'},
                                    {'label': 'Olive', 'value': '#3D9970'},
                                        ],
                                    value='#001f3f',
                                    style = {'padding': 10, 'flex': 1}
                                ),
                    html.Br()], style={'display': 'flex', 'flex-direction': 'row'})

vis = dcc.Graph(style= {'backgroundColor': colors['background']}, id = 'sale-graph')

app.layout = html.Div([
                header,
                region_picker_wrap,
                html.Br(),
                html.H2('Sales by Period', style = {'textAlign': 'left', 'color': colors['text']}),
                vis 
])

@callback(
    Output('sale-graph', 'figure'),
    [
    Input('region_picker', 'value'),
    Input('color','value')
    ]
    )
def update_figure(region_picker, color_id):
    filtered_df = df[df['region'] == region_picker]

    fig = px.line(filtered_df, x = 'date', 
                  y = 'sales', 
                  color = 'region',
                  hover_name= 'region',
                  color_discrete_sequence=px.colors.qualitative.G10)

    
    fig.update_layout(
        hovermode='closest',
        plot_bgcolor=color_id,
        paper_bgcolor=colors['background'],
        font_color='black'
    )

    fig.update_xaxes(title='Sales record over years (from 2018 - 2022)')
    fig.update_yaxes(title = 'Total Sales number, counted by quality x price')

    return fig

if __name__ == '__main__':
    app.run_server()