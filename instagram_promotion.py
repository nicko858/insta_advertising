from instabot import Bot
from os import getenv
from dotenv import load_dotenv
import re
from pprint import pprint
from collections import defaultdict
import argparse


def get_args():
    script_usage = "python instagram_promotion.py <promo_owner> <post_url>"
    parser = argparse.ArgumentParser(
        description="How to run instagram_promotion.py:",
        usage=script_usage
    )
    parser.add_argument(
        "promo_owner",
        type=str,
        help="Specify the promo_owner"
    )
    parser.add_argument(
        "post_url",
        type=str,
        help="Specify the instagram-post url"
    )
    args = parser.parse_args()
    return args


def is_user_exist(mentioned_friends):
    user_exist = any(bot.get_user_id_from_username(username)
                     for username in mentioned_friends)
    return user_exist


def is_friend_mentioned(comment):
    # Regex for Instagram Username by Jonathan Stassen:
    # https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
    pattern = ("(?:@)([A-Za-z0-9_]"
               "(?:(?:[A-Za-z0-9_]|"
               "(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)")
    mentioned_friends = re.findall(pattern, comment)
    return mentioned_friends


def get_winners(members):
    winners = []
    winner_flags = ["friend_mentioned", "is_liker", "is_follower"]
    for user, user_flags in members.items():
        if all(flag in user_flags for flag in winner_flags):
            winners.append(user)
    return winners


if __name__ == '__main__':
    load_dotenv()
    args = get_args()
    bot = Bot()
    inst_login = getenv("INST_LOGIN")
    inst_passwd = getenv("INST_PASSWD")
    bot.login(username=inst_login, password=inst_passwd, use_cookie=False)
    promo_owner = args.promo_owner
    media_id = bot.get_media_id_from_link(args.post_url)
    likers = bot.get_media_likers(media_id)
    comments = bot.get_media_comments_all(media_id)
    followers = bot.get_user_followers(promo_owner)
    members = defaultdict(list)
    for comment in comments:
        mentioned_friends = is_friend_mentioned(comment["text"])
        if not mentioned_friends:
            continue
        author_user_id = comment["user_id"]
        author_user_name = comment["user"]["username"]
        if is_user_exist(mentioned_friends):
            members[author_user_name].append("friend_mentioned")
        if str(author_user_id) in likers:
            members[author_user_name].append("is_liker")
        if str(author_user_id) in followers:
            members[author_user_name].append("is_follower")
    winners = get_winners(members)
    pprint(winners)
