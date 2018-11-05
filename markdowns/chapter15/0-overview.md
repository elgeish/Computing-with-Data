# Overview

Why should we care about code craftsmanship? The long answer is in this chapter.
First, let's see what a French philosopher, by the name of Guillaume Ferrero,
discovered: the Principle of Least Effort. He wrote about it in 1894 — long
before a single line of computer code, as we know it today, was written.
Nevertheless, we can't help but think that, had he been alive to witness how
most code is written, he would have demonstrated coding as the epitome
of the least effort principle:
>[Coding] stops as soon as minimally acceptable results are found.

Sounds familiar? Well, we've all been there; once we find acceptable results,
there's no immediate need to improve the current solution; we just want to get
the task done, get that dose of instant gratification, and move on to the shiny
new project. Putting out fires and plugging holes are good examples of tasks
that we don't want to revisit once we found a good enough fix; and that notion
is a perilous inclination, especially in the face of deadlines. It's also hard
to resist the temptation of instant gratification; it takes discipline,
self-control, and foresight to seek delayed gratification instead.
A landmark psychological study, the Stanford marshmallow experiment,
found a correlation between seeking delayed gratification and being more
successful in life. I believe the same concept can be applied to code:
We can stop at acceptable results and have a marshmallow to celebrate
checking off a box that says we're done; or we can strive for more and have two
marshmallows to celebrate the better results of going the extra mile.

But is completing a task as tempting as enjoying a sweet treat? You bet!
It may even be more tempting than you think; thanks to dopamine:
a neurotransmitter connected to certain feelings like reward (completing tasks)
and pleasure (enjoying sweets). Usually, code requires multiple iterations
to reach acceptable results; with each disappointing attempt, the level
of dopamine that gets fired is reduced; when our code works — according to our
acceptance criteria (test cases) — we get a pleasant surprise: increased levels
of dopamine. But why are we inclined to seek a new task after finding
minimally accepted results for the one at hand? According to Hilary Scarlett
in *Neuroscience for Organizational Change*, "[dopamine] levels rise when we
experience something new"; so it's no surprise that our brains seek more
dopamine by making us want to move on to that shiny new task. Yet, experienced
coders understand that building a successful and growing business is more about
making sure existing solutions scale sustainably rather than creating new ones.

We should care for the code we inherited, and the code we are writing for others
to inherit someday; we should exert more effort to keep on improving all code
to reach a higher level of craftsmanship than what's minimally acceptable.
Michael Feathers, author of *Working Effectively with Legacy Code*, eloquently
stated:
>Clean code always looks like it was written by someone who cares.
>There is nothing obvious that you can do to make it better.

In order to justify that extra effort though, we need to have a good reason;
otherwise, our actions will fade away because we weren't inspired to fight
the uphill battle against our natural tendency to be lazy (by sweeping the messy
code under the rug). One good reason is that craftsmanship is vital for software
to really thrive; we explain why in later sections of this chapter.

So how do we define software craftsmanship? This is a hard question to answer;
one may borrow an analogy of hardware craftsmanship because it's tangible;
a good example is that drawn by Walter Isaacson in his book about Steve Jobs:
>Jobs had always indulged his obsession that the unseen parts of a product
>should be crafted as beautifully as its façade, just as his father had taught
>him when they were building a fence. This too he took to extremes when he found
>himself unfettered at NeXT. He made sure that the screws inside the machine had
>expensive plating. He even insisted that the matte black finish be coated
>onto the inside of the cube’s case, even though only repairmen would see it.

Similarly, software developers should pay attention to details that repairmen —
other developers — will see when they read up the source code; reading code is
much more frequent than writing it. Code is not only written for machines
to execute, but also represents a means of communicating with the next person
who will read your code (or your future self).

Besides code, big data represent a set of craftsmanship challenges that are
shaped by the four V's of big data: Volume, Velocity, Variety, and Veracity.
It's challenging to keep track and make sense of the colossal number of data
points collected and processed at a mind-boggling throughput; the various data
sets, formats, and sources we handle; and the high bar of quality that enables
us to trust said data.

In this chapter, we explore ways to elevate the state of computing with data
from minimally acceptable result to balancing craftsmanship and pragmatism.
