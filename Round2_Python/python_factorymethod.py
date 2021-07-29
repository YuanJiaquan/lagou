from Round2_Python.Python_1 import Jinx,Timo


class HeroFactory:



    def Create_hero(self,hero):
        if hero=='jinx':
            return Jinx()
        elif hero=='timo':
            return Timo()
        else:
            print(f'该{hero}不存在')


if __name__ == '__main__':
    H=HeroFactory()
    Jx=H.Create_hero('jinx')
    Tm=H.Create_hero('timo')
    Jx.fight(Tm.hp,Tm.power,Tm.name)