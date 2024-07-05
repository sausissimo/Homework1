class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def printName(self):
        print('\x1B[3mName: \x1B[0m' + self.name)

    def doubleHealth(self):
        self.health_points *= 2
        print('\x1B[3mDoubling health points...\x1B[0m')

    def __printHeroInfo__(self):
        print(f'\x1B[3mNickname: \x1B[0m{self.nickname}, \x1B[3msuperpower: \x1B[0m{self.superpower}, \x1B[3mhealth points: \x1B[0m{self.health_points}')

    def __getCatchphraseLength__(self):
        return len(self.catchphrase)

hero1 = SuperHero("Гордон Фримен", "Бульба", "Докторская степень", 100, "...")

hero1.printName()
hero1.__printHeroInfo__()
hero1.doubleHealth()
hero1.__printHeroInfo__()
hero1.__getCatchphraseLength__()