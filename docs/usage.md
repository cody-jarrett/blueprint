# Usage

Now you can program your application inside the blueprint directory. The following command will start your application:

```bash
python <app_name>
```

The above command will run the `run` function, within the `__main__.py` script, from the `main.py` module in the `modules` folder. You can import your custom functions and hook it to the `run` function to run them.

**To change the main module name**, you can rename the `blueprint` directory. But make sure you also rename the `name` in the `pyproject.toml` file.

**You can add project configuration** directly to the config toml file's `[app]` section. You can read it in anywhere in your project by calling the following lines:

```python
import toml
CONFIG = toml.load("config.toml")["app"]

app_name = CONFIG.get('APP_NAME')
```

You can also add app secrets directly to an `.env` file in the root project directory and read it anywhere from your project with the help of Python's built in `os` module.

```python
import os
secret = os.environ.get('APP_SECRET')
```
