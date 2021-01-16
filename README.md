# mcc-tools
Tools for Python Coding Challenge of Math, Chess, and Coding Club (MCC)

## A. Prerequisite

### a. For macOS/Linux users

Copy the commands in the sections below and paste that in a macOS Terminal or Linux shell prompt.

1. Install [Homebrew](https://brew.sh):

  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Install Python 3

  `brew install python3`

3. Create your virtual environment

  `python3 -m venv ~/38`


4. Enable your virual environment

  `source ~/38/bin/activate`

5. Install `pip` tools:

  `~/387/bin/pip install --upgrade pip setuptools`

6. Install `mcc-tools`:

  `~/387/bin/pip install --upgrade mcc-tools`

7. Create a working directory for the contest

  `cd`

  `mkdir pcc`

8. Download your credential file named `mcc.conf` from the shared folder the club assigned to you and move it into `pcc` directory just created.

### b. For Windows users

1. Make sure that you have Adminstrator privilege on your computer. Ask somebody who can give you if you don't have it. Do not continue until you are sure that you have. Download and install Python 3.8 for Windows. Follow the instructions for Windows on this [page](https://installpython3.com). Close PowerShell if you have open it.

2. Open `Command Prompt` in Windows. Click `Start` button and type to search for `Command Prompt`. Alternatively, you can also access the command prompt by pressing `Ctrl + r` on your keyboard, type `cmd` and then click OK. Type the following to make sure that you have Python version 3.8+:

  `C:\Users\<YOUR_NAME>\python --version`

  *Note: `<YOUR_NAME>` should be the string containing your login.*

3. Create your virtual environment

  `python -m venv C:\Users\<YOUR_NAME>\38`

4. Enable your virtual environment

  `C:\Users\<YOUR_NAME>\38\Scripts\activate.bat`

5. Install `pip` tools:

  `C:\Users\<YOUR_NAME>\38\Scripts\pip install --upgrade pip setuptools`

6. Install `mcc-tools`:

  `C:\Users\<YOUR_NAME>\38\Scripts\pip install --upgrade mcc-tools`

7. Create a working directory for the contest

  `cd`

  `mkdir pcc`

8. Download your credential file `mcc.conf` and move it into the `pcc` directory just created.

## B. Test Run

### a. Test if the evaluation server Astria is ready

  Open a tab on your favourite browser by clicking on this link to [Astria](http://206.47.13.10:8080).

### b. Test if your Pegasus is ready to communicate with Astria

In the Command Prompt or Terminal, run three tests with Pegasus:

  `python test_run.py`

The word `OK` should appear three times on the Terminal/Command Prompt.
In addition, on the browser your name and login time should be displayed.

Congratulations! You are now ready for Python Coding Challenges.

### c. Test run problems
#### 1. Problem One: Find the next prime
##### The problem: *Given an positive integer, find the next prime that is equal or larger than the given number.*

The function `my_next_prime` receives a positive integer and try to check if that is a prime.

    # Verify if any odd number equal to or larger than the given number is a prime
    #
    def my_next_prime(number):
        number = int(number)
        next_prime = number if number % 2 == 1 else number + 1
        found_prime = False
        while not found_prime:
            found_prime = is_prime(next_prime)
            if found_prime:
                return next_prime
            next_prime += 2
        return next_prime

This implementation uses a helper function to determine if a number is a prime:

    # Determine if a number is a prime by looking at the remainder
    # when divided the number by all integers
    # between 2 and the number's square root
    #
    def is_prime(number):
        for i in range(2, ceil(sqrt(number)+1)):
            if number % i == 0:
                return False
        return True

An example is given for how to submit for this problem:

    # Test 3 times if my_next_prime function is correct
    #
    result = p.submit('next_prime', my_next_prime, 3)
    print('next_prime:', result

You should see this result when testing it against Astria:

    next_prime: [['OK', '8', 11], ['OK', '3', 3], ['OK', '3', 3]]    

#### 2. Problem Two: Find the fake coins
##### The problem: *There are eight identical-looking coins. One of them is a counterfeit (a fake coin) and lighter than the others. What is the minimum number of weighings needed to identify the fake coin with a two-pan balance scale and without weights? You are given a string of seven 1's and one 0. You have to simulate a weighing process to find the position of the fake coin.*

If you see the list of coins as '10111111', you *know* that the second coin, or the character with index 1 in the '10111111' string, is a '0'. But of course you have to implement a function to determine this fake coin via weighing, not by looking into the string.

An implementation of `my_fake_coin` function is given:

    #
    # Find the position of the fake coin in two weighings
    #
    def my_fake_coin(coins):
        my_coins = [int(c) for c in coins]  # Convert to integers
        group_a, group_b, group_c = my_coins[0:3], my_coins[3:6], my_coins[6:]
        weight_a, weight_b = sum(group_a), sum(group_b)

        if weight_a < weight_b:  # First weighing, fake coin is in group A
            if group_a[0] < group_a[1]:
                return 0
            elif group_a[0] > group_a[1]:
                return 1
            else:  # group_a[0] == group_a[1]
                return 2
        elif weight_a > weight_b:  # fake coin is in group B
            if group_b[0] < group_b[1]:
                return 3
            elif group_b[0] > group_b[1]:
                return 4
            else:  # group_a[0] == group_a[1]
                return 5
        else:  # weight_a == weight_b, fake coin is in group C
            if group_c[0] < group_c[1]:
                return 6
            else:  # group_c[0] < group_c[1]
                return 7

Similar to the first problem, the implementation for `my_fake_coin` can be tested bu using the following code.

    ########################################
    # Test 3 times if my_fake_coin function is correct
    #
    result = p.submit('fake_coin', my_fake_coin, 3)
    print('fake_coin', result)

You should see this result when testing it against Astria:

    fake_coin [['OK', '11011111', 2], ['OK', '11101111', 3], ['OK', '11101111', 3]]

#### 3. Problem Three: Find the sequence of moves
##### The problem: *A knight stand on a square in the 3x3 chessboard. The squares on the board are number 1 to 9 from the top to the bottom row and from left to right. The number of the square where the knight stands is the position of the knight. Given the position, find the sequence of numbers that representing the squares the knight visit, each once, before return to the original squares.*

So this is how the board looks like:

    1 2 3
    4 5 6
    7 8 9

So from 1, you can move to 6 or 8. From 6 you can move to 7, but not back to 1, and so on. Below is the correct implementation.

    #
    # Demonstrate the move sequence of a knight
    #
    def my_move_sequence(position):
        valid_moves = {
            1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9],
            6: [1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }

        current_position = int(position)
        move_sequence = [current_position]  # starts from the given position

        while len(move_sequence) < 8:  # until all 8 moves are made
            next_postion_1, next_postion_2 = valid_moves[current_position]
            if next_postion_1 not in move_sequence:
                current_position = next_postion_1
                move_sequence.append(next_postion_1)
            elif next_postion_2 not in move_sequence:
                current_position = next_postion_2
                move_sequence.append(next_postion_2)
            else:
                break
        return ''.join(['%s' % i for i in move_sequence])

You should see this result when testing it against Astria:

    move_sequence [['OK', '9', '92761834'], ['OK', '8', '81672943'], ['OK', '4', '43816729']]

*Note: The problem asks to simulate move sequences, not to show done sequences. For example to simulate a move of a knight from square 1, you have two choices: square 6, or square 8. The way your code is written is to make the knight move on a preset sequence. You have to write a code that PLAYS the moves based on the chess rules.*

## Recording of results and submissions
`Astria` records all your submissions. Every single one. She also keeps the final submission of each problem, so don't be worried if you lost the right answer in your testing. This also means she can see your guesses and brute force answers, so solve wisely.

## Evaluation of submissions
*If all final submissions are correct AND your submitted codes work accordingly, you are now admitted into the contest.*
***Congratulations!***

## C. Rules

  - Students who pass the qualification will be invited to attend the orientation o how to use `Pegasus` - the communication API to receive inputs and submit outputs to `Astria` - the evaluation server.
  - At the beginning of the semester or after each PCC contest, a new problem set of ***three (3) problems*** are ***published on the club website***. Each problem consists of a description and some example inputs. The students can start working immediately on creating Python programs to solve the given problems. They have `no access to Astria until the contest’s time` and have to validate their program themselves.
  - Each contest starts at 12:00 PM Eastern Time (12:00 PM Ottawa, 9:00 AM Vancouver, 12:00 PM in Toronto, 1:00 PM Moncton, 5:00 PM UK, 6:00 France) and lasts for 90 minutes. The test supervisor(s) - Contest Organizer (CO) - decides how much additional time is allowed for students to scan and upload their work.
  - When the `contest starts`, the students will `have access to Astria`. They now can run their programs and will see Astria evaluation. They can `modify the incorrectly working programs and rerun against Astria until all correctly done`.
  - The test is carried out via Zoom under supervision of the above mentioned CO. The CO will be responsible to deliver the solutions to the personal shared folders assigned by the club to the students when the test starts. Students submit the source codes to the folder.
  - All students must follow rules when using Zoom: raise your hand when you want to talk; mute your microphone all the time except when talking; use chat if your audio not working. Paper-based books, notes, and calculators are allowed. Using computer, tablet, or mobile phone to search for any Internet source is not allowed. Help from anyone outside the team is not allowed. Violation by using external help simply results in failure of the test.
  - Grading:
    - `Correct program`: the program that provides all correct outputs for the list of given inputs will receive **maximum 7 points**.
    - Submission that is `not executable` will result in **deduction of 5 points**.
    - Total number points can be earned is 21 points.
