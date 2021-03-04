test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *
          >>> is_leap(2000)
          True
          >>> is_leap(1900)
          False
          >>> is_leap(2004)
          True
          >>> is_leap(2005)
          False
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
