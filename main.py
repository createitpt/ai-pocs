"""
POCs about artificial intelligence.
"""
from article_image_gen import generate_image_url
from comment_moderator import moderate_content
from title_generator import generate_title


def generate(content: str) -> None:
    """
    Generate article properties based on text.
    """
    try:
        moderated_content = moderate_content(content)

        if moderated_content.get("terms") is not None and len(moderated_content["terms"]) > 0:
            terms = [x["term"] for x in moderated_content["terms"]]
            print('\nContent contains inappropriate terms:')
            for term in terms:
                print(f'- {term}')
            print()
            return

        article_title = generate_title(content)
        image_url = generate_image_url(article_title)

        print(
            f'\n\033[1m{article_title}\033[0m',
            content,
            image_url,
            sep='\n\n',
            end='\n\n',
        )
    except Exception as err:
        print(f'\n {err}')


if __name__ == '__main__':
    content = input('Enter article\'s content: ')
    generate(content)