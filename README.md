# alpaca [![CircleCI](https://circleci.com/gh/felipemfp/alpaca.svg?style=shield)](https://circleci.com/gh/felipemfp/alpaca) [![codecov](https://codecov.io/gh/felipemfp/alpaca/branch/master/graph/badge.svg)](https://codecov.io/gh/felipemfp/alpaca)

> :sweat_drops: Spitting JSON as a microservice

**Alpaca** is a tool that aims to mock API requests in test enviroments such as CI.

It is available in [Docker Hub](https://hub.docker.com/r/felipemfp/alpaca/):

```bash
docker run -p 5000:5000 felipemfp/alpaca
```

#### Setting up an endpoint

You should send a POST request to `/__setup/<endpoint>`. For example:

```bash
curl \
  -d "[{"name": "Foo"}, {"name": "Joe"}]" \
  -X POST \
  http://localhost:5000/__setup/v2/users?method=GET&status=200&Content-Type=application/json
```

Now `alpaca` will send `[{"name": "Foo"}, {"name": "Joe"}]` when `/v2/users` is requested:

```bash
curl http://localhost:5000/v2/users
```

> The response status code is `200` and `Content-Type` header is `application/json`.


#### Clearing endpoints

You should send a POST request to `/__clear` in order to clear all endpoints.

#### List endpoints

You should send a GET request to `/__list` in order to list all saved endpoints.

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
