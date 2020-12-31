import pandas as pd
import numpy as np
import scipy.stats as st

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px


# Styling
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initiate app and server
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Import and Cleanse Data
flights = pd.read_csv('./assets/flights_departing_nyc.csv')

# Convert values to DT
flights.departure_date = pd.to_datetime(flights.departure_date)
flights.arrival_date = pd.to_datetime(flights.arrival_date)
flights.depart_time = pd.to_timedelta(flights.depart_time)
flights.arrival_time = pd.to_timedelta(flights.arrival_time)

all_destinations = flights.destination.unique()
all_airlines = flights.airline.unique()

# Main App Layout
app.layout = html.Div(className='container', children=[
    html.Br(),
    # App Header
    html.H1('Scraping Outbound NYC Tripadvisor Flights', style={'textAlign': 'center'}),
    html.Hr(),
    html.Br(),

    html.Div(style={'textAlign': 'center', 'marginBottom': '5em'},
             children=[html.H4(children=['Developed By ',
                                         html.A(children='Edwin Back', href='https://edwinback.vercel.app/',
                                                target='_blank'),
                                         ' | ', html.A(children='LinkedIn', href='https://linkedin.com/in/edwin-back/',
                                                       target='_blank')]),
                       html.H5('Data Extracted on January 26, 2020 (Pre-COVID19)')]),


    # Average Daily Flight Prices
    html.Hr(),
    html.H2(children="Average Daily NYC Flight Prices", style={'textAlign': 'center'}),
    html.Hr(),

    html.H3("Select Destination(s)"),
    dcc.Dropdown(id="slct_airport_daily",
                 options=[
                     {"label": "Montreal, CAN (YUL)", "value": 'YUL'},
                     {"label": "Los Angeles (LAX)", "value": 'LAX'},
                     {"label": "Miami (MIA)", "value": 'MIA'},
                     {"label": "Chicago (ORD)", "value": 'ORD'},
                     {"label": "San Juan, PR (SJU)", "value": 'SJU'}],
                 multi=True,
                 value=['LAX', 'MIA', 'ORD'],
                 style={'width': "75%"}
                 ),
    html.Br(),
    html.Br(),

    html.Div(id='output_container_1a', children=[]),
    html.Br(),

    html.Div(id='output_container_1b', children=[]),
    html.Br(),

    dcc.Graph(id='daily_flight_prices', figure={}),

    # Average MONTHLY Flight Prices
    html.Hr(style={'marginTop': '6em'}),
    html.H2(children="Average Monthly NYC Flight Prices", style={'textAlign': 'center'}),
    html.Hr(),

    html.H3("Select Destination(s)"),
    dcc.Dropdown(id="slct_airport_monthly",
                 options=[
                     {"label": "Montreal (YUL)", "value": 'YUL'},
                     {"label": "Los Angeles (LAX)", "value": 'LAX'},
                     {"label": "Miami (MIA)", "value": 'MIA'},
                     {"label": "Chicago (ORD)", "value": 'ORD'},
                     {"label": "San Juan, PR (SJU)", "value": 'SJU'}],
                 multi=True,
                 value=['LAX', 'MIA', 'ORD'],
                 style={'width': "75%"}
                 ),

    html.Br(),

    html.Div(id='output_container_2a', children=[]),
    html.Br(),

    html.Div(id='output_container_2b', children=[]),
    html.Br(),

    dcc.Graph(id='monthly_flight_prices_2a', figure={}),
    html.Br(),

    dcc.Graph(id='monthly_flight_prices', figure={}),
    html.Br(),
    html.Br(),

    # Flight Prices by Day of the Week
    html.Hr(),
    html.H2(children="Flight Price Distribution by Day of the Week", style={'textAlign': 'center'}),
    html.Hr(),

    html.H3("Select Destination(s)"),
    dcc.Dropdown(id="slct_airport_price_dow",
                 options=[
                     {"label": "Montreal (YUL)", "value": 'YUL'},
                     {"label": "Los Angeles (LAX)", "value": 'LAX'},
                     {"label": "Miami (MIA)", "value": 'MIA'},
                     {"label": "Chicago (ORD)", "value": 'ORD'},
                     {"label": "San Juan, PR (SJU)", "value": 'SJU'}],
                 multi=True,
                 value=['LAX', 'MIA', 'ORD', 'SJU', 'YUL'],
                 style={'width': "75%"}
                 ),
    html.Br(),

    html.Div(id='output_container_3', children=[]),
    html.Br(), html.Br(),

    html.H3("Select Airline(s)"),
    dcc.Dropdown(id="slct_airline_prices",
                     options=[
                         {"label": "Air Canada", "value": 'Air Canada'},
                         {"label": "Alaska", "value": 'Alaska'},
                         {"label": "American", "value": 'American'},
                         {"label": "Frontier", "value": 'Frontier'},
                         {"label": "Jet Blue", "value": 'JetBlue'},
                         {"label": "Spirit", "value": 'Spirit'},
                         {"label": "United", "value": 'United'},
                         {"label": "West Jet", "value": 'WestJet'}],
                     multi=True,
                     value=['Air Canada', 'Alaska', 'American', 'Frontier', 'JetBlue', 'Spirit', 'United', 'WestJet'],
                     style={'width': "75%"}
                     ),
    html.Br(),
    html.Div(id='output_container_5', children=[]),
    html.Br(), html.Br(),

    dcc.Graph(id='prices_dow', figure={}),
    html.Br(),
    html.Br(),
    html.Br(),

    # Flight Ratings by Day of the Week
    html.Hr(),
    html.H2(children="Flight Ratings Distribution by Day of the Week", style={'textAlign': 'center'}),
    html.Hr(),
    html.H3("Select Destination(s)"),
    dcc.Dropdown(id="slct_airport_rating_dow",
                 options=[
                     {"label": "Montreal (YUL)", "value": 'YUL'},
                     {"label": "Los Angeles (LAX)", "value": 'LAX'},
                     {"label": "Miami (MIA)", "value": 'MIA'},
                     {"label": "Chicago (ORD)", "value": 'ORD'},
                     {"label": "San Juan, PR (SJU)", "value": 'SJU'}],
                 multi=True,
                 value=['LAX', 'MIA', 'ORD', 'SJU', 'YUL'],
                 style={'width': "75%"}
                 ),

    html.Br(),
    html.Div(id='output_container_4', children=[]),
    html.Br(), html.Br(),

    html.H3("Select Airline(s)"),
    dcc.Dropdown(id="slct_airline_ratings",
                 options=[
                     {"label": "Air Canada", "value": 'Air Canada'},
                     {"label": "Alaska", "value": 'Alaska'},
                     {"label": "American", "value": 'American'},
                     {"label": "Frontier", "value": 'Frontier'},
                     {"label": "Jet Blue", "value": 'JetBlue'},
                     {"label": "Spirit", "value": 'Spirit'},
                     {"label": "United", "value": 'United'},
                     {"label": "West Jet", "value": 'WestJet'}],
                 multi=True,
                 value=['Air Canada', 'Alaska', 'American', 'Frontier', 'JetBlue', 'Spirit', 'United', 'WestJet'],
                 style={'width': "75%"}
                 ),

    html.Br(),
    html.Div(id='output_container_6', children=[]),

    dcc.Graph(id='ratings_dow', figure={})
])


# Average Daily Flight Prices
@app.callback(
    [Output(component_id='output_container_1a', component_property='children'),
     Output(component_id='output_container_1b', component_property='children'),
     Output(component_id='daily_flight_prices', component_property='figure')],
    [Input(component_id='slct_airport_daily', component_property='value')]
)

def update_daily(slct_airport_daily):
    flights1 = flights.copy()
    flights1 = flights1[flights1.destination.isin(slct_airport_daily)]

    total_flights = len(flights1.index)

    data = flights1["price"]
    confidence_interval = st.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data))
    confidence_interval_r = (round(confidence_interval[0], 2), round(confidence_interval[1], 2))

    container1a = "Total Number of Flights: {}".format(total_flights)
    container1b = "95% Confidence Interval: {}".format(confidence_interval_r)

    flights1 = flights1.groupby('departure_date').agg({'price': 'mean'}).reset_index()

    fig1 = go.Figure(go.Scatter(x=flights1["departure_date"], y=round(flights1["price"], 2)))

    fig1.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=9, label="9m", step="month", stepmode="backward"),
                dict(label="All", step="all")
            ])
        )
    )

    fig1.update_layout(
        xaxis_title="Full Datetime Range (01/27/20 through 12/21/20)",
        yaxis=dict(
            title="Average Price ($USD)",
            tickmode='linear',
            tick0=50,
            dtick=50,
            tickprefix='$'
        ),
        font=dict(
            family="Verdana, monospace",
            size=14,
            color="#7f7f7f"
        ),
        height=500,
        margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=1
        )
    )

    return container1a, container1b, fig1

# Average Monthly Flight Prices
@app.callback(
    [Output(component_id='output_container_2a', component_property='children'),
     Output(component_id='output_container_2b', component_property='children'),
     Output(component_id='monthly_flight_prices', component_property='figure'),
     Output(component_id='monthly_flight_prices_2a', component_property='figure')],
    [Input(component_id='slct_airport_monthly', component_property='value')]
)

def update_monthly(slct_airport_monthly):
    flights2 = flights.copy()
    flights2 = flights2[flights2.destination.isin(slct_airport_monthly)]

    total_flights = len(flights2.index)

    data = flights2["price"]
    confidence_interval = st.t.interval(alpha=0.95, df=len(data) - 1, loc=np.mean(data), scale=st.sem(data))
    confidence_interval_r = (round(confidence_interval[0], 2), round(confidence_interval[1], 2))

    standev = st.tstd(data)

    container2a = "Total Flights Available: {}".format(total_flights)
    container2b = "95% Confidence Interval: {}".format(confidence_interval_r)

    # blue bars
    colors = ['rgb(26, 118, 255)'] * 11
    # convert smallest value to green
    colors[0] = 'LightGreen'
    # convert largest value to red
    colors[-1] = 'Crimson'

    # Bar chart
    flights2a = flights2[flights2.mo_name != 'Jan'].groupby('mo_name').agg({'price': 'mean'}).reset_index().sort_values('price')

    fig2a = go.Figure(
        go.Bar(x=flights2a["mo_name"],
               y=round(flights2a["price"], 2)
               )
    )

    fig2a.update_traces(marker_color=colors, opacity=0.6)
    fig2a.update_layout(
        xaxis=dict(
            title="",
            categoryorder='array',
            categoryarray=['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ),
        yaxis=dict(
            title="Average Price Per Flight ($USD)",
            tickmode='linear',
            tick0=0,
            dtick=25,
            tickprefix='$'
        ),
        font=dict(
            family="Verdana, monospace",
            size=14,
            color="#7f7f7f"
        ),
        height=500,
        margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=1
        )
    )

    # Scatter plot
    flights2b = flights2[flights2.mo_name != 'Jan'].groupby(['destination', 'mo_name', 'month']).agg({'price': 'mean'}).reset_index().sort_values('month')

    fig2b = px.line(flights2b,
                    x=flights2b["mo_name"],
                    y=round(flights2b["price"], 2),
                    color='destination'
    )

    fig2b.update_traces(mode = 'markers+lines')

    fig2b.update_layout(
        xaxis=dict(
            title="",
            categoryorder='array',
            categoryarray=['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ),
        yaxis=dict(
            title="Average Price Per Flight ($USD)",
            tickmode='linear',
            tick0=0,
            dtick=25,
            tickprefix='$'
        ),
        font=dict(
            family="Verdana, monospace",
            size=14,
            color="#7f7f7f"
        ),
        height=500,
        margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=1
        )
    )

    return container2a, container2b, fig2a, fig2b

# Flight Prices by Day of the Week
@app.callback(
    [Output(component_id='output_container_3', component_property='children'),
     Output(component_id='output_container_5', component_property='children'),
     Output(component_id='prices_dow', component_property='figure')],
    [Input(component_id='slct_airport_price_dow', component_property='value'),
     Input(component_id='slct_airline_prices', component_property='value')]
)

def update_price_dow(slct_airport_price_dow, slct_airline_prices):
    flights3 = flights.copy()
    flights3 = flights3[flights3.price <= 500]

    filter1 = flights3.destination.isin(slct_airport_price_dow)
    filter2 = flights3.airline.isin(slct_airline_prices)
    flights3 = flights3[filter1 & filter2]

    container3 = "The following destinations are selected: {}".format(slct_airport_price_dow)
    container5 = "The following airlines are selected: {}".format(slct_airline_prices)

    fig3 = go.Figure()

    fig3 = fig3.add_trace(go.Box(
        y=flights3.price,
        x=flights3.day_of_week,
        marker_color='indianred'
    ))

    fig3 = fig3.update_layout(
        xaxis=dict(
            title="",
            categoryorder='array',
            categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        ),
        yaxis=dict(
            title="Flight Price ($USD)",
            tickmode='linear',
            tick0=0,
            dtick=50,
            tickprefix='$'
        ),
        font=dict(
            family="Verdana, monospace",
            size=14,
            color="#7f7f7f"
        ),
        height=500,
        margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=1
        )
    )

    return container3, container5, fig3

# Flight Ratings by Day of the Week
@app.callback(
    [Output(component_id='output_container_4', component_property='children'),
     Output(component_id='output_container_6', component_property='children'),
     Output(component_id='ratings_dow', component_property='figure')],
    [Input(component_id='slct_airport_rating_dow', component_property='value'),
     Input(component_id='slct_airline_ratings', component_property='value')]
)
def update_rating_dow(slct_airport_rating_dow, slct_airline_ratings):
    flights4 = flights.copy()
    flights4 = flights4[flights4.price <= 500]

    filter1 = flights4.destination.isin(slct_airport_rating_dow)
    filter2 = flights4.airline.isin(slct_airline_ratings)
    flights4 = flights4[filter1 & filter2]

    container4 = "The following destinations are selected: {}".format(slct_airport_rating_dow)
    container6 = "The following airlines are selected: {}".format(slct_airline_ratings)

    fig4 = go.Figure()

    fig4 = fig4.add_trace(go.Box(
        y=flights4.fly_score,
        x=flights4.day_of_week,
        marker_color='#FF851B'
    ))

    fig4 = fig4.update_layout(
        xaxis=dict(
            title="",
            categoryorder='array',
            categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        ),
        yaxis=dict(
            title="Flight Rating (0 to 10)",
            tickmode='linear',
            tick0=5,
            dtick=0.5
        ),
        font=dict(
            family="Verdana, monospace",
            size=14,
            color="#7f7f7f"
        ),
        height=500,
        margin=dict(
            l=25,
            r=25,
            b=25,
            t=25,
            pad=1
        )
    )

    return container4, container6, fig4

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
