function calculateAverage(list) {
  let sum = 0;

  for (let i = 0; i < list.length; i++) {
    sum += list[i];
  }

  return sum / list.length;
}
