champions = [
  (2014, 'San Antonio Spurs'),
  (2015, 'Golden State Warriors'),
  (2016, 'The Cleveland Cavaliers'),
  (2017, 'Golden State Warriors'),
  (2018, 'Golden State Warriors'),
]
for team in {c[1] for c in champions}: # unordered
    print(team)
