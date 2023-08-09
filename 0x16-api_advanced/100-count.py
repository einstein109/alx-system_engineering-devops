#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


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
                    if title.count(word) > 0:
                        if word in counts:
                            counts[word] += title.count(word)
                        else:
                            counts[word] = title.count(word)
            
            after = data['data']['after']
            count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)
    except requests.RequestException:
        print_results(counts)

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Example usage
subreddit_name = 'python'
keywords = ['python', 'programming', 'code']
count_words(subreddit_name, keywords)
