import random
import sys

# Generowanie przedmiotów
def generate_items(n, max_value, max_weight):
    items = []
    for _ in range(n):
        value = random.randint(1, max_value)
        weight = random.randint(1, max_weight)
        items.append((value, weight))
    return items

# Odczyt danych z pliku
def read_items_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        C = int(lines[0].strip())
        n = int(lines[1].strip())
        for line in lines[2:2+n]:
            value, weight = map(int, line.split())
            items.append((value, weight))
    return C, items

# Algorytm programowania dynamicznego
def knapsack_dynamic(items, C):
    n = len(items)
    dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(C + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][1]] + items[i-1][0])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][C]

# Algorytm brute force
def knapsack_brute_force(items, C):
    n = len(items)
    
    def helper(index, remaining_capacity):
        if index == n or remaining_capacity == 0:
            return 0
        
        if items[index][1] > remaining_capacity:
            return helper(index + 1, remaining_capacity)
        else:
            include_item = items[index][0] + helper(index + 1, remaining_capacity - items[index][1])
            exclude_item = helper(index + 1, remaining_capacity)
            return max(include_item, exclude_item)
    
    return helper(0, C)

# Funkcja główna
def main():
    print("Wybierz tryb uzupełniania danych:")
    print("1. Losowe generowanie przedmiotów")
    print("2. Wczytywanie przedmiotów z pliku")
    choice = input("Wybierz opcję (1/2): ")

    if choice == '1':
        n = int(input("Podaj liczbę przedmiotów: "))
        max_value = int(input("Podaj maksymalną wartość przedmiotu: "))
        max_weight = int(input("Podaj maksymalną objętość przedmiotu: "))
        C = int(input("Podaj pojemność plecaka: "))
        items = generate_items(n, max_value, max_weight)
    elif choice == '2':
        filename = input("Podaj nazwę pliku z danymi: ")
        C, items = read_items_from_file(filename)
    else:
        print("Nieprawidłowa opcja!")
        sys.exit(1)

    print("\nWygenerowane przedmioty (wartość, objętość):")
    for item in items:
        print(item)
    
    print("\nWybierz algorytm do rozwiązania problemu plecakowego:")
    print("1. Programowanie dynamiczne")
    print("2. Brute force")
    algorithm_choice = input("Wybierz opcję (1/2): ")

    if algorithm_choice == '1':
        max_value_dynamic = knapsack_dynamic(items, C)
        print("\nMaksymalna wartość (programowanie dynamiczne):", max_value_dynamic)
    elif algorithm_choice == '2':
        max_value_brute_force = knapsack_brute_force(items, C)
        print("Maksymalna wartość (brute force):", max_value_brute_force)
    else:
        print("Nieprawidłowa opcja!")
        sys.exit(1)

if __name__ == "__main__":
    main()