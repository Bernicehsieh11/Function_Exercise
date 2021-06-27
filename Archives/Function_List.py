
class fruits:

    def __init__(self, fruitAll):
        self.fruitAll = fruitAll

    def get_fruits():
        fruit_list = ['水蜜桃', '香蕉', '鳯梨', '李子']
        return fruit_list


def main():
    fruitAll = fruits.get_fruits()

    num = 0
    while num < len(fruitAll):
        print(f'{fruitAll[num]}真的很好吃喔~')
        num += 1


if __name__ == "__main__":
    main()
