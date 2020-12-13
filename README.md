# monei
The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.5
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/monei/monei-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/monei/monei-python-sdk.git`)

Then import the package:
```python
import monei
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import monei
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import monei
from monei.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID
cancel_payment_request = monei.CancelPaymentRequest() # CancelPaymentRequest |  (optional)

    try:
        # Cancel Payment
        api_response = api_instance.cancel(id, cancel_payment_request=cancel_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->cancel: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://api.monei.net/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PaymentsApi* | [**cancel**](docs/PaymentsApi.md#cancel) | **POST** /payments/{id}/cancel | Cancel Payment
*PaymentsApi* | [**capture**](docs/PaymentsApi.md#capture) | **POST** /payments/{id}/capture | Capture Payment
*PaymentsApi* | [**confirm**](docs/PaymentsApi.md#confirm) | **POST** /payments/{id}/confirm | Confirm Payment
*PaymentsApi* | [**create**](docs/PaymentsApi.md#create) | **POST** /payments | Create Payment
*PaymentsApi* | [**get**](docs/PaymentsApi.md#get) | **GET** /payments/{id} | Get Payment
*PaymentsApi* | [**recurring**](docs/PaymentsApi.md#recurring) | **POST** /payments/{sequenceId}/recurring | Recurring Payment
*PaymentsApi* | [**refund**](docs/PaymentsApi.md#refund) | **POST** /payments/{id}/refund | Refund Payment


## Documentation For Models

 - [Address](docs/Address.md)
 - [CancelPaymentRequest](docs/CancelPaymentRequest.md)
 - [CapturePaymentRequest](docs/CapturePaymentRequest.md)
 - [Card](docs/Card.md)
 - [ConfirmPaymentRequest](docs/ConfirmPaymentRequest.md)
 - [CreatePaymentRequest](docs/CreatePaymentRequest.md)
 - [Error](docs/Error.md)
 - [Payment](docs/Payment.md)
 - [PaymentBillingDetails](docs/PaymentBillingDetails.md)
 - [PaymentCancellationReason](docs/PaymentCancellationReason.md)
 - [PaymentCustomer](docs/PaymentCustomer.md)
 - [PaymentLastRefundReason](docs/PaymentLastRefundReason.md)
 - [PaymentNextAction](docs/PaymentNextAction.md)
 - [PaymentPaymentMethod](docs/PaymentPaymentMethod.md)
 - [PaymentPaymentMethodBizum](docs/PaymentPaymentMethodBizum.md)
 - [PaymentPaymentMethodCard](docs/PaymentPaymentMethodCard.md)
 - [PaymentPaymentMethodInput](docs/PaymentPaymentMethodInput.md)
 - [PaymentPaymentMethodPaypal](docs/PaymentPaymentMethodPaypal.md)
 - [PaymentRefundReason](docs/PaymentRefundReason.md)
 - [PaymentSequence](docs/PaymentSequence.md)
 - [PaymentSequenceRecurring](docs/PaymentSequenceRecurring.md)
 - [PaymentSessionDetails](docs/PaymentSessionDetails.md)
 - [PaymentShippingDetails](docs/PaymentShippingDetails.md)
 - [PaymentShop](docs/PaymentShop.md)
 - [PaymentStatus](docs/PaymentStatus.md)
 - [PaymentTraceDetails](docs/PaymentTraceDetails.md)
 - [PaymentTransactionType](docs/PaymentTransactionType.md)
 - [RecurringPaymentRequest](docs/RecurringPaymentRequest.md)
 - [RefundPaymentRequest](docs/RefundPaymentRequest.md)


## Documentation For Authorization


## APIKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



