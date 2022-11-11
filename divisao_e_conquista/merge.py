def merge(array1, array2):
    if (array1 and array2):
        if (array1[0] > array2[0]):
            array1, array2 = array2, array1
        
        return [array1[0]] + merge(array1[1:], array2)
    return array1 + array2