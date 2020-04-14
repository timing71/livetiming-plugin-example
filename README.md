# Timing71 Service plugin example

This repo contains an example of a timing service plugin for the Timing71
system.

Note that it relies on the `livetiming-core` package which is not currently
available, but will be open-sourced towards the middle of 2020.

## Getting started

1. Clone this repo:

   ```bash
   git clone https://github.com/timing71/livetiming-plugin-example.git
   cd livetiming-plugin-example
   ```

2. Set up a Python virtual environment (optional, but recommended):

   ```bash
   python3 -m venv virtualenv
   source virtualenv/bin/activate
   pip install --upgrade pip setuptools
   ```

3. Set up this project and its dependencies:

   ```bash
   pip install -e .
   ```

4. Examine `src/livetiming/service/plugins/example/__init__.py`: this
   demonstrates the basic code required to write a plugin.

## Running the plugin

Plugins don't get run by themselves, but instead via the `livetiming-service`
runner, and are identified by package name, for example:

```bash
livetiming-service -v example
```

will run the plugin found at `livetiming.service.plugins.example.Service`.
_The plugin's main class **must** be called `Service`._

By default the plugin will try to connect to the Timing71 network (and fail,
since it won't be able to authenticate). You can instead run the plugin in
standalone mode, which will create a local websocket server through which the
plugin will publish data:

```bash
livetiming-service -v --standalone example
```

You can also run the plugin through the Timing71 desktop client by configuring
it to search for plugins in the `virtualenv/bin` directory you created above.

## Advanced usage notes

- You can (of course) install multiple plugins into one virtual environment.
- Note that the `livetiming/service/plugins` directories are all lacking the
  `__init__.py` file you might expect. This makes it possible to install
  plugins from different source packages.
