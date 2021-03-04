test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *

          >>> magic_month(1)
          0
          >>> magic_month(2)
          31
          >>> magic_month(7)
          181
          >>> magic_month(11)
          304
          """,
          'hidden': False,
          'locked': False,
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
