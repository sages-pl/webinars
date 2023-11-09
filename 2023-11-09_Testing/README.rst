Dragon (version alpha)
======================
* Source: https://python.astrotech.io/dragon/alpha.html
* Assignment: Dragon (version alpha)
* Complexity: medium
* Lines of code: 100 lines
* Time: 89 min, then 144 min live coding with instructor
* Warning: Don't delete code, assignment will be continued


English
-------
1. In your directory create file ``dragon_alpha.py`` with class representing Dragon

2. Dragon has (attributes):

    a. name
    b. position on the screen
    c. texture file name, default ``img/dragon/alive.png``
    d. health points, default random ``int`` in range from 50 to 100

3. Dragon can (methods):

    a. have position set to any place on the screen
    b. make damage in range from 5 to 20
    c. take damage
    d. move in any direction by specified value

4. Assume left-top screen corner as an initial coordinates position:

    a. going right add to ``x``
    b. going left subtract from ``x``
    c. going up subtract from ``y``
    d. going down add to ``y``

5. When health points drop to, or below zero:

    a. Dragon is dead
    b. Set object status to dead
    c. Change texture file name to  ``img/dragon/dead.png``
    d. Print ``XXX is dead``, where ``XXX`` is the dragon's name
    e. Print how much gold dragon dropped (random integer from 1 to 100)
    f. Print position where dragon died

6. Run the game:

    a. Create dragon at x=50, y=120 position and name it "Wawelski"
    b. Set new position to x=10, y=20
    c. Move dragon left by 10 and down by 20
    d. Move dragon left by 10 and right by 15
    e. Move dragon right by 15 and up by 5
    f. Move dragon down by 5
    g. Dragon makes damage
    h. Make 10 points damage to the dragon
    i. Make 5 points damage to the dragon
    j. Make 3 points damage to the dragon
    k. Make 2 points damage to the dragon
    l. Make 15 points damage to the dragon
    m. Make 25 points damage to the dragon
    n. Make 75 points damage to the dragon

Non-functional requirements:

    a. Assignment is simulation of a software development process.
    b. Assignment is a business requirements specification.
    c. Solution must fulfill all the acceptance criteria.
    d. How to implement those criteria is up to you.
    e. You - programmer, Instructor - Product Owner.
    f. Product Owner will not help you in architectural decisions.
    g. Do not check neither solution nor future versions (beta and rc).

Post notes:

    b. Trainer acts as Product Owner with little technical knowledge
    c. You are the software engineer who need to decide and live with
       consequences of your choices
    d. Task is a narrative story telling to demonstrate OOP
       and good engineering practices
    e. Calculated last position of the game should be x=20, y=40
    f. You can introduce new fields, methods, functions, variables,
       constants, classes, objects, whatever you want
    g. Don't use modules form outside the Python Standard Library
    h. Task is business requirement specification, not a technical
       documentation, i.e., "what Dragon has to do, not how to do it"
    i. You don't have to keep order of specification while writing code
    j. This is `alpha` version, so no new functionality like
       negative position checking etc.
    l. You can create tests, i.e.: unittest, doctest
    k. Do not read solution or any future iterations of this exercise;
       if you read future tasks, you will spoil fun and learning


Polish
------
1. W swoim katalogu stwórz plik ``dragon_alpha.py`` a w nim klasę reprezentującą Smoka

2. Smok ma (atrybuty):

    a. nazwę
    b. pozycję na ekranie
    c. nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
    d. punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

3. Smok może (metody):

    a. być ustawiony w dowolne miejsce ekranu
    b. zadawać komuś losowe obrażenia z przedziału od 5 do 20
    c. otrzymywać obrażenia
    d. być przesuwany w którymś z kierunków o zadaną wartość

4. Przyjmij górny lewy róg ekranu za punkt początkowy:

    a. idąc w prawo dodajesz ``x``
    b. idąc w lewo odejmujesz ``x``
    c. idąc w górę odejmujesz ``y``
    d. idąc w dół dodajesz ``y``

5. Kiedy punkty życia Smoka spadną do lub poniżej zera:

    a. Smok jest martwy
    b. Ustaw status obiektu na dead
    c. Zmień nazwę pliku tekstury na ``img/dragon/dead.png``
    d. Wypisz ``XXX is dead``, gdzie ``XXX`` to nazwa smoka
    e. Wypisz ile złota smok wyrzucił (losowa liczba od 1 do 100)
    f. Wypisz pozycję gdzie smok zginął

6. Przeprowadź grę:

    a. Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
    b. Ustaw nową pozycję na x=10, y=20
    c. Przesuń smoka w lewo o 10 i w dół o 20
    d. Przesuń smoka w lewo o 10 i w prawo o 15
    e. Przesuń smoka w prawo o 15 i w górę o 5
    f. Przesuń smoka w dół o 5
    g. Smok zadaje obrażenia (5-20)
    h. Zadaj 10 obrażeń smokowi
    i. Zadaj 5 obrażeń smokowi
    j. Zadaj 3 obrażeń smokowi
    k. Zadaj 2 obrażeń smokowi
    l. Zadaj 15 obrażeń smokowi
    m. Zadaj 25 obrażeń smokowi
    n. Zadaj 75 obrażeń smokowi
    o. Smok powinien zginąć na pozycji: x=20, y=40

Wymagania niefunkcjonalne:

    a. **Zadanie jest symulacją procesu wytwarzania oprogramowania.**

       Posłuży do demonstracji obiektowego paradygmatu programowania,
       i dobrych praktyk programistycznych. Nie piszemy gry i nie będziemy
       omawiali specyfiki game-dev. Siłą rzeczy poruszymy kilka kwestii
       z tym związanych, ale całość dyskusji znajdzie zastosowanie do
       dowolnego rodzaju projektów informatycznych i problemów inżynierii
       oprogramowania w dowolnej domenie biznesowej.

    b. **Zadanie jest specyfikacją wymagań biznesowych.**

       Nie jest to dokumentacja techniczna. Zadanie opisuje "co Smok ma
       robić", a nie "jak to ma robić". To ważna różnica i zwróć na to uwagę.
       Z tego powodu nie musisz trzymać się kolejności punktów i podpunktów
       w zadaniu, a także rozwiązać problemy inaczej niż jest napisane.

    c. **Rozwiązanie musi spełniać kryteria akceptacyjne.**

       Pamiętaj, że jest to wersja `alpha` więc nie wprowadzaj dodatkowych
       niezamówionych funkcjonalności (np. dodatkowych postaci, sprawdzania
       wychodzenia poza planszę itp.)

    d. **Sposób implementacji jest dowolny.**

       Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
       klasy, obiekty, unittest lub doctest, type annotation - co tylko
       chcesz, ale `nie korzystaj z modułów spoza biblioteki standardowej`.
       Wyjątkiem może być framework do testów.

    e. **Ty - programista, Prowadzący - Product Owner.**

       Przy tym zadaniu wcielisz się w rolę inżyniera oprogramowania
       (programisty), a Prowadzący będzie zachowywał się jak Product Owner
       z niewielką wiedzą techniczną - 10 lat temu był programistą, a teraz
       większość czasu spędza w Excelu i na spotkaniach. Pamiętaj, że
       doświadczenie Product Ownera rzutuje na sposób w jaki pisze kryteria
       akceptacyjne. Jego kariera programisty może powodować,
       że w specyfikacji wymagań pojawią się kwestie techniczne i sugestie
       jak dany problem rozwiązać. Musisz to odfiltrować z treści zadania.
       Niestety to bardzo częsty scenariusz w branży IT.

    f. **Product Owner nie doradzi Ci w sprawie decyzji architektonicznych.**

       Nie podpowie Ci czy lepiej będzie zrobić to w jakiś konkretny sposób,
       albo czy jak zastosujesz to pewne rozwiązanie to jaki będzie wpływ na
       przyszłość. Zadanie polega na tym, że to Ty musisz podejmować decyzje
       i ponosić ich konsekwencje, tj. łatwa możliwość wprowadzania zmian w
       przyszłych wersjach. Musisz znaleźć balans, między wdrożeniem szybkim
       funkcjonalności, łatwością zrozumienia i utrzymywania kodu i nie
       zablokowaniem sobie drogi na wprowadzanie zmian w przyszłości.
       Pamiętaj o TDD, YAGNI, DRY, KISS, emerging architecture
       i over-engineering.

    g. **Nie przeglądaj rozwiązań ani treści kolejnych części zadania.**

       Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę. To
       zadanie ma niesamowity potencjał edukacyjny. Nie niszcz go.

Powodzenia i miłej zabawy!


Hints
-----
* Shortest possible solution could have 24 lines of code
* ``from random import randint``
* ``randint(a, b)`` - random integer between ``a`` and ``b`` (inclusive!)


Tests
-----
Integration Tests:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m doctest -v test/*.py

Unit Tests:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m unittest discover -v test

Test Coverage:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m coverage run src
    python3 -m coverage xml -o .tmp/coverage.xml

Security Test:

.. code-block:: sh

    export PYTHONPATH=src
    mkdir -p .tmp
    python3 -m bandit --format json --output=.tmp/bandit.json --recursive src

Static Tests:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m mypy --ignore-missing-imports --cobertura-xml-report=.tmp src

Code Style:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m flake8 --doctest --output-file=.tmp/flake8.txt src

Lint:

.. code-block:: sh

    export PYTHONPATH=src
    python3 -m pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --output=.tmp/pylint.txt --disable=C0114,C0115,C0116,E0401,C0103 src
    python3 -m pylama --verbose --async src/

Mutation Testing:

.. code-block:: sh

    mutmut run || true
    mutmut results
    mutmut junitxml --suspicious-policy=ignore --untested-policy=ignore > .tmp/xunit.xml

Test Report:

.. code-block:: sh

    docker run --rm --net=ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli

Errors:

* C0114 - missing-module-docstring
* C0115 - missing-class-docstring
* C0116 - missing-function-docstring
* E0401 - import-error
* C0103 - invalid-name (errors on ``x`` and ``y`` attribute names)


Package
-------
.. code-block:: sh

    python3 -m pip install --upgrade --no-cache-dir -r requirements.prod --target src
    rm -fr src/*.dist-info
    python3 -m compileall -f src
    # find src -name '*.py' -not -name '__main__.py' -not -name '__init__.py' -delete  # not working for now
    python3 -m zipapp --python="/usr/bin/env python3" --output=game.pyz src

.. code-block:: sh

    unzip -l game.pyz


Docker
------
.. code-block:: dockerfile

    FROM python:3.10
    COPY game.pyz /game.pyz
    CMD python3 /game.pyz
