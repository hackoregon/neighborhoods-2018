
bike_parking_meta = {
  'attributes': {
    'primary': {
      'field': None,
      'name': None,
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None,
    'date_granularity': None,
    'default_date_filter': '2017',
    },
  }

bike_lanes_meta = {
  'attributes': {
    'primary': {
      'field': None,
      'name': None,
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None, 
    'date_granularity': None,
    'default_date_filter': '2018',
    },
  }

taxlot_block_groups_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2010',
  },
}

parks_meta = {
'attributes': {
  'primary': {
    'field': 'name',
    'name': 'Park',
  },
  'secondary': {
    'field': 'acres',
    'name': 'Park Acreage',
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

parks_trails_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}


multiuse_trails_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

community_gardens_meta = {
'attributes': {
  'primary': {
    'field': 'sitename' ,
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2017',
  },
}

bike_greenways_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

rail_stops_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2016',
  },
}

demolitions_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '18',
  },
}


camp_sweeps_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'reportdate',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  },
}

camp_reports_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'date',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  },
}

retail_grocers_meta = {
'attributes': {
  'primary': {
    'field': 'company_na',
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}
trees_meta = {
'attributes': {
  'primary': {
    'field': 'company_na',
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'date_inventoried',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bus_stops_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

under18_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_children_under_18',
    'name': 'Households with Children',
    'visualization': {
      'type': 'PercentDonut',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}

over65_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_individuals_65_ovr',
    'name': 'Households w/ Seniors',
    'visualization': {
      'type': 'PercentDonut',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}

population_meta = {
'attributes': {
  'primary': {
    'field': 'total_population',
    'name': 'Total Population',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'5005',
      'comparison_name':'Average Total Population',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}