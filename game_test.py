from game import Game

game1 = Game(player1='Jonas', player2='Clemens')


def test_game_has_two_players():
    assert game1.get_player1_name() and game1.get_player2_name()


def test_dice_rolls():
    game2 = Game(player1='Jonas', player2='Clemens')
    assert game2.dice == None
    game2.roll_dice()
    assert type(game2.dice) == tuple

def test_space_player1():
    game2 = Game(player1='Jonas', player2='Clemens')
    assert game2.player1_space == None
    game2.roll_dice()
    assert game2.player1_space == int