## Some helper functions are defined here in order to keep the notebook clean
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out


def extract_auth(rec):
    return [auth['authname'] for auth in rec]


def extract_keywords(rec):
    if isinstance(rec, str):
        rec = rec.split(" | ")
    else:
        pass
        # raise TypeError
    return rec


def display_rec(dataframe, loc):
    print("index key : \t", loc)
    single_record = dataframe.loc[loc]
    for column, field in zip(dataframe.columns, single_record):
        print(column, ": \t", field)


def count_items(rec):
    try:
        rec_length = len(rec)
    except TypeError:
        rec_length = 0
    return rec_length


def word_count(words):
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
