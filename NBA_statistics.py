from bs4 import BeautifulSoup
import requests 
import matplotlib.pyplot as plt
import csv

""" A program to analyse the relationship between multiple statistics (NBA - Basketball) """


def scrape_page():
    """
    A function to scrape an NBA satistics webpage and draw releveant data from a table
    
    returns:
        Player_data (list of dict): Basketball Statistics
    """

    try:
        # Sending a request to the wepage with NBA statistics
        page_to_scrape = requests.get('https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/qualifiers/')

        # Check if the page was successfully fetched
        if not page_to_scrape:
            raise ValueError("Link doesn't work")
    except ValueError as e:
        print(e)

    # Parsing the page using BeautifulSoup
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

    # Find the statistics table within the webpage
    table = soup.find('table', {'class': 'TableBase-table'})
    if table is None:
        print('Table not found')
        return []

    player_data = []
    headers = []

    # Locate the header row in table to extract the column names
    header_row = table.find('thead')
    if header_row is None:
        print('Header row not found')
        return [] 

    # Extract header row for column titles
    header_row = header_row.find('tr')
    for th in header_row.find_all('th'):
        headers.append(th.text.strip())

    # Extract player statistics from each row in the table body
    for row in table.find('tbody').find_all('tr'):
        player_stats = {}
        columns = row.find_all('td')

        # Store each player's stats as key-value pairs in dictionary
        for i, column in enumerate(columns):
            player_stats[headers[i]] = column.text.strip()
   
        player_data.append(player_stats)
    
    return player_data



data = scrape_page()


def clean_data(d):
    """
    Cleans the keys and values in the dictionary by removign extra spaces and newlines.
    
    Parameters:
        d(dict): Dictionary of player stats where keys are column headers and values are stats.
        
    Returns:
        cleaned_data (dict): Cleaned dictionary with formatted keys and values
    
    
    """
    
    cleaned_data = {}
    
    # Cleaning key and value by removing excess whitespace
    for key, value in d.items():
        clean_key = ' '.join(key.split()).replace('\n', ' ')
        clean_value = ' '.join(value.split()).replace('\n', ' ')
        cleaned_data[clean_key] = clean_value
        return cleaned_data

# List to store cleaned player data
clean_players = []

# Cleans each player's data and stores it in 'clean_players'
for player in data:
        clean_player = clean_data(player)
        clean_players.append(clean_player)


def export_csv(data, filename):
    """
    
    Exports the player statistics data to a CSV file.
    
    
    Parameters:
        data(list of dict): List of dictionaires containing player stats
        filename (str): Name of the file to export data to
    
    """
    if not data:
        print('No data to write') 
        return

    # Write the data to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        header = data[0].keys() # Extract the column headers from the first player's data
        writer.writerow(header) # Write the headers to the CSV

        # Write each player's data row by row
        for player in data:
            writer.writerow(player.values())

# Export cleaned player data to a CSV file
export_csv(clean_players, 'nba_player_stats.csv')

# Sort players by their free throw percentage
sorted_players = sorted(clean_players, key=lambda x: float(x['FT% Free Throw Percentage']))

# Extracting statistics for plotting from sorted players
free_throw_pct = [float(player['FT% Free Throw Percentage']) for player in sorted_players]
points_per_game = [float(player['PPG Points Per Game']) for player in sorted_players]
player_names = [player['Player Player on team'] for player in sorted_players]
three_point_percentage = [float(player['3FG% Three-Point Field Goal Percentage']) for player in sorted_players]


# Setting up figure and plotting free throw percentage and points per game
fig, ax = plt.subplots()
ax.plot(free_throw_pct, points_per_game, marker='o')

# Label the axes
ax.set_xlabel('Free Throw Percentage')
ax.set_ylabel('Points per Game')
ax.set_xticks(range(0, 101, 10 ))
ax.set_yticks(range(0, 40, 5))
ax.set_title('Relationship Between Free Throw Percentage and PPG')
ax.grid(True)

# Display the first plot
plt.show()


# Plotting relationship between free throw percentage and three point percentage
fig, ax = plt.subplots()
ax.plot(free_throw_pct, three_point_percentage, marker='o')

# Label the axes
ax.set_xlabel('Free Throw Percentage')
ax.set_ylabel('Thee Point Percentage')
ax.set_xticks(range(0, 101, 10))
ax.set_yticks(range(0, 101, 10))
ax.set_title('Relationship Between Three Point and Free Throw Percentage')
ax.grid(True)

# Display the second plot
plt.show() 

# Second fig only shows when the previous is closed























        


    