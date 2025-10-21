action-setup-venv
==================

Sets up python and a virtual environment with caching.

The main benefit of this action over using `setup-python` is that it caches
the entire venv directory and will skip the `pip install ...` entirely
when the cache is available.

### Usage

uv:
```yaml
    - uses: astral-sh/setup-uv@884ad927a57e558e7a70b92f2bccf9198a4be546 # v6
      with:
        version: "0.8.2"
        # we just cache the venv-dir directly in action-setup-venv
        enable-cache: false

    - uses: getsentry/action-setup-venv@v3.0.0
      with:
        cache-dependency-path: uv.lock
        install-cmd: uv sync --frozen --active
```

pip:
```yaml
    - uses: getsentry/action-setup-venv@v3.0.0
      id: venv
      with:
        # starting from action-setup-venv@v3.0.0, if python-version isn't specified,
        # we default to using the version in .python-version file.
        python-version: 3.11.6
        cache-dependency-path: |
          requirements.txt
          requirements-frozen.txt
        install-cmd: pip install -r requirements.txt -c requirements-frozen.txt
```
