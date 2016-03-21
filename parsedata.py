import yaml, os, csv

# TO DO:
# figure out how to handle dates (+ multiple dates)


def build_simple_csv(csv_file_name):
    # if the file exists, overwrite it.  If not, create it.
    with open(csv_file_name, 'wb') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        wr.writerow( ["file_id", "city", "date", "team1", "team2", "toss_winner", "toss_decision", "result", "win_team"] )


        count = 0
        for filename in os.listdir("raw data/odis"):
            if filename.endswith(".yaml"):
                file_id, file_extension = os.path.splitext(filename)
                filepath = 'raw data/odis/'+ str(file_id) + '.yaml'

                with open(filepath, 'r') as f:
                    data = yaml.load(f)

                    try: city = data["info"]["city"]
                    except: city = ""
                    try: date = data["info"]["dates"]
                    except: date = ""
                    try:
                        teams = data["info"]["teams"]
                        team1 = teams[0]
                        team2 = teams[1]
                    except:
                        teams = ""
                        team1 = ""
                        team2 = ""
                    try: toss_winner = data["info"]["toss"]["winner"]
                    except: toss_winner = ""
                    try: toss_decision = data["info"]["toss"]["decision"]
                    except: toss_decision = ""
                    try: result = data["info"]["outcome"]["result"]
                    except: result = ""
                    try: win_team = data["info"]["outcome"]["winner"]
                    except: win_team = ""

                    count = count+1
                    print str(file_id) + ": " + city + ". " + team1 + " vs " + team2 + ". Winner: " + win_team + " " + result
                    wr.writerow( [file_id, city, date, team1, team2, toss_winner, toss_decision, result, win_team] )

        print str(count) + " rows written"


def build_detailed_csv(csv_file_name):
    pass


build_simple_csv('odi_data_simple.csv')
