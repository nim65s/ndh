# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v6.10.1] - 2025-03-13

## [v6.10.0] - 2025-03-13

- poetry -> uv
- drop safety

## [v6.9.2] - 2024-12-17

- dependency / tooling upgrades

## [v6.9.1] - 2024-02-01

- templates: fix log out button

## [v6.9.0] - 2024-01-25

- add `widgets.AccessibleDateInput`
- update release process

## [v6.8.0] - 2024-01-17

- Improve `show_email`:
    - allow css "klass"

## [v6.7.0] - 2024-01-17

- Improve `show_email`:
    - allow single argument which is iterable

## [v6.6.0] - 2024-01-17

- Improve `show_email`:
    - set recipient by email string or `User` object
    - allow multiple recipient
    - allow optional link text
    - allow optional mail subject

## [v6.5.3] - 2023-09-13

- fix release

## [v6.5.2] - 2023-09-13

- release: use pipx
- `show_phone`: allow (+33)

## [v6.5.1] - 2023-09-13

- `show_phone`: remove spaces in link

## [v6.5.0] - 2023-09-07

- css: remove brackets around .mail

## [v6.4.2] - 2023-09-06

- fix curly brace escaping in format strings

## [v6.4.1] - 2023-09-06

- `show_email` & `show_phone`: fix for multiple occurences per page

## [v6.4.0] - 2023-09-06

- Add `show_phone` simple tag
- `show_email` & `show_phone`: provide links via javascript

## [v6.3.0] - 2023-09-01

- Add `ndh.utils.set_env`

## [v6.2.0] - 2023-04-06

- Add `ndh.tests.TestNDHLinks`

## [v6.1.0] - 2023-04-03

- improve `Links` with getters for create, delete, detail, list & update urls

## [v6.0.0] - 2023-03-24

- :warning: require python 3.10
- add `AttrContextMixin`
- update tooling

## [v5.12.1] - 2023-02-02

- typo

## [v5.12.0] - 2023-02-02

- `utils.get_env()` works in main dir or subdir, for use in `manage.py`, `wsgi.py` and `asgi.py`
- `utils.get_env()` discard lines starting with `#`

## [v5.11.3] - 2022-10-16

- update unit tests

## [v5.11.2] - 2022-10-16

- navbar with more flex and less floats

## [v5.11.1] - 2022-10-16

- fix navbar responsiveness

## [v5.11.0] - 2022-10-16

- add template tags to docs
- add `user_smcp` filter, for capitalized `first_name` + capitalized & small-capsed `last_name`

## [v5.10.0] - 2022-10-11

- add `templates/ndh/dt.html` to represent a datetime

## [v5.9.1] - 2022-10-10

- clarify delete.html

## [v5.9.0] - 2022-10-07

- add `ndh_form_action` variable in `ndh/form.html`

## [v5.8.2] - 2022-09-24

- fix tables template for non paginated ones

## [v5.8.1] - 2022-09-08

- update bootstrap to 5.2.1
- update django-bootstrap5 to 22.1

## [v5.8.0] - 2022-08-30

- add datalist support

## [v5.7.4] - 2022-08-29

- fix previous release

## [v5.7.3] - 2022-08-29

- fix `AccessiblDateTimeField` for localized date initial value

## [v5.7.2] - 2022-08-26

- fix `NDHFormMixin.get_success_url`

## [v5.7.1] - 2022-08-26

- implement `NDHFormMixin.continue_edit` for formsets

## [v5.7.0] - 2022-08-26

- added `NDHFormMixin.continue_edit`

## [v5.6.0] - 2022-08-25

- added `Links.get_md_link`
- added `Links.get_full_link`
- added `Links.get_full_md_link`

## [v5.5.5] - 2022-08-19

- Allow `ManyRelatedManager` in `Links`
- Remove mypy

## [v5.5.4] - 2022-03-16

- update tools configuration
- fix 88 col line length
- remove uselesse button in password reset complete

## [v5.5.3] - 2022-03-13

- extraneous block in registration

## [v5.5.2] - 2022-03-13

- missing load in registration

## [v5.5.1] - 2022-03-12

- typo
- model fields translations

## [v5.5.0] - 2022-03-11

- templates: add formset & tables over `django_tables2/bootstrap4.html` for pagination
- style: bigger buttons

## [v5.4.2] - 2022-02-28

- fix missing load i18n in templates

## [v5.4.1] - 2022-02-28

## [v5.4.0] - 2022-02-28

- translations
- add pyupgrade

## [v5.3.0] - 2022-02-23

- add `Links.get_full_admin_url`

## [v5.2.0] - 2022-02-23

- fix typing for related manager
- yapf → black
- move most tooling conf from setup.cfg to pyproject.toml
- CI: check python 3.10
- set `__version__` / `__version_tuple__` from release.sh

## [v5.1.2] - 2021-12-20

- fix docs

## [v5.1.1] - 2021-12-20

- release: typo

## [v5.1.0] - 2021-12-20

- remove obsolete boostrap 4 css
- remove setuptools & setup.py

## [v5.0.1] - 2021-09-17

- fix README

## [v5.0.0] - 2021-09-17

- :warning: BREAKING :warning: require python >= 3.8
- fix doc generation

## [v4.0.0] - 2021-09-17

- :warning: BREAKING :warning: bootstrap 4 → 5. Please read
  [boostrap 5 migration guide](https://getbootstrap.com/docs/5.1/migration/) and
  [django-bootstrap5 migration guide](https://django-bootstrap5.readthedocs.io/en/latest/migrate.html)
- :warning: BREAKING :warning: remove deprecated `enum_to_choices`
- require django >= 3

## [v3.12.6] - 2021-08-07

- fix release action

## [v3.12.5] - 2021-08-07

- fix release action

## [v3.12.4] - 2021-08-07

- fix release action

## [v3.12.3] - 2021-08-07

- fix release action

## [v3.12.2] - 2021-08-07

- fix release action

## [v3.12.1] - 2021-08-07

- fix release action

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


[Unreleased]: https://github.com/nim65s/ndh/compare/v6.10.1...master
[v6.10.1]: https://github.com/nim65s/ndh/compare/v6.10.0...v6.10.1
[v6.10.0]: https://github.com/nim65s/ndh/compare/v6.9.2...v6.10.0
[v6.9.2]: https://github.com/nim65s/ndh/compare/v6.9.1...v6.9.2
[v6.9.1]: https://github.com/nim65s/ndh/compare/v6.9.0...v6.9.1
[v6.9.0]: https://github.com/nim65s/ndh/compare/v6.8.0...v6.9.0
[v6.8.0]: https://github.com/nim65s/ndh/compare/v6.7.0...v6.8.0
[v6.7.0]: https://github.com/nim65s/ndh/compare/v6.6.0...v6.7.0
[v6.6.0]: https://github.com/nim65s/ndh/compare/v6.5.3...v6.6.0
[v6.5.3]: https://github.com/nim65s/ndh/compare/v6.5.2...v6.5.3
[v6.5.2]: https://github.com/nim65s/ndh/compare/v6.5.1...v6.5.2
[v6.5.1]: https://github.com/nim65s/ndh/compare/v6.5.0...v6.5.1
[v6.5.0]: https://github.com/nim65s/ndh/compare/v6.4.2...v6.5.0
[v6.4.2]: https://github.com/nim65s/ndh/compare/v6.4.1...v6.4.2
[v6.4.1]: https://github.com/nim65s/ndh/compare/v6.4.0...v6.4.1
[v6.4.0]: https://github.com/nim65s/ndh/compare/v6.3.0...v6.4.0
[v6.3.0]: https://github.com/nim65s/ndh/compare/v6.2.0...v6.3.0
[v6.2.0]: https://github.com/nim65s/ndh/compare/v6.1.0...v6.2.0
[v6.1.0]: https://github.com/nim65s/ndh/compare/v6.0.0...v6.1.0
[v6.0.0]: https://github.com/nim65s/ndh/compare/v5.12.1...v6.0.0
[v5.12.1]: https://github.com/nim65s/ndh/compare/v5.12.0...v5.12.1
[v5.12.0]: https://github.com/nim65s/ndh/compare/v5.11.3...v5.12.0
[v5.11.3]: https://github.com/nim65s/ndh/compare/v5.11.2...v5.11.3
[v5.11.2]: https://github.com/nim65s/ndh/compare/v5.11.1...v5.11.2
[v5.11.1]: https://github.com/nim65s/ndh/compare/v5.11.0...v5.11.1
[v5.11.0]: https://github.com/nim65s/ndh/compare/v5.10.0...v5.11.0
[v5.10.0]: https://github.com/nim65s/ndh/compare/v5.9.1...v5.10.0
[v5.9.1]: https://github.com/nim65s/ndh/compare/v5.9.0...v5.9.1
[v5.9.0]: https://github.com/nim65s/ndh/compare/v5.8.2...v5.9.0
[v5.8.2]: https://github.com/nim65s/ndh/compare/v5.8.1...v5.8.2
[v5.8.1]: https://github.com/nim65s/ndh/compare/v5.8.0...v5.8.1
[v5.8.0]: https://github.com/nim65s/ndh/compare/v5.7.4...v5.8.0
[v5.7.4]: https://github.com/nim65s/ndh/compare/v5.7.3...v5.7.4
[v5.7.3]: https://github.com/nim65s/ndh/compare/v5.7.2...v5.7.3
[v5.7.2]: https://github.com/nim65s/ndh/compare/v5.7.1...v5.7.2
[v5.7.1]: https://github.com/nim65s/ndh/compare/v5.7.0...v5.7.1
[v5.7.0]: https://github.com/nim65s/ndh/compare/v5.6.0...v5.7.0
[v5.6.0]: https://github.com/nim65s/ndh/compare/v5.5.5...v5.6.0
[v5.5.5]: https://github.com/nim65s/ndh/compare/v5.5.4...v5.5.5
[v5.5.4]: https://github.com/nim65s/ndh/compare/v5.5.3...v5.5.4
[v5.5.3]: https://github.com/nim65s/ndh/compare/v5.5.2...v5.5.3
[v5.5.2]: https://github.com/nim65s/ndh/compare/v5.5.1...v5.5.2
[v5.5.1]: https://github.com/nim65s/ndh/compare/v5.5.0...v5.5.1
[v5.5.0]: https://github.com/nim65s/ndh/compare/v5.4.2...v5.5.0
[v5.4.2]: https://github.com/nim65s/ndh/compare/v5.4.1...v5.4.2
[v5.4.1]: https://github.com/nim65s/ndh/compare/v5.4.0...v5.4.1
[v5.4.0]: https://github.com/nim65s/ndh/compare/v5.3.0...v5.4.0
[v5.3.0]: https://github.com/nim65s/ndh/compare/v5.2.0...v5.3.0
[v5.2.0]: https://github.com/nim65s/ndh/compare/v5.1.2...v5.2.0
[v5.1.2]: https://github.com/nim65s/ndh/compare/v5.1.1...v5.1.2
[v5.1.1]: https://github.com/nim65s/ndh/compare/v5.1.0...v5.1.1
[v5.1.0]: https://github.com/nim65s/ndh/compare/v5.0.1...v5.1.0
[v5.0.1]: https://github.com/nim65s/ndh/compare/v5.0.0...v5.0.1
[v5.0.0]: https://github.com/nim65s/ndh/compare/v4.0.0...v5.0.0
[v4.0.0]: https://github.com/nim65s/ndh/compare/v3.12.6...v4.0.0
[v3.12.6]: https://github.com/nim65s/ndh/compare/v3.12.5...v3.12.6
[v3.12.5]: https://github.com/nim65s/ndh/compare/v3.12.4...v3.12.5
[v3.12.4]: https://github.com/nim65s/ndh/compare/v3.12.3...v3.12.4
[v3.12.3]: https://github.com/nim65s/ndh/compare/v3.12.2...v3.12.3
[v3.12.2]: https://github.com/nim65s/ndh/compare/v3.12.1...v3.12.2
[v3.12.1]: https://github.com/nim65s/ndh/compare/v3.12.0...v3.12.1
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
