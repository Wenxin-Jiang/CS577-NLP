---
language: en
tags:
- allennlp
- question-answering
widget:
- context: 'A reusable launch system (RLS, or reusable launch vehicle, RLV) is a launch
    system which is capable of launching a payload into space more than once. This
    contrasts with expendable launch systems, where each launch vehicle is launched
    once and then discarded. No completely reusable orbital launch system has ever
    been created. Two partially reusable launch systems were developed, the Space
    Shuttle and Falcon 9. The Space Shuttle was partially reusable: the orbiter (which
    included the Space Shuttle main engines and the Orbital Maneuvering System engines),
    and the two solid rocket boosters were reused after several months of refitting
    work for each launch. The external tank was discarded after each flight.'
  text: How many partially reusable launch systems were developed?
  example_title: Reusable launch systems
- context: Robotics is an interdisciplinary branch of engineering and science that
    includes mechanical engineering, electrical engineering, computer science, and
    others. Robotics deals with the design, construction, operation, and use of robots,
    as well as computer systems for their control, sensory feedback, and information
    processing. These technologies are used to develop machines that can substitute
    for humans. Robots can be used in any situation and for any purpose, but today
    many are used in dangerous environments (including bomb detection and de-activation),
    manufacturing processes, or where humans cannot survive. Robots can take on any
    form but some are made to resemble humans in appearance. This is said to help
    in the acceptance of a robot in certain replicative behaviors usually performed
    by people. Such robots attempt to replicate walking, lifting, speech, cognition,
    and basically anything a human can do.
  text: What do robots that resemble humans attempt to do?
  example_title: Robots
- context: In the first quarter, the Bears drew first blood as kicker Robbie Gould
    nailed a 22-yard field goal for the only score of the period. In the second quarter,
    the Bears increased their lead with Gould nailing a 42-yard field goal. They increased
    their lead with Cutler firing a 7-yard TD pass to tight end Greg Olsen. The Bears
    then closed out the first half with Gould's 41-yard field goal. In the third quarter,
    the Vikes started to rally with running back Adrian Peterson's 1-yard touchdown
    run (with the extra point attempt blocked). The Bears increased their lead over
    the Vikings with Cutler's 2-yard TD pass to tight end Desmond Clark. The Vikings
    then closed out the quarter with quarterback Brett Favre firing a 6-yard TD pass
    to tight end Visanthe Shiancoe. An exciting fourth quarter ensued. The Vikings
    started out the quarter's scoring with kicker Ryan Longwell's 41-yard field goal,
    along with Adrian Peterson's second 1-yard TD run. The Bears then responded with
    Cutler firing a 20-yard TD pass to wide receiver Earl Bennett. The Vikings then
    completed the remarkable comeback with Favre finding wide receiver Sidney Rice
    on a 6-yard TD pass on 4th-and-goal with 15 seconds left in regulation. The Bears
    then took a knee to force overtime. In overtime, the Bears won the toss and marched
    down the field, stopping at the 35-yard line. However, the potential game-winning
    45-yard field goal attempt by Gould went wide right, giving the Vikings a chance
    to win. After an exchange of punts, the Vikings had the ball at the 26-yard line
    with 11 minutes left in the period. On the first play of scrimmage, Favre fired
    a screen pass to Peterson who caught it and went 16 yards, before being confronted
    by Hunter Hillenmeyer, who caused Peterson to fumble the ball, which was then
    recovered by Bears' linebacker Nick Roach. The Bears then won on Jay Cutler's
    game-winning 39-yard TD pass to wide receiver Devin Aromashodu. With the loss,
    not only did the Vikings fall to 11-4, they also surrendered homefield advantage
    to the Saints.
  text: Who threw the longest touchdown pass of the game?
  example_title: Argmax
- context: Hoping to rebound from their loss to the Patriots, the Raiders stayed at
    home for a Week 16 duel with the Houston Texans.  Oakland would get the early
    lead in the first quarter as quarterback JaMarcus Russell completed a 20-yard
    touchdown pass to rookie wide receiver Chaz Schilens.  The Texans would respond
    with fullback Vonta Leach getting a 1-yard touchdown run, yet the Raiders would
    answer with kicker Sebastian Janikowski getting a 33-yard and a 30-yard field
    goal.  Houston would tie the game in the second quarter with kicker Kris Brown
    getting a 53-yard and a 24-yard field goal. Oakland would take the lead in the
    third quarter with wide receiver Johnnie Lee Higgins catching a 29-yard touchdown
    pass from Russell, followed up by an 80-yard punt return for a touchdown.  The
    Texans tried to rally in the fourth quarter as Brown nailed a 40-yard field goal,
    yet the Raiders' defense would shut down any possible attempt.
  text: How many yards was the longest passing touchdown?
  example_title: Max
- context: In 1085, Guadalajara was retaken by the Christian forces of Alfonso VI
    . The chronicles say that the Christian army was led by Alvar Fanez de Minaya,
    one of the lieutenants of El Cid. From 1085 until the Battle of Las Navas de Tolosa
    in 1212, the city suffered wars against the Almoravid and the Almohad Empires.
    In spite of the wars, the Christian population could definitely settle down in
    the area thanks to the repopulation with people from the North  who received their
    first fuero in 1133 from Alfonso VII.In 1219, the king Fernando III gave a new
    fuero to the city .During the reign of Alfonso X of Castile, the protection of
    the king allowed the city to develop its economy by protecting merchants and allowing
    markets.
  text: How many years did the city suffer wars against Almoravid and the Almohad
    Empires?
  example_title: Arithmetic
---

An augmented version of QANet that adds rudimentary numerical reasoning ability, trained on DROP (Dua et al., 2019), as published in the original DROP paper.
An augmented version of QANet model with some rudimentary numerical reasoning abilities. The main idea here is that instead of just predicting a passage span after doing all of the QANet modeling stuff, we add several different ‘answer abilities’: predicting a span from the question, predicting a count, or predicting an arithmetic expression. Near the end of the QANet model, we have a variable that predicts what kind of answer type we need, and each branch has separate modeling logic to predict that answer type. We then marginalize over all possible ways of getting to the right answer through each of these answer types.