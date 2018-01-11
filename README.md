# Password Kitchen

## Intro

This is a small project to hash passwords and verify hashed passwords.

## Design

The designer sent us the following plans:

### Hashing - User input

![Hashing - User input](design/design_hash_input.png)

### Hashing - Result hash

![Hashing - Result hash](design/design_hash_result.png)

### Verification - User input

![Verification - User input](design/design_verify_input.png)

### Verification - Match

![Verification - Match](design/design_verify_match.png)

### Verification - Doesn't match

![Verification - Doesn't match](design/design_verify_fail.png)


### Details

Use the following info to achieve the desired result:
- Colors:
  - Background:
    - Default: ![](http://via.placeholder.com/15/1976d2?text=%20) #1976d2
    - Verified: ![](http://via.placeholder.com/15/1976d2?text=%20) #1976d2
    - Failed verification: ![](http://via.placeholder.com/15/1976d2?text=%20) #1976d2
  - Text:
    - Page header: ![](http://via.placeholder.com/15/fff?text=%20) #fff
    - Card header: ![](http://via.placeholder.com/15/222?text=%20) #222
  - Inputs:
    - Background: ![](http://via.placeholder.com/15/fff?text=%20) #fff
    - Border color: ![](http://via.placeholder.com/15/01579b?text=%20) #01579b
    - Text color: ![](http://via.placeholder.com/15/222?text=%20) #222
    - Inactive textarea: ![](http://via.placeholder.com/15/eee?text=%20) #eee
  - Buttons:
    - Background: ![](http://via.placeholder.com/15/1976d2?text=%20) #1976d2
    - Border color: ![](http://via.placeholder.com/15/01579b?text=%20) #01579b
    - Text color: ![](http://via.placeholder.com/15/fff?text=%20) #fff
- Background:
  - It should cover the whole page
  - When the verification succeeds, the background should change to green.
  - When the verification fails, the background should change to red.
- Cards:
  - They are 400px wide and have 40px gap between them.
  - For the shadow, you can use this snippet: `box-shadow: 0 1px 5px rgba(0, 0, 0, .9)`
  - There is 40px space inside between the edge of the card and the start of the inputs and buttons

## Hashing

The following code snippet provides a short example of how the `bcrypt` library can help hash passwords and verify them:

```python
import bcrypt


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


if __name__ == '__main__':
    # Test these functions
    original_password = 'my_very_secureP4ssword!'  # From registration form
    print('original_password: ' + original_password)

    hashed_password = hash_password(original_password)  # This shall be saved in the DB
    print('hashed_password: ' + hashed_password)

    user_input_password = 'Hey Siri, what is my password?'  # From a login form, a mistyped input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))

    user_input_password = 'my_very_secureP4ssword!'  # From a login form, the correct input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))

```
