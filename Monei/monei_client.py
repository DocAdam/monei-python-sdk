import lib

class MoneiClient(object):
    _default = None

    def __init__(self, api_key=None, config=None):

        self.config = config if config else lib.Configuration(
            host="https://api.microapps-staging.com/v1" # REMOVE
        )

        self.config.api_key = {
            'Authorization': api_key
        }

        # Enter a context with an instance of the API client
        with lib.ApiClient(self.config) as api_client:
            api_client.user_agent = 'MONEI/PYTHON/0.1.5'
            self.payments = lib.PaymentsApi(api_client)

    def verifySignature(self, body, signature):
        """Verifies response signature
        :param body: string JSON content to be verified
        :param signature: string signature to verify against
        :return: parsed object of the body
        """
        # $parts = array_reduce(explode(',', $signature), function ($result, $part) {
        #     [$key, $value] = explode('=', $part);
        #     $result[$key] = $value;
        #     return $result;
        # }, []);

        # $hmac = hash_hmac('SHA256', $parts['t'] . '.' . $body, $this->config->getApiKey('Authorization'));

        # if ($hmac !== $parts['v1']) {
        #     throw new ApiException('[401] Signature verification failed', 401);
        # }

        # return json_decode($body);

        return {}
