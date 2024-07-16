import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Create connection string with your credentials
conn_string = 'postgresql://postgres:Welcome%402024@localhost/music_mentalhealth'

# Create SQLAlchemy engine
engine = create_engine(conn_string)

# Load data from PostgreSQL
df = pd.read_sql('SELECT * FROM music_data', engine)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Music and Mental Health Analysis"),
    
    dcc.Tabs([
        dcc.Tab(label='Music Genre Preferences', children=[
            html.Div([
                dcc.Graph(id='genre-distribution'),
                dcc.Graph(id='genre-age')
            ])
        ]),
        dcc.Tab(label='Mental Health Analysis', children=[
            html.Div([
                html.Label('Select Mental Health Issue:'),
                dcc.Dropdown(
                    id='mental-health-dropdown',
                    options=[
                        {'label': 'Anxiety', 'value': 'Anxiety'},
                        {'label': 'Depression', 'value': 'Depression'},
                        {'label': 'Insomnia', 'value': 'Insomnia'},
                        {'label': 'OCD', 'value': 'OCD'}
                    ],
                    value='Anxiety'
                ),
                dcc.Graph(id='mental-health-age'),
                dcc.Graph(id='mental-health-distribution')
            ])
        ]),
        dcc.Tab(label='Correlation Analysis', children=[
            html.Div([
                dcc.Graph(id='genre-mental-health-correlation'),
                dcc.Graph(id='frequency-mental-health-severity')
            ])
        ])
    ])
])

# Define callback to update Music Genre Preferences
@app.callback(
    Output('genre-distribution', 'figure'),
    Output('genre-age', 'figure'),
    Input('genre-distribution', 'id')
)
def update_genre_preferences(_):
    # Distribution of favorite music genres
    genre_counts = df['Fav genre'].value_counts().reset_index()
    genre_counts.columns = ['Genre', 'Count']
    fig1 = px.bar(genre_counts, x='Genre', y='Count', title='Distribution of Favorite Music Genres')
    
    # Preference for music genres by age
    fig2 = px.histogram(df, x='Age', color='Fav genre', title='Music Genre Preferences by Age', barmode='group')
    
    return fig1, fig2

# Define callback to update Mental Health Analysis
@app.callback(
    Output('mental-health-age', 'figure'),
    Output('mental-health-distribution', 'figure'),
    Input('mental-health-dropdown', 'value')
)
def update_mental_health_analysis(selected_issue):
    # Mental health issues by age
    fig1 = px.histogram(df, x='Age', y=selected_issue, title=f'{selected_issue} by Age', color='Age', nbins=20)
    
    # Distribution of selected mental health issue
    issue_counts = df[selected_issue].value_counts().reset_index()
    issue_counts.columns = ['Severity', 'Count']
    fig2 = px.bar(issue_counts, x='Severity', y='Count', title=f'Distribution of {selected_issue} Severity')
    
    return fig1, fig2

# Define callback to update Correlation Analysis
@app.callback(
    Output('genre-mental-health-correlation', 'figure'),
    Output('frequency-mental-health-severity', 'figure'),
    Input('genre-mental-health-correlation', 'id')
)
def update_correlation_analysis(_):
    # Correlation between favorite music genres and mental health issues
    correlation_data = df[['Fav genre', 'Anxiety', 'Depression', 'Insomnia', 'OCD']]
    correlation_data = correlation_data.melt(id_vars=['Fav genre'], var_name='Mental Health Issue', value_name='Severity')
    fig1 = px.scatter(correlation_data, x='Fav genre', y='Severity', color='Mental Health Issue', title='Correlation Between Favorite Music Genres and Mental Health Issues')
    
    # Severity of mental health issues by frequency of listening to different genres
    frequency_columns = [col for col in df.columns if col.startswith('Frequency')]
    frequency_data = df[['Fav genre'] + frequency_columns + ['Anxiety', 'Depression', 'Insomnia', 'OCD']]
    frequency_data = frequency_data.melt(id_vars=['Fav genre'] + frequency_columns, var_name='Mental Health Issue', value_name='Severity')
    fig2 = px.box(frequency_data, x='value', y='Severity', color='Fav genre', facet_col='Mental Health Issue', title='Severity of Mental Health Issues by Listening Frequency')
    
    return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)