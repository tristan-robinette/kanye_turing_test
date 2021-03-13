from flask import Flask, jsonify, render_template
import random
from ai.ai import is_kanye

app = Flask(__name__)

REAL_TWEET = 0
FAKE_TWEET = 1

@app.route('/gen/', methods=['POST'])
def gen_tweet():
    data = generate_tweet()
    return jsonify(data)


@app.route('/')
def index():

    context = generate_tweet()

    return render_template('index.html', context=context)


def generate_tweet():

    # pick randomly if tweet will be real or not.
    status = random.randint(REAL_TWEET,FAKE_TWEET)

    tweet = is_kanye(status)
    # enhances the user experience with better tweets
    if len(tweet) < 5:
        while len(tweet) < 5:
            tweet = is_kanye(status)

    # setup initial tweet
    context = dict()
    context['total_comments'] = str(round(random.uniform(1, 2), 2)) + 'k'
    context['total_retweets'] = str(round(random.uniform(3, 5), 2)) + 'k'
    context['total_hearts'] = str(round(random.uniform(5, 8), 2)) + 'k'
    context['tweet'] = tweet
    context['status'] = status

    return context


if __name__ == '__main__':
    app.run(threaded=True, port=4000)
