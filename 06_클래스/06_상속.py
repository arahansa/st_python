class Parent:
    def can_sing(self):
        print("Sing a song")

class LuckyChild(Parent):
    def can_dance(self):
        print("Shuffle Dance")


child1 = LuckyChild()

child1.can_sing()
child1.can_dance()