# THIS CODE WAS TO BE EXECUTED VIA DJANGO SHELL,
# RUN manage.py shell TO OPEN THE SHELL AND WRITE THIS CODE

from csv_to_db.models import EsportTeamModel

import csv

path = '../sample_data.csv'

with open(path) as f:
    reader = csv.reader(f)
    for column in reader:
        if column[0] != 'Team Name':
            _, created = EsportTeamModel.objects.get_or_create(
                    team_name = column[0],
                    prize = column[1],
            )
