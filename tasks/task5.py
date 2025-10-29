# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    symbols = input().split()
for symbol in symbols:
    print(f"Код символа {symbol} равен {ord(symbol)}")
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
