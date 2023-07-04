# COVAT
Collection of Various Attractor Types (in 2D).

## Introduction
Attractors are plots of unique equations. They are created by iterating over an equation multiple times and using the result at each iteration to plot a point. The result is then fed back into the equation. After millions of points have been plotted, fractal-like structures begin to appear. Over time, the repeated points fall into a basin of attraction that forms the unique shape.

## Attractors
Below are the list of implemented attractors:

| Name          | Number of Parameters | Restrictions  | Source | Link |
| :-----------: |:--------------------:|:-------------:|:-------:|:----:|
| Arnold        | 1                    | ```δ < 1/2π -- 0 ≤ x ≤ 0.2 -- 0 ≤ y ≤ 0.2```| ```Irregular Attractors - Vadim S. Anishchenko & Galina I. Strelkova``` | [PDF](https://www.emis.de/journals/HOA/DDNS/2/153.pdf) | 
| Bedhead       | 2                    | ```-1 ≤ a ≤ 1 -- -1 ≤ b ≤ 1 --x, y == 1.0```   |Discovered by Ivan Emrich -- ```Jason Rampe - 2D Strange Attractors Blog```| [BLOG](https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/)|
| Belykh        | 3                    | ```0 < λ < 1/2```  1 < γ ≤ $$2/(1+abs(k))$$  ```abs(k) < 1 -- 0 ≤ x ≤ 1 -- 0 ≤ y ≤ 1```     | ```Belykh Map - Vladimir N. Belykh & Igor Belykh``` | [ARTICLE](http://www.scholarpedia.org/article/Belykh_map)|
|  Belykh V1|  2| Unknown |```Symbolic dynamics of Belykh-type maps - Denghui Li & Jianhua Xie``` | [ARTICLE](https://link.springer.com/article/10.1007/s10483-016-2080-9)|
| Burgers |  2|```stable for µ < 0.5 -- loses stability at µ = 0.5 -- invariant closed curve when µ exceeds 0.5```  |```Bifurcation Analysis, Chaos and Control in the Burgers Mapping - E. M. ELabbasy, H. N. Agiza, H. EL-Metwally, A. A. Elsadany``` |[PDF](http://www.worldacademicunion.com/journal/1749-3889-3897IJNS/IJNSVol4No3Paper02.pdf) |
| Business Cycle |  2| Unknown | ```A Business Cycle Model with Cubic Nonlinearity - Tönu Puu & Irina Sushko```| [PDF](http://www.diva-portal.org/smash/get/diva2:227245/FULLTEXT01.pdf)|
|  Cao-Lai|  2| ```0 ≤ x ≤ 1 -- -0.5 ≤ y ≤ 0.5``` | ```Antiphase synchronism in chaotic systems - Ling-Yuan Cao1 & Ying-Cheng Lai```| [PDF](http://chaos1.la.asu.edu/~yclai/papers/PRE_98_CL.pdf)|
|  Cat|  0|  N/A| ```Arnold's Cat Map```|[WIKIPEDIA](https://en.wikipedia.org/wiki/Arnold%27s_cat_map) |
|  Cathala|  2| Unknown |```Invariant Sets for Windows: Resonance Structures, Attractors, Fractals and Patterns -- Albert D. Morozov, Timothy N. Dragunov, Olga V. Malysheva``` | Unknown|
|  Chirikov Standard| 1 | ```0 ≤ x ≤ 1 -- 0 ≤ y ≤ 1```|```Ulam method for the Chirikov standard map --  Klaus M. Frahm & Dima L. Shepelyansky``` ```A Glance at the Standard Map -- Ryan Tobin```|[PDF](https://arxiv.org/pdf/1004.1349.pdf) [PDF](https://csc.ucdavis.edu/~chaos/courses/nlp/Projects2009/RyanTobin/A%20Glance%20at%20the%20Standard%20Map.pdf) |
|  Clifford|  4| ```x, y == 0.1 -- -3 < a, b, c, d < 3``` | Discovered by Clifford A. Pickover -- ```Jason Rampe - 2D Strange Attractors Blog```| [BLOG](https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/)|
|  Coupled Logistic|  |  | | |
|  Cross Chaotic|  |  | | |
|  DeJong|  |  | | |
|  Dual Hénon|  |  | | |
|  Elhadj-Sprott C|  |  | | |
|  Fractal Dream|  |  | | |
|  Gingerbreadman|  |  | | |
|  Gumowski-Mira|  |  | | |
|  HCA|  |  | | |
|  Heagy-Hammel|  |  | | |
|  Hopalong|  |  | | |
|  Ikeda|  |  | | |
|  Joshi-Blackmore|  |  | | |
|  MacMillan|  |  | | |
|  Martin|  |  | | |
|  Maynard-Smith|  |  | | |
|  Mira|  |  | | |
|  Modified Lozi|  |  | | |
|  Modified Mira|  |  | | |
|  Multifold Hénon |  |  | | |
|  Popcorn|  |  | | |
|  Provenzale-Balmforth|  |  | | |
|  Separatrix|  |  | | |
|  Sine|  |  | | |
|  Sine Delay|  |  | | |
|  Sine Sine|  |  | | |
|  Strelkova-Anishchenko|  |  | | |
|  Sunflower|  |  | | |
|  Svensson|  |  | | |
|  Tinkerbell|  |  | | |
|  Ushiki|  |  | | |
|  Yang-Cao|  |  | | |


## Requirements

Although you could install ```requirements.txt```, datashader contains all libraries within except for pillow. So running ```pip install datashader``` ```pip install pillow``` will suffice.

#### To-Do:
- Turn functions into class methods (done for arnold, just need to do all of the rest)
- Finish incomplete attractors..
- Add argparsers..
- Implement 3D attractors..
- Credits/References..
- Instructions/Usage/Restrictions..
- Gallery of examples..
