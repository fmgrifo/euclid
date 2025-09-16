def disuguaglianza_triangolare(a: int, b: int, c: int) -> bool:
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
# Ciao pippo, ho aggiunto questo commento
disuguaglianza_triangolare(2, 8, 3)
