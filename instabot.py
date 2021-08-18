from instapy import InstaPy

session = InstaPy(username="neilstark74", password="8k8StWgJjjdx8Lr")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()