
library(Lahman)
library(data.table)

# tables:
#   players
#   batting > players
#   fielding > players

data(Master)
data(Batting)
data(Fielding)

players <- as.data.table(Master)
players <- players[, .(id = playerID,
                       country = birthCountry,
                       birthDate = format(as.Date(paste0(birthYear, '-', birthMonth, '-', birthDay), format='%Y-%m-%d'), '%Y-%m-%d'),
                       deathDate = format(as.Date(paste0(deathYear, '-', deathMonth, '-', deathDay), format='%Y-%m-%d'), '%Y-%m-%d'),
                       nameFirst, nameLast,
                       weight, height,
                       bats, throws)]

batting <- as.data.table(Batting)
batting <- batting[, .(players_id = playerID, year = yearID, team = teamID, league = lgID, G, AB, R, H, HR, RBI, SB, CS, BB, SO)]

fielding <- as.data.table(Fielding)
fielding <- fielding[, .(players_id = playerID, year = yearID, team = teamID, league = lgID, POS, G, GS, InnOuts, PO, A, E, DP)]

fwrite(players, 'baseball/players.csv.gz')
fwrite(batting, 'baseball/batting.csv.gz')
fwrite(fielding, 'baseball/fielding.csv.gz')
