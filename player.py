class Player:
    def __init__(
        self,
        name='Гость',
        score=0.0,
        bonus=0.0,
        games=0,
        wins="0(",
        mvp=0,
        first_blood = 0,
        last_word_3=0,
        last_word_2=0,
        citizen="0/0 ",
        mafia="0/0 ",
        sheriff="0/0 ",
        don="0/0 "
    ):
        self.name = name
        self.score = float(score)
        self.bonus = float(bonus)
        self.games = int(games)
        self.wins = int(wins[:wins.index("(")])
        self.mvp = int(mvp)
        self.first_blood = int(first_blood)
        self.last_word_3 = int(last_word_3)
        self.last_word_2 = int(last_word_2)
        self.citizen = self.convert_role(citizen)
        self.mafia = self.convert_role(mafia)
        self.sheriff = self.convert_role(sheriff)
        self.don = self.convert_role(don)
    
    @staticmethod
    def convert_role(string):
        return dict(
            games = 
                int(string[:string.index("/")]) +
                int(string[
                    string.index("/") + 1:
                    string.index(" ")
                ]),
            wins = int (string[:string.index("/")])
        )

    @staticmethod
    def merge_role_stat(this_dict,other_dict):
        return dict(
            games = this_dict['games'] + other_dict['games'],
            wins = this_dict['wins'] + other_dict['wins']
        )

    def merge(self, other):
        self.score = (self.score + other.score) / 2
        self.bonus += other.bonus
        self.games += other.games
        self.wins += other.wins
        self.mvp = other.mvp
        self.last_word_3 = other.last_word_3
        self.last_word_2 = other.last_word_2  
        self.citizen = self.merge_role_stat(
            self.citizen,
            other.citizen)
        self.mafia = self.merge_role_stat(
            self.mafia,
            other.mafia)
        self.sheriff = self.merge_role_stat(
            self.sheriff,
            other.sheriff)
        self.don = self.merge_role_stat(
            self.don,
            other.don)