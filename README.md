# Linter for jinja2 #

Every now and then, it's pretty useful to just have a cli tool that does the job. This does it.

## Ansible ##

This fork of [jinja2-lint](https://github.com/drm/jinja2-lint) updates the
scripts to use `python3` as `python` isn't available by default on Debian
Bullseye and also adds a [ansiblej2lint.py](ansiblej2lint.py) script with a
list of [Ansible
filters](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html)
and [Ansible
tests](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tests.html).

## Usage: ##
```
cp j2lint.py /usr/local/bin/
j2lint.py my-template.j2
```

It accepts multiple arguments so shell expansion and/or combining with find is no issue:

```
j2lint.py *.j2
find src -type f -name "*.j2" -exec j2lint.py '{}' +
```

## Usage with custom filters, tests, etc ##

If you want to use this linter with custom filters, tests, etc, you can easily
extend the main cli endpoint by passing in a `env` keyword argument.

The file [custom_check_example.py](custom_check_example.py) provides a working example for the filter
'to_nice_json'. 

Note that for linting it is not necessary to refer to the actual implementation
of the filters, jinja2 only needs to know they exist.

## Usage with docker ##

To run this using docker, run:

```
docker run --rm -v "$(pwd)":/check kaictl/j2lint
```

Important options:

* `-e CUSTOMLINT=path/to/custom/lint`: the path to a custom lint py file in the directory you're checking.
  By default we check for `/custom.py`, so you can mount a file there instead of specifying this.
* `-v "$(pwd)":/check`: mount the current directory to `/check` on the container
