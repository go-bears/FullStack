import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def bartender_asks():
    customer_answers ={}
    for ask in questions:
        #print questions.get(ask)
        answer=raw_input(questions[ask])
        if answer == 'yes' or answer == "y":
            customer_answers[ask] = True
        else:
            customer_answers[ask] = False


        #customer_answers[ask]=answer
    return customer_answers


def pirate_drinks(customer_answers):
    drink_mix = []
    for answer, recipes in ingredients.items():
        customer_prefers = customer_answers[answer]
        if customer_prefers == True:
            drink_mix.append(random.choice(recipes))

        else:
            print "I still make you a drink!"


    #print drink_mix
    print "how about a drink with: {}".format(drink_mix)

def main():
    """ Main function """
    customer_answers = bartender_asks() 
    pirate_drinks(customer_answers)

if __name__ == '__main__':
    main()