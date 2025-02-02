class Game:
    def __init__(self, title):
        self.title = title


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, 'title'):
              self._title = title
        # might need to use raise AttributeError("Title cannot be changed after the game is instantiated.")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player): #why are they giving us player?
        return sum([result.score for result in self.results()]) / len([result.score for result in self.results()])

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game): 
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game