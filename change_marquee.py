from flask import Flask, request

app = Flask(__name__)

# function to evaluate character difference between two texts
def get_char_diff(text1, text2):
    char_diff = {}

    # Remove spaces and newlines from text1 and text2
    text1 = text1.replace(" ", "").replace("\n", "")
    text2 = text2.replace(" ", "").replace("\n", "")

    # text1 and text2 iterations, based on user input vars
    for char in text1:
        if char in char_diff:
            char_diff[char] -= 1
        else:
            char_diff[char] = -1

    for char in text2:
        if char in char_diff:
            char_diff[char] += 1
        else:
            char_diff[char] = 1

    # Remove characters that are extra in text1
    char_diff = {char: count for char, count in char_diff.items() if count != 0}

    # Return updated dictionary
    return char_diff

# function to print character difference
def print_char_diff(char_diff):
    sorted_char_diff = sorted(char_diff.items(), key=lambda x: x[0])

    added_diff = []
    removed_diff = []

    for char, count in sorted_char_diff:
        action = "removed" if count < 0 else "added"
        if action == "removed":
            removed_diff.append(f"{abs(count)} '{char}' needs to be {action}.")
        else:
            added_diff.append(f"{abs(count)} '{char}' needs to be {action}.")

    sorted_diff_output = sorted(added_diff) + sorted(removed_diff)

    return "<br>".join(sorted_diff_output)

@app.route('/', methods=['GET', 'POST'])
def execute_script():
    if request.method == 'POST':
        text1 = request.form['text1'].upper()
        text2 = request.form['text2'].upper()

        char_diff = get_char_diff(text1, text2)
        diff_output = print_char_diff(char_diff)

        return f'''
        <p>{diff_output}</p>
        <form method="post">
            <label for="text1">Enter the text currently on the marquee:</label><br>
            <textarea name="text1" rows="4" cols="50"></textarea><br>
            <label for="text2">Enter the new marquee text:</label><br>
            <textarea name="text2" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
            <input type="reset" value="Reset">
        </form>
        '''

    return '''
    <form method="post">
        <label for="text1">Enter the text currently on the marquee:</label><br>
        <textarea name="text1" rows="4" cols="50"></textarea><br>
        <label for="text2">Enter the new marquee text:</label><br>
        <textarea name="text2" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
