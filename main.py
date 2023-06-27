"""
POC about how to use the article image generator and the comment moderator.
"""
from article_image_gen import generate_image_url
from comment_moderator import moderate_content


article_title = 'Idea generation model for cells'
# article_title = 'Idea generation model for fucking cells'

try:
    moderated_content = moderate_content(article_title)

    if moderated_content.get("terms") is not None and len(moderated_content["terms"]) > 0:
        terms = [x["term"] for x in moderated_content["terms"]]
        raise Exception(f"Content contains inappropriate terms: {terms}")

    image_url = generate_image_url(article_title)

    print('Title:', article_title)
    print('Image:', image_url)
except Exception as err:
    print(err)