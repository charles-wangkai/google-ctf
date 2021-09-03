function controlCar(scanArray) {
  let farthestIndex = 0;
  for (let i = 1; i < scanArray.length; ++i) {
    if (
      scanArray[i] * (Math.abs(i - 8) + 1) >
      scanArray[farthestIndex] * (Math.abs(farthestIndex - 8) + 1)
    ) {
      farthestIndex = i;
    }
  }

  if (farthestIndex <= 6) {
    return -1;
  } else if (farthestIndex >= 10) {
    return 1;
  }

  return 0;
}
