# COVAT
Collection of Various Attractor Types (in 2D).

## Introduction
Attractors are plots of unique equations. They are created by iterating over an equation multiple times and using the result at each iteration to plot a point. The result is then fed back into the equation. After millions of points have been plotted, fractal-like structures begin to appear. Over time, the repeated points fall into a basin of attraction that forms the unique shape.

## Attractors
Below are the list of implemented attractors:

| Name          | Number of Parameters | Restrictions  | Source | Link |
| :-----------: |:--------------------:|:-------------:|:-------:|----:|
| Arnold        | 1                    | ```δ < 1/2π -- 0 ≤ x ≤ 0.2 -- 0 ≤ y ≤ 0.2```| ```Irregular Attractors - Vadim S. Anishchenko and Galina I. Strelkova``` | [PDF](https://www.emis.de/journals/HOA/DDNS/2/153.pdf) | 
| Bedhead       | 2                    | ```-1 ≤ a ≤ 1 -- -1 ≤ b ≤ 1 --x, y == 1.0```   |Discovered by Ivan Emrich -- ```Jason Rampe - 2D Strange Attractors Blog```| [SITE](https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/) |
| Belykh        | 3                    | blah blah     |

#### To-Do:
- Finish incomplete attractors..
- Add argparsers..
- Implement 3D attractors..
- Credits/References..
- Instructions/Usage/Restrictions..
- Gallery of examples..
