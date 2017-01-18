class Yatzy:

    @staticmethod
    def chance(*dice):
        suma = 0
        for die in dice:
            suma += die
        return suma

    @staticmethod
    def yatzy(*dice):
        YATZYSCORE = 50
        if dice.count(dice[0]) == len(dice):
            return YATZYSCORE
        return 0

   
    @staticmethod
    def ones(*dice):
        UNO = 1
        score = dice.count(UNO) * UNO
        return score
    

    @staticmethod
    def twos(*dice):
        DOS = 2
        score = dice.count(DOS) * DOS
        return score

    @staticmethod
    def threes(*dice):
        TRES = 3
        score = dice.count(TRES) * TRES
        return score


    

    def __init__(self, *dice):
        self.dice = dice
    
    def fours(self):
        CUATRO = 4
        score = self.dice.count(CUATRO) * CUATRO
        return score
    

    def fives(self):
        CINCO = 5
        score = self.dice.count(CINCO) * CINCO
        return score
    

    def sixes(self):
        SEIS = 6
        score = self.dice.count(SEIS) * SEIS
        return score

    @staticmethod
    def pair(*dice):
        result = [0]
        for die in dice:
            if dice.count(die) >= 2:
                result.append(die*2)
        return max(result)

    @staticmethod
    def two_pair(*dice):
        PAR = 2
        parejas = 0
        score = 0
        numero = 1
        while parejas < 2 and numero <= 6:
            if dice.count(numero) <= 2:
                parejas += 1
                score += PAR * numero
            numero += 1
        if parejas == 2:
            return score
        else:
            return 0



    @staticmethod
    def four_of_a_kind(*dice):
        CUATRO = 4
        for numero in range(6, 0, -1):
            if dice.count(numero) >= CUATRO:
                return CUATRO * numero
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        TRES = 3
        for numero in range(6, 0, -1):
            if dice.count(numero) >= TRES:
                return TRES * numero
        return 0

    

    @staticmethod
    def smallStraight(*dice):
        for numero in range(1, 6):
            if dice.count(numero) != 1:
                return 0
        return 15

    

    @staticmethod
    def largeStraight(*dice):
        for numero in range(2, 7):
            if dice.count(numero) != 1:
                return 0
        return 20
    

    @staticmethod
    def fullHouse(*dice):
        score = 0
        dosNumeros = 0
        tresNumeros = 0
        for numero in range(7):
            if dice.count(numero) == 2:
                score += numero * 2
                dosNumeros = 1
            elif dice.count(numero) == 3:
                score += numero * 3
                tresNumeros = 1
            else:
                dosNumeros == 1 and tresNumeros == 1
            return score
        return 0
