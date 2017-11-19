from books import *

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0])
    else:
        return False

def splitter(pattern):
    au = None
    titl = None
    yr = None
    if type(pattern[0]) == list:
        au = pattern[0]
    else:
        au = [pattern[0]]
    if type(pattern[1]) == list:
        titl = pattern[1]
    else:
        titl = [pattern[1]]
    if type(pattern[2]) == list:
        yr = pattern[2]
    else:
        yr = [pattern[2]]
    return au, titl, yr

def search(pattern, db):
    au_pt, titl_pt, yr_pt = splitter(pattern)
    all_matches = []
    for book in db:
        au_bk, titl_bk, yr_bk = splitter(book)
        if match(au_bk, au_pt) and match(titl_bk, titl_pt) and match(yr_bk, yr_pt):
            all_matches.append([au_bk, titl_bk, yr_bk])
    return all_matches
