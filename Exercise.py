import csv


class Member:
    def __init__(self, name, age, nationality):
        self.Name = name
        self.Age = age
        self.Nationality = nationality


class Coach(Member):
    def __init__(self, name, age, nationality, numOfExp):
        Member.__init__(self, name, age, nationality)
        self.NumOfExp = numOfExp


class Player(Member):
    def __init__(self, name, age, nationality, jerseyNumber, position, captain):
        Member.__init__(self, name, age, nationality)
        self.JerseyNumber = jerseyNumber
        self.Position = position
        self.Captain = captain


class Referee(Member):
    def __init__(self, name, age, nationality, numOfMatches):
        Member.__init__(self, name, age, nationality)
        self.NumOfMatches = numOfMatches


class Team:
    def __init__(self, teamName, teamNationality, coach):
        self.TeamName = teamName
        self.TeamNationality = teamNationality
        self.Coach = coach

    def assignLineup(self, playerGk, playerDefence, playerMiddle, playerForward):
        Players = [playerGk, playerDefence, playerMiddle, playerForward]
        LineUp = []
        for i in Players:
            FillLineUp = []
            FillLineUp.append(i.Name)
            FillLineUp.append(i.Age)
            FillLineUp.append(i.Nationality)
            FillLineUp.append(i.JerseyNumber)
            FillLineUp.append(i.Position)
            FillLineUp.append(i.Captain)
            LineUp.append(FillLineUp)
        return LineUp

    def addSubtitue(self, p, Substitute):
        FillSubstitute = []
        FillSubstitute.append(p.Name)
        FillSubstitute.append(p.Age)
        FillSubstitute.append(p.Nationality)
        FillSubstitute.append(p.JerseyNumber)
        FillSubstitute.append(p.Position)
        FillSubstitute.append(p.Captain)
        Substitute.append(FillSubstitute)

    def substitution(self, inP, outP, Bench, LineeUp):
        for i in LineeUp:
            if i[3] == outP and i[5] == True:
                i[5] = False
                Bench.append(i)
                LineeUp.remove(i)
                for j in Bench:
                    if j[3] == inP:
                        j[5] = True
                        LineeUp.append(j)
                        Bench.remove(j)
            elif i[3] == outP and i[5] == False:
                Bench.append(i)
                LineeUp.remove(i)
                for j in Bench:
                    if j[3] == inP:
                        LineeUp.append(j)
                        Bench.remove(j)

    def SaveLineup(self, FillSaveLineUp):
        print(f" Team : {self.TeamName}\t Coach  : {self.Coach}"
              f" \n\t Jersey Number \t\t Name \t\t Position\n\t--------------- \t--------   \t-----------")
        for i in FillSaveLineUp:
            if i[5] == True:
                print(f"\t\t{i[3]}\t\t\t\t{i[0]}\t\t{i[4]} (C)")
            else:
                print(f"\t\t{i[3]}\t\t\t\t{i[0]}\t\t{i[4]}")


class Match:
    def __init__(self, event, stadiumName, referee, homeTeam, awayTeam):
        self.Event = event
        self.StadiumName = stadiumName
        self.Referee = referee
        self.HomeTeam = homeTeam
        self.AwayTeam = awayTeam
        referee.NumOfMatches += 1
        referee.Name
        referee.Nationality
        referee.Age

    def addGoal(self, teamName, playerName, minute, AddGoalList):
        AddGoalList.append([teamName, playerName, minute])
        print(playerName, minute)

    def displayScore(self, scorehome, scoreaway):
        HomeGoalCounter = 0
        AwayGoalCounter = 0
        for i in scorehome:
            HomeGoalCounter += 1
        for i in scoreaway:
            AwayGoalCounter += 1
        return HomeGoalCounter, AwayGoalCounter

    def displayWinner(self):
        HomeGoalCounter, AwayGoalCounter = Match.displayScore(self, scorehome, scoreaway)
        if HomeGoalCounter == AwayGoalCounter:
            return f"Draw Go Penalties"
        elif HomeGoalCounter > AwayGoalCounter:
            return f"{t1.TeamName} are the champions of {self.Event}"
        else:
            return f"{t2.TeamName} are the champions of {self.Event}"

    def printScoreSheet(self):
        home, away = Match.displayScore(self, scorehome, scoreaway)
        with open('Result.csv', 'w', newline='') as f:
            fieldnames = ['1', '2', '3', '4']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'1': 'Event:', '2': self.Event})
            writer.writerow({'1': 'Staduim:', '2': self.StadiumName})
            writer.writerow(
                {'1': 'Refree :', '2': self.Referee.Name, '3': self.Referee.Nationality, '4': self.Referee.Age})
            writer.writerow({'1': 'Home Team', '2': 'VS', '3': 'Away Team', '4': ' '})
            writer.writerow({'1': f"{t1.TeamName} {t1.TeamNationality}", '2': f"{home}:{away}",
                             '3': f"{t2.TeamName} {t2.TeamNationality}", '4': ''})
            writer.writerow({'1': '', '2': '', '3': '', '4': ''})
            for i in scorehome:
                writer.writerow({'1': f"{i[1]} {i[2]}"})
            for i in scoreaway:
                writer.writerow({'1': '', '2': '', '3': f"{i[1]} {i[2]}", '4': ''})
            writer.writerow({'1': '', '2': '', '3': '', '4': ''})
            writer.writerow({'1': self.displayWinner()})


player1 = Player("Cristiano Ronaldo", "35", "Portugese", "7", "Forward", False)
player2 = Player("Sergio Ramos", "31", "Spanish", "5", "Defence", True)
player3 = Player("Modric", "30", "Coratia", "11", "Middle", False)
player4 = Player("Messi", "32", "Argintena", "10", "Forward", False)
player5 = Player("Varane", "29", "France", "2", "Defence", False)
t1 = Team("Barcelona", "Spanish", "Valverdi")
t2 = Team("Real Madrid", "Spanish", "Zidane")
lineup = t1.assignLineup(player1, player2, player3, player4)
outsidelist = []
t1.addSubtitue(player5, outsidelist)
t1.substitution(player5, player1, outsidelist, lineup)

refree = Referee("Antonio Mateu Lahoz", 45, "Spanish", 60)
match1 = Match("Champions", "Santiago Bernabu", refree, "Real Madrid", "Barcelona")
scoreteam = []
scorehome = []
scoreaway = []
match1.addGoal("Real Madrid", "CR7", 53, scoreteam)
print(match1.displayScore(scorehome, scoreaway))
print(match1.displayWinner())
print(scoreteam)
match1.printScoreSheet()
""""
dsajkdasdsad
asdsadsa
"""
