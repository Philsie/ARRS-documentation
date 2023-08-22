# This is a sample Python script.
import json
import time
import client

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

LOGINS = ["galx3", "observer54-5", "galgalgal"]
PASSWORDS = ["6.62607015*10^−34J*Hz^−1", "123456test", "662607015", "607015", "60701", "6070", "607", "60", "6", "66260701510341", "6626070151034",
             "662607015103", "66260701510", "6626070151", "662607015", "66260701", "6626070", "662607", "66260", "6626",
             "662", "66", "planck", "0.00000000000000000000000000000000066260702",
             "000000000000000000000000000000000066260702", "Planck", "MaxPlanck", "Planck's constant",
             "Planck constant", "plancksconstant", "PlanckConstant", "planckconstant", "6.62607015", "6.6260701",
             "6.6260702", "66260702", "6.626070", "6.626070", "6.62607", "6.6261", "6.6260", "6.626", "6.62", "6.63",
             "6.6", "7",
             "66260702", "66260702", "6626070", "6626070", "662607", "66261", "66260", "6626", "662", "663", "66", "7"]


def save_attempts(data):
    f = open("attempts.json", "w")
    json.dump(data, f)
    f.close()


def attempt(c, login, password):
    res = c.login(login, password)
    if res == client.LoginResult.ALREADY_LOGGED_IN:
        c.logout()
        time.sleep(2)
        return attempt(c, login, password)

    return res == client.LoginResult.OK


checked = 0
skipped = 0


def main():
    global checked
    global skipped
    with open("config.json") as f:
        config = json.load(f)

    with open(config["attempts_file"], "r") as f:
        attempts = json.load(f)

    c = client.ArrsClient(config["session_id"], config["token"])
    for login in LOGINS:
        for password in PASSWORDS:
            if login not in attempts:
                attempts[login] = {}
            if password not in attempts[login]:
                checked += 1
                res = attempt(c, login, password)
                attempts[login][password] = res
                save_attempts(attempts)
                print(login + ":" + password + " = " + str(res))
                if res:
                    return
                time.sleep(15)
            else:
                skipped += 1


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()
    print("checked: " + str(checked))
    print("skipped: " + str(skipped))
