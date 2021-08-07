# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v3.12.0] - 2021-08-07

- fix docs generation
- fix tags name in CHANGELOG
- setup github release from github actions

## [v3.11.1] - 2021-07-25

- add README on PyPI

## [v3.11.0] - 2021-07-25

- :warning: deprecated `enum_to_choices`, as [a better
  version](https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types) is available in django 3.0.
- added `output_field` argument for `query_sum`, and a unit test
- added documentation
- added changelog
- setup automatic publication on PyPI & Docker Hub
- internaly fixed W042
- internaly switched from pipenv to poetry
- internaly switched from travis to github actions
- internaly switched from coveralls to codecov

## [v3.10.4] - 2020-02-03

- more type hints
- update CI

## [v3.10.3] - 2020-01-11

- use setuptools-scm

## [v3.10.2] - 2020-01-11

- Add mypy to pre-commit
- pep-561 compliance

## [v3.10.1] - 2020-01-06

- Improve tooling with:
    - mypy
    - pydocstyle
    - pre-commit
- Update:
    - Python 3.8
    - Django 3.0

## [v3.10.0] - 2020-01-06
## [v3.9.4] - 2019-02-24

- fix the regex to get the requirements right.

## [v3.9.3] - 2019-02-24
## [v3.9.2] - 2019-02-24
## [v3.9.1] - 2019-02-24

- Use django-autoslug again

## [v3.9.0] - 2018-09-05

- Add `navbar_item` templatetag

## [v3.8.1] - 2018-08-08

- Fix packaging for python 3.6 & 3.7

## [v3.8.0] - 2018-08-08

- update dependencies (bootstrap 4.0.0 -> 4.1.3)
- add semantic blocks (`<header>` & `<main>`)
- allow customisation by adding xblocks `header_navbar` & `main_content`

## [v3.7.1] - 2018-08-04

- Fix packaging

## [v3.7.0] - 2018-08-04

- use only Pipfile
- add `NDHDeleteMixin`
- fix compatibility with Django 2.1

## [v3.6.0] - 2018-07-13

- `NamedModel` querysets can now be ordered by name with `NamedModel.objects.name_ordered()`

## [v3.5.1] - 2018-04-01
## [v3.5.0] - 2018-04-01
## [v3.4.0] - 2018-03-31
## [v3.3.0] - 2018-03-26
## [v2.1.0] - 2018-03-12

- backport `utils.get_env` in v2

## [v3.2.1] - 2018-03-10
## [v3.2.0] - 2018-03-05
## [v3.1.0] - 2018-03-01
## [v3.0.3] - 2018-02-17
## [v3.0.2] - 2018-02-17
## [v3.0.1] - 2018-02-17
## [v3.0.0] - 2018-02-17
## [v2.0.0] - 2018-01-12


[Unreleased]: https://github.com/nim65s/ndh/compare/v3.12.0...master
[v3.12.0]: https://github.com/nim65s/ndh/compare/v3.11.1...v3.12.0
[v3.11.1]: https://github.com/nim65s/ndh/compare/v3.11.0...v3.11.1
[v3.11.0]: https://github.com/nim65s/ndh/compare/v3.10.4...v3.11.0
[v3.10.4]: https://github.com/nim65s/ndh/compare/v3.10.3...v3.10.4
[v3.10.3]: https://github.com/nim65s/ndh/compare/v3.10.2...v3.10.3
[v3.10.2]: https://github.com/nim65s/ndh/compare/v3.10.1...v3.10.2
[v3.10.1]: https://github.com/nim65s/ndh/compare/v3.10.0...v3.10.1
[v3.10.0]: https://github.com/nim65s/ndh/compare/v3.9.4...v3.10.0
[v3.9.4]: https://github.com/nim65s/ndh/compare/v3.9.3...v3.9.4
[v3.9.3]: https://github.com/nim65s/ndh/compare/v3.9.2...v3.9.3
[v3.9.2]: https://github.com/nim65s/ndh/compare/v3.9.1...v3.9.2
[v3.9.1]: https://github.com/nim65s/ndh/compare/v3.9.0...v3.9.1
[v3.9.0]: https://github.com/nim65s/ndh/compare/v3.8.1...v3.9.0
[v3.8.1]: https://github.com/nim65s/ndh/compare/v3.8.0...v3.8.1
[v3.8.0]: https://github.com/nim65s/ndh/compare/v3.7.1...v3.8.0
[v3.7.1]: https://github.com/nim65s/ndh/compare/v3.7.0...v3.7.1
[v3.7.0]: https://github.com/nim65s/ndh/compare/v3.6.0...v3.7.0
[v3.6.0]: https://github.com/nim65s/ndh/compare/v3.5.1...v3.6.0
[v3.5.1]: https://github.com/nim65s/ndh/compare/v3.5.0...v3.5.1
[v3.5.0]: https://github.com/nim65s/ndh/compare/v3.4.0...v3.5.0
[v3.4.0]: https://github.com/nim65s/ndh/compare/v3.3.0...v3.4.0
[v3.3.0]: https://github.com/nim65s/ndh/compare/v3.2.1...v3.3.0
[v2.1.0]: https://github.com/nim65s/ndh/compare/v2.0.0...v2.1.0
[v3.2.1]: https://github.com/nim65s/ndh/compare/v3.2.0...v3.2.1
[v3.2.0]: https://github.com/nim65s/ndh/compare/v3.1.0...v3.2.0
[v3.1.0]: https://github.com/nim65s/ndh/compare/v3.0.3...v3.1.0
[v3.0.3]: https://github.com/nim65s/ndh/compare/v3.0.2...v3.0.3
[v3.0.2]: https://github.com/nim65s/ndh/compare/v3.0.1...v3.0.2
[v3.0.1]: https://github.com/nim65s/ndh/compare/v3.0.0...v3.0.1
[v3.0.0]: https://github.com/nim65s/ndh/compare/v2.0.0...v3.0.0
[v2.0.0]: https://github.com/nim65s/ndh/releases/tag/v2.0.0
