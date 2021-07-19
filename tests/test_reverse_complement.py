from finding_hidden_messages_in_dna import find_reverse_complement


def test_find_reverse_complement():

    assert find_reverse_complement('ATCG') == 'CGAT'
