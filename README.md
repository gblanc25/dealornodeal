# DEAL OR NO DEAL
#### Video Demo:  https://youtu.be/bvfiUnlRoOY
#### Description:
  For my final project, I implemented a command-line version of the classic
  game, Deal or No Deal. Before beginning to code, I knew that I wanted an
  interactive interface with the following:

  -> A visual representation of the game stage
  -> Randomized case numbers and values that are stored using OOP
  -> Mid-game interruptions like a mathematically sound Banker
  -> Plenty of error checking to make sure the game runs consistently

  Below, I'll explain how I implemented each of those features!

  #1: Visual Representation

    For each stage in the game, I wanted users to know which cases they
    could choose from, so I created a print_cases function that makes
    use of the __str__ function in each Case class and prints all 22 cases
    out in two rows of 11. I designed that __str__ function to have three
    different states, represented by emojis: one that displays a case number
    if it can be chosen, one that is "locked" if the case is stored for later,
    and one that is crossed out if the case is already opened. This function
    was a good way to practice implementing loops and working with OOP!

  #2: More OOP

    To allow for easy access to prize values and numbers, and to keep the order
    of all cases consistent as I use them in print_cases and other areas, I
    decided to implement each case as an object that the program interacts with
    at each stage of the game. Each case stores a series of accessible values,
    and also maintains two states (iscase and opened) to determine functionality
    if the case has been stored or opened. As such, the class also includes two
    class functions (assign_case and open) that modify those states, print out
    a visual representation of opening, AND adjust outside data structures
    as needed to allow for other functionality (i.e. removing a prize from the
    prize list once its case has been opened - but not removing it if a case
    has been stored!).

  #3: Mid-Game Interruptions

    After every 6 rounds of opening cases, I implemented a Banker. I did some
    research, and it turns out that the Deal or No Deal Banker calculates offers
    using the root-mean-square formula, which is what I implemented in the
    banker_value function. I then asked for user input to determine whether
    to take the deal, with some added functions for the last banker round (when
    the user must choose between the last two available cases).

  #4: Error Checking and Testing

    Since my game requires user input, I implemented several error checks
    on user-provided values. For instance, when opening a case, I ensure that
    not only is the (stripped) integer they provide a valid case that has *not*
    been opened yet, but I reprompt them as well if they don't enter an integer.
    This helps eliminate mid-game exists due to exceptions. Similarly, with
    deciding Deal or No Deal, I limit reponses to a (lowered) "d" or "nd" for
    ease of typing and processing.

    In terms of testing, I did two things: one, I implemented test functions
    in test_project.py to ensure that my helper functions were returning
    appropriate values. Then, I also ran through the game several times over,
    trying different corner cases and making note of error changes along the way.
    This helped me eliminate issues like excess spacing, and it allowed me to
    catch exceptions that I didn't plan for initially. In the future, I'd like
    to work on a more efficient way of visually testing the game, instead of
    having to play through up to 22 cases per trial!

To play my game, simply run "python project.py" and prompts will begin appearing
in your terminal window. Thanks so much for viewing my project!