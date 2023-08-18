import requests
import exllama_api_client

# TODO initialize a static variable for the URL

class Completion:

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new completion for the provided prompt and parameters.
        """

        if not exllama_api_client.api_url:
            raise ValueError("API URL cannot be empty")

        response = requests.post(
                exllama_api_client.api_url+'/api/v1/completions', 
                headers={'Content-Type': 'application/json'},
                json=kwargs
            ).json()
        return response
