#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

if not os.path.isfile("Count.txt"):
    Count = []
else:
    with open("Count.txt","+") as c:
        count = c.read()

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('India')
for submission in subreddit.new(limit=100):

    #print(submission.title)

    for comments in submission.comments:
    # If we haven't replied to this post before
        if submission.comments.id not in posts_replied_to:

        # Do a case insensitive search
            if re.search("D A I L Y", comments, re.IGNORECASE):
                # Reply to the post
                submission.reply("Total number of threads I've counted")
                print("Bot replying to : ", submission.title)

            # Store the current id into our list
                posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
