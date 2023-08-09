#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Custom User-Agent'}
    
    # Create the API URL for the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the response status code is OK
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            
            return subscribers
        elif response.status_code == 404:
            # Subreddit not found
            return 0
        else:
            # Handle other error cases
            return 0
    except requests.RequestException:
        # Handle network errors
        return 0
