test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *

          >>> new_years_day(2019)
          2
          >>> new_years_day(2020)
          3
          >>> new_years_day(1900)
          1
          >>> new_years_day(2021)
          5
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
