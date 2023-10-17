list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
ind_for_teams_distribution = len(list_players) // 2
team1 = list_players[:ind_for_teams_distribution]
team2 = list_players[ind_for_teams_distribution:]
print(team1, team2, sep = '\n')
