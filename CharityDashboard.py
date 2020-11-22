import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('/Users/Derrick Zipperer/Documents/Software Engineering/Charity Project/CharityInfo.csv')

app = dash.Dash()

app.layout = html.Div(children=[html.H1(children="Python Dash",style={"textAlign": "center","color": "#ef3e18"}),
    html.Div("Web dashboard for Charity Information",
    style={"textAlign": "center"}),
    html.Div("Charity Information for the top Charities in the US in 2019",
    style={"textAlign": "center"}),
    html.Br(),
    html.Br(),
    html.Hr(style={"color": "#7FDBFF"}),
    html.H3("Interactive Bar chart", style={"color": "#df1e56"}),
    html.Div("This bar chart displays the total revenue of charities from the selected category"),
    dcc.Graph(id="graph1"),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
    ],
    value="Domestic Needs"
    )
])

@app.callback(Output("graph1", "figure"),
                [Input('select-category', 'value')])
def update_figure(selected_category):
    filtered_df = df[df['Category'] == selected_category]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    new_df = filtered_df.groupby(['Name'])['Total Revenue'].sum().reset_index()
    new_df = new_df.sort_values(by=['Total Revenue'], ascending=[False])
    data_interactive_barchart = [go.Bar(x=new_df['Name'],
    y=new_df['Total Revenue'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Total Revenue for ' +selected_category+ ' charities',
    xaxis={'title': 'Name of Charity'},
    yaxis={'title': 'Total Revenue'})}

if __name__ == '__main__':
        app.run_server()