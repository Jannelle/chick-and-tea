# Declare characters used by this game.
define jack = Character(_("Jack"), color="#c8ffc8")
define me = Character(_("Me"), color="#c8c8ff")
define vikki = Character(_("Vikki"))
define may = Character(_("May"))


# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False


# The game starts here.
label start:

    $ may_points = 0

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

        "It still counts!":
            jump stillcounts

        "Whatever.":
            jump whatever



label stillcounts:

    jack "How is this any different from watching porn?"
    jack "What about those stupid fan fictions you read? You read those sex scenes and I read texts! It's the same!"
    jump itsover

   
label whatever:

    jack "Come on, don't be like this."

label itsover:

    "We went back and forth like that for hours. It was clear the conversation wasn't going anywhere until I finally gave it a destination."

    me "It's over."

# Flash to present time


label day1:

    "And now I'm here at the cafe."

    vikki "Welcome to Chick and Tea! How may I help you?"

    "That's Vikki, the cashier. She's okay."

    vikki "Thank you! Come again!"

    me "That was great. Just keep doing that!"

    vikki "Okay, okay. I just get so nervous when I have to calculate change!"

    me "You'll get used to it."

    me "Well, if you need me, I'll be in the back."

    "Vikki just started last week. She's getting the hang of things, but she still is obviously uncomfortable with her new job."

    "I start rummaging through the inventory, making sure we were prepared for tomorrow."

    ## Vikki pops her head through the door
    vikki "Hey, do you have any plans after we finish closing?"

    me "Um, not really, why?"

    vikki "Well...I know this is kind of weird, but do you think we could talk for a bit afterward?"

    menu:

        "Sure. About what?":
            jump sure_about_what

        "Sorry, I'm pretty tired tonight. Maybe another day.":
            vikki "Please?"
            # vikki looks cute and sad
            me "Well, okay. What do you want to talk about?"

label sure_about_what:
    
    vikki "I need some help memorizing the menu."

    me "Oh okay, yeah. Sure thing."

    "The rest of the shift went by pretty uneventfully. We started closing up."

    # bell noise or someting

    "{color=#f00}Hello? Is anyone here?{/color}"

    "I rush to the the counter and see one of our regulars. I don't really know her personally, but I've taken her order enough times to know her name is May."

    # show a hot girl

    me "Sorry ma'am, we're closing."

    may "Please, I had a tough day at work and I really need my fix."

    "I look around. We've already put a way the boba, but I could fix up her a simple milk tea...but I know Vikki really wanted to talk."


    menu:
        "Make the drink happily":
            me "Alright, ma'am, but just because we want to keep you around."
            "I open the boba and start cooking it again or whatever you do with boba idk."
            "This takes mroe time and Vikki is sad I guess"
            $ may_points += 1
        "Make the drink without boba":
            me "Alright, sure."
        "Don't make drink":
            me "No please die"

    if may_points == 1:
        may "Happy response"
    else: 
        may "Neutral response." 

    "Later that night"

    vikki "Thanks for talking to me."

    me "No problem, but I'm honestly kind of surprised. Like I've said, you've been doing find."

    vikki "I know, but a lot of times customers come in asking for recommendations, and I always feel so stupid not being able to answer them."

    me "Well, you know our most popular items, right?"

    vikki "Yeah, but then people start asking me for details, like 'Oh does this have avocado? Is there peanut oil? Is this gluten-free?'"

    me "First of all, we sell chicken and boba. Everything is gluten free."

    vikki "See! It's stuff like that that seems so obvious, but it's like my mind goes blank."

    me "Honestly, it's your first week here. It's normal to stumble sometimes and that's why I'm still supervising you."

    # vikki blushes
    vikki "Yeah, but I hate looking stupid in front of you."

    me "You don't look stupid. You just look new."

    vikki "That's nice of you to say, but to be honest, sometimes I'm not sure why you hired me."

    "The truth is that Vikki's available hours were the best, but I'm not sure if I should say that..."

    # choices 
        # be honest
        # lie

    menu:
        "Be honest.":
            jump be_honest

        "Lie":
            jump lie


label be_honest:

    me "Well, to be honest, you had the best available hours out of the candidates. But that doesn't mean you weren't qualified!"

label lie:
    
    $ vikki_points = 0

    me "You were the best!"
    
    $ lied = True
    
    $ vikki_points += 1
    
    vikki "Anyway, do you have time to maybe quiz me?"

    # choices
        # yes
        # no
menu:
    
    "Yes":
        jump yes

    "No":
        jump no

label yes:
    
    me "Is boba gluten-free?"
    vikki "We only sell chicken and boba."
    jump to_here

label no:
    
    me "Sorry, maybe text time. I need to go have sex with my wife now"
    vikki "What."

label to_here:

    return
