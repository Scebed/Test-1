import time

#Ця функція вспоповільнює виведдення тексту
def print_with_pause(text):
    print(text)
    time.sleep(1)

#Початок чудесної гри
print_with_pause("\nВітаємо вас у грі під назвою Едем!")
print_with_pause("Ця гра основана лишень на особистій хворій фантазії автора, в якій ви будете в ролі вчителя школи з особливими учнями.")
print_with_pause("Учні були дітьми, яких залишали батьки під воротами школи. Але більш детальніше можна буде дізнатись лишень в сюжеті гри.")
print_with_pause("Тому бажаю вам удачі та приготуйтесь до чудових пригод.\n")
print_with_pause("Ви вчитель якому запропонували роботу в красивій школі")
choice = input("1. Піти до школи.\n2. Обдивитись зовнішній дизайн школи\n")

if choice == "1":
    print_with_pause("Ви ввійшли до школи де вас зустрів маленький хлопчик який провів вас до директора")
    choice = input("1. Ви пожали руку директору.\n2. Ви зразу запитали за заробітню плату\n")
    if choice == "1":
        print_with_pause("Вам взаємно пожали руку і вас провели до класу")
        print_with_pause("У класі була повна тишина в якій можна поїхати дахом")
        print_with_pause("Діти сиділи всі слухняно і ви почали перекличку")
        print_with_pause("Відмічавши учнів ви не знайшли одного учня в класі та запитали де він, але учні перелякано мовчали")
        print_with_pause("Ви залишили клас та пішли на пошуки учня")
        choice = input("1. Ви пішли на вулицю\n2. Ви вирішили піти по коридору\n")
        if choice == '1':
            print_with_pause("Ви вийшли на задній дворик де стояла маленька дівчинка")
            print_with_pause("Ви запитали її ім'я і чому вона не на уроці")
            print_with_pause("Мене звати Єва і я не хочу там бути")
            print_with_pause("Після чого вона вбиває вас ножем")
            print_with_pause("Кінець гри")
        else:
            print_with_pause("Ви вирішили піти по коридору та заглядали в різні класи і всі вони були пусті")
            print_with_pause("Після пошуків ви повенулись в клас де всі діти як сиділи так і сидять на своїх місцях")
            print_with_pause("Ви хочете познайомитись з класом ліпше і придумали інтересну гру")
            print_with_pause("Ви задали перше питання але учні все-одно мовчали")
            print_with_pause("Раптом ви замітили, що один учень поводить себе не як всі інші")
            print_with_pause("Ви запитаєте його що тут відбувається і хочете щоб він вам все обяснив")
            print_with_pause("Після чого хлопчик подивився на вас переляканими очима і втік з уроку")
            choice = input("1. Ви побігли за хлопчиком\n2. Ви подзвонили директору, що учень втік з уроку\n")
            if choice == '1':
                print_with_pause("Ви побігли за хлопчимок і знайшли його в куточку одного з пустих класів")
                print_with_pause("Ви підійшли та запитали чого він втік і дали йому цукерку")
                print_with_pause("Він переляканими очима подивився на вас і сказав щоб ви тікали з цієї школи")
                print_with_pause("Ви не розуміючи що він говорить таке, почали заспокоювати його")
                print_with_pause("Хлопчик подивився вам за спину, закричав і ви обернулися та нічого не побачили")
                print_with_pause("Обертаючись з заспокіливими словами до хлопчина, не находите його на місці")
                print_with_pause("Ви вирішили це сказати директору, але його не було на місці")
                print_with_pause("Після цього ви з маленьким переляком повертаєтесь до класу де всі як сиділи так і сидять")
                print_with_pause("Ви починаєте кричати на дітей з питаннями що тут відбувається")
                print_with_pause("Але діти як сиділи онімівши так і сидять")
                print_with_pause("Після чого ви чуєте дитячий крик з коридору")
                print_with_pause("Ви вибігаєте з класу")
                choice = input("1. Ви побігли на право\n2.Ви побігли на ліво\n")
                if choice == '1':
                    print_with_pause("Ви чуєте крик ліпше та підходите до підвалу")
                    print_with_pause("Спускаєтесь у підвал та знаходите побитого хлопчика")
                    print_with_pause("Підходите ближче і розумієте що це хлопчик за яким ви бігли")
                    print_with_pause("Ви питаєтесь що тут сталось і як він пропав")
                    print_with_pause("Він розказав що тут є 2 злі духи, які можуть вбити якщо їм щось не подобається, звати їх Адам і Єва")
                    print_with_pause("Розказує що всі тут вже померли всередині, а оболочка їхня те й робить що просто онімівши сидить")
                    print_with_pause("Тут він вирішив забрати його з собою та втекти з цієї проклятої школи")
                    choice = input("1. Вилізти через маленьке вікно\n2. Вийти через чорний вихід\n")
                    if choice == '1':
                        print_with_pause("Дитина вилізла але ви застрягли і вас побачив Адам")
                        print_with_pause("Ви вирішили тікати, але провалились з цією місією")
                        print_with_pause("Адам з легкістю вас наздогнав та вбив своєю Арфою")
                        print_with_pause("Кінець, поганий кінець")
                    else:
                        print_with_pause("Вам вдалось незамітньо вийти через чорний вихід та втекти з хлопчиком")
                        print_with_pause("Ви зберегли останнє життя в цій школі")
                        print_with_pause("Щасливий кінець!\nДякую за гру")
                else:
                    print_with_pause("Ви побігли на ліво та зустріли хлопчика який грає на Арфі")
                    print_with_pause("Не встигши нічого зробити Адам вас вбиває")
                    print_with_pause("Поганий кінець")
            else:
                print_with_pause("Директор знайшов хлопчика , але він повернувся зовсім іншим")
                print_with_pause("Був таким ж спокійним як і всі інші")
                print_with_pause("Лишень з однією сьозинкою на очах він сказав пробачте")
                print_with_pause("Після чого проходять роки і вчитель сам став таким ж бездушним як і всі інші")
                print_with_pause("І тут одного дня він просто падає та помирає")
                print_with_pause("Кінець гри, поганий кінець")
    else:
        print_with_pause("Директор не зацінивши жарту попросив вчителя покинути його школу")
        print_with_pause("Вчитель нерозумівши що відбувається пішов з школи")
        print_with_pause("Кінець, максимально скучний")
else:
    print_with_pause("Ви обходите школу")
    print_with_pause("Замічаєте що всі класи пусті і лишень в одному з всіх грає хлопчик на Арфі")
    print_with_pause("Ви чуєте як він прекрасно грає та зачаровуєтесь піснею")
    print_with_pause("Після чого він різько пропадає і ви приходите до тями")
    print_with_pause("Дальше ви підходите до заднього дворика де побачили маленьку дівчинку")
    print_with_pause("Вона просто стояла та дивилось на давно зарозші травою качелі")
    print_with_pause("Ви підходите до неї та даєте цукерку")
    print_with_pause("Вона подивилась на вас та посміхнулась")
    print_with_pause("Ви пішли до качелей за якими було дуже багато могил")
    print_with_pause("Ви з перелякани лицем повертаєтесь до дівчинки")
    print_with_pause("Її вже на місці не було і ви обернулись назад до могил та побачили на перших могилах тих самих двох дітей що ви бачили")
    print_with_pause("Після цього ви відправились назад до воріт")
    print_with_pause("Зрозумівши що тут щось не так ви пішли з школи")
    print_with_pause("Кінець, хоть щось, але можна було поступити по іншому")