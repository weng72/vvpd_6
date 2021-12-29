def integral_view(image, x, y, integral_image):
    '''
    Функция, осуществляющая расчёт элементов матрицы интегрального представления изображения
    Args:
        image: Исходная матрица
        x: Координата пикселя по "х"
        y: Координата пикселя по "y"
        integral_image: Матрица в интегральном представлении   

    Returns:
        Пиксель в его интегральном представлении
    '''
    if (x-1) > -1 and (y-1) > -1:
        return image[x][y]-integral_image[x-1][y-1]+integral_image[x-1][y]+integral_image[x][y-1]
    else:
        return image[x][y]


def integral_view_final(image):
    '''
    Функция, осуществляющая расчёт матрицы интегрального представления изображения
    Args:
        image: Исходная матрица

    Returns:
        integral_image: Матрица в интегральном представлении   
    '''
    M = 3
    N = 5
    integral_image = []
    for k in range(N):
        integral_image.append([0]*M)
    for i in range(N):
        for j in range(M):
            integral_image[i][j] = integral_view(
                image, i, j, integral_image)
    return integral_image