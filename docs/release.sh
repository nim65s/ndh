#!/bin/bash -eux
# ./docs/release.sh [patch|minor|major]

[[ $(basename "$PWD") == docs ]] && cd ..

OLD=$(uv run --script docs/release.py old)
NEW=$(uv run --script docs/release.py "$1")
DATE=$(date +%Y-%m-%d)

sed -ri "/__version__ /s/[0-9.]+/$NEW/" ndh/__init__.py
sed -i "/^## \[Unreleased\]/a \\\n## [v$NEW] - $DATE" CHANGELOG.md
sed -i "/^\[Unreleased\]/s/$OLD/$NEW/" CHANGELOG.md
sed -i "/^\[Unreleased\]/a [v$NEW]: https://github.com/nim65s/ndh/compare/v$OLD...v$NEW" CHANGELOG.md

git add ndh/__init__.py pyproject.toml CHANGELOG.md
git commit -m "Release v$NEW"
git tag -s "v$NEW" -m "Release v$NEW"
git push
git push --tags
