#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

def number_of_subscribers(subreddit):
  # Set a custom User-Agent header to avoid errors
  headers = {"User-Agent": "Bing Chat Bot"}
  # Construct the URL for the subreddit
  url = "https://www.reddit.com/r/" + subreddit + "/about.json"
  # Send a GET request to the URL and get the response
  response = requests.get(url, headers=headers)
  # Check if the response status code is 200 (OK)
  if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    # Get the number of subscribers from the data
    subscribers = data["data"]["subscribers"]
    # Return the number of subscribers
    return subscribers
  else:
    # If the response status code is not 200, return 0
    return 0
