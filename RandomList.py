import random
def random_list(size):
        out = []
        for x in range(0, size):
                out.append(random.randint(0, 99999999999999))
        return out