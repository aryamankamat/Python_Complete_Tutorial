class Mother():

    def __init__(self):
        print("Mother constructor...")
        return

    def eyecolor(self):
        print("Mother: Eyes are black")
        return


class Father():

    def __init__(self):
        print("Father constructor...")
        return

    def eyecolor(self):
        print("Mother: Eyes are Blue")
        return


class Offeset(Mother, Father):

    def __init__(self):
        super().__init__()
        print("child constructor...")
        return


o1 = Offeset()
# o1.eyecolor()
# print(o1.__dict__)
# print(dir(o1))
# print(Offeset.mro())
# print(Offeset.__mro__)
