import bcrypt
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(
        plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/hash-password')
def return_hash_password():
    input_password = request.args.get('user-password-in')
    hashed_password = hash_password(input_password)
    print(hashed_password)
    return render_template('index.html', hashed_password=hashed_password)


@app.route('/verify-password')
def verify_password_result():
    input_password = request.args.get('user-password-out')
    hashed_password = request.args.get('hash-input')
    verification_result = verify_password(input_password, hashed_password)

    if verification_result:
        wrong_combination = False
    else:
        wrong_combination = True

    return render_template('index.html', verification_result=verification_result, wrong_combination=wrong_combination)


@app.route('/set-cookie')
def cookie_insertion():
    redirect_to_index = redirect('/')
    response = make_response(redirect_to_index)
    response.set_cookie('better cookie', value='eat it',
                        expires='Wed, 09 Jun 2021 10: 18: 14 GMT')
    return response


if __name__ == '__main__':

    app.run(debug=True,
            port=8000)


# if __name__ == '__main__':
#     # Test the above functions manually
#     original_password = 'my_very_secureP4ssword!'  # From registration form
#     print('original_password: ' + original_password)

#     # This shall be saved in the DB
#     hashed_password = hash_password(original_password)
#     print('hashed_password: ' + hashed_password)

#     # From a login form, a mistyped input
#     user_input_password = 'Hey Siri, what is my password?'
#     is_matching = verify_password(user_input_password, hashed_password)
#     print('is_matching: ' + str(is_matching))

#     # From a login form, the correct input
#     user_input_password = 'my_very_secureP4ssword!'
#     is_matching = verify_password(user_input_password, hashed_password)
#     print('is_matching: ' + str(is_matching))
