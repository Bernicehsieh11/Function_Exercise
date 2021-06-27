
class removel:

    def __init__(self, fruitAll):
        self.fruitAll = fruitAll

    def get_fruits():
        fruit_list = ['水蜜桃', '香蕉', '鳯梨', '李子', '橘子', '西瓜']
        return fruit_list


def main():
    fruitAll = removel.get_fruits()

    while True:
        print(f'串列元素有:{fruitAll}')
        fruit = input("請輸入要刪除的水果(Enter 結束):")
        if(fruit == ''):
            break
        num = fruitAll.count(fruit)
        if (num > 0):
            fruitAll.remove(fruit)
        else:
            print(f'{fruit},不在串列中')


if __name__ == "__main__":
    main()
