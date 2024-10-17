from bs4 import BeautifulSoup
import requests 
import matplotlib.pyplot as plt
import csv
# A program to analyse the relationship between multiple statistics (NBA - Basketball)


def scrape_page():

    try:
        page_to_scrape = requests.get('https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/qualifiers/')

        if not page_to_scrape:
            raise ValueError("Link doesn't work")
    except ValueError as e:
        print(e)

    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

    table = soup.find('table', {'class': 'TableBase-table'})
    if table is None:
        print('Table not found')
        return []

    player_data = []
    headers = []

    header_row = table.find('thead')
    if header_row is None:
        print('Header row not found')
        return []

    header_row = header_row.find('tr')
    for th in header_row.find_all('th'):
        headers.append(th.text.strip())

    for row in table.find('tbody').find_all('tr'):
        player_stats = {}
        columns = row.find_all('td')

        for i, column in enumerate(columns):
            player_stats[headers[i]] = column.text.strip()
   
        player_data.append(player_stats)
    
    return player_data



data = scrape_page()


def clean_data(d):
    cleaned_data = {}
    for key, value in d.items():
        clean_key = ' '.join(key.split()).replace('\n', ' ')
        clean_value = ' '.join(value.split()).replace('\n', ' ')
        cleaned_data[clean_key] = clean_value
        return cleaned_data


clean_players = []


for player in data:
        clean_player = clean_data(player)
        clean_players.append(clean_player)


def export_csv(data, filename):
    if not data:
        print('No data to write')
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        header = data[0].keys()
        writer.writerow(header)

        for player in data:
            writer.writerow(player.values())

export_csv(clean_players, 'nba_player_stats.csv')


sorted_players = sorted(clean_players, key=lambda x: float(x['FT% Free Throw Percentage']))

free_throw_pct = [float(player['FT% Free Throw Percentage']) for player in sorted_players]
points_per_game = [float(player['PPG Points Per Game']) for player in sorted_players]
player_names = [player['Player Player on team'] for player in sorted_players]
three_point_percentage = [float(player['3FG% Three-Point Field Goal Percentage']) for player in sorted_players]



fig, ax = plt.subplots()
ax.plot(free_throw_pct, points_per_game, marker='o')

ax.set_xlabel('Free Throw Percentage')
ax.set_ylabel('Points per Game')
ax.set_xticks(range(0, 101, 10 ))
ax.set_yticks(range(0, 40, 5))
ax.set_title('Relationship Between Free Throw Percentage and PPG')
ax.grid(True)

plt.show()


fig, ax = plt.subplots()
ax.plot(free_throw_pct, three_point_percentage, marker='o')

ax.set_xlabel('Free Throw Percentage')
ax.set_ylabel('Thee Point Percentage')
ax.set_xticks(range(0, 101, 10))
ax.set_yticks(range(0, 101, 10))
ax.set_title('Relationship Between Three Point and Free Throw Percentage')
ax.grid(True)

plt.show() # Second fig only shows when the previous is closed























        


    