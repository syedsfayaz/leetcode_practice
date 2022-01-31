System
Design:
We
would
like
you
to
design
a
system
to
continuously
integration and continuously
deliver(release)
software.There
are
multiple
teams
contributing
to
the
software.
The
teams
are
working
independently(adding
new
feature and fixing
bugs).Code
from all the

teams is built
into
one
monolithic
image
which
should
be
released
periodically
to
the
customers.

Callouts:
1.
Releases
are
mainly
driven
by
code
changes and testing
2.
Make
sure
we
do
full
regression
testing
before
the
image is released
a.Each
team
works in isolation and cannot
validate / test
each
other’s
use
cases
3.
Testing
has
to
be
done
on
virtual as well as real
hardware / devices

1.
Assuming
the
code is stored in Git
repo.
2.
Jenkins
CI - CI
tool
to
do
continuous
integration.
3.
Unit
tests
will
be
run
for every build.
    4.
    Code
    Quality
    scans
    for testing the Quality Gate.

--- Master
-- Dev
-- Feature / bugfix

5.
Final
mono
binary.Final_artifact - BuildNumber - date - time.tar
