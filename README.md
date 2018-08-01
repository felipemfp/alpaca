# alpaca

> :sweat_drops: Spitting JSON as a microservice

**Alpaca** is a tool that aims to mock API requests in test enviroments such as CI.

It is available in [Docker Hub](https://hub.docker.com/r/felipemfp/alpaca/):

```bash
docker run -p 5000:5000 felipemfp/alpaca
```

#### Setting up an endpoint

You should send a POST request to `/__setup/<endpoint>`.

Where `<endpoint>` is the URL you expect to use. For example:

If I want `/v2/users`, I'll send a setup request to `/__setup/v2/users`.

In the body, you should send what you expect to receive as a response.

You could use query strings to specify `status` (e.g.: 200, 404, 401) and other headers. For example:

Let's say my response should send a JSON with a status code equals to 401, I'll setup an endpoint with:

```
/__setup/v2/users?status=401&Content-Type=application/json
```

And the body:

```json
[{"name": "Foo"}, {"name": "Joe"}]
```

Once setup is done, when I ask `/v2/users`, **alpaca** will answer with `[{"name": "Foo"}, {"name": "Joe"}]`, status code as `401` and `Content-Type` in headers with `application/json`.

#### Clearing endpoints

You should send a POST request to `/__clear` in order to clear all endpoints.

> More docs are coming.

---

### Prerequisites

* Python 3
* pipenv

### Installing

Once you have the project cloned to your computer, install the dependencies with pipenv:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

Run the project:

```bash
FLASK_APP=alpaca.py flask run --reload
```

Now you can try it on http://localhost:5000.

## Contributing

Please feel free for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/felipemfp/alpaca/tags). 

## Authors

* **Felipe Pontes** - *Initial work* - [felipemfp](https://github.com/felipemfp)

See also the list of [contributors](https://github.com/felipemfp/alpaca/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
