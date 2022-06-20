class balancing:
    @staticmethod
    def partition(array, low, high):
        pivot = array[high].mmr
        i = low - 1
        for j in range(low, high):
            if array[j].mmr <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    @staticmethod
    def balance(array, low, high):
        if low < high:
            pi = balancing.partition(array, low, high)
            balancing.balance(array, low, pi - 1)
            balancing.balance(array, pi + 1, high)

    @staticmethod
    def beautification(list):
        panjang = 0
        for i in list:
            if len(i.name) > 15:
                i.name = i.name[0:15] + "..."
            if len(i.name) >= panjang:
                panjang = len(i.name)
        for k in list:
            if len(k.name) < panjang:
                k.name += (" " * (panjang - len(k.name)))
        return list