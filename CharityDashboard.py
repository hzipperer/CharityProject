import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import plotly.graph_objs as go

#class CharityDashboard:

#<<<<<<< HEAD
df = pd.read_csv('/Users/Amari/Desktop/CharityProject/CharityInfo.csv')
#=======
df = pd.read_csv('/Users/Amari/Desktop/CharityProject-master/CharityInfo.csv')
dc = pd.read_csv('/Users/Amari/Desktop/CharityProject-master/CharityInfoAll.csv')
#>>>>>>> 31c494a0b5ffe2ed46b92af6c97c1676bf9fa552

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

    #Interactive Bar Chart
    html.Hr(style={"color": "#7FDBFF"}),
    html.H3("Interactive Bar chart", style={"color": "#df1e56"}),
    html.Div("This bar chart displays the total revenue of charities from the selected category"),
    dcc.Graph(id="graph1"),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-bar-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
        {"label": "Health", "value": "Health"},
        {"label": "Religious", "value": "Religious"},
    ],
    value="Domestic Needs"
    ),
    html.Br(),
    html.Br(),
    html.Br(),

    #Interactive Stack Bar Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div('This stack bar chart represents the total revenue broken down into donations vs other sources for the selected charities '),
    dcc.Graph(id='graph2'),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-stack-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
        {"label": "Health", "value": "Health"},
        {"label": "Religious", "value": "Religious"},
    ],
    value="Domestic Needs"
    ),

    #Interactive Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the fundraising efficiency (percent of donations remaining after fundraising expenses) for the selected charities.'),
    dcc.Graph(id='graph3'),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-line-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
        {"label": "Health", "value": "Health"},
        {"label": "Religious", "value": "Religious"},
    ],
    value="Domestic Needs"
    ),

    #Interactive MultiLine Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi-Line chart', style={'color': '#df1e56'}),
    html.Div('This Multi-Line chart represents the fundraising efficiency vs charitible commitment percentages for the selected charities.'),
    dcc.Graph(id='graph4'),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-multi-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
        {"label": "Health", "value": "Health"},
        {"label": "Religious", "value": "Religious"},
    ],
    value="Domestic Needs"
    ),

    #Heatmap
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heatmap', style={'color': '#df1e56'}),
    html.Div('This Heatmap represents the amount of donations recieved from the selected charities.'),
    dcc.Graph(id='graph5'),
    html.Div("Please select a category",style={"color": "#ef3e18", "margin": "10px"}),
    dcc.Dropdown(id="select-heat-category", options=[
        {"label": "Domestic Needs", "value": "Domestic Needs"},
        {"label": "International Needs", "value": "International Needs"},
        {"label": "Medical", "value": "Medical"},
        {"label": "Youth", "value": "Youth"},
        {"label": "Environment/Animal", "value": "Environment/Animal"},
        {"label": "Health", "value": "Health"},
        {"label": "Religious", "value": "Religious"},
    ],
    value="Domestic Needs"
    ),

    #Charity Info Table
    html.Div([html.H1(children="TOP 50 CHARITIES IN THE United States",style={"textAlign": "center","color": "white","backgroundColor": "black"}),
    dash_table.DataTable(style_data={"textAlign": "left"}, id='table', columns=[{"name": i, "id": i} for i in dc.columns], data=dc.to_dict('records'), style_cell={"backgroundColor": "lightblue"})])
])



@app.callback(Output('graph1', 'figure'),
                [Input('select-bar-category', 'value')])
def bar_update_figure(selected_category):
    bar_filtered_df = df[df['Category'] == selected_category]
    bar_filtered_df = bar_filtered_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    bar_new_df = bar_filtered_df.groupby(['Name'])['Total Revenue'].sum().reset_index()
    bar_new_df = bar_new_df.sort_values(by=['Total Revenue'], ascending=[False])
    data_interactive_barchart = [go.Bar(x=bar_new_df['Name'], y=bar_new_df['Total Revenue'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Total Revenue for ' +selected_category+ ' charities', xaxis={'title': 'Name of Charity'}, yaxis={'title': 'Total Revenue'})}

@app.callback(Output('graph2', 'figure'),
                [Input('select-stack-category', 'value')])
def stack_update_figure(selected_category):
    stack_filtered_df = df[df['Category'] == selected_category]
    stack_filtered_df = stack_filtered_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    stack_filtered_df["Other Revenue"] = stack_filtered_df["Total Revenue"] - stack_filtered_df["Private Donations"]
    stack_new_df = stack_filtered_df.groupby(['Name']).agg({"Total Revenue": "sum", "Private Donations": "sum", "Other Revenue": "sum"}).reset_index()
    stack_new_df = stack_new_df.sort_values(by=['Total Revenue'], ascending=[False])
    trace1_stackbarchart = go.Bar(x=stack_new_df["Name"], y=stack_new_df["Private Donations"], name="Donations",
    marker={"color": "#FFD700"})
    trace2_stackbarchart = go.Bar(x=stack_new_df["Name"], y=stack_new_df["Other Revenue"], name="Other Revenue",
    marker={"color": "#9EA0A1"})
    data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart]
    return {'data': data_stackbarchart, 'layout': go.Layout(title='Total Revenue for ' +selected_category+ ' charities', xaxis={'title': 'Name of Charity'}, yaxis={'title': 'Total Revenue'}, barmode = 'stack')}

@app.callback(Output('graph3', 'figure'),
                [Input('select-line-category', 'value')])
def line_update_figure(selected_category):
    line_filtered_df = df[df['Category'] == selected_category]
    line_new_df = line_filtered_df.groupby(["Name"]).agg({"Fundraising Efficiency %": "max"}).reset_index()
    data_linechart = [go.Scatter(x=line_new_df['Name'], y=line_new_df['Fundraising Efficiency %'], mode='lines', name='Temp')]
    return {'data': data_linechart, 'layout': go.Layout(title='Fundraising Efficiency for ' +selected_category+ ' charities', xaxis={'title': 'Name of Charity'}, yaxis={'title': 'Fundraising Efficiency %'})}

@app.callback(Output('graph4', 'figure'),
                [Input('select-multi-category', 'value')])
def multi_update_figure(selected_category):
    multi_filtered_df = df[df['Category'] == selected_category]
    multi_new_df = multi_filtered_df.groupby(["Name"]).agg({"Fundraising Efficiency %": "max", "Charitible Commitment %": "max"}).reset_index()
    trace1_multiline = go.Scatter(x=multi_new_df["Name"], y=multi_new_df["Fundraising Efficiency %"], mode="lines", name="Fundraising Efficiency %")
    trace2_multiline = go.Scatter(x=multi_new_df["Name"], y=multi_new_df["Charitible Commitment %"], mode="lines", name="Charitible Commitment %")
    data_multiline = [trace1_multiline,trace2_multiline]
    return {'data': data_multiline, 'layout': go.Layout(title='Fundraising Efficiency vs Charitible Commitment for ' +selected_category+ ' charities', xaxis={'title': 'Name of Charity'}, yaxis={'title': 'Fundraising Efficiency and Charitible Commitment %'})}

@app.callback(Output('graph5', 'figure'),
                [Input('select-heat-category', 'value')])
def heat_update_figure(selected_category):
    heat_filtered_df = df[df['Category'] == selected_category]
    data_heatmap = [go.Heatmap(x=heat_filtered_df["Name"],y=heat_filtered_df["Category"],z=heat_filtered_df["Private Donations"].values.tolist(),colorscale="Jet")]
    return {'data': data_heatmap, 'layout': go.Layout(title='Private Donation Amounts for ' +selected_category+ ' charities', xaxis={'title': 'Name of Charity'}, yaxis={'title': 'Category'})}

def table_dash():
    return {'data': dc}

if __name__ == '__main__':
        app.run_server()