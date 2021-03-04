test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from pcalendar import *
          
          >>> day_of_year(7, 29, 2019)
          210
          >>> day_of_year(4, 11, 2016)
          102
          >>> day_of_year(12, 31, 2100)
          365
          >>> day_of_year(1, 30, 2016)
          30
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
