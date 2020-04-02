# Declare characters used by this game.
define jack = Character(_("Jack"), color="#c8ffc8")
define me = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False


# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg lecturehall
    with fade

    "My name is Melissa. I just graduated from SFSU with a degree in humanities."
    "As you might expect from someone with the prestiguous, coveted, Bachelor's degree in Humanities, I work at..."
    "A cafe."


    scene bg uni
    with fade

    "I wish I could say that I was following my passions when I chose my major. That I knew my options after graduation were going to be limited, but loved humanities so much that I didn't care."
    "But the truth is, I barely knew what humanities even was when I first decided on it."
    "I only chose it so that I could have more classes with him."


    show jack green normal
    with dissolve

    jack "It was just innocent fun! It's not like I was really doing anything with her!"
    jack "It was just texting!"


    menu:        

        "It still xcounts!":
            pass

        "Whatever. Fuck you.":
            pass



label stillcounts:

    show jack green smile

    jack "You were always so cute the way you thought sexting was the same as sex."

    me "You were always an asshole the way you thought it wasn't. Stop smiling and die."  
   
label fuckyou:

    show jack green sad

    scene bg meadow
    with fade

    "And now it's the end good bye."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show jack green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show jack green surprised

    "Silence."

    "She looks so shocked that I begin to fear the worst. But then..."

    show jack green smile

    menu:

        s "Sure, but what's a \"visual novel?\""

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:

    m "It's a kind of videogame you can play on your computer or a console."

    m "Visual novels tell a story with pictures and music."

    m "Sometimes, you also get to make choices that affect the outcome of the story."

    s "So it's like those choose-your-adventure books?"

    m "Exactly! I've got lots of different ideas that I think would work."

    m "And I thought maybe you could help me...since I know how you like to draw."

    m "It'd be hard for me to make a visual novel alone."

    show jack green normal

    s "Well, sure! I can try. I just hope I don't disappoint you."

    m "You know you could never disappoint me, jack."

    jump marry


label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    show jack green surprised

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show jack green smile

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of jack's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    "And one day..."

    show jack blue normal
    with dissolve

    s "Hey..."

    m "Yes?"

    show jack blue giggle

    s "Will you marry me?"

    m "What? Where did this come from?"

    show jack blue surprised

    s "Come on, how long have we been dating?"

    m "A while..."

    show jack blue smile

    s "These last few years we've been making visual novels together, spending time together, helping each other..."

    s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

    m "jack..."

    show jack blue giggle

    s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

    show jack blue normal

    s "So will you marry me?"

    m "Of course I will! I've actually been meaning to propose, honest!"

    s "I know, I know."

    m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

    show jack blue giggle

    s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

    scene black
    with dissolve

    "We get married shortly after that."

    "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

    "Together, we live happily ever after even now."

    "{b}Good Ending{/b}."

    return

label later:

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    "{b}Bad Ending{/b}."

    return
