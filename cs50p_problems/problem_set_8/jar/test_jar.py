from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar2 = Jar(6)
    assert jar2.capacity == 6


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3
    jar.deposit(3)
    assert jar.size == 6
    jar.deposit(4)
    assert jar.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(2)
    assert jar.size == 7
    jar.withdraw(3)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0
