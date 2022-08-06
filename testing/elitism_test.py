from elitism import Elitism


def test_find_elites1():
    population = [[[1, 1, 0], [0, 1, 0], [0, 0, 0]],
                  [[1, 1, 1], [1, 0, 1], [0, 0, 1]],
                  [[1, 1, 1], [0, 1, 0], [1, 1, 1]],
                  [[0, 0, 1], [1, 0, 1], [0, 1, 1]]]
    fit = [1, 2, 4, 7]
    elit = Elitism()
    elites = elit.find_elites(fit, population)
    assert elites[2] == [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert elites[3] == [[0, 0, 1], [1, 0, 1], [0, 1, 1]]


def test_find_elites2():
    population = [[[1, 1, 0], [0, 1, 0], [0, 0, 0]],
                  [[1, 1, 1], [1, 0, 1], [0, 0, 1]],
                  [[1, 1, 1], [0, 1, 0], [1, 1, 1]],
                  [[0, 0, 1], [1, 0, 1], [0, 1, 1]]]
    fit = [7, 2, 7, 7]
    elit = Elitism()
    elites = elit.find_elites(fit, population)
    assert elites[2] == [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert elites[3] == [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
