import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Custom CSS styles to enhance the appearance
st.markdown(
    """
    <style>
    .big-font {
        font-size: 24px !important;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .custom-padding {
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    df = pd.read_csv('covid_19_cleaned dataset.csv')

    st.title('COVID-19 Dashboard')

    # Create a layout with two columns in each row with custom padding
    col1, col2 = st.columns(2)
    with col1:
        st.header('Missing Values Heatmap')
        display_heatmap(df)
    with col2:
        st.header('Pie Chart: COVID-19 Data')
        display_pie_chart()

    # Create a new row with two columns and custom padding
    col3, col4 = st.columns(2)
    with col3:
        st.header('Confirmed Cases by Region')
        display_confirmed_cases_line_plot(df)
    with col4:
        st.header('Cured Cases by Region')
        display_cured_cases_bar_chart(df)

    # Create a new row with two columns and custom padding
    col5, col6 = st.columns(2)
    with col5:
        st.header('Heatmap of Selected Features')
        display_selected_features_heatmap(df)
    with col6:
        st.header('Death Cases by Region')
        display_death_cases_bar_chart(df)

    # Create a new row with two columns and custom padding
    col7, col8 = st.columns(2)
    with col7:
        st.header('Scatter Plot: Relationship between Total Individuals and Vaccine Types')
        display_vaccine_scatter_plot(df)

def display_heatmap(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.isnull(), cmap='viridis', cbar=True, ax=ax)
    st.pyplot(fig)

def display_pie_chart():
    data = {"State": ["Confirmed", "Deaths", "Cured"],
            "Values": [481664691, 8346196, 384032915],
            "labels": ["Confirmed", "Deaths", "Recovered"]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df["Values"], labels=df["labels"], autopct='%1.1f%%')
    ax.axis('equal')
    st.pyplot(fig)

def display_confirmed_cases_line_plot(df):
    df = pd.read_csv("covid_19_cleaned dataset.csv")

    # Sort the DataFrame by State/UnionTerritory
    df = df.sort_values(by="State/UnionTerritory")

    # Extract the top 20 confirmed cases and corresponding regions
    confirmed_cases = df["Confirmed"].head(20)
    regions = df["State/UnionTerritory"].sample(20)
    regions = regions.astype(str)

    # Create the horizontal bar chart
    fig, ax = plt.subplots()
    ax.barh(regions, confirmed_cases)

    # Add labels and title
    ax.set_xlabel("Confirmed Cases")
    ax.set_ylabel("Region")
    ax.set_title("Confirmed Cases by Region")

    # Rotate the x-axis labels for readability
    plt.xticks(rotation=90)

    # Display the plot using st.pyplot()
    st.pyplot(fig)

def display_cured_cases_bar_chart(df):
     df = pd.read_csv("covid_19_cleaned dataset.csv")

    # Sort the DataFrame by State/UnionTerritory
     df = df.sort_values(by="State/UnionTerritory")

    # Extract a sample of 1000 cured cases and corresponding regions
     cured_cases = df["Cured"].sample(50)
     regions = df["State/UnionTerritory"].sample(50)
     regions = regions.astype(str)

    # Create the horizontal bar chart
     fig, ax = plt.subplots()
     ax.barh(regions, cured_cases)

    # Add labels and title
     ax.set_xlabel("Cured Cases")
     ax.set_ylabel("Region")
     ax.set_title("Cured Cases by Region")

    # Rotate the x-axis labels for readability
     plt.xticks(rotation=90)

    # Display the plot using st.pyplot()
     st.pyplot(fig)

def display_selected_features_heatmap(df):
    
    data = pd.read_csv('covid_19_cleaned dataset.csv')

    # Select the columns you want to use for the heatmap
    selected_columns = [' Covaxin (Doses Administered)', 'CoviShield (Doses Administered)', 'Sputnik V (Doses Administered)']

    # Create a subset of the data with the selected columns
    data_subset = data[selected_columns]

    # Calculate the correlation matrix
    correlation_matrix = data_subset.corr()

    # Configure the heatmap style
    sns.set_theme(style="white")

    # Generate the heatmap
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)

    # Add a title and labels
    plt.title("Heatmap of Selected Features")
    plt.xlabel("Features")
    plt.ylabel("Features")

    # Display the heatmap using st.pyplot()
    st.pyplot(fig)

def display_death_cases_bar_chart(df):
      df = pd.read_csv("covid_19_cleaned dataset.csv")

    # Sort the DataFrame by State/UnionTerritory
      df = df.sort_values(by="State/UnionTerritory")

    # Extract the top 20 death cases and corresponding regions
      death_cases = df["Deaths"].head(20)
      regions = df["State/UnionTerritory"].sample(20)
      regions = regions.astype(str)

    # Create the horizontal bar chart
      fig, ax = plt.subplots()
      ax.barh(regions, death_cases)

    # Add labels and title
      ax.set_xlabel("Death Cases")
      ax.set_ylabel("Region")
      ax.set_title("Death Cases by Region")

    # Rotate the x-axis labels for readability
      plt.xticks(rotation=90)

    # Display the plot using st.pyplot()
      st.pyplot(fig)

def display_vaccine_scatter_plot(df):
    data = pd.read_csv('covid_19_cleaned dataset.csv')

    # Select the relevant columns
    total_individuals_column = 'Total Individuals Vaccinated'
    covaxin_column = ' Covaxin (Doses Administered)'
    covishield_column = 'CoviShield (Doses Administered)'
    sputnikv_column = 'Sputnik V (Doses Administered)'

    # Create the scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot Covaxin vs Total Individuals
    ax.scatter(data[total_individuals_column], data[covaxin_column], label='Covaxin')

    # Plot Covishield vs Total Individuals
    ax.scatter(data[total_individuals_column], data[covishield_column], label='Covishield')

    # Plot SputnikV vs Total Individuals
    ax.scatter(data[total_individuals_column], data[sputnikv_column], label='SputnikV')

    # Add labels and title
    ax.set_xlabel('Total Individuals Vaccinated')
    ax.set_ylabel('Number of Doses Administered')
    ax.set_title('Scatter Plot: Relationship between Total Individuals and Vaccine Types')

    # Add legend
    ax.legend()

    # Display the plot using st.pyplot()
    st.pyplot(fig)

if __name__ == '_main_':
    main()