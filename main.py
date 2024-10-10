import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """
    Loads the Titanic dataset from a CSV file.

    Args:
    file_path (str): The path to the Titanic dataset CSV file.

    Returns:
    pd.DataFrame: The cleaned Titanic dataset.
    """
    try:
        titanic_df = pd.read_csv(file_path)
        # Clean the dataset by removing unnecessary columns
        titanic_df_clean = titanic_df.drop(columns=[col for col in titanic_df.columns if 'Unnamed' in col])
        return titanic_df_clean
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def calculate_survival_rate(titanic_df):
    """
    Calculates the survival rate of passengers in the Titanic dataset.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    float: The survival rate percentage.
    """
    total_passengers = len(titanic_df)
    survived_passengers = titanic_df['Survived'].sum()
    return (survived_passengers / total_passengers) * 100

def calculate_gender_proportion(titanic_df):
    """
    Calculates the proportion of male and female passengers.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    pd.Series: Proportion of male and female passengers.
    """
    return titanic_df['Sex'].value_counts(normalize=True) * 100

def calculate_class_survival_rate(titanic_df):
    """
    Calculates the survival rate for each passenger class.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    pd.Series: Survival rate for each passenger class.
    """
    return titanic_df.groupby('Pclass')['Survived'].mean() * 100

def count_siblings_spouses_aboard(titanic_df):
    """
    Counts the number of passengers with siblings or spouses aboard.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    int: The number of passengers with siblings or spouses aboard.
    """
    return (titanic_df['SibSp'] > 0).sum()

def calculate_average_fare_by_class(titanic_df):
    """
    Calculates the average fare paid by passengers in each class.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    pd.Series: The average fare for each passenger class.
    """
    return titanic_df.groupby('Pclass')['Fare'].mean()

def count_passengers_by_port(titanic_df):
    """
    Counts the number of passengers who embarked from each port.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    pd.Series: The number of passengers by port of embarkation.
    """
    return titanic_df['Embarked'].value_counts()

def calculate_gender_survival_rate(titanic_df):
    """
    Calculates the average survival rate for male and female passengers.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    pd.Series: The survival rate for male and female passengers.
    """
    return titanic_df.groupby('Sex')['Survived'].mean() * 100

def count_unique_tickets(titanic_df):
    """
    Counts the number of unique ticket numbers.

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Returns:
    int: The number of unique ticket numbers.
    """
    return titanic_df['Ticket'].nunique()

def visualize_distributions(titanic_df):
    """
    Visualizes the age distribution of passengers (Question 7) and fare distribution by class (Question 8).

    Args:
    titanic_df (pd.DataFrame): The cleaned Titanic dataset.

    Displays:
    Two subplots: one for age distribution and one for fare distribution by class.
    """
    plt.figure(figsize=(14, 6))

    # 7. Age distribution (on the left)
    plt.subplot(1, 2, 1)
    sns.histplot(titanic_df['Age'].dropna(), bins=30, kde=True)
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # 8. Fare distribution by class (on the right)
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Pclass', y='Fare', data=titanic_df)
    plt.title('Fare Distribution by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Fare')

    # Show the plots together
    plt.tight_layout()
    plt.show()

# Main execution flow
if __name__ == "__main__":
    file_path = './data/Titanic.csv'
    titanic_df_clean = load_dataset(file_path)
    
    if titanic_df_clean is not None:
        # 1. Calculate the survival rate
        survival_rate = calculate_survival_rate(titanic_df_clean)
        print(f'Survival Rate:\n\t{survival_rate:.2f}%\n')

        # 2. Calculate the proportion of male and female passengers
        gender_distribution = calculate_gender_proportion(titanic_df_clean)
        print(f'Gender Proportion:\n\tMale: {gender_distribution["male"]:.2f}%\n\tFemale: {gender_distribution["female"]:.2f}%\n')

        # 3. Calculate the survival rate for each passenger class
        class_survival_rate = calculate_class_survival_rate(titanic_df_clean)
        highest_survival_class = class_survival_rate.idxmax()
        print(f'Survival Rate by Class:\n\t1st Class: {class_survival_rate[1]:.2f}%\n\t2nd Class: {class_survival_rate[2]:.2f}%\n\t3rd Class: {class_survival_rate[3]:.2f}%')
        print(f'\tClass with Highest Survival Rate: {highest_survival_class}st Class\n')

        # 4. Count passengers with siblings or spouses aboard
        sibsp_count = count_siblings_spouses_aboard(titanic_df_clean)
        print(f'Passengers with Siblings or Spouses Aboard:\n\t{sibsp_count} passengers\n')

        # 5. Calculate the average fare paid by passengers in each class
        average_fare_by_class = calculate_average_fare_by_class(titanic_df_clean)
        print(f'Average Fare by Class:\n\t1st Class: ${average_fare_by_class[1]:.2f}\n\t2nd Class: ${average_fare_by_class[2]:.2f}\n\t3rd Class: ${average_fare_by_class[3]:.2f}\n')

        # 6. Count passengers who embarked from each port
        embarked_count = count_passengers_by_port(titanic_df_clean)
        print(f'Passengers by Port of Embarkation:\n\tCherbourg (C): {embarked_count["C"]}\n\tQueenstown (Q): {embarked_count["Q"]}\n\tSouthampton (S): {embarked_count["S"]}\n')

        # 9. Calculate the average survival rate for male and female passengers
        gender_survival_rate = calculate_gender_survival_rate(titanic_df_clean)
        print(f'Survival Rate by Gender:\n\tMale: {gender_survival_rate["male"]:.2f}%\n\tFemale: {gender_survival_rate["female"]:.2f}%\n')

        # 10. Count unique ticket numbers
        unique_ticket_count = count_unique_tickets(titanic_df_clean)
        print(f'Unique Ticket Numbers:\n\t{unique_ticket_count} unique tickets\n')

        # Visualize both the age distribution (Q7) and fare distribution by class (Q8)
        visualize_distributions(titanic_df_clean)
