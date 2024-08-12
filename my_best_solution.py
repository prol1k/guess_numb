"""Задача для нахождения кол-ва платформ."""
# 116806295

def main():
    """Функция в которой описаны все действия."""
    weights: int = list(map(int, input().split()))
    limit: int = int(input())
    weights.sort()
    left = 0
    right = len(weights) - 1
    quantity = 0
    while left <= right:
        # Проверяем , сумму первого и последнего элементов, если их сумма
        # меньше limit то ставим оба робота, иначе самый большой
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        quantity += 1
    return quantity


if __name__ == '__main__':
    print(main())
