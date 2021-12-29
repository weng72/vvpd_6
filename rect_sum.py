def rect_sum(image, x1: int, y1: int, x2: int, y2: int):
    '''
    Функция, находящая сумму пикселей произвольного прямоугольника,
    ограниченного заданными пикселями
    Args:
        image: Исходная матрица
        x1: Координата верхнего правого пикселя по "х"
        y1: Координата верхнего правого пикселя по "y"
        x2: Координата нижнего левого пикселя по "х"
        y2: Координата нижнего левого пикселя по "y"

    Returns:
        summ: Сумма пикселей ограниченных дополнительной матрицой,
              заданной двумя точками  
    '''
    summ = 0
    for i in range(int(y1)-1, int(y2)):
        for j in range(int(x1-1), int(x2)):
            summ += image[i][j]
    return summ
