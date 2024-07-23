# Ceate Code for Overall Stats
import pandas as pd
import plotly.express as px
import panel as pn

# Load the data
df = pd.read_csv('/Users/elisabethtrujillo/Desktop/ASU_Bootcamp/Project_3/Project-3/Music_mentalhealth.csv')

# Select only the columns of interest
columns_of_interest = ['While working', 'Foreign languages', 'Composer']
df_small = df[columns_of_interest]

# Function to count responses for each question
def get_overall_counts():
    work_counts = df_small['While working'].value_counts().reset_index()
    work_counts.columns = ['While working', 'Count']

    foreign_counts = df_small['Foreign languages'].value_counts().reset_index()
    foreign_counts.columns = ['Foreign languages', 'Count']

    compose_counts = df_small['Composer'].value_counts().reset_index()
    compose_counts.columns = ['Composer', 'Count']
    
    return work_counts, foreign_counts, compose_counts





# Create pie charts for the overall data
overall_work_counts, overall_foreign_counts, overall_compose_counts = get_overall_counts()

fig_work = px.pie(
    overall_work_counts,
    names='While working',
    values='Count',
    title='Overall: Do you listen to music while working?'
)

fig_foreign = px.pie(
    overall_foreign_counts,
    names='Foreign languages',
    values='Count',
    title='Overall: Do you listen to foreign music?'
)

fig_compose = px.pie(
    overall_compose_counts,
    names='Composer',
    values='Count',
    title='Overall: Do you compose music?'
)

# Convert Plotly figures to Panel objects
plot_work = pn.pane.Plotly(fig_work)
plot_foreign = pn.pane.Plotly(fig_foreign)
plot_compose = pn.pane.Plotly(fig_compose)

# Create a layout with the charts
layout = pn.Column(plot_work, plot_foreign, plot_compose)


layout.servable()

layout.save('/Users/elisabethtrujillo/Desktop/ASU_Bootcamp/Project_3/Project-3/overall_dashboard.html')