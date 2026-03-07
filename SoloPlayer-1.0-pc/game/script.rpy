# Сценарий игры "Три грани анализа: Путь аналитика"

# Определение персонажей игры.
define alex = Character('Алексей', color='#4287f5')  # Наставник, руководитель аналитики
define daria = Character('Дарья', color='#f5a442')   # Бизнес-аналитик
define semen = Character('Семён', color='#42f554')   # Системный аналитик
define elena = Character('Елена', color='#f542ec')   # Аналитик данных
define client = Character('Клиент', color='#f55442')
define team = Character('Команда', color='#a842f5')

# Переменные для отслеживания пути
define business_skill = 0      # Навыки бизнес-аналитика
define system_skill = 0        # Навыки системного аналитика
define data_skill = 0          # Навыки аналитика данных
define balance = 0             # Сбалансированный подход

# Игра начинается здесь:
label start:

    scene building
    with fade

    show alex
    alex "Привет! Я Алексей, руководитель отдела аналитики. Слышал, ты хочешь стать аналитиком?"
    hide alex

    show alex
    alex "Но есть нюанс... аналитики бывают разные. И нам нужен человек, который сможет закрыть сразу несколько направлений."
    hide alex

    show alex
    menu:
        alex "Расскажи, что тебя привлекает в аналитике?"
        "Хочу понимать бизнес и помогать принимать решения.":
            $ business_skill += 1
            alex "Бизнес-аналитика — отличный выбор! Будешь мостом между бизнесом и IT."
            jump scene_analyst_1
        "Люблю проектировать системы и описывать требования.":
            $ system_skill += 1
            alex "Системный анализ — это фундамент любой разработки. Без тебя никуда!"
            jump scene_analyst_1
        "Обожаю работать с данными, искать закономерности и строить прогнозы.":
            $ data_skill += 1
            alex "Аналитика данных сейчас на пике! Готов к цифрам и инсайтам?"
            jump scene_analyst_1
        "Хочу попробовать всё и найти свой путь.":
            $ balance += 1
            alex "Универсалы тоже нужны. Погружайся во все направления!"
            jump scene_analyst_1

label scene_analyst_1:

    scene workplace
    with fade

    show daria
    daria "Привет, коллега! Я Дарья, бизнес-аналитик. У нас тут интересная задача — крупный заказчик хочет автоматизировать складской учёт."
    hide daria

    show daria
    daria "Но проблема в том, что они сами не знают, чего хотят. Говорят: 'Сделайте удобно, как в том приложении'."
    hide daria

    show daria
    menu:
        daria "Как бы ты начал работу с таким клиентом?"
        "Проведу серию интервью, чтобы выявить реальные боли бизнеса.":
            $ business_skill += 1
            daria "Отлично! Главное — задавать правильные вопросы."
            jump scene_analyst_2
        "Попрошу показать текущие процессы и нарисую AS-IS и TO-BE модели.":
            $ system_skill += 1
            daria "Системный подход! Моделирование процессов — наше всё."
            jump scene_analyst_2
        "Посмотрю, какие данные у них уже есть, и предложу решение на основе метрик.":
            $ data_skill += 1
            daria "Интересный подход. Данные не врут!"
            jump scene_analyst_2
        "Предложу провести небольшой пилот, чтобы понять, что реально нужно.":
            $ balance += 1
            daria "Гибкий подход. Итеративность — ключ к успеху."
            jump scene_analyst_2

label scene_analyst_2:

    scene office
    with fade

    show client
    client "Нам нужно, чтобы система сама понимала, когда товар заканчивается, и заказывала новый."
    hide client

    show client
    client "И ещё чтобы видеть аналитику в реальном времени на дашборде."
    hide client

    show daria
    daria "А какой объём данных? Сколько товаров на складе?"
    hide daria

    show client
    client "Ну, примерно 10 тысяч наименований, поставки каждый день."
    hide client

    show semen at left
    show elena at right
    with move

    semen "Системе нужно будет интегрироваться с 1С и несколькими CRM. Надо продумать архитектуру."
    elena "И настроить ETL-процессы, чтобы данные грузились быстро и без ошибок."

    menu:
        "Что сейчас важнее всего уточнить?"
        "Какие бизнес-процессы должны автоматизироваться в первую очередь?":
            $ business_skill += 1
            daria "Без этого нельзя. Приоритеты бизнеса — основа."
            jump scene_analyst_3
        "Нужно описать требования к интеграциям и API.":
            $ system_skill += 1
            semen "Системный аналитик во мне ликует!"
            jump scene_analyst_3
        "Какая частота обновления данных нужна и какие метрики критичны?":
            $ data_skill += 1
            elena "Точный вопрос! Без этого дашборд будет бесполезен."
            jump scene_analyst_3
        "Надо синхронизировать все три аспекта: бизнес-цели, системные ограничения и данные.":
            $ balance += 1
            alex "Универсальный подход. Именно так рождаются лучшие решения."
            jump scene_analyst_3

label scene_analyst_3:

    scene whiteboard
    with fade

    show semen
    semen "Так, я набросал схему интеграций. У нас будет микросервис для расчёта прогнозов и отдельное хранилище данных."
    hide semen

    show daria
    daria "Пользователи просят, чтобы интерфейс был максимально простым. Они не хотят 100 кнопок."
    hide daria

    show elena
    elena "А у меня первые результаты по данным: сезонность влияет на 40 процентов заказов, и есть товары, которые часто заказывают вместе."
    hide elena

    show alex
    alex "Нужно собрать всё воедино и написать документ для разработки."
    hide alex

    menu:
        alex "Как лучше структурировать документацию?"
        "Сначала опишем бизнес-требования, потом функциональные, потом нефункциональные.":
            $ business_skill += 1
            show alex
            alex "Классика жанра. Бизнес-аналитики это любят."
            hide alex
            jump scene_analyst_4
        "Сделаем Use Case диаграммы, спецификацию API и описание интеграций.":
            $ system_skill += 1
            show semen
            semen "Мой любимый подход!"
            hide semen
            jump scene_analyst_4
        "Опишем требования к данным: источники, форматы, частоту обновления, метрики.":
            $ data_skill += 1
            show elena
            elena "Без этого дашборды не построить."
            hide elena
            jump scene_analyst_4
        "Создадим единый документ, где связаны бизнес-цели, системные требования и аналитические отчёты.":
            $ balance += 1
            show alex
            alex "Системная аналитика в лучшем виде!"
            hide alex
            jump scene_analyst_4

label scene_analyst_4:

    scene development
    with fade

    show semen at left
    show elena at right
    show daria
    with move 
    team "А как нам понять, что мы сделали то, что нужно? Критерии приёмки какие?"
    hide semen
    hide elena
    hide daria

    show alex
    alex "Отличный вопрос. Петя, что скажешь?"
    hide alex

    menu:
        "Какие критерии приёмки предложить команде?"
        "Каждый сценарий должен соответствовать бизнес-процессу, описанному в требованиях.":
            $ business_skill += 1
            show daria
            daria "Приёмка через бизнес-сценарии — золотой стандарт."
            hide daria
            jump scene_analyst_5
        "API должен отвечать за меньше 200мс, интеграции работать без сбоев.":
            $ system_skill += 1
            show semen
            semen "Чёткие технические критерии — то, что нужно разработчикам."
            hide semen
            jump scene_analyst_5
        "Дашборд должен обновляться раз в 15 минут, прогнозы с точностью не ниже 85 процентов.":
            $ data_skill += 1
            show elena
            elena "Критерии качества данных — наше всё."
            hide elena
            jump scene_analyst_5
        "Составим чек-лист из бизнес-сценариев, технических требований и проверки данных.":
            $ balance += 1
            show alex
            alex "Комплексный подход — признак зрелого аналитика."
            hide alex
            jump scene_analyst_5

label scene_analyst_5:

    scene problem
    with fade

    show client
    client "У нас изменились правила учёта! Теперь нужно учитывать не только приход, но и резервирование товаров."
    hide client

    show daria
    daria "Это сильно меняет бизнес-процесс..."
    hide daria

    show semen
    semen "И нам придётся менять логику расчёта остатков."
    hide semen

    show elena
    elena "А ещё перестраивать витрину данных."
    hide elena

    show alex
    alex "Спокойно. Петя, твоя задача — оценить влияние изменений."
    hide alex

    menu:
        alex "Как оценить влияние изменений?"
        "Посмотрю, какие бизнес-процессы затронуты, и согласую приоритеты с клиентом.":
            $ business_skill += 1
            show daria
            daria "Управление ожиданиями — ключевой навык!"
            hide daria
            jump scene_analyst_6
        "Опишу, какие модули системы нужно доработать, и оценю трудозатраты.":
            $ system_skill += 1
            show semen
            semen "Техническая оценка — основа планирования."
            hide semen
            jump scene_analyst_6
        "Проанализирую, как изменения повлияют на отчёты и метрики.":
            $ data_skill += 1
            show elena
            elena "Важно сохранить целостность аналитики."
            hide elena
            jump scene_analyst_6
        "Составлю матрицу влияния: бизнес-процессы → системные компоненты → данные.":
            $ balance += 1
            show alex
            alex "Профессионально! Видишь полную картину."
            hide alex
            jump scene_analyst_6

label scene_analyst_6:

    scene dashboard
    with fade

    show elena
    elena "Смотри, что я нашла в данных! Оказывается, 20 процентов товаров приносят 80 процентов выручки, и именно они чаще всего заканчиваются."
    hide elena

    show daria
    daria "Это же отличная бизнес-возможность! Предложим клиенту систему приоритетного пополнения этих товаров."
    hide daria

    show semen
    semen "Я могу добавить в систему флаг 'VIP-товар' и отдельную логику для них."
    hide semen

    show alex
    alex "Петя, как думаешь, стоит ли предлагать это клиенту как отдельную фичу?"
    hide alex

    menu:
        alex "Что скажешь?"
        "Да, это добавит бизнес-ценности продукту. Надо оценить выгоду.":
            $ business_skill += 1
            show daria
            daria "Бизнес-аналитик всегда ищет ценность для клиента!"
            hide daria
            jump scene_analyst_7
        "Технически это несложно, опишу требования к доработке.":
            $ system_skill += 1
            show semen
            semen "Системный аналитик готов к новым задачам!"
            hide semen
            jump scene_analyst_7
        "Проверю гипотезу статистически и построю модель прогноза дефицита.":
            $ data_skill += 1
            show elena
            elena "Data-driven подход рулит!"
            hide elena
            jump scene_analyst_7
        "Сделаем презентацию для клиента с бизнес-обоснованием, техописанием и дашбордом для отслеживания.":
            $ balance += 1
            show alex
            alex "Идеально! Ты мыслишь как настоящий аналитик-универсал."
            hide alex
            jump scene_analyst_7

label scene_analyst_7:

    scene presentation
    with fade

    show client
    client "Отличная работа! Система работает, дашборды красивые, прогнозы сбываются. А главное — я вижу, как это помогает бизнесу."
    hide client

    show alex
    alex "Петя, пришло время подвести итоги. Каким аналитиком ты стал?"
    hide alex

    if (business_skill > system_skill) and (business_skill > data_skill) and (business_skill > balance):
        show daria
        daria "Поздравляю! Ты прирождённый бизнес-аналитик. Ты умеешь слышать клиента, переводить его потребности на язык требований и находить бизнес-ценность в каждом решении."
        hide daria
        show alex
        alex "Такие специалисты — золотой фонд компании. Клиенты тебя обожают, а команда понимает, зачем что-то делает."
        hide alex
        $ analyst_path = "business"
        
    elif (system_skill > business_skill) and (system_skill > data_skill) and (system_skill > balance):
        show semen
        semen "Поздравляю! Ты настоящий системный аналитик. Твой конёк — чёткие спецификации, продуманная архитектура и требования, по которым разработчикам легко работать."
        hide semen
        show alex
        alex "Разработчики молятся на таких аналитиков. Всё разложено по полочкам, никакой неопределённости."
        hide alex
        $ analyst_path = "system"
        
    elif (data_skill > business_skill) and (data_skill > system_skill) and (data_skill > balance):
        show elena
        elena "Поздравляю! Ты аналитик данных до мозга костей. Ты видишь закономерности там, где другие видят хаос, и умеешь превращать цифры в инсайты."
        hide elena
        show alex
        alex "В мире Big Data такие специалисты на вес золота. Твои дашборды помогают принимать правильные решения."
        hide alex
        $ analyst_path = "data"
        
    else:
        show alex
        alex "Поздравляю! Ты стал универсальным аналитиком — тем, кто понимает и бизнес, и системы, и данные. Это редкое сочетание!"
        hide alex
        show daria
        daria "Ты можешь говорить с клиентами..."
        hide daria
        show semen
        semen "...проектировать сложные системы..."
        hide semen
        show elena
        elena "...и находить инсайты в данных. Ты — полный стек аналитики!"
        hide elena
        $ analyst_path = "balance"

    window hide
    scene analyst_end with fade
    
    if analyst_path == "business":
        "Твой путь — БИЗНЕС-АНАЛИТИК. Ты соединяешь бизнес и технологии, находишь точки роста и создаёшь ценность."
    elif analyst_path == "system":
        "Твой путь — СИСТЕМНЫЙ АНАЛИТИК. Ты строишь мосты между требованиями и кодом, создаёшь порядок из хаоса."
    elif analyst_path == "data":
        "Твой путь — АНАЛИТИК ДАННЫХ. Ты добываешь золото из цифр, видишь будущее в графиках и меняешь мир через данные."
    else:
        "Твой путь — УНИВЕРСАЛЬНЫЙ АНАЛИТИК. Ты видишь картину целиком и можешь закрыть любой участок работы. Таких, как ты, единицы!"

    "Конец. Спасибо за игру!"

    $ persistent.analyst_complete = True

        