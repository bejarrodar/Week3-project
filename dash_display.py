import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("ZAll_Combine_Stock_Histry.csv")
df["Date"] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df["Day Change"] = df["Close"] - df["Open"]
columns = ["Open","High","Low","Close","Adj Close","Volume","Day Change"]

app.layout = html.Div([
    html.H1("Top ten stock data"),
    html.Br(),
    dcc.Dropdown(
        id="select_company",
        placeholder="Select a company",
        options=[
            {"label":"Apple", "value":"AAPL"},
            {"label":"Amazon", "value":"AMZN"},
            {"label":"Tesla", "value":"TSLA"},
            {"label":"Google", "value":"GOOGL"},
            {"label":"JP Morgan", "value":"JP-MRGN"},
            {"label":"Microsoft", "value":"M-SOFT"},
            {"label":"Netflix", "value":"NTFLX"},
            {"label":"Nvidia", "value":"NVDA"},
            {"label":"Visa", "value":"VISA"},
            {"label":"Walmart", "value":"WLMART"}],
        multi=True,
        style={"width":"60%"}),
    dcc.Dropdown(
        id="select_column",
        placeholder="Select the data",
        options=columns,
        value=columns,
        multi=False,
        style={"width":"60%"}),
    html.Br(),
    html.Div(id="graph_draw")
])

@app.callback(
    Output("graph_draw","children"),
    Input("select_company","value"),
    Input("select_column","value")
)
def change_company(company,column):
    filtered_data = df.query("@company in Company")
    return dcc.Graph(id="graph",figure=px.line(filtered_data, x="Date", y=column, title="Stock Graph"))
        

if __name__ == '__main__':
    app.run_server()
