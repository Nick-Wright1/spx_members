import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

url = 'https://raw.githubusercontent.com/Nick-Wright1/sp500/85d80dce303c466f0030477d7960ce4088c5e385/sp500data.csv'

df = pd.read_csv(url, sep=',')
df = df.drop(df.columns[[0]], axis=1)

available_names = df['Asset Name'].unique()
available_names.sort()

app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Weight of the Company in S&P500 Index over time', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': k, 'value': k} for k in available_names],
        placeholder='Select Company Name Here....',
        multi=True),
    html.Hr(),
    dcc.Graph(id='display-selected-values')
])


@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    dash.dependencies.Input('demo-dropdown', 'value'))
def update_output(value):
    ts = df[df["Asset Name"].isin(value)]
    fig = px.line(ts, x="Holdings Date", y="Weight (%)", color="Asset Name")
    return fig


if __name__ == '__main__':
    app.run_server()