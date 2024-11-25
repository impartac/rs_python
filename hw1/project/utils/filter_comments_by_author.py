def filter_comments_by_author(comments, author):
    return list(filter(lambda c: c.author == author, comments))
