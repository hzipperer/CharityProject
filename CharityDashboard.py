import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import plotly.graph_objs as go

df = pd.read_csv('C:/Users/Owner/Desktop/Software Engineering/CharityProject-main/CharityInfo.csv')
dc = pd.read_csv('C:/Users/Owner/Desktop/Software Engineering/CharityProject-main/CharityInfoAll.csv')

app = dash.Dash()

app.layout = html.Div(style={"textAlign": "center"}, children=[html.H1(children="CHARITY DASHBOARD",style={"textAlign": "center","color": "white","backgroundColor": "black"}),
html.Img(src='https://media.giphy.com/media/1McM0n5dCButedp9wG/giphy.gif',
    style={
        "height": "100%",
        "width": "100%",
        "image-resolution": "500dpi"}),
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

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
    ],
    value="Domestic Needs"
    ),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([html.H1(children="TOP 50 CHARITIES IN THE United States",style={"textAlign": "center","color": "white","backgroundColor": "black"}),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i}
                     for i in
    dc.columns],
            data=dc.to_dict('records'),
            style_data={"textAlign": "left"},
            style_cell={"backgroundColor": "lightblue"}
        )
    ]
              )
])



@app.callback(Output("graph1", "figure"),
                [Input('select-category', 'value')])
def update_figure(selected_category):

    filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    new_df = filtered_df.groupby(['Name'])['Total Revenue'].sum().reset_index()
    new_df = new_df.sort_values(by=['Total Revenue'], ascending=[False])
    data_interactive_barchart = [go.Bar(x=new_df['Name'],
    y=new_df['Total Revenue'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Total Revenue for ' +selected_category+ ' charities',
    xaxis={'title': 'Name of Charity'},
    yaxis={'title': 'Total Revenue'})}

def table_dash():
    return {'data': dc}

if __name__ == '__main__':
        app.run_server()