from flask import Flask, render_template

app = Flask(__name__)

# Reduce a number to single digit
def num_to_digit(value):
    temp = 0
    while value > 0:
        temp += value % 10
        value //= 10
    if temp > 9:
        return num_to_digit(temp)
    return temp


# Numerology logic
def numerology(name):
    total = 0
    for ch in name:
        if ch in ['a', 'r', 's']:
            total += 1
        elif ch in ['b', 'q', 't']:
            total += 2
        elif ch in ['c', 'p', 'u']:
            total += 3
        elif ch in ['d', 'o', 'v']:
            total += 4
        elif ch in ['e', 'n', 'w']:
            total += 5
        elif ch in ['f', 'm', 'x']:
            total += 6
        elif ch in ['g', 'l', 'y']:
            total += 7
        elif ch in ['h', 'k', 'z']:
            total += 8
        elif ch in ['i', 'j']:
            total += 9
        else:
            return "Invalid characters detected!"

    digit = num_to_digit(total)

    messages = {
        1: "You are a sad person",
        2: "You are an angry person",
        3: "An introvert",
        4: "You have a jolly nature",
        5: "You like to party",
        6: "Your revenge is bitter",
        7: "A nerd",
        8: "Too much attitude",
        9: "You are a shy person"
    }

    return messages.get(digit, "I know who you are. THE ROBOT :P")


@app.route('/')
def home():
    return render_template(
        'index.html',
        message="Hello dear, let's have some fun!",
        imgname="hello"
    )


@app.route('/<username>')
def user_profile(username):
    username = username.lower()
    result = numerology(username)
    return render_template(
        'index.html',
        message=f"{username}: {result}",
        imgname="jenkins"
    )


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
