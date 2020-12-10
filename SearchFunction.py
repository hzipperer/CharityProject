import random
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_table import DataTable
from dash.exceptions import PreventUpdate
import pandas as pd

df = pd.read_csv('../CharityProject/CharityInfo.csv')
df['Category'] = df['Category'].astype('category')
df['Name'] = df['Name'].astype('object')

def get_str_dtype(df, col):
    """Return dtype of col in df"""
    dtypes = ['category', 'object']
    for d in dtypes:
        try:
            if d in str(df.dtypes.loc[col]).lower():
                return d
        except KeyError:
            return None

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Div(id='container_col_select',
                 children=dcc.Dropdown(id='col_select', placeholder= 'Choose Search Criteria...',
                                       options=[{
                                           'label':'Category',
                                           'value': 'Category'},
                                           {'label':'Name',
                                           'value': 'Name'}]),
                 style={'display': 'inline-block', 'width': '30%', 'margin-left': '7%'}),
        # DataFrame filter containers
        html.Div(id='container_cat_filter',
                 children=dcc.Input(id='cat_filter', placeholder= 'Search Categories...')),
        html.Div(id='container_name_filter',
                 children=dcc.Input(id='name_filter', placeholder= 'Search Names...')),
    ]),
    DataTable(id='table',
              columns=[{"name": i, "id": i} for i in df.columns],
              style_cell={'maxWidth': '400px', 'whiteSpace': 'normal'},
              data=df.to_dict("rows"))
])

@app.callback([Output(x, 'style')
               for x in ['container_cat_filter', 'container_name_filter']],
              [Input('col_select', 'value')])
def display_relevant_filter_container(col):
    if col is None:
        return [{'display': 'none'} for i in range(2)]
    dtypes = [['category'], ['object']]
    result = [{'display': 'none'} if get_str_dtype(df, col) not in d
              else {'display': 'inline-block',
                    'margin-left': '7%',
                    'width': '400px'} for d in dtypes]
    return result

@app.callback(Output('table', 'data'),
              [Input('col_select', 'value'),
               Input('cat_filter', 'value'),
               Input('name_filter', 'value')])
def filter_table(col, category, name):
    if all([param is None for param in [col, category, name]]):
        raise PreventUpdate
    if category and (get_str_dtype(df, col) == 'category'):
        dff = df[df[col].str.contains(category, case=False)]
        return dff.to_dict('rows')
    elif name and (get_str_dtype(df, col) == 'object'):
        dff = df[df[col].str.contains(name, case=False)]
        return dff.to_dict('rows')      
    else:
        return df.to_dict('rows')

if __name__ == '__main__':
    app.run_server(debug=True)