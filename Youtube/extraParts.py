animals = ["cat", "dog", "lion", "fish", "llama", "giraffe", "tiger", "owl"]

def animal(name):
    if len(name) >= 5:
        return True
    else:
        return False

bigNameAnimals = filter(animal, animals)

print(list(bigNameAnimals))