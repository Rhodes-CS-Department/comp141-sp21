test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *

          >>> day_of_week_str(7, 29, 2019)
          'Monday'
          >>> day_of_week_str(12, 25, 2020)
          'Friday'
          >>> day_of_week_str(10, 31, 2056)
          'Tuesday'
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
