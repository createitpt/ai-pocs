import os
import io
from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from msrest.authentication import CognitiveServicesCredentials


def moderate_content(text: str) -> dict:
    """
    Moderate content using Azure Content Moderator.
    """
    client = ContentModeratorClient(
        endpoint='https://content-moderator-vrb.cognitiveservices.azure.com/',
        credentials=CognitiveServicesCredentials(os.getenv('SUBSCRIPTION_KEY'))
    )
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=io.StringIO(text),
        language='',
        autocorrect=True,
        pii=True
    )
    return screen.as_dict()
