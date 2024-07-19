import pandas as pd
import plotly.express as px
import panel as pn

# Load the data
df = pd.read_csv('/Users/elisabethtrujillo/Desktop/ASU_Bootcamp/Project_3/Project-3/Music_mentalhealth.csv')

# Select only the columns of interest
columns_of_interest = ['Age', 'While working', 'Foreign languages', 'Composer']
df_small = df[columns_of_interest]

# Categorize ages into groups for filtering
bins = [13, 18, 25, 31, 41, 51, 61, 71, 81, 91, 101]
labels = ['13-17', '18-24', '25-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
df_small['Age Group'] = pd.cut(df_small['Age'], bins=bins, labels=labels, right=False)

# Create a filter widget for age groups
age_filter = pn.widgets.Select(name='Age Group', options=labels, value='18-24')

# Function to count responses for each question based on selected age group
def get_counts(age_group):
    filtered_df = df_small[df_small['Age Group'] == age_group]
    
    work_counts = filtered_df['While working'].value_counts().reset_index()
    work_counts.columns = ['While working', 'Count']

    foreign_counts = filtered_df['Foreign languages'].value_counts().reset_index()
    foreign_counts.columns = ['Foreign languages', 'Count']

    compose_counts = filtered_df['Composer'].value_counts().reset_index()
    compose_counts.columns = ['Composer', 'Count']
    
    return work_counts, foreign_counts, compose_counts

# Create initial pie charts
initial_work_counts, initial_foreign_counts, initial_compose_counts = get_counts(age_filter.value)

fig_work = px.pie(
    initial_work_counts,
    names='While working',
    values='Count',
    title='Do you listen to music while working?'
)

fig_foreign = px.pie(
    initial_foreign_counts,
    names='Foreign languages',
    values='Count',
    title='Do you listen to foreign music?'
)

fig_compose = px.pie(
    initial_compose_counts,
    names='Composer',
    values='Count',
    title='Do you compose music?'
)

# Convert Plotly figures to Panel objects
plot_work = pn.pane.Plotly(fig_work)
plot_foreign = pn.pane.Plotly(fig_foreign)
plot_compose = pn.pane.Plotly(fig_compose)

# Update plots when the age filter changes
def update_plots(event):
    work_counts, foreign_counts, compose_counts = get_counts(event.new)
    
    # Create new figures with updated data
    fig_work = px.pie(
        work_counts,
        names='While working',
        values='Count',
        title='Do you listen to music while working?'
    )
    
    fig_foreign = px.pie(
        foreign_counts,
        names='Foreign languages',
        values='Count',
        title='Do you listen to foreign music?'
    )
    
    fig_compose = px.pie(
        compose_counts,
        names='Composer',
        values='Count',
        title='Do you compose music?'
    )
    
    # Update plot objects
    plot_work.object = fig_work
    plot_foreign.object = fig_foreign
    plot_compose.object = fig_compose

# Watch the age_filter for changes
age_filter.param.watch(update_plots, 'value')

# Create a layout with the filter and charts
layout = pn.Column(age_filter, plot_work, plot_foreign, plot_compose)

# Mark the layout as servable
layout.servable()

# Optionally, save layout as an HTML file to check if it renders correctly
layout.save('/Users/elisabethtrujillo/Desktop/ASU_Bootcamp/Project_3/Project-3/test_dashboard.html')
