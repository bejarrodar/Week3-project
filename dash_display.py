import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("ZAll_Combine_Stock_Histry.csv")

app.layout = html.Div([
    html.H1("Top ten stock data"),
    html.Br(),
    dcc.Dropdown(
        id="select_company",
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
    html.Br(),
    html.Div(id="graph_draw")
])

@app.callback(
    Output("graph_draw","children"),
    Input("select_company","value")
)
def change_company(company):
    filtered_data = df.query("@company in Company")
    return dcc.Graph(id="graph",figure=px.line(filtered_data, x="Date", y="Close", title="Stock Closing Costs"))
        

if __name__ == '__main__':
    app.run_server()
