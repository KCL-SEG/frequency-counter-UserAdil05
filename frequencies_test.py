def frequencies(items):
    frequency_dict = {}

    
    for item in items:
        item_str = str(item)
    
        if item_str in frequency_dict:
            frequency_dict[item_str] += 1
        else:
           
            frequency_dict[item_str] = 1
    return frequency_dict

# Test functions
def test_mixed_list():
    input_list = ['0', 4, 4, '4', 'd', 'd', 'e', 0, 'a', 'd', '4']
    output = frequencies(input_list)
    assert output['4'] == 4
    assert output['d'] == 3
    assert output['e'] == 1
    assert output['a'] == 1
    assert output['0'] == 2
    assert '4' in output.keys()
    assert '0' in output.keys()

def test_empty_list():
    input_list = []
    output = frequencies(input_list)
    assert output == {}

def test_example_1():
    input_list = ['a', 'a', 'b', 'b', 'b', 'c']
    output = frequencies(input_list)
    assert output['a'] == 2
    assert output['b'] == 3
    assert output['c'] == 1

def test_example_2():
    input_list = [100, 'Hello', '100', '100', 100]
    output = frequencies(input_list)
    assert output['100'] == 4
    assert output['Hello'] == 1
    assert '100' in output.keys()

test_mixed_list()
test_empty_list()
test_example_1()
test_example_2()

