# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

launch_sites = spacex_df['Launch Site'].unique()
options = [{'label': 'All Sites', 'value': 'ALL'}]

for l in launch_sites:
    option = {'label':l, 'value':l}
    options.append(option)

  

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                 dcc.Dropdown(id='site-dropdown',
                                options=options,
                                value='ALL',
                                placeholder="Launch Site Selection",
                                searchable=True
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                dcc.RangeSlider(id='payload-slider',
                                min=0, max=10000, step=1000,    
                                value=[0, 10000]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    print(entered_site+' ......................')
    if entered_site == 'ALL':
        all_df = spacex_df.groupby(['class', 'Launch Site'], as_index=False)['class'].sum()

        print(all_df)
        fig = px.pie(all_df, values='class', 
        names='Launch Site', 
        title='All Success Pie Chart', 
        color_discrete_sequence=px.colors.sequential.Cividis_r)
        return fig
    else:
        selected_df = spacex_df[spacex_df['Launch Site']==entered_site]
        total = len(selected_df.index)
        total_success = selected_df['class'].sum()
        selected_site_df = pd.DataFrame()
        selected_site_df['class'] = [0, 1]
        selected_site_df['success']  = [(total - total_success), total_success]      
        
        print(selected_site_df)
        fig = px.pie(selected_site_df, values='success', 
        names='class', 
        title=entered_site+ ' Success Pie Chart', 
        color_discrete_sequence=px.colors.sequential.Cividis_r
        )
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value')
              )
def get_scatter_chart(entered_site, payload_mass):
    filtered_df = spacex_df
    print(entered_site+' ......................')
    if entered_site == 'ALL':
        all_df = spacex_df[spacex_df['Payload Mass (kg)']>=payload_mass[0]]
        all_df = all_df[all_df['Payload Mass (kg)']<=payload_mass[1]]
        fig = px.scatter(all_df, x='Payload Mass (kg)', y='class', 
        color="Booster Version Category", title='All Scatter Chart', 
        color_discrete_sequence=px.colors.sequential.Cividis_r)
        return fig
    else:
        selected_df = spacex_df[spacex_df['Launch Site']==entered_site]
        selected_df = selected_df[selected_df['Payload Mass (kg)']>=payload_mass[0]]
        selected_df = selected_df[selected_df['Payload Mass (kg)']<=payload_mass[1]]
        fig = px.scatter(selected_df, x='Payload Mass (kg)', y='class', 
        color="Booster Version Category", title= entered_site+' Scatter Chart',
        color_discrete_sequence=px.colors.sequential.Cividis_r)
        return fig


# Run the app
if __name__ == '__main__':
    app.run_server(port=8052)
