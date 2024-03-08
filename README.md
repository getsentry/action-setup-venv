action-setup-venv
==================

Sets up python and a virtual environment with caching.

The main benefit of this action over using `setup-python` is that it caches
the entire venv directory and will skip the `pip install ...` entirely
when the cache is available.

### Usage

```yaml
    - uses: getsentry/action-setup-venv@v2.0.0
      id: venv
      with:
        python-version: 3.10.7
        cache-dependency-path: |
          requirements.txt
          requirements-frozen.txt
        install-cmd: pip install -r requirements.txt -c requirements-frozen.txt
```
