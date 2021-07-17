import finding_hidden_messages_in_dna


def test_find_reverse_complement():

    assert finding_hidden_messages_in_dna.find_reverse_complement('ATCG') == 'CGAT'
