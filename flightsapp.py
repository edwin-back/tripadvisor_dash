import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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

# Main App Layout
app.layout = html.Div(className='container', children=[
    html.Br(),
    # App Header
    html.H1('Scraping Outbound NYC Tripadvisor Flights', style={'textAlign': 'center'}),
    html.Hr(),
    html.H4(children=['Developed By ',
                      html.A(children='Edwin Back', href='https://edwinback.vercel.app/', target='_blank'),
                      ' | ', html.A(children='LinkedIn', href='https://linkedin.com/in/edwin-back/', target='_blank')]),

    html.H5('Data Extracted on January 26, 2020 (Pre-COVID19)'),
    html.Br(),
    html.Br(),

    # Average Daily Flight Prices
    html.H2("Average Daily NYC Flight Prices"),
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
    html.Div(id='output_container_1', children=[]),
    html.Br(),

    dcc.Graph(id='daily_flight_prices', figure={}),
    html.Br(),
    html.Br(),
    html.Br(),

    # Monthly Flight Prices
    html.H2("Average Monthly NYC Flight Prices"),
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
    html.Div(id='output_container_2', children=[]),
    html.Br(),

    dcc.Graph(id='monthly_flight_prices', figure={}),
    html.Br(),

    # Flight Prices by Day of the Week
    html.H2("Flight Price Distribution by Day of the Week"),
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

    # Flight Ratings by Day of the Week
    html.H2("Flight Ratings Distribution by Day of the Week"),
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


# Daily Flight Prices
@app.callback(
    [Output(component_id='output_container_1', component_property='children'),
     Output(component_id='daily_flight_prices', component_property='figure')],
    [Input(component_id='slct_airport_daily', component_property='value')]
)
def update_daily(slct_airport_daily):
    flights1 = flights.copy()
    flights1 = flights1[flights1.destination.isin(slct_airport_daily)]
    flights1 = flights1.groupby('departure_date').agg({'price': 'mean'}).reset_index()

    container = "The following destinations are selected: {}".format(slct_airport_daily)

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
            b=30,
            t=25,
            pad=3
        )
    )

    return container, fig1

# Monthly Flight Prices
@app.callback(
    [Output(component_id='output_container_2', component_property='children'),
     Output(component_id='monthly_flight_prices', component_property='figure')],
    [Input(component_id='slct_airport_monthly', component_property='value')]
)
def update_monthly(slct_airport_monthly):
    flights2 = flights.copy()
    flights2 = flights2[flights2.destination.isin(slct_airport_monthly)]
    flights2 = flights2[flights2.mo_name != 'Jan'].groupby('mo_name').agg({'price': 'mean'}).reset_index().sort_values('price')

    container = "The following destinations are selected: {}".format(slct_airport_monthly)
    colors = ['rgb(26, 118, 255)'] * 11
    colors[0] = 'LightGreen'
    colors[-1] = 'Crimson'

    fig2 = go.Figure(
        go.Bar(x=flights2["mo_name"],
               y=round(flights2["price"], 2)
               )
    )

    fig2.update_traces(marker_color=colors, opacity=0.6)
    fig2.update_layout(
        title={
            'text': "Average Monthly Flight Prices Departing NYC",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis=dict(
            title="",
            categoryorder='array',
            categoryarray=['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ),
        yaxis=dict(
            title="Average Monthly Price (USD)",
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
        height=550,
        margin=dict(
            l=125,
            r=125,
            b=100,
            t=100,
            pad=4
        )
    )

    return container, fig2

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
        title={
            'text': "Price Distribution by Day of the Week",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
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
        height=550,
        margin=dict(
            l=125,
            r=125,
            b=100,
            t=100,
            pad=4
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
        title={
            'text': "Rating Distribution by Day of the Week",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
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
        height=550,
        margin=dict(
            l=125,
            r=125,
            b=100,
            t=100,
            pad=4
        )
    )

    return container4, container6, fig4

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
