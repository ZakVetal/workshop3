from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

fullName = {
    "firstName": "Ihor",
    "lastName": "Riasyk"
}
fullMessage = {
    "subjectName": "Some subject",
    "description": "some message"
}

dictionary = dict.fromkeys(['message', 'user', 'all'], "dictionary_name") # dict.fromkeys - создание нового словаря с ключами и значениями

@app.route('/api/<action>', methods=['GET']) # сообщаем Flaskо, какой URL должен запускать нашу функцию
def renderingPages(action):

    if action == "message":
        return render_template("message.html", message=fullMessage) # render_template(name.html, values)
    elif action == "user":
        return render_template("user.html", user=fullName)
    elif action == "all":
        return render_template("allData.html", message=fullMessage, user=fullName)
    else:
        return render_template("error.html", action_value=action, available=dictionary)


@app.route('/api', methods=['POST'])
def transferInformation():
    if request.form["action"] == "message__updateValue":
        fullMessage["subjectName"] = request.form["subject--name"]
        fullMessage["description"] = request.form["description"]

        return redirect(url_for('renderingPages', action="all"))

    elif request.form["action"] == "user__updateValue":
        fullName["firstName"] = request.form["first--name"]
        fullName["lastName"] = request.form["last--name"]

        return redirect(url_for('renderingPages', action="all")) # redirect - функция перенаправления url
        # url_for(name function, аргумент что соответствует переменной части URL)

if __name__ == '__main__':
    app.run()
