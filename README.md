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

### c. Preparations

  Study carefully three examples inside the test run.

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
