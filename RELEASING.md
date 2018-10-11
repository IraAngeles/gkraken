# Releasing

1. Bump the `APP_VERSION` property in `gkraken/conf.py` based on Major.Minor.Patch naming scheme
2. Update `CHANGELOG.md` for the impending release.
3. Update the `README.md` with the new changes (if necessary).
4. `python3 setup.py sdist` 
5. `git commit -am "Prepare for release X.Y.Z"` (where X.Y.Z is the version you set in step 1)
6. `git push`
7. Create a new release on Github
    1. Tag version `X.Y.Z` (`git tag -s X.Y.Z && git push --tags`)
    2. Release title `X.Y.Z`
    3. Paste the content from `CHANGELOG.md` as the description
    4. Upload the `dist/gkraken-X.X.X.tar.gz`
8. Create a PR from [master](../../tree/master) to [release](../../tree/release)
9. `twine upload dist/*`