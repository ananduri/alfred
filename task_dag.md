O
`Make` an _AI_ that chases another agent around
|
V
`Print` out a _grid_
|
V
`Create` _rules_ for the agent to move
|
V
`Make` another _agent_ follow the first one around
|
V
`Put` _state_ in a 'state' namedtuple
|
V
`Reorganize` _code_ to make it acceptable to show Mike
|
V
`Introduce` drops (_'socks'_)
|    - or, bring meals to agent?
|    - or, it has to pick up a certain meal and bring it to Batman,
|      depending on Batman's state
|    - either way, it can't observe the drops (it's dark in the batcave)
|      it just knows when it has collected one (or how many it has collected)
|
--->
   |
   V
   `Print` the _board_ with socks included
   |
   V
   `Refactor` _code_ to take in 'state' 'batman' and 'alfred' variables
   |
   V
   `Make` alfred _'pick up'_ the socks
   |
   --->
      |
      V
      `Implement` _collision detection_
      |   - with batman
      |   - with socks
      V
   <---
   |
   V
   `Make` batman _drop_ socks
   |
   V
   `Introduce` a way to keep track of how many socks are picked up
   |
<---
|
V   
`Fix` _bug?_ in movement
|
--->
   |
   V
   `Find out` why alfred _disappears_ sometimes
   |    - I think it's b/c collision detection is not working right
   |
   V
   * `Write` a manual test that checks for collision after a large number of runs
   |
   V
   `Write` some _unit tests_ for movement





























