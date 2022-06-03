import operator

import utils.iterator


def test_uniques_true():
    assert utils.iterator.uniques((1, (1,), "1", False))


def test_uniques_false():
    assert not utils.iterator.uniques((1, True, 1.0))


def test_uniques_true_given_itemgetter():
    data = [
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 2,
            'name': 'n2',
        },
        {
            'id': 3,
            'name': 'n3',
        }
    ]
    uniques = utils.iterator.uniques(data, operator.itemgetter('id', 'name'))
    assert uniques


def test_uniques_false_given_itemgetter():
    data = [
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 1,
            'name': 'n1',
        },
        {
            'id': 3,
            'name': 'n3',
        }
    ]
    uniques = utils.iterator.uniques(data, operator.itemgetter('id', 'name'))
    assert not uniques
