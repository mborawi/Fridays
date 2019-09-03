## The lazy donkey

Given a grid of x by x where x is an odd number (5x5, 9x9 etc)
and a robo-donkey positioned at center cell of the grid help it find the least steepest way downhill.

Once robo-donkey reachs a location where neighboring locations are of the same altitude or higher, it stops moving.

Robo-donkey moves only in N,W,E,S directions when possible... earth is flat in case u missed that memo ت

### Example:
|C/R| __C1__ | __C2__ | __C3__| __C4__ | __C5__ |
|:--:|:----: |:----:|:----:|:----:|:----:|
|__R1__|-46 | 91 | 68 | 8  | 88  |
|__R2__| 11 | 71 | 80 | 27 | 38  |
|__R3__|13 | 71 |  100  | 89 | 57 |
|__R4__| -33 | 83 | 54 | 90 | 96 |
|__R5__| 60 | 36 | 76 | 53 | 29|


### Solution:
Robo-Donkey's Path of least steep decline
|C/R| __C1__ | __C2__ | __C3__| __C4__ | __C5__ |
|:--:|:----: |:----:|:----:|:----:|:----:|
|__R1__|-46 | 91 | 68 | 8 &#x1F44C; | 88  |
|__R2__| 11 | 71 | 80 | 27 &#x1F446;| 38 &#x1F448;  |
|__R3__|13 | 71 |  100 &#x1F449; | 89 &#x1F449;| 57 &#x1F446; |
|__R4__| -33 | 83 | 54 | 90 | 96 |
|__R5__| 60 | 36 | 76 | 53 | 29|

100 -> 89 -> 57 -> 38 -> 27 ->  8

### Data:
File name will indicate grid size and wether it contains solution.


Each line will be a grid represents as comma sepearated altitudes, if solution is available it will be after a colon.
previous example:


-46,91,68,8,88,11,71,80,27,38,13,71,100,89,57,-33,83,54,90,96,60,36,76,53,29:100,89,57,38,27,8\n

