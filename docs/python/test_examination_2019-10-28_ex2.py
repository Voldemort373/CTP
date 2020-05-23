# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

from re import sub


def test(gn, fn, mn):
    result = 0

    c_gn = cnt(gn)
    c_fn = cnt(fn)

    for c in c_gn:
        if c in c_fn:
            result = result + (c_gn[c] - c_fn[c])

    idx = (len(gn) + len(fn)) % len(mn)
    return result * (int(mn[idx]) + 1)


def cnt(s):
    result = {}

    for c in s:
        if c not in result:
            result[c] = 0
        result[c] = result[c] + 1

    return result


my_gn = sub("[^a-z]", "", input("Please provide your given name: ").lower())
my_fn = sub("[^a-z]", "", input("Please provide your family name: ").lower())
my_mn = input("Please provide your matriculation number: ").strip()

print("Result:", test(my_gn, my_fn, my_mn))
