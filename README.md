# mdformat-crystal

> Mdformat plugin to format crystal code blocks

## Description

mdformat-crystal is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format crystal code blocks embedded in Markdown with `crystal tool format`.
The plugin invokes crystal in a subprocess so having either crystal, Docker or Podman installed is a requirement.

## Installing

1. Install either [crystal](https://crystal-lang.org/), [Docker](https://docs.docker.com/get-docker/) or [Podman](https://podman.io/docs/installation)
1. Install mdformat-crystal
   ```bash
   pip install mdformat-crystal
   ```

## Usage

```bash
mdformat YOUR_MARKDOWN_FILE.md
```

## Limitations

The Docker/Podman fallback is only tested on Linux.
If you experience issues with it on Windows or macOS, please install crystal.
