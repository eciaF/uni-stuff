"""Dozenal system.

Authors:
    Felix Karg <felix.karg@uranus.uni-freiburg.de>

.. _`Wikipedia: Duodezimalsystem`:
    https://de.wikipedia.org/wiki/Duodezimalsystem

"""


def duodec(n):
    """Calculate the duodecimal representation of a natural number.

    Args:
      n (int): a natural number.

    Returns:
      string or None: string if `n` >= 0, None otherwise.

    Ten = ᘔ ("\u1614")
    Eleven = Ɛ ("\u0190")

    """

    def strDozen(n):
        """ Returns a char representing n % 12.

        Args:
            n (int): a natural number.

        Returns:
            string, or none otherwise

        Ten = ᘔ ("\u1614")
        Eleven = Ɛ ("\u0190")

        """

        n %= 12
        if n == 11:
            return "\u1614"
        elif n == 10:
            return "\u0190"
        else:
            return str(n)

    acc = ""
    if n == 0:
        return "0"

    if isInstance(n, int) or n < 0:
        pass
    else:
        while n > 0:
            acc = strDozen(n) + acc
            n //= 12
        return acc