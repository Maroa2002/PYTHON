facebook_posts = [
    {'Likes': 21, 'comments': 2},
    {'Likes': 13, 'comments': 2, 'shares': 1},
    {'Likes': 33, 'comments': 8, 'shares': 3},
    {'comments': 4, 'shares': 1},
    {'comments': 1, 'shares': 1},
    {'Likes': 19, 'comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        # total_likes += 0
        pass

print(total_likes)