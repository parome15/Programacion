import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 1, 2)

def test_ones():
    assert 2 == Yatzy.ones(1, 2, 1, 3, 3)
    assert 2 == Yatzy.ones(1, 2, 1, 3, 3)
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)

def test_twos():
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
    assert 0 == Yatzy.twos(1, 3, 4, 5, 6)

def test_threes():
    assert 9 == Yatzy.threes(3, 1, 3, 2, 3)
    assert 0 == Yatzy.threes(1, 2, 4, 5, 6)




@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    assert 4 == inyector.fours()

def test_fives(inyector):
    assert 5 == inyector.fives()

def test_sixes(inyector):
    assert 0 == inyector.sixes()


def test_pair():
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 4 == Yatzy.pair(2, 2, 3, 4, 5)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)

def test_two_pair():
    assert 8 == Yatzy.two_pair(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pair(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pair(1, 1, 2, 2, 2)


def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 2, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)
    assert 24 == Yatzy.four_of_a_kind(6, 6, 6, 6, 2)

def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(2, 1, 3, 3, 3)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 3)

def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 15 == Yatzy.smallStraight(5, 4, 3, 2, 1)

def test_large_straight():
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.largeStraight(6, 5, 4, 3, 2)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)


def test_full_house():
    assert 14 == Yatzy.fullHouse(4, 1, 4, 1, 4)
    assert 0 == Yatzy.fullHouse(1, 2, 3, 4, 5)
    assert 21 == Yatzy.fullHouse(5, 3, 5, 3, 5)

    