# action-setup-venv

Sets up Python with `actions/setup-python`, creates a virtual environment, and caches the whole venv directory.
On a cache hit, the action restores the venv and skips `install-cmd`.

## Usage

With uv:

```yaml
    - uses: astral-sh/setup-uv@884ad927a57e558e7a70b92f2bccf9198a4be546 # v6
      with:
        version: "0.8.2"
        # action-setup-venv caches the venv directory itself
        enable-cache: false

    - uses: getsentry/action-setup-venv@v3.2.0
      with:
        cache-dependency-path: uv.lock
        install-cmd: uv sync --frozen --active
```

With pip:

```yaml
    - uses: getsentry/action-setup-venv@v3.2.0
      id: venv
      with:
        python-version: 3.11.6
        cache-dependency-path: |
          requirements.txt
          requirements-frozen.txt
        install-cmd: pip install -r requirements.txt -c requirements-frozen.txt
```

To run your own install step instead of `install-cmd`, omit `install-cmd` and gate your step on the `cache-hit` output:

```yaml
    - run: pip install -r requirements.txt
      if: steps.venv.outputs.cache-hit != 'true'
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `python-version` | `''` | Python or PyPy version, passed to `actions/setup-python`. If empty, the action reads `.python-version` from `working-directory`. If set, it takes precedence over `.python-version`. |
| `cache-dependency-path` | `**/requirements*.txt` | Files hashed into the cache key. Accepts globs and multiple lines. Paths resolve from `github.workspace`, not from `working-directory`. |
| `venv-dir` | `.venv` | Venv directory, relative to `working-directory`. |
| `install-cmd` | none | Command that installs dependencies into the venv. The action runs it only on a cache miss. |
| `working-directory` | `${{ github.workspace }}` | Directory where the action creates the venv and runs `install-cmd`. |

## Outputs

| Output | Description |
| --- | --- |
| `cache-hit` | `'true'` when the action restored the venv from cache. |

## Environment

After the action runs, later steps in the job have the venv activated:

- `VIRTUAL_ENV` points to the venv.
- The venv `bin` directory (`Scripts` on Windows) is on `PATH`.

## Cache key

The cache key includes the runner OS, the Python version and path, the hash of `cache-dependency-path`, and the literal `install-cmd`.
A change to any of these creates a new venv.

## Help

Open an issue at [getsentry/action-setup-venv](https://github.com/getsentry/action-setup-venv/issues).
