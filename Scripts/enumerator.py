import json
import pathlib
from datetime import datetime

import client

USERS = [("observer54-5", "rtuihfij34fi23poetgy3wed23sdc2125"), ("galgalgal", "6.62607015*10^−34J*Hz^−1"),
         ("defaultuser", "123456test"), ("observer33-4", "098712345")]


def scan(log, path, list_fn, data_fn, entity_type):
    html_template = """<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>{0}</title>
 </head>
 <body>
  {1}
 </body>
</html>"""
    path.mkdir(exist_ok=True)
    for f in list_fn():
        p = path / (f + ".html")
        data = data_fn(f, raw=True)
        data = html_template.format(f, data)
        old_data = None
        if p.is_file():
            with p.open(mode="r", encoding="UTF-8") as file:
                old_data = file.read()
        if old_data is None:
            log.write("New {0}: {1}\n".format(entity_type, p))
        elif old_data != data:
            log.write("{0} content changed: {1}\n".format(entity_type, p))

        with p.open(mode="w+", encoding="UTF-8") as file:
            file.write(data)


def main():
    with open("config.json") as f:
        config = json.load(f)
    path = pathlib.Path(config["enumerator_path"])
    path.mkdir(exist_ok=True)
    log = (path / "changelog.txt").open("a+", encoding="utf-8")
    log.write("[{0}]\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    c = client.ArrsClient(config["session_id"], config["token"])
    for u in USERS:
        user_path = path / u[0]
        user_path.mkdir(exist_ok=True)

        c.logout()
        if c.login(u[0], u[1]) != client.LoginResult.OK:
            raise Exception("Invalid account: ", u)

        scan(log, user_path / "files", c.dir, c.file, "File")
        scan(log, user_path / "notes", c.notes, c.note, "Note")
        scan(log, user_path, lambda: ["user"], lambda _, raw: c.user(raw), "User")  # I'm too lazy

    log.close()


if __name__ == '__main__':
    main()
