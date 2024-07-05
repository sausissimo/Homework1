class SuperHero:

    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.fly = fly

    def printName(self):
        print('\x1B[3mName: \x1B[0m' + self.name)

    def squareHealthAndLetFly(self):
        self.health_points *= self.health_points
        self.fly = True

    def __printHeroInfo__(self):
        print(f'\x1B[3mNickname: \x1B[0m{self.nickname}, \x1B[3msuperpower: \x1B[0m{self.superpower}, \x1B[3mhealth points: \x1B[0m{self.health_points}, \x1B[3mflying ability: \x1B[0m{self.fly}.')

    def __getCatchphraseLength__(self):
        return len(self.catchphrase)


class StrongHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, specialization, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.specialization = specialization
        self.damage = damage
        self.fly = fly

    def __printHeroInfo__(self):
        print(f'\x1B[3mNickname: \x1B[0m{self.nickname}, \x1B[3msuperpower: \x1B[0m{self.superpower}, \x1B[3mhealth points: \x1B[0m{self.health_points}, \x1B[3mdamage: \x1B[0m{self.damage}, \x1B[3mflying ability: \x1B[0m{self.fly}.')


    def printTruePhrase():
        print('True in the True_phrase.')


class Villain(StrongHero):

    people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, specialization, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, specialization, damage)
        self.fly = fly
    
    def gen_x(): ...

    def crit(self, character):
        character.damage *= character.damage
        

heroBig = SuperHero("Гордон Фримен", "Бульба", "Докторская степень", 100, "...")

heroSmall = StrongHero("Джон", "Дурачок", "Сила", 100, "Аблывлубла!", "Земля", 100)

villain = Villain("Саня", "Тёмный Властелин", "Перевоплощение", 100, "Уничтожу.", "Параллельное измерение", 100)


heroBig.__printHeroInfo__()
heroSmall.__printHeroInfo__()
villain.__printHeroInfo__()

print('\nsquaring health points and granting flying ability...\n')
heroSmall.squareHealthAndLetFly()
heroBig.squareHealthAndLetFly()
villain.squareHealthAndLetFly()
villain.crit(heroSmall)

heroBig.__printHeroInfo__()
heroSmall.__printHeroInfo__()
villain.__printHeroInfo__()
StrongHero.printTruePhrase()
