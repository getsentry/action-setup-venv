action-setup-venv
==================

Sets up python and a virtual environment with caching.

### Usage

```yaml
    - uses: getsentry/action-setup-venv@v1.0.0
      id: venv
      with:
        python-version: 3.10.7
    - run: pip install -r requirements.txt
      if: steps.venv.outputs.cache-hit != 'true'
```
