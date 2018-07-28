# losp-dopplershift
SciPy 2019 tutorial

* `source activate suos`  will install this package to the suos environment
* `pip install -e .`  -e is for editable installation
* test with `pytest`
* test coverage with `pytest --cov=hugs`
* add repository to Travis
* create and switch to a new branch `git checkout -b add-travis`
* create a travis config file .travis.yml
* add, commit, and push to github `git push --set-upstream origin add-travis`
* in Github, check in the Pull requests tab if the Travis build has passed
* If no problems, press Confirm merge request, and confirm merge
* test for pep8 violations `pytest --flake8`
* setup.cfg is a configuration file, there can specify flake8 warning to ignore
