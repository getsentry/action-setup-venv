action-setup-venv
==================

Sets up python and a virtual environment with caching.

### Usage

```yaml
    - uses: getsentry/action-setup-venv@v1.0.0
      id: venv
      with:
        python-version: 3.10.7
        cache-dependency-path: |
          requirements.txt
          requirements-frozen.txt
        install-cmd: pip install -r requirements.txt -c requirements-frozen.txt
```
