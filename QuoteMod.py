#The Super Mario Bros Super Show Quotes Twitter Bot
#or SMBSSQTB for short

from random import *

#Quotes come from https://www.mariowiki.com/List_of_The_Super_Mario_Bros._Super_Show!_quotes

#Mario's quotes
mario = ['"Hey paisanos! It\'s The Super Mario Bros. Super Show!" - Opening Credits',
         '"Do the Mario!" - Closing Credits',
         '"Don\'t worry, Princess! Luigi and me\'ll climb that mountain before you can say "Spaghetti and Meatballs"! -"The Bird! The Bird!"',
         '"Okay, wait here! And if you become lunch for a polar bear, don\'t blame us! -"The Bird! The Bird!"',
         '"I hate to run on an empty stomach!" - "The Bird! The Bird!"',
         '"Must be a beehive nearby, and when there\'s bees; there\'s raviolis smothered with honey" - "King Mario of Cramalot"',
         '"If Toad doesn\'t get us outta here soon, I\'m gonna eat this mattress!" - "Butch Mario & the Luigi Kid"',
         '"Wake up, Luigi! The only time plumbers sleep on the job, is when we\'re working by the hour!" - "Butch Mario & the Luigi Kid"',
         '"Catfish pizza? This may be a first, but I\'m not hungry!" - "Rolling Down the River"',
         '"Excuse my brother, he gets nervous around guys six times bigger than him." - "The Great Gladiator Gig"',
         '"We can fix anything if there\'s spaghetti involved!" - "The Great Gladiator Gig"',
         '"Hey, Koopa! I hope your Big and Tall shop blows up, with you in it!" - "Mario and the Beanstalk"',
         '"Those ain\'t wedding bells in your tower! They\'re bats in your belfry!" - "Love \'Em and Leave \'Em"',
         '"Hey! Where\'d you learn how to ride a bike!?" - "The Great BMX Race"',
         '"Get back here, Koopa! Don\'t you know vegetables are good for you?" - "The Great BMX Race"',
         '"Not on my melted mozarrella! - "Stars in Their Eyes"',
         '"If food isn\'t pasta, it doesn\'t count!" - "Jungle Fever"',
         '"Unstoppable? We\'re plumbers! If we can unstop a stop, we can stop the unstoppable!" - "The Fire of Hercufleas"',
         '"Magnifico! You\'re stronger than Grandma Mia\'s garlic chip cookies!" - "The Fire of Hercufleas"',
         '"Faster than a vanishing clog! More powerful than an electric drainsnake! It\'s Super Mario!" - "Pirates of Koopa"',
         '"If you can\'t beat \'em, join \'em! Then beat \'em!" - "Pirates of the Koopa"',
         '*singing* "Hush, little Princess, don\'t you cry. I\'m gonna buy you a pizza pie. And if that pizza pie gets ate, Luigi\'ll buy you a New York steak." - "Two Plumbers and a Baby"',
         '"This is the first time my lunch ever took a bite out of me!" - "The Adventures of Sherlock Mario"',
         '"I just love food that\'s spicy!" - "On Her Majesty\'s Sewer Service"',
         '"I always cry at wedding feasts!" - "Mario and Joliet"',
         '"Koopa\'s gonna take a trip he didn\'t plan on!" - "Too Hot to Handle"',
         '"I hope the food\'s better than the furniture!" - "Mighty McMario and the Pot of Gold"',
         '"As we say in Brooklyn; Banzai!" - "Mario Meets Koop-zilla"',
         '"Save the spaghetti! Save the spaghetti!" - "Mario and the Red Baron Koopa"',
         '"Koopone, you\'ve Kooped your last Koop!" - "The Unzappables"',
         '"It doesn\'t look good for the good guys, Luigi!" - "The Mark of Zero"',
         '"I guess Mexican food doesn\'t agree with El Koopitan!" - "The Mark of Zero"',
         '"When Luigi\'s unfrozen, he\'s goin\' on a diet!" - "The Koopas Are Coming! The Koopas Are Coming!"',
         '"It\'s ugly, but it floats!" - "The Trojan Koopa"',
         '"What? Only one pizza?" - "Quest for Pizza"',
         '"The Mushroom People get the mine, and Koopa gets the shaft!" - "The Great Gold Coin Rush"',
         '"When the plumbing gets tough, the tough get plumbing!" - "Plummers Academy"',
         '"Me Marzan! King of the jungle!" - "Mario of the Apes"',
         '"Can\'t we discuss this man to Mouser?" - "Princess, I Shrunk the Mario Brothers"',
         '"First, we\'d better get inside by a fire, before we turn into pastasicles!" - "Little Red Riding Princess"',
         '"The Provolone Ranger is ready to ride. High ho, Ostro, away!" - "The Provolone Ranger"',
         '"Help, help! There\'s a big, ugly spider in here! Help! My yelling\'s gonna keep you up all night, unless you get this spider outta here!" - "Escape from Koopatraz"',
         '"Luigi, are you a man or a Mouser?" - "Mario of the Deep"',
         '"I guess someday, even Super Mario can\'t think of everything!" - "Flatbush Koopa"',
         '"Don\'t count your reptiles before they\'re hatched, lizard lips!" - "Raiders of the Lost Mushroom"',
         '"I was hoping we\'d have lunch, not be lunch!" - "Crocodile Mario"',
         '"I just love playin\' Koopa in the middle!" - "Crocodile Mario"',
         '"I just had the strangest dream. I was a TV dinner!" - "Star Koopa"',
         '"He\'s showing a plumber how a garbage disposal works?" - "Star Koopa"',
         '"Watch it, gang! His toes are loaded!" - "Robo Koopa"']


luigi = ['Uwu',
         '"I can\'t I\'m allergic to mountains!" - "The Bird! The Bird!"',
         '"P-polar bear? Lunch!?" - "The Bird! The Bird!"',
         '"Hey, Super Mario! Super-cook their goose!" - "The Bird! The Bird!"',
         '(*sobs*) He was the nicest little fungus I ever knew!" - "The Bird! The Bird!"',
         '"Who could forget? Don\'t take chances or you\'ll go down the drain!" -"The Bird! The Bird!"',
         '"C-c-crama\'s here in-in Koopalot? Uh, I mean, uh, Koopa\'s here in Cramalot? I mean, uh, shee, let\'s split this place!" - "King Mario of Cramalot"',
         '"Me? B-b-but I can\'t swim across the moat! I\'m, uh, gonna have a baby!" - "King Mario of Cramalot"',
         '"Fellons? Yo, I never fell on nobody! I\'m uh..." - "Butch Mario & the Luigi Kid"',
         '"Oh no! End dend! I mean, dend dead! I mean shee, we\'re trapped!" - "Butch Mario & the Luigi Kid"',
         '"I\'ve had it! I\'ve had it, I\'ve had it! I\'m tired of Koopa chasing us from world to world! I wanna go home!" - "Brooklyn Bound"',
         '"Guess we\'re stayin\' in Mushroom Land." - "Brooklyn Bound"',
         '"Mama mia! We shoulda rented a camel with air conditioning!" - "Mario\'s Magic Carpet"',
         '"Look at that loot! Diamonds, gold, rubies! It must be worth over a hundred bucks!" - "Mario\'s Magic Carpet"',
         '"I told him that he wants really yummy carpet to head for Koopa." - Mario\'s Magic Carpet',
         '"So, what do we do now, Mr. Big Time Gambler?" - "Rolling Down the River"',
         '"Okay, Mario. One all ya got, coming up!" - "Rolling Down the River"',
         '"He\'s too busy eating, Mario! He\'s your kind of horse." - "The Great Gladiator Gig"',
         '"Hey! That\'s my brother Mario, you three-faced double-crosser!" - "The Great Gladiator Gig"',
         '"Leapin\' lasagna! This room\'s bigger than the Brooklyn Public Library!" - "Mario and the Beanstalk"',
         '"I th-think I liked it better when we outnumbered them!" - "The Great BMX Race"',
         '"I\'d feel better if we went back and got my stomach." - "The Great BMX Race"',
         '"That\'s what I call Shower Power!" - "Stars in Their Eyes"',
         '"Yo, my brother: the pasta vampire." - "Count Koopula"',
         '"Gee, that Mario. He can pulverize a pasta factory and still have room for dessert!" - "The Adventures of Sherlock Mario"',
         '"Gee. Mario gets the brainstorms, and I get the backaches!" - "Do You Princess Toadstool Take This Koopa...?"',
         '"You got \'em!" - "Koopenstein"',
         '"You don\'t got \'em." - "Koopenstein"',
         '"Let\'s really keep it a secret that we\'re agents, uhh, by stayin\' here"! - "On Her Majesty\'s Sewer Service"',
         '"Eh, it was nothin\'! Danger is our business!" - "On Her Majesty\'s Sewer Service"',
         '"Annette Funicello? Where?" - "Mario and Joliet"',
         '"Pluggin\' up pipes goes against everythin\' we stand for!" - "Too Hot to Handle"',
         '"Zelda of Legend! Next the from scenes! Some me show halfwit you!" - "Time Out Luigi"',
         '"The dungeon? I\'m allergic to dungeons!" - "Hooded Robin and His Mario Men"',
         '"Better make that "The more for Mario"!" - "Hooded Robin and His Mario Men"',
         '"We\'re stuck here like hairballs in a drainpipe!" - "Mario Meets Koop-zilla"',
         '"Hey! I may be crazy, but I\'m not dumb!" - "Mario and the Red Baron Koopa"',
         '"This place is emptier than a flushed drainpipe!" - "The Ten Koopmandments"',
         '"I want my mommy!" - "The Ten Koopmandments"',
         '"The Koopas are coming! The Koopas are coming!"',
         '"When our soldiers thaw out, we\'re gonna throw your tea in the harbor!" - "The Koopas Are Coming! The Koopas Are Coming!"',
         '"But I get seasick on a horse!" - "The Koopas Are Coming! The Koopas Are Coming!"',
         '"Aww, Toad. Did\'ya hafta say dead?" - "The Trojan Koopa"',
         '"How ooga bugga-mugga wa-ooga-ma!" - "Quest for Pizza"',
         '"Ouch! Someone\'s standin\' on my toe, and it\'s not me!" - "The Great Gold Coin Rush"',
         '"Mario\'s mind was where it always is: on pasta." - "Karate Koopa"',
         '"Relax, princess! He knows who he is! Mario\'s always gone ape for meatballs!" - "Mario of the Apes"',
         '"I\'m a chicken of the sea!" - "Mario of the Deep"',
         '"The only good thing so far is: we got to ride the roller coaster without a ticket!" - "Flatbush Koopa"',
         '"Stop him, Mario! Tell him Italian food is not on his diet!" - "Crocodile Mario"',
         '"I knew we should\'ve built this raft with brakes!" - "Crocodile Mario"',
         '"Bein\' garbage really makes a guy feel down in the dumps!" - "Star Koopa"',
         '"Koopa was scary enough when he was just a slimy reptile!" - "Robo Koopa"']


bowser = ['oWO',
          '"Koopa Pack, attack!" - Various episodes',
          '"He who koops and runs away lives to koop another day!" - Various episodes',
          '"Watch it soldier, when I want my feet licked, I\'ll ask for it! {quickly} I want my feet licked." - "The Bird! The Bird!"',
          '"Like my grandfather Poopa La Koopa always said: "Cheat, beat, and be merry!" - "Butch Mario & the Luigi Kid"',
          '"Don\'t know what I\'d do without my carpet phone!" - "Mario\'s Magic Carpet"',
          '"I\'ll get you for this, you pesky plumbers! A Koopa never forgets!" - "Mario\'s Magic Carpet"',
          '"Happy? Imposter! I never use the H word." - "Rolling Down the River"',
          '"Fool! Those pinhead plumbers are bound to try to rescue Princess Toadstool, and I intend to capture them before they do." - "Rolling Down the River"',
          '"Don\'t question my orders, you rotten rodent! Just do it!" - "Rolling Down the River"',
          '"Don\'t interrupt me, not while I\'m boasting and gloating!" - "Rolling Down the River"',
          '"Stop wisecracking, mushroom, or I\'ll turn you into soap!" - "Rolling Down the River"',
          '"One of the nice things about being evil is... you get to lie a lot. Ha ha." - "The Great Gladiator Gig"',
          '"Fum fee fi fo! I smell the brothers Mario!" - "Mario and the Beanstalk"',
          '"That goose is gonna smother you brothers!" - "Mario and the Beanstalk"',
          '"OK, that does it! You\'re all gonna be Koopatized!" - "The Great BMX Race"',
          '"There\'ll be other crooked races and other ways to cheat!" - "The Great BMX Race"',
          '"You\'re breaking my heart, princess! Now, get to work! Now that you and these Quirks are my slaves, I got other planets to plunder! *laughs*" - "Stars in Their Eyes"',
          '"You call that music? Stop that racket! I hate that music! I hate spaghetti! I hate Quirks! I hate those faucet freaks!" - "Stars in Their Eyes"',
          '"Alright! Which one of you messed up? Who ruined all my sneaky underhanded plans?" - "Jungle Fever"',
          '"Thank you, princess! You saved me all the trouble of hunting you down! You\'re so nice to me!" - "Jungle Fever"',
          '"The courage beyond compare, the bravery beyond description, I praise this great hero, the superior fiend... me. Koopa Khan the magnificent. If I didn\'t deserve this, I wouldn\'t give it to me." - "Brooklyn Bound"',
          '"Last one into the cave is a goodie-goodie!" - "Brooklyn Bound"',
          '"Goodbye, jerkos! And don\'t come back!" - "Brooklyn Bound"',
          '"Those annoying wrench-heads won’t ruin my evil plan! Prepare an ambush, Mouser! Make road pizzas out of them!" - "Toad Warriors"',
          '"These fireballs are fantastic! Think of the destruction; think of the wreckage; think of how much this\'ll lower my heating bill!" - "The Fire of Hercufleas"',
          '"Mouser! More marshmallows!" - "The Fire of Hercufleas"',
          '"Say ciao to your friends, Princess Toadstool. That\'s goodbye in Italian, because when you see \'em again, you\'ll be a tomato sauce sucking vampire, just like me! - "Count Koopula"',
          '"Fire a warning shot! ... On second thought, blow the plumber-boys and the Princess right off the boat!" - "Pirates of Koopa"',
          '"Listen up, you reptile retches! It\'s time to play \'Auction the Princess\'! Do I hear one-thousand gold coins? Remember, the money goes to my favorite charity... Me." - "Pirates of Koopa"',
          '"I\'m rich! I\'m filthy, stinkin\', mouth-watering rich!" - "Pirates of Koopa"',
          '"Ga ga goo goo! Now you terrible tots will do all my chores, while I play!" - "Two Plumbers and a Baby"',
          '"Stop, or I\'ll tell on you!" - "Two Plumbers and a Baby"',
          '"I\'ll be back to get you! When I grow up!" - "Two Plumbers and a Baby"',
          '"Rotten reptiles! It\'s that pasta-eatin\' plumber!" - "The Adventures of Sherlock Mario"',
          '"You don\'t scare me, you linguini-lickin\' losers!" - "The Adventures of Sherlock Mario"',
          '"I\'m gonna turn these two fat little plumbers into two flat little plumbers." - "Do You Princess Toadstool Take This Koopa...?"',
          '"Keep your crown on! You want people to think I\'m marrying a nag?" - "Do You Princess Toadstool Take This Koopa...?"',
          '"Boogie with Koopa, you fungus brats! Boogie right into my double-dealing clutches! Gwa-ha-ha-ha-ha-ha! (playing flute)" - "The Pied Koopa"',
          '"Mouser, this is not a nursery school! This is an evil castle!" - "The Pied Koopa"',
          '"No one is that stupid!" - "Koopenstein"',
          '"Oh, goody-goody! The Tunnel of Doom! My favorite!" - "On Her Majesty\'s Sewer Service"',
          '"When I get my mitts on you, you\'re gonna be creamed, Mushroom!" - "Too Hot to Handle"',
          '"I\'m always ready for sneaky badness!" - "Too Hot to Handle"',
          '"I love being rotten!" - "Too Hot to Handle"',
          '"Just because I said it doesn\'t mean I meant it!" - "Too Hot to Handle"',
          '"You mean I can\'t destroy the island? I hate those Marios! They always spoil my fun!" - "Too Hot to Handle"',
          '"You were hoodwinked by Hooded Robin! I\'m gonna pluck that bird nerd wing from wing!" - "Hooded Robin and His Mario Men"',
          '"Kiss Koopa\'s feet and I\'ll gladly get rid of the sea monster for ya!" - "20,000 Koopas Under the Sea"',
          '"Let\'s ram \'em, slam \'em, and ruin their day!" - "20,000 Koopas Under the Sea"',
          '"Pesky persnickety plumbers! I wish they\'d never been invented!" - "20,000 Koopas Under the Sea"',
          '"Mouser, if anything happens to the princess, I\'ll turn you into Swiss cheese!" - "Mighty McMario and the Pot of Gold"',
          '"Too late! His gorgeous self is here!" - "Mighty McMario and the Pot of Gold"',
          '"Run, you teensy tempura tasters! I\'m gonna squash this city flatter than a tofu pancake!" - "Mario Meets Koop-zilla"',
          '"Scram, pests, or I\'ll call an exterminator!!" - "Mario Meets Koop-zilla"',
          '"Stand still so I can squash ya, you little vermin!" - "Mario Meets Koop-zilla"',
          '"Ba humkoop!" - "Koopa Klaus"',
          '"Plug your ears and watch your rears! We\'re goin\' Bob-Omb bowlin\'" - "The Unzappables"',
          '"Let\'s stash this cash and dash!" - "The Unzappables"',
          '"Gosh, this tyrant business is hard work! I\'m too pooped to Koop! Think I\'ll take a Koopa catnap." - "The Ten Koopmandments"',
          '"Lousy lizards! This is enough to make a grown Koopa cry!" - "The Ten Koopmandments"',
          '"You call yourself an army, you miserable misfits? Why am I cursed with such incompetents?!" - "The Koopas Are Coming! The Koopas Are Coming!"',
          '"It\'s those dumber plumbers, the Mario Bros.!" - "The Trojan Koopa"',
          '"It\'s... it\'s... it\'s horrible! It\'s disgusting! It\'s me!" - "The Trojan Koopa"',
          '"And you\'re gonna spend the rest of your life digging for it! Hahahahaha!" - "The Great Gold Coin Rush"',
          '"More! I want more! More!" - "The Great Gold Coin Rush"',
          '"Make way for the big daddio, the headman, the new king of Sock Hop Land: Koopa, the Kool!" "Elvin Lives"',
          '"Come back here! We got a date for the prom!" "Elvin Lives"',
          '"No way, José! They\'ll never catch the Koopilac! I got dual carbs! I got four on the floor!" "Elvin Lives"',
          '"When you hurt Koopa\'s nose, you\'ve blown it!" - "Plummers Academy"',
          '"In just a few minutes, the bidding for Princess Toadstool and her slimy friend Toad will begin! So drink up your Koopa Kola!" - "Karate Koopa"',
          '"Welcome aboard Air Albatoss. This is your Koopa speaking. This flight is non-stop \'til ya drop!" - "Mario of the Apes"',
          '"We\'re gonna celebrate the capture of those faucet freaks by letting me win a baseball game." - "Princess, I Shrunk the Mario Brothers"',
          '"Now is plumber squashing time!" - "Princess, I Shrunk the Mario Brothers"',
          '"OW! I hate plumbers! OW! I hate... OW! Why can\'t they pick on... OW! Someone their own size?" - "Princess, I Shrunk the Mario Brothers"',
          '"It makes me feel so warm, to be so cold!" - "Little Red Riding Princess"',
          '"I want that ranger in danger! Now!" - "The Provolone Ranger"',
          '"Koopa Court is now in session! Bailiff Mouser, read those phony charges you and I cooked up!" - "Escape from Koopatraz"',
          '"Congratulations! You\'ve won a five-hundred year all-expense paid trip to Club Koopatraz!" - "Escape from Koopatraz"',
          '"It was so much fun being your crooked judge, I decided to become your cruel warden!" - "Escape from Koopatraz"',
          '"This better be a bad dream, plumber, \'cause if it\'s not, you\'re in deep fettuccine!" - "Escape from Koopatraz"',
          '"What the Koop are you talkin\' about?" "Mario of the Deep"',
          '"You mean this is all?! There ain\'t enough gold here to bother Kooping about!" - "Mario of the Deep"',
          '"You Mario Bros. ruined my evil schemes, so I\'m gonna ruin the burg that you love best!" - "Flatbush Koopa"',
          '"Hold your applause! I know it\'s a genius idea, but I have them all the time!" - "Flatbush Koopa"',
          '"Fan-kooping-tastic, it worked!" - "Raiders of the Lost Mushroom"',
          '"I love Down Under Land! It\'s where Mario Bros. went down- and under!" - "Crocodile Mario"',
          '"Go to Warp 10, Mouser!" "Star Koopa"',
          '"If you want something wrong done right, you gotta wrong-do it yourself!" - "Star Koopa"',\
          '"The fun\'s not over yet! I\'ve got Super-vision; Super-hearing; Super-strength; And yes, even... Super-toes!" - "Robo Koopa"',
          '"If it isn\'t... Robo-Rooter!" - "Robo Koopa"']

          
toad = ['"Hey! Let me go!" -"The Bird! The Bird!"',
        '"I\'m warning you, I get airsick. Heeeelp!" -"The Bird! The Bird!"',
        '"What\'re ya trying\' to do, ya wacko bird, drown me?" -"The Bird! The Bird!"',
        '"Mommy? You\'re not my mommy!" -"The Bird! The Bird!"',
        '"I can\'t be your little Cheepy, lady! I don\'t have wings! Look! No wings, no feathers. I\'m just a mushroom that can\'t stand heights!" -"The Bird! The Bird!"',
        '"Flyin\' lessons!? Are you outta your mind!?" -"The Bird! The Bird!"',
        '"The least that featherbrain could\'ve done was lend me a parachute. Hey! That\'s it! A parachute!" -"The Bird! The Bird!"',
        '"Hey! It\'s me! I mean, him! It\'s little Cheepy! The Birdo\'s real lost baby!" -"The Bird! The Bird!"',
        '"Oh no! I\'m not going back up there! Never!" -"The Bird! The Bird!"',
        '"When I get my hands on that King Koopa, I\'ll fix his wagon!" - "Butch Mario & the Luigi Kid"',
        '"I\'m no frog. I can\'t even swim." - "Butch Mario & the Luigi Kid"',
        '"Bombs awaaaaaaaaaaaayyy!!" - "Butch Mario & the Luigi Kid"',
        '"What did you tell him?" - "Mario\'s Magic Carpet"',
        '"Who did you expect? Pee-wee Herman?" - "Rolling Down the River"',
        '"Looks like you guys saved the day again! Almost." - "Rolling Down the River"',
        '"By the power of the shining star, I am the...Toad Warrior!" - "Toad Warriors"',
        '"Hey, man, I’m the Fantastic Fungus! The supercharged Mushroom of Might! I’m the Toad Warrior!" - "Toad Warriors"',
        '"Give me five. NO! Give me five bomb plants!" - "Toad Warriors"',
        '"Whoever slows down first, loses!" - "Toad Warriors"',
        '"Whoa! No more Toad Warrior!" - "Toad Warriors"',
        '"Y\'all made it!" - "Toad Warriors"',
        '"You blew that one, Koopa Stoopa!" - "Pirates of Koopa"',
        '"Some Mushroom Retainer I turned out to be... I was so close! I couldn\'t save her..." - "The Trojan Koopa"',
        '"Naughty turtle, you\'ve been hittin\' the sauce again, well, have some more!" - "Count Koopula"',
        '"Let\'s make like eggs and SCRAMBLE!!!" - "Mario of the Deep"',
        '"So much for hope." - "Stars in Their Eyes"',
        '"Don\'t do it, Princess! Don\'t marry Koopa! I\'d rather be a rock!" - "Do You Princess Toadstool Take This Koopa...?"',
        '"Koopa you stoopa! Watch it with the Bob-Ombs!" - "The Great Gold Coin Rush"',
        '"By order of his most royal repulsiveness, the reptile Sheriff of Koopingham! The castle road shall require a toll! In the amount of: One wagon full of gold coins!" - "Hooded Robin and His Mario Men"']

          
peach = ['"Oh no! Poor Toad! Bring him back you dimwitted Birdo!" - "The Bird! The Bird!"',
         '"Look! The Birdo took Toad to the highest peak! Please, Mario! Toad saved my life a hundred times! We\'ve got to save his!" - "The Bird! The Bird!"',
         '"(*Teary eyed*) Goodbye Mario, goodbye Luigi." - "Brooklyn Bound"',
         '"Mario! {Kisses him} Luigi! {Kisses him} You came back!" - "Brooklyn Bound"',
         '"(*sobs*) I always cry at weddings!" - "Mario and Joliet"',
         '"What was that about pancakes and maple syrup?" - "Quest for Pizza"']
quotes = mario + luigi + bowser + toad + peach

def GimmeQuote():
    random_quote = choice(quotes)
    return random_quote

print(GimmeQuote())
         
