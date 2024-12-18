from mistralai import Mistral

from app.core.settings import get_property


def create_client():
    try:
        return Mistral(api_key=get_property('mistral_api_key'))
    except Exception as e:
        print(f'Execption occurred on mistral client: {e}')
