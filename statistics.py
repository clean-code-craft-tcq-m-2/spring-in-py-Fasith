import math

def calculateStats(numbers):
  if len(numbers) == 0:
    return{
      'avg':math.nan,
      'max':math.nan,
      'min':math.nan,
    }

  average = sum(numbers)/len(numbers)
  maximum = max(numbers)
  minimum = min(numbers)
  return {
    'avg':average,
    'max':maximum,
    'min':minimum,
  }
