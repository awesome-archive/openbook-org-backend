<img alt="Open book logo" src="https://i.snag.gy/conKBO.jpg" width="200">

![Human Friendly](https://img.shields.io/badge/human-friendly-brightgreen.svg) ![Privacy](https://img.shields.io/badge/privacy-first-690ddc.svg) [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/openbook-org/Lobby?source=orgpage)

The backend code for [api.open-book.org](https://api.open-book.org).

## Table of contents

- [Requirements](#requirements)
- [Project overview](#project-overview)
- [Contributing](#contributing)
    + [Code of Conduct](#code-of-conduct)
    + [License](#license)
    + [Other issues](#other-issues)
    + [Git commit message conventions](#git-commit-message-conventions)
- [Getting started](#getting-started)

## Requirements

* [Pipenv](https://github.com/pypa/pipenv)

## Project overview

The project is a [Django](https://www.djangoproject.com/start/) application. 

## Contributing

There are many different ways to contribute to the website development, just find the one that best fits with your skills and open an issue/pull request in the repository.

Examples of contributions we love include:

- **Code patches**
- **Bug reports**
- **Patch reviews**
- **Translations**
- **UI enhancements**

#### Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/OpenBookOrg/openbook-org-backend/blob/master/CODE_OF_CONDUCT.md).

#### License

Every contribution accepted is licensed under [AGPL v3.0](http://www.gnu.org/licenses/agpl-3.0.html) or any later version. 
You must be careful to not include any code that can not be licensed under this license.

Please read carefully [our license](https://github.com/OpenBookOrg/openbook-org-backend/blob/master/LICENSE.txt) and ask us if you have any questions.

#### Other issues

We have a [keybase public channel](https://keybase.io/team/openbookorg.public) where you can talk to us!

#### Git commit message conventions

Help us keep the repository history consistent 🙏!

We use [gitmoji](https://gitmoji.carloscuesta.me/) as our git message convention.

If you're using git in your command line, you can download the handy tool [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli).

## Getting started

Clone the repository

```sh
git clone git@github.com:OpenBookOrg/openbook-org-backend.git
```

Create and configure your .env file

```bash
cp sample.env .env
nano .env
```

Install the dependencies
```bash
$ pipenv install
```

Activate the pipenv environment
```bash
pipenv shell
```

Serve with hot reload at http://127.0.0.1:8000
```bash
$ python manage.py runserver
```

<br>

#### Happy coding 🎉!


