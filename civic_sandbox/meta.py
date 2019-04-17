## slide
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
    'min_date': None,
    'max_date': None,
    },
  }

## slide
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
    'min_date': None,
    'max_date': None,
    },
  }

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
demolitions_meta = {
'attributes': {
  'primary': {
    'field': 'description',
    'name': 'Demolition Description',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  'min_date': '2000',
  'max_date': '2018',
  },
}

## slide
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
  'date_attribute': 'formatted_date',
  'date_granularity': 'month',
  'default_date_filter': 'Apr2018',
  'min_date': 'Oct2016',
  'max_date': 'May2018',
  },
}

## slide
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
  'min_date': '2015',
  'max_date': '2018',
  },
}

## slide
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
  'min_date': None,
  'max_date': None,
  },
}

## slide
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

## slide
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

## foundation
under18_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_children_under_18',
    'name': 'Households with Children',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
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
  'min_date': '2000',
  'max_date': '2010',
  },
}

## foundation
over65_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_individuals_65_ovr',
    'name': 'Households w/ Seniors',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
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
  'min_date': '2000',
  'max_date': '2010',
  },
}

## foundation
population_meta = {
'attributes': {
  'primary': {
    'field': 'total_population',
    'name': 'Total Population',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'10000000',
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
  'min_date': '2000',
  'max_date': '2010',
  },
}

## foundation
owner_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'pc_owner_occupied_housing_units',
    'name': 'Owner Occupied Households',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2010',
  },
}

## foundation
living_alone_meta = {
'attributes': {
  'primary': {
    'field': 'pc_householders_living_alone',
    'name': 'Householders Living Alone',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2010',
  },
}
bg_income_meta = {
'attributes': {
  'primary': {
    'field': 'median_household_income',
    'name': 'Median Household Income',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'55013',
      'comparison_name':'Average Median Household Income',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}
bg_gross_rent_meta = {
'attributes': {
  'primary': {
    'field': 'Median_gross_rent',
    'name': 'Median Gross Rent',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}
bg_evictions_meta = {
'attributes': {
  'primary': {
    'field': 'evictions',
    'name': 'Evictions',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}
bg_renter_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'renter_occupied_households',
    'name': 'Renter Occupied Households',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}
bg_pctrenter_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'pctrenter_occupied',
    'name': 'Percent Renter Occupied Households',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}
bg_rent_burden_meta = {
'attributes': {
  'primary': {
    'field': 'rent_burden',
    'name': 'Rent Burden',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}

bg_eviction_rate_meta = {
'attributes': {
  'primary': {
    'field': 'eviction_rate',
    'name': 'Eviction Rate',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}

bg_poverty_rate_meta = {
'attributes': {
  'primary': {
    'field': 'poverty_rate',
    'name': 'Poverty Rate',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016',
  },
}

voters18to25_meta = {
'attributes': {
  'primary': {
    'field': 'pct_18_25',
    'name': 'Registered Voters 18 to 25',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

voters18to25_meta = {
'attributes': {
  'primary': {
    'field': 'pct_18_25',
    'name': 'Registered Voters 18 to 25',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
    'comparison_value': None,
    'comparison_name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

voters26to32_meta = {
'attributes': {
  'primary': {
    'field': 'pct_26_32',
    'name': 'Registered Voters 26 to 32',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
    'comparison_value': None,
    'comparison_name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

voters33to39_meta = {
'attributes': {
  'primary': {
    'field': 'pct_33_39',
    'name': 'Registered Voters 33 to 39',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
    'comparison_value': None,
    'comparison_name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

voters40to49_meta = {
'attributes': {
  'primary': {
    'field': 'pct_40_49',
    'name': 'Registered Voters 40 to 49',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
    'comparison_value': None,
    'comparison_name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

voters50plus_meta = {
'attributes': {
  'primary': {
    'field': 'pct_50_plus',
    'name': 'Registered Voters 50+',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
    'comparison_value': None,
    'comparison_name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2006',
  'max_date': '2016',
  },
}

reports_month_meta = {
'attributes': {
  'primary': {
    'field': 'count',
    'name': 'Count',
    'visualization': {
      'type': 'Text',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
  },
},
  'dates': {
  'date_attribute': 'formatted_date',
  'date_granularity': 'month',
  'default_date_filter': 'Apr2018',
  'min_date': 'Dec2015',
  'max_date': 'Apr2018',
  },
}

bike_daily_meta = {
'attributes': {
  'primary': {
    'field': 'year_2016',
    'name': 'Daily Estimates of Bike Traffic',
    },
  'secondary': {
    'field': None,
    'name': None,
    'type': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': 2016,
  'min_date': None,
  'max_date': None,
  },
}

bike_counts_meta = {
'attributes': {
  'primary': {
    'field': 'year_2017',
    'name': 'Actual Bike Count',
    },
  'secondary': {
    'field': 'count_time',
    'name': 'Count Time',
    'type': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': 2017,
  'min_date': None,
  'max_date': None,
  },
}

