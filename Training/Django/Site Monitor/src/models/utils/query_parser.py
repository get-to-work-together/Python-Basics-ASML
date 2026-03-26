import re


def query_parser(query: str):
    """
    Google type query parsing

    Reference: https://ahrefs.com/blog/google-advanced-search-operators/

    Supported syntax:
        "A B"           => ['A B']
        A or B          => ['A', 'B']
        A OR B          => ['A', 'B']
        A, B            => ['A', 'B']
        A|B             => ['A', 'B']
        A and B         => [('A', 'B')]
        A AND B         => [('A', 'B')]
        A B             => [('A', 'B')]
        A&B             => [('A', 'B')]
        A or B and C    => ['A', ('B', 'C')]
        A or B C        => ['A', ('B', 'C')]
        A B, C          => [('A', 'B'), 'C']

    :param query: the string to parse
    :return: a list of keywords
    """

    query = re.sub(r'"(.+?)"', lambda m: m[1].replace(' ', '_'), query)
    query = re.sub(r'( +)', ' ', query)    # replace multiple spaces with single space
    query = re.sub(r'(\s*(?:\sOR\s|\sor\s|\||,)\s*)', '-OR-', query)      # replace comma with
    query = re.sub(r'(\s*(?:\sAND\s|\sand\s|&| )\s*)', '-AND-', query)
    query = query.replace('_', ' ')
    keywords = query.split('-OR-')
    keywords = [tuple(keyword.split('-AND-')) if '-AND-' in keyword else keyword for keyword in keywords]
    return keywords


def query_matcher(keywords: list, s: str, ignore_case: bool = True):
    """
    Returns True if the query matches the string. Else False.

    :param keywords: str the query to match
    :param s: str the string
    :param ignore_case: bool ignore case or not
    :return: bool query matches s or not
    """

    if ignore_case:
        s = s.lower()

    return any(kw_or.lower() in s
               if isinstance(kw_or, str) else
               all(kw_and.lower() in s
                   for kw_and in kw_or)
               for kw_or in keywords)


if __name__ == '__main__':

    print(q := '"A B"', '=>', query_parser(q))
    print(q := 'A or B', '=>', query_parser(q))
    print(q := 'A OR B', '=>', query_parser(q))
    print(q := 'A, B', '=>', query_parser(q))
    print(q := 'A|B', '=>', query_parser(q))
    print(q := 'A and B', '=>', query_parser(q))
    print(q := 'A AND B', '=>', query_parser(q))
    print(q := 'A B', '=>', query_parser(q))
    print(q := 'A&B', '=>', query_parser(q))
    print(q := 'A or B and C', '=>', query_parser(q))
    print(q := 'A or B C', '=>', query_parser(q))
    print(q := 'A B, C', '=>', query_parser(q))
    print()

    s = 'De zomer is een van de vier seizoenen op Aarde. De oorsprong van de naam is waarschijnlijk afgeleid van het Middelnederlands somer en verwant aan het Oudsaksisch, Oudhoogduits en Oudnoords sumar. Het astronomisch bepaalde begin van de zomer is de zomerzonnewende (rond 21 juni op het noordelijk halfrond en rond 21 december op het zuidelijk halfrond). De zon gaat dan door het zomerpunt, de zon bereikt die dag de hoogste stand boven de horizon en de dag duurt het langst. De zomer eindigt met de herfst-equinox (rond 23 september op het noordelijk halfrond en 20 maart op het zuidelijk halfrond).'
    print(s)

    print(q := '"vier seizoenen"', '=>', query_matcher(q, s))
    print(q := 'vier or seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier OR seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier, seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier | seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier|seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier and seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier AND seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier & seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier&seizoenen', '=>', query_matcher(q, s))
    print(q := 'vier or seizoenen and vivaldi', '=>', query_matcher(q, s))
    print(q := 'vier or seizoenen vivaldi', '=>', query_matcher(q, s))
    print(q := 'vier seizoenen, vivaldi', '=>', query_matcher(q, s))

    print(q := 'drie and seizoenen', '=>', query_matcher(q, s))
    print(q := 'drie or seizoenen and vivaldi', '=>', query_matcher(q, s))
