from __future__ import annotations

import time
from enum import Enum

import requests

URL = "https://arrs.host/ajax.php"


class LoginResult(Enum):
    OK = 1
    INVALID_PASSWORD = 2
    ALREADY_LOGGED_IN = 3


class ArrsClient:
    def __init__(self, session, token):
        self.cookies = {'PHPSESSID': session}
        self.token = token

    def cmd(self, cmd, attempts=10) -> str | None:
        d = {'token': self.token, 'q': cmd, 'act': 'command'}
        while attempts > 0:
            res = requests.post(url=URL, cookies=self.cookies, data=d)
            if res.status_code == 200:
                return res.json()["message"]

            time.sleep(2)
            attempts -= 1
        return None

    # TODO: use html parser for !raw output
    def cmd_output(self, cmd, raw=False):
        separator = "<br />"
        error_header = "<span class='error'>[ERROR]</span> "
        data = self.cmd(cmd)
        e = data.find(error_header)
        if e != -1:
            raise Exception(data[e + len(error_header):])

        s = data.find(separator)
        if s == -1:
            raise Exception("Invalid output: ", data)

        data = data[s + len(separator):]
        if not raw:
            data = data.replace("<br />", "\n")
        return data

    def login(self, login, password):
        blocked = "Temporarily blocked"
        invalid = "Invalid password"
        waiting = "waiting for password"
        denied = "Access denied"

        while True:
            t = self.cmd("login " + login)
            if waiting in t:
                break
            if denied in t:
                return LoginResult.ALREADY_LOGGED_IN
            time.sleep(2)
        res = self.cmd(password)
        if blocked in res:
            time.sleep(10)
            return self.login(login, password)
        if invalid in res:
            return LoginResult.INVALID_PASSWORD

        return LoginResult.OK

    def logout(self):
        self.cmd("logout")

    def dir(self):
        data = self.cmd("dir")
        files = data.split("<br />")[1:-1]
        return files

    def notes(self):
        data = self.cmd("notes")
        files = data.split("<br />")[1:-1]
        return files

    def file(self, name, raw=False):
        return self.cmd_output("file " + name, raw)

    def note(self, name, raw=False):
        return self.cmd_output("note " + name, raw)

    def user(self, raw=False):
        return self.cmd_output("user", raw)
