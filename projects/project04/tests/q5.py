test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *
          
          >>> day_of_week(7, 29, 2019)
          1
          >>> day_of_week(12, 25, 2020)
          5
          >>> day_of_week(7, 4, 1900)
          3
          >>> day_of_week(2, 14, 2000)
          1
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
