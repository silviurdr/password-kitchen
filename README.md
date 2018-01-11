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
    - Verified: ![](http://via.placeholder.com/15/43a047?text=%20) #43a047
    - Failed verification: ![](http://via.placeholder.com/15/e53935?text=%20) #e53935
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
- Font:
  - The light *(300)* version of **Montserrat** font family is used in the whole application
  - It can be linked from Google's font repository
- Background:
  - It should cover the whole page
  - When the verification succeeds, the background should change to green.
  - When the verification fails, the background should change to red.
- Cards:
  - They are 400px wide and have 40px gap between them.
  - For the shadow, you can use this snippet: `box-shadow: 0 1px 5px rgba(0, 0, 0, .9)`
  - There is 40px space inside between the edge of the card and the start of the inputs and buttons
  - They have 4px border radius
- Inputs:
  - Every input has 4px border radius
  - The hash result textarea has an inactive property
