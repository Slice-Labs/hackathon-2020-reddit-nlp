# Hackathon 2020: NLP on Reddit

## Getting Started

* Clone this repository to your local machine:

  ```bash
  git clone https://github.com/Slice-Labs/hackathon-2020-reddit-nlp.git
  ```

  Or downlod the code as a [ZIP file](https://github.com/Slice-Labs/hackathon-2020-reddit-nlp/archive/master.zip)

* Download the data at the link provided with the handout

* Extract the data:

  ```bash
  unzip data.zip -d data
  ```

  The data directory will now contain one `.json` file per subreddit (think of
  this JSON as just a list of nested dictionaries and lists containing raw
  strings and numeric values).

* Inspect the data format. Loading one subreddit `.json` file here in python we
  can see the structure of a submission (one post). The most important content
  to note here are the `title`, `text`, and `comments` fields. Not all comments
  are included since expanding the comment forest requires additional API calls
  and becomes time consuming. The submission score as well as comment scores
  are also included. For additional information on Reddit and how this data was
  obtained, consult the [PRAW
  documentation](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)
  and specifically the attributes of the [Submission model](
  https://praw.readthedocs.io/en/latest/code_overview/models/submission.html#praw.models.Submission)


  ```python
  $ python3
  >>> import json
  >>> from pprint import pprint
  >>> data = json.load(open('data/ridesharedrivers_top.json', 'r'))
  >>> # print a submission (data is a list of submissions):
  >>> pprint(data[1])
  {'comments': [{'body': 'I hate this. I once drove 25 minutes one way to drive '
                      'someone a mile up the road and then drive 25 minute '
                      'back without getting another ride in the meantime. An '
                      'hour of my life wasted for $3, not even $3.75\n'
                      '\n'
                      'When I tried editing my driver profile to request that '
                      'riders cancel the trip if they see I’ll be driving '
                      'over ten minutes to pick them up just to have them in '
                      'my car for less than three, Uber wouldn’t allow it. '
                      'Priceless',
              'created_utc': 1560306746.0,
              'score': 1},
              {'body': "How much was Lyft's fee?",
              'created_utc': 1560347877.0,
              'score': 1},
              {'body': 'I did this without complaining. I did get burn out on '
                      'ride-share after they continued to hire more and more '
                      'and the work was less and less. Head to a bigger city, '
                      'maybe? Sleep in your car? Lots of coffee? .... Maybe '
                      'just share your private thoughts in an emergency room?',
              'created_utc': 1560369188.0,
              'score': 1},
              {'body': "That's a problem with Lyft. At least with Uber, you "
                      'get time and distance after 10 minutes.',
              'created_utc': 1561445601.0,
              'score': 1},
              {'body': 'I had a 45 minute shared lyft get me 12$ before. '
                      'Rental drivers in my area make 45cents a mile amd '
                      '22cents/minute. So really, we are reimbursed for '
                      'mileage, not "paid" haha',
              'created_utc': 1561482544.0,
              'score': 1},
              {'body': 'Thats why you dont accept those unless if they say 45+ '
                      'minute ride.  They cant punish you for not accepting '
                      'work even though they make it seem like they can.',
              'created_utc': 1564856883.0,
              'score': 1},
              {'body': 'Contact Lyft in that rides help section. You get a '
                      'bonus for rides over 10 minutes but you got to contact '
                      'them to get it. Just FYI contact them ASAP',
              'created_utc': 1567529999.0,
              'score': 1}],
  'created_utc': 1560293747.0,
  'is_self': True,
  'num_comments': 9,
  'permalink': '/r/ridesharedrivers/comments/bzjf1y/just_drove_20_mins_to_wait_5_mins_finally_pick/',
  'score': 10,
  'text': '',
  'title': 'Just drove 20 mins to wait 5 mins finally pick the man up to then '
          'go 1.1 miles. Thanks for the $3.75 lyft!',
  'upvote_ratio': 0.92,
  'url': 'https://www.reddit.com/r/ridesharedrivers/comments/bzjf1y/just_drove_20_mins_to_wait_5_mins_finally_pick/'}
  ```

* To convert all of this into a [Pandas
  Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html),
  use the builtin function:

  ```python
  >>> import pandas as pd
  >>> df = pd.read_json('data/ridesharedrivers_top.json')
  ```
