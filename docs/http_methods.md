# Supported HTTP Methods

Not all HTTP methods are supported by Scheems, as each method is given a different purpose.
The methods listed here are effective for the [`scheems.applications.Scheems.add_model`](api_reference.md#scheems.applications.Scheems.add_model) and [`scheems.routes.scheems_route`](#) methods.

=== "GET"
    HTTP GET requests are used for endpoints that allow data retrieval.

    Allowing this method allows the following endpoints

    - `/model/{identifier}`
    - `/model/?foo=value&bar=value`; where `foo` and `bar` are fields defined in the model.

    !!! attention
        The second endpoint is a [Bulk Retrieve Endpoint](bulk_endpoints.md).

=== "POST"
    HTTP POST requests are used for endpoints that allow data modification

    This can be either

    - UPDATE
    - INSERT

    Effectively an UPSERT takes place.

    Allowing this method allows the following endpoints

    - `/model/{identifier}`

=== "DELETE"
    HTTP DELETE requests are allowed for endpoints that allow data deletion.

    Allowing this method allows the following endpoints

    - `/model/{identifier}`; deletes that single record
