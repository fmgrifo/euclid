def disuguaglianza_triangolare(a: int, b: int, c: int) -> bool:
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

disuguaglianza_triangolare(2, 8, 3)
