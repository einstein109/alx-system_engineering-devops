#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'Custom User-Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            if not posts:
                print_results(counts)
                return
            
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    normalized_word = normalize_word(word)
                    if normalized_word in title:
                        if normalized_word in counts:
                            counts[normalized_word] += 1
                        else:
                            counts[normalized_word] = 1
            
            after = data['data']['after']
            count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)
    except requests.RequestException:
        print_results(counts)

def normalize_word(word):
    return word.lower().strip('.!_')

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
