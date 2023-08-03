
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('cleaned_data.csv')
app = Dash(__name__)

fig = px.line(df, x = "date", y = "sales", hover_data="region")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div( style= {'backgroundColor': colors['background']}, children= [
                        html.H1( children= 'Soul Foods:', 
                                 style = {'textAlign': 'center', 'color': colors['text']}), 
                        html.H3(children= 'Pink Morsel Price Changes Over Year',
                                 style = {'textAlign': 'center', 'color': colors['text']}),
                        dcc.Graph(
                            id = 'sale-graph',
                            figure= fig
                        )
])

if __name__ == '__main__':
    app.run(debug=True)

